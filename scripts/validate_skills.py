#!/usr/bin/env python3
"""Validate invocation-ready skill definitions in this repository."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
INDEX_PATH = ROOT / "SKILL_INDEX.md"
REQUIRED_FIELDS = ("name", "description", "version")
REQUIRED_SECTIONS = (
    "# ",
    "## Purpose",
    "## Easy invocation",
    "## Required inputs",
    "## Completion standard",
)


@dataclass(frozen=True)
class SkillRecord:
    path: Path
    metadata: dict[str, str]
    body: str


def parse_frontmatter(text: str, path: Path) -> SkillRecord:
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML frontmatter")
    marker = text.find("\n---\n", 4)
    if marker == -1:
        raise ValueError(f"{path}: unterminated YAML frontmatter")

    metadata: dict[str, str] = {}
    for raw_line in text[4:marker].splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        key, separator, value = line.partition(":")
        if not separator or not key.strip() or not value.strip():
            raise ValueError(f"{path}: invalid frontmatter line: {raw_line!r}")
        metadata[key.strip()] = value.strip().strip('"\'')

    body = text[marker + 5 :].strip()
    return SkillRecord(path=path, metadata=metadata, body=body)


def discover_skills(root: Path = SKILLS_ROOT) -> list[SkillRecord]:
    records: list[SkillRecord] = []
    for path in sorted(root.glob("*/SKILL.md")):
        records.append(parse_frontmatter(path.read_text(encoding="utf-8"), path))
    return records


def validate(records: list[SkillRecord], index_text: str) -> list[str]:
    errors: list[str] = []
    if not records:
        return ["No skills/*/SKILL.md definitions were found"]

    names: set[str] = set()
    for record in records:
        relative = record.path.relative_to(ROOT).as_posix()
        for field in REQUIRED_FIELDS:
            if not record.metadata.get(field):
                errors.append(f"{relative}: missing frontmatter field {field}")

        name = record.metadata.get("name", "")
        if name:
            if name in names:
                errors.append(f"{relative}: duplicate skill name {name}")
            names.add(name)
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
                errors.append(f"{relative}: name must be lower-case kebab-case")

        version = record.metadata.get("version", "")
        if version and not re.fullmatch(r"\d+\.\d+\.\d+", version):
            errors.append(f"{relative}: version must use semantic X.Y.Z form")

        for section in REQUIRED_SECTIONS:
            if section not in record.body:
                errors.append(f"{relative}: missing required section {section.strip()}")

        if relative not in index_text:
            errors.append(f"{relative}: missing from SKILL_INDEX.md")

    return errors


def main() -> int:
    if not INDEX_PATH.is_file():
        print("SKILL_INDEX.md is missing", file=sys.stderr)
        return 1

    try:
        records = discover_skills()
        errors = validate(records, INDEX_PATH.read_text(encoding="utf-8"))
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"Validated {len(records)} skill definition(s): {', '.join(r.metadata['name'] for r in records)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
