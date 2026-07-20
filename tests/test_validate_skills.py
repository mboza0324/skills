from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_skills import parse_frontmatter, validate


VALID_SKILL = """---
name: example-skill
description: Validate a representative skill.
version: 1.2.3
---

# Example Skill

## Purpose
Test validation.

## Easy invocation
Use Example Skill.

## Required inputs
A repository.

## Completion standard
All checks pass.
"""


class SkillValidatorTests(unittest.TestCase):
    def test_valid_skill_passes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "skills" / "example-skill" / "SKILL.md"
            path.parent.mkdir(parents=True)
            path.write_text(VALID_SKILL, encoding="utf-8")
            record = parse_frontmatter(VALID_SKILL, path)
            # Replace the project-relative path expectation with a matching
            # synthetic index entry while retaining the parser/validator path.
            record = type(record)(Path(__file__).resolve().parents[1] / "skills/example-skill/SKILL.md", record.metadata, record.body)
            self.assertEqual([], validate([record], "skills/example-skill/SKILL.md"))

    def test_missing_completion_section_fails(self):
        text = VALID_SKILL.replace("## Completion standard\nAll checks pass.\n", "")
        path = Path(__file__).resolve().parents[1] / "skills/example-skill/SKILL.md"
        record = parse_frontmatter(text, path)
        errors = validate([record], "skills/example-skill/SKILL.md")
        self.assertTrue(any("Completion standard" in error for error in errors))

    def test_duplicate_names_fail(self):
        first = parse_frontmatter(
            VALID_SKILL,
            Path(__file__).resolve().parents[1] / "skills/example-skill/SKILL.md",
        )
        second = parse_frontmatter(
            VALID_SKILL,
            Path(__file__).resolve().parents[1] / "skills/example-copy/SKILL.md",
        )
        errors = validate(
            [first, second],
            "skills/example-skill/SKILL.md\nskills/example-copy/SKILL.md",
        )
        self.assertTrue(any("duplicate skill name" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
