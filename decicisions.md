# DECISIONS.md

This file records important technical, product, and process decisions.

AI agents must check this file before changing:
- architecture
- dependencies
- deployment strategy
- database design
- authentication
- security model
- major workflows

## Decision Format

```md
## YYYY-MM-DD - Decision Title

Decision:
Reason:
Alternatives considered:
Risks:
Rollback plan:
```

## Decisions

## YYYY-MM-DD - Add Universal Repository Control System

Decision:
Add standardized repository documentation and AI agent behavior files.

Reason:
Improve consistency, reduce hallucinations, preserve project context, and prevent unsafe changes.

Alternatives considered:
Only using README documentation.

Risks:
Documentation may become stale if not maintained.

Rollback plan:
Remove or simplify unused documentation files.
