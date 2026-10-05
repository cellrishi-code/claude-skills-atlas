import tempfile
import unittest
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_atlas import validate_catalog


class TestValidateAtlas(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "CATALOG.md").touch()
        (self.root / "skills").mkdir()
        (self.root / "prompts").mkdir()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_valid_links_and_anchors(self):
        (self.root / "doc1.md").write_text(
            "# Doc 1\n\nLink to [doc2](doc2.md#section-2) and [itself](#doc-1).",
            encoding="utf-8",
        )
        (self.root / "doc2.md").write_text("# Doc 2\n\n## Section 2", encoding="utf-8")
        self.assertEqual(validate_catalog(self.root), [])

    def test_missing_file(self):
        (self.root / "doc1.md").write_text("[broken](missing.md)", encoding="utf-8")
        errors = validate_catalog(self.root)
        self.assertTrue(any("Missing file" in e for e in errors))

    def test_missing_anchor(self):
        (self.root / "doc1.md").write_text(
            "[broken](doc2.md#missing-section)", encoding="utf-8"
        )
        (self.root / "doc2.md").write_text("# Doc 2", encoding="utf-8")
        errors = validate_catalog(self.root)
        self.assertTrue(any("Missing anchor" in e for e in errors))

    def test_skill_required_metadata_and_sections(self):
        skill = self.root / "skills" / "example"
        skill.mkdir()
        (skill / "SKILL.md").write_text(
            "---\nname: example\ncategory: coding\ntags: [test]\n---\n\n"
            "# Example\n\n## Purpose\ntext\n## When to use\ntext\n"
            "## Instructions\ntext\n## Inputs\ntext\n## Outputs\ntext\n"
            "## Example\ntext\n## Limitations\ntext\n",
            encoding="utf-8",
        )
        self.assertEqual(validate_catalog(self.root), [])

    def test_skill_missing_required_section(self):
        skill = self.root / "skills" / "example"
        skill.mkdir()
        (skill / "SKILL.md").write_text(
            "---\nname: example\ncategory: coding\ntags: [test]\n---\n\n"
            "# Example\n\n## Purpose\ntext\n",
            encoding="utf-8",
        )
        errors = validate_catalog(self.root)
        self.assertTrue(any("missing required section 'Instructions'" in e for e in errors))

    def test_duplicate_prompt_names(self):
        (self.root / "prompts" / "first.md").write_text(
            "# Duplicate Prompt\n\nPrompt body.", encoding="utf-8"
        )
        (self.root / "prompts" / "second.md").write_text(
            "# Duplicate Prompt\n\nAnother body.", encoding="utf-8"
        )
        errors = validate_catalog(self.root)
        self.assertTrue(any("Duplicate prompt name" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
