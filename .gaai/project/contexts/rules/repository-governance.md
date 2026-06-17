# Repository Governance

The root governance files in this repository are authoritative.

Before Discovery or Delivery:

1. Read `AGENT_RULES.md`.
2. Read `AGENT_USAGE_RULES.md` when present.
3. Read `README.md`.
4. Read `ARCHITECTURE.md`.
5. Read `TESTING.md`.
6. Read `SECURITY.md`.
7. Read `DEPLOYMENT.md`.

GAAI must preserve existing project-specific content.

It must not overwrite `README.md`, `.gitignore`, or `.env.example`.
It must not commit secrets, credentials, tokens, private keys, or real environment values.
Meaningful implementation must occur on a focused branch.
Delivery must report files changed, testing performed, risks, deployment impact, and rollback steps.

This repository is a control and skill library. Discovery and Delivery must avoid changing imported upstream skill content unless the Story explicitly authorizes it.
