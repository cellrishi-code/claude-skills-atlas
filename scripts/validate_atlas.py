from pathlib import Path
import re
import urllib.parse

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_SKILL_SECTIONS = (
    "Purpose",
    "When to use",
    "Instructions",
    "Inputs",
    "Outputs",
    "Example",
    "Limitations",
)


def get_anchors(text: str) -> set:
    anchors = set()
    for match in re.finditer(r"^(#{1,6})\s+(.+)$", text, re.MULTILINE):
        heading = match.group(2).strip()
        slug = heading.lower()
        slug = re.sub(r"[^\w\- ]", "", slug)
        slug = slug.replace(" ", "-")
        if slug:
            anchors.add(slug)
    for match in re.finditer(
        r'<(?:a|[\w]+)[^>]+(?:id|name)="([^"]+)"', text, re.IGNORECASE
    ):
        anchors.add(match.group(1))
    return anchors


file_cache = {}


def get_file_info(filepath: Path):
    if filepath not in file_cache:
        try:
            text = filepath.read_text(encoding="utf-8")
            file_cache[filepath] = {"text": text, "anchors": get_anchors(text)}
        except Exception:
            file_cache[filepath] = None
    return file_cache[filepath]


def heading_names(text: str) -> set:
    return {
        match.group(1).strip().casefold()
        for match in re.finditer(r"^#{1,6}\s+(.+)$", text, re.MULTILINE)
    }


def frontmatter(text: str) -> str:
    match = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.DOTALL)
    return match.group(1) if match else ""


def resource_name(path: Path, text: str) -> str:
    if path.name == "SKILL.md":
        match = re.search(r"(?im)^name:\s*([^\n]+)", frontmatter(text))
        if match:
            return match.group(1).strip().strip("'\"")
    match = re.search(r"(?m)^#\s+(.+)$", text)
    return match.group(1).strip() if match else path.stem.replace("-", " ")


def validate_catalog(root_dir: Path) -> list:
    errors = []
    seen_names = {"skills": {}, "prompts": {}}

    for directory in ["skills", "prompts", "workflows", "agents"]:
        base = root_dir / directory
        if not base.exists():
            continue

        for path in base.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in {".md", ".markdown"}:
                continue

            text = path.read_text(encoding="utf-8")
            rel = path.relative_to(root_dir).as_posix()

            if not text.strip():
                errors.append(f"Empty resource: {rel}")

            if directory == "skills" and path.name == "SKILL.md":
                fm = frontmatter(text)
                if not fm:
                    errors.append(f"Skill lacks frontmatter: {rel}")
                else:
                    for field in ("name", "category", "tags"):
                        if not re.search(rf"(?im)^{re.escape(field)}:\s*.+$", fm):
                            errors.append(f"Skill missing frontmatter field '{field}': {rel}")

                        recommendation_fields = (
                        "recommendation_use_cases",
                        "recommendation_audience",
                        "recommendation_domain",
                        "recommendation_prerequisites",
                        "recommendation_related_skills",
                        )

                        present_recommendation_fields = [
                            field
                            for field in recommendation_fields
                            if re.search(rf"(?im)^{re.escape(field)}:\s*.+$", fm)
                        ]

                        if (
                            present_recommendation_fields
                            and len(present_recommendation_fields) != len(recommendation_fields)
                        ):
                            errors.append(
                                f"Skill recommendation metadata must define all fields: {rel}"
                            )

                if not re.search(r"(?im)^# .+", text):
                    errors.append(f"Skill lacks a heading: {rel}")

                headings = heading_names(text)
                for section in REQUIRED_SKILL_SECTIONS:
                    if section.casefold() not in headings:
                        errors.append(f"Skill missing required section '{section}': {rel}")

            if directory in seen_names:
                name = resource_name(path, text)
                key = name.casefold()
                if key in seen_names[directory]:
                    errors.append(
                        f"Duplicate {directory[:-1]} name '{name}': "
                        f"{rel} and {seen_names[directory][key]}"
                    )
                else:
                    seen_names[directory][key] = rel

    # Check relative Markdown links point to existing files and anchors.
    for path in root_dir.rglob("*.md"):
        if any(part in {".git", ".github"} for part in path.parts):
            continue

        info = get_file_info(path)
        if not info:
            continue

        for raw_target in re.findall(r"\]\(([^)]+)\)", info["text"]):
            link = raw_target.split()[0]
            if link.startswith(("http://", "https://", "mailto:")):
                continue

            parsed = urllib.parse.urlparse(link)
            file_path_part = urllib.parse.unquote(parsed.path)
            anchor_part = parsed.fragment

            target_path = path
            if file_path_part:
                target_path = (path.parent / file_path_part).resolve()

            try:
                target_path.relative_to(root_dir.resolve())
            except ValueError:
                continue

            if not target_path.exists():
                errors.append(
                    f"Broken internal link in {path.relative_to(root_dir)}: "
                    f"{link} (Missing file)"
                )
                continue

            if anchor_part and target_path.is_file() and target_path.suffix.lower() in {
                ".md",
                ".markdown",
            }:
                target_info = get_file_info(target_path)
                if target_info and anchor_part not in target_info["anchors"]:
                    errors.append(
                        f"Broken internal link in {path.relative_to(root_dir)}: "
                        f"{link} (Missing anchor '{anchor_part}')"
                    )

    if not (root_dir / "CATALOG.md").exists():
        errors.append("CATALOG.md is missing")

    return errors


if __name__ == "__main__":
    errors = validate_catalog(ROOT)
    if errors:
        print("\n".join(f"ERROR: {e}" for e in errors))
        raise SystemExit(1)

    print("Atlas validation passed.")
