# AGENT_USAGE_RULES.md

## Purpose

This repository contains installable agent skills and reusable repository-governance files.

Use it as a focused skill and tool library. Do not use it as a general notes folder, prompt dump, or personal command center.

## Startup Rule

Before using this repository, agents should:

1. Read this file.
2. Read the root `README.md`.
3. Decide whether the task needs `agentspace` or `find-skills`.
4. Read only that skill's `SKILL.md`.
5. Do not inspect unrelated files unless the user explicitly asks.

## Token Efficiency

Use the smallest amount of context needed. Pick the exact skill required, summarize relevant rules briefly, and stop reading once sufficient context exists.

## Environment Rule

Default development environment is GitHub Codespaces unless the user says otherwise.

Do not assume local terminal access, local filesystem paths, local Python or Node installations, Docker Desktop, or existing private `.env` files.

## Agentspace Safety Rule

Use `agentspace` only when the user explicitly asks to share a folder, file, artifact, or workspace.

Before syncing or sharing, check for:

- `.env` and `.env.local`
- API keys, tokens, passwords, and private credentials
- private documents and customer data
- employer, proprietary, regulated, or confidential information
- `node_modules`, `.git`, build caches, and unnecessary large files

Never upload employer, customer, regulated, proprietary, or confidential data without explicit authorization from the data owner and the user's organization.

Default to read-only sharing:

```bash
ascli sync . --permission view
```

or:

```bash
ascli share . --permission view
```

Use edit access only when the user explicitly requests it and confirms the material is approved for external sharing.

## Install Rule

Prefer install methods in this order:

1. Existing `ascli`
2. A pinned package version through `npx`
3. A reviewed installer only when necessary

Do not use `curl | bash` casually. Avoid unpinned `@latest` dependencies in workplace workflows.

## Share Link Rule

Do not invent share links. Only return a share link actually printed by the CLI. If the CLI fails, explain the failure.

## Find-Skills Rule

Use `find-skills` to locate or compare skills, but do not install a discovered skill automatically. Review its behavior and installation instructions first.

## Security Rule

Never commit, sync, or share real API keys, tokens, passwords, private `.env` values, private customer data, or sensitive personal data. Use placeholders only.

## Git Rule

Do not commit directly to `main` unless explicitly instructed. Use a feature branch for edits and preserve upstream skill files unless a change is necessary.

## Agent Execution Rule

Agents must:

1. Identify the user's actual goal.
2. Choose only the relevant skill.
3. Read only that skill's `SKILL.md`.
4. Execute the smallest safe command set.
5. Return what was done, the command used, the result, security warnings, and the next required step.

## Absolute Do Nots

- Do not default to edit permission.
- Do not upload folders blindly.
- Do not install unreviewed or unpinned tools.
- Do not claim a share link exists unless the CLI printed it.
- Do not include personal names or account-specific repository paths in reusable instructions.
