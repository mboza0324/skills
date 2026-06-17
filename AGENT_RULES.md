# AGENT_RULES.md

Read this file completely before taking action.

## Primary Directive

Build reliable, maintainable, production-quality software.

- Do not invent APIs, packages, files, commands, or features.
- Do not claim something works unless it was verified.
- Do not remove working functionality without approval.
- Do not expose secrets, credentials, private keys, tokens, or `.env` files.
- Prefer the smallest safe change that solves the problem.

## Required Pre-change Checks

1. Identify the repository and current branch.
2. Inspect the repository structure and affected files.
3. State whether the change affects code, docs, tests, security, deployment, data, or infrastructure.
4. Use a feature branch for risky, code, dependency, infrastructure, database, or bug-fix changes.
5. Preserve existing project-specific content.

## Verification

- Run relevant tests, build, and lint/lype checks when available.
- Never claim a change is fixed, working, tested, or production-ready unless verification actually occurred.
- If unable to test, state: `Not tested — theoretical implementation only.`

## Security

- Use environment variables for secrets.
- Validate user input and uploads.
- Protect server-side routes and use least-privilege access.
- Avoid logging secrets, stack traces, or private data.

## Change Summary

Summarize files changed, why they changed, testing performed, risks, deployment impact, and rollback path.
