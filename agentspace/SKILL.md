---
name: agentspace
displayName: "🚪 Agentspace — Share agent workspaces"
description: >
  Share a user-selected folder or file through Agentspace. Use only after checking
  the target for secrets, private data, employer information, and unnecessary files.
emoji: "🚪"
homepage: https://agentspace.so
license: MIT
---

# 🚪 Agentspace

Share a user-selected local folder or file through a browser workspace.

## Safety first

Before sharing, inspect the exact target for:

- `.env` files, credentials, API keys, tokens, passwords, and private keys
- customer, employee, health, financial, legal, or regulated data
- employer-confidential, proprietary, or internal-only material
- `.git`, dependency folders, build caches, logs, and unnecessary large files

Do not upload work-related or third-party data unless the user confirms that external sharing is authorized.

## Choose the CLI path

1. Use `ascli` directly when it is already available.
2. Otherwise use a reviewed, pinned package version through `npx`.
3. Do not pipe a remote installer directly into a shell.

Avoid `@latest` in workplace workflows. Use a tested version supplied by repository documentation or the user.

## Share a path

Ask for the exact folder or file when the user has not named it.

Default to view-only:

```bash
ascli share <path> --permission view
```

Use edit access only when the user explicitly requests it and confirms the content is approved for external editing:

```bash
ascli share <path> --permission edit
```

Return the share URL exactly as printed by the CLI. Never invent or reconstruct a URL.

## Guardrails

- Upload only the path explicitly named by the user.
- Do not default to the current directory.
- Do not read environment variables, shell history, or files outside the selected path.
- Do not move the user into a different project merely to use Agentspace.
- If the path is ambiguous, stop before uploading.
- If sensitive or workplace data is detected, do not upload it until the user removes it or confirms authorization.
- If the CLI fails, report the failure rather than claiming a workspace exists.
