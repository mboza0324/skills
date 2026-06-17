# GAAI Integration

This repository uses GAAI for structured Discovery and Delivery while the root governance files remain authoritative.

## Install or update the framework core

Run from the repository root in GitHub Codespaces:

```bash
bash scripts/install-gaai.sh
```

The installer is pinned to a reviewed `mboza0324/GAAI-framework` commit. To deliberately test another revision:

```bash
GAAI_REF=<commit-sha> bash scripts/install-gaai.sh
```

Review all generated changes before committing:

```bash
git status
git diff --stat
git diff
```

## Bootstrap

After installation, instruct the coding agent:

```text
Read AGENT_RULES.md, AGENT_USAGE_RULES.md, README.md, ARCHITECTURE.md,
TESTING.md, SECURITY.md, and DEPLOYMENT.md.

Then read .gaai/core/README.md and bootstrap this project.
Preserve existing project-specific content.
Do not implement a feature yet.
```

## Workflow

Use Discovery to produce a refined backlog Story. Review its scope and acceptance criteria. Then run Delivery on a focused branch.

The project-specific governance rule is stored at:

`.gaai/project/contexts/rules/repository-governance.md`
