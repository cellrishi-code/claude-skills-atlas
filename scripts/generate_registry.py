from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
OUTPUT = ROOT / "registry.json"
SCHEMA_VERSION = "1.0.0"


def parse_frontmatter(text):
    match = re.match(r"^---\s*\n([\s\S]*?)\n---", text)
    if not match:
        return {}
    metadata = {}
    for line in match.group(1).splitlines():
        item = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not item:
            continue
        key, value = item.groups()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            value = [v.strip().strip("\\\"'") for v in value[1:-1].split(",") if v.strip()]
        else:
            value = value.strip("\\\"'")
        metadata[key] = value
    return metadata


def build_registry():
    resources = []
    for path in sorted(SKILLS.rglob("SKILL.md")):
        metadata = parse_frontmatter(path.read_text(encoding="utf-8"))
        name = metadata.get("name") or path.parent.name
        tags = metadata.get("tags", [])
        if not isinstance(tags, list):
            tags = [tags]
        resources.append({
            "name": name,
            "path": path.relative_to(ROOT).as_posix(),
            "version": metadata.get("version", "1.0.0"),
            "category": metadata.get("category", "uncategorized"),
            "tags": tags,
            "capabilities": tags,
            "metadata": metadata,
        })
    return {"schema_version": SCHEMA_VERSION, "generated_by": "scripts/generate_registry.py", "resources": resources}


if __name__ == "__main__":
    registry = build_registry()
    OUTPUT.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Generated {OUTPUT.relative_to(ROOT)} with {len(registry['resources'])} skills")
