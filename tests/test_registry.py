import json
import re
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import generate_registry


class RegistryTests(unittest.TestCase):
    def test_registry_matches_skill_files(self):
        registry = json.loads((ROOT / "registry.json").read_text(encoding="utf-8"))
        paths = {item["path"] for item in registry["resources"]}
        actual = {p.relative_to(ROOT).as_posix() for p in (ROOT / "skills").rglob("SKILL.md")}
        self.assertEqual(paths, actual)

    def test_registry_entries_have_required_fields(self):
        registry = json.loads((ROOT / "registry.json").read_text(encoding="utf-8"))
        for item in registry["resources"]:
            for field in ("name", "path", "version", "category", "tags", "capabilities", "metadata"):
                self.assertIn(field, item)
            self.assertRegex(item["version"], r"^\d+\.\d+\.\d+$")

    def test_generator_matches_checked_in_registry(self):
        expected = generate_registry.build_registry()
        actual = json.loads((ROOT / "registry.json").read_text(encoding="utf-8"))
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
