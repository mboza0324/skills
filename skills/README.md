# Repository Skills

The invocation-ready skills in this directory extend the root repository-control system without replacing repository-specific rules.

## Available skills

### Repo Auditor

Path: [`repo-auditor/SKILL.md`](repo-auditor/SKILL.md)

```text
Use Repo Auditor on <repository or GitHub owner>.
```

Use this first when current completion, risk, CI, deployment, duplication, and external-blocker evidence is not already captured in a fresh audit.

### Repo Builder

Path: [`repo-builder/SKILL.md`](repo-builder/SKILL.md)

```text
Use Repo Builder on <repository URL>.
```

Use this after the next acceptance criterion is known. Repo Builder continues through implementation, tests, CI, documentation, PR review, merge, post-merge verification, and audit refresh.

## Portfolio mode

```text
Use Repo Auditor on all repositories under <owner>, then use Repo Builder on every repository in priority order until each repository has validated delivery or a merged lifecycle resolution.
```

The authoritative discovery table is [`../SKILL_INDEX.md`](../SKILL_INDEX.md). Run `python scripts/validate_skills.py` from the repository root after editing any skill definition.
