# Skill Index

This index lists reusable, invocation-ready skills maintained in this repository.

| Skill | Path | Easy invocation | Purpose |
|---|---|---|---|
| Repo Auditor | `skills/repo-auditor/SKILL.md` | `Use Repo Auditor on <repository or owner>.` | Produce evidence-backed repository or portfolio completion, risk, and shipping priorities. |
| Repo Builder | `skills/repo-builder/SKILL.md` | `Use Repo Builder on <repository>.` | Execute an audited repository through validated delivery, merge, and post-merge verification. |

## Portfolio invocation

```text
Use Repo Auditor on all repositories under <owner>, then use Repo Builder on every repository in priority order until each repository has validated delivery or a merged lifecycle resolution.
```

## Selection rules

- Use Repo Auditor before implementation when current repository state is not already backed by a fresh audit.
- Use Repo Builder when the target repository and next acceptance criterion are known.
- In portfolio mode, keep one authoritative machine-readable registry and update it after every material merge or lifecycle decision.
- Repository-specific instructions override generic skill guidance when they are stricter and do not conflict with security or user intent.
