import sys
import tempfile
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_atlas import validate_catalog


class TestRecommendationMetadataValidation(unittest.TestCase):
    def test_incomplete_recommendation_metadata_reports_one_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "CATALOG.md").touch()
            skill_dir = root / "skills" / "example"
            skill_dir.mkdir(parents=True)
            (root / "prompts").mkdir()

            (skill_dir / "SKILL.md").write_text(
                "---\n"
                "name: example\n"
                "category: coding\n"
                "tags: [test]\n"
                "recommendation_use_cases: [review code]\n"
                "---\n\n"
                "# Example\n\n"
                "## Purpose\ntext\n"
                "## When to use\ntext\n"
                "## Instructions\ntext\n"
                "## Inputs\ntext\n"
                "## Outputs\ntext\n"
                "## Example\ntext\n"
                "## Limitations\ntext\n",
                encoding="utf-8",
            )

            errors = validate_catalog(root)
            metadata_errors = [
                error for error in errors
                if "recommendation metadata must define all fields" in error
            ]
            self.assertEqual(len(metadata_errors), 1)


if __name__ == "__main__":
    unittest.main()
