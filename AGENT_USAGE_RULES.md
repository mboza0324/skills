# AGENT_USAGE_RULES.md

## Purpose

This fork contains installable agent skills from `agentspace-so/skills`.

Use this repo as a focused skill/tool library.

Do not use this repo as a general notes folder, prompt dump, or personal command center.

This repo is mainly for:

- `agentspace` — sharing folders, files, artifacts, and workspaces
- `find-skills` — finding useful agent skills

---

## Startup Rule

Before using this repo, agents should:

1. Read this file.
2. Read the root `README.md`.
3. Decide whether the task needs `agentspace` or `find-skills`.
4. Read only that skill’s `SKILL.md`.
5. Do not read the entire repo unless Mike explicitly asks.

---

## Token Efficiency Rule

Use the smallest amount of context needed.

Agents must not:

- read unrelated folders
- summarize the whole repo
- inspect every file “just in case”
- copy long skill files into chat
- install unnecessary skills

Agents should:

- pick the exact skill needed
- summarize the relevant rules briefly
- give exact commands
- stop reading once enough context exists

---

## Environment Rule

Default development environment is GitHub Codespaces unless Mike says otherwise.

Do not assume:

- local terminal access
- local filesystem paths
- local Python installation
- local Node installation
- local Docker Desktop
- local `.env` files already exist

When giving commands, frame them as:

```bash
# In GitHub Codespaces terminal
```

Do not tell Mike to install software locally unless he explicitly asks.

---

## Agentspace Safety Rule

Use `agentspace` when Mike asks to:

- share the current folder
- upload generated files
- send build artifacts
- hand off a project
- give another agent access to a workspace
- create a shareable workspace link

Before syncing or sharing, warn Mike to check for:

- `.env`
- `.env.local`
- API keys
- tokens
- passwords
- private credentials
- private documents
- customer data
- `node_modules`
- `.git`
- build cache folders
- unnecessary large files

Default to read-only sharing.

Prefer:

```bash
ascli sync . --permission view
```

or:

```bash
ascli share . --permission view
```

Only use edit access if Mike specifically asks for edit access.

---

## Install Rule

Prefer install methods in this order:

1. Existing `ascli`
2. `npx @agentspace-so/ascli@latest`
3. `curl -fsSL https://agentspace.so/install.sh | bash` only if needed

Do not use `curl | bash` casually.

---

## Share Link Rule

Do not invent share links.

Only return a share link actually printed by the CLI.

If the CLI fails, explain the failure.

---

## Find-Skills Rule

Use `find-skills` when Mike asks to:

- find a skill for a task
- compare agent skills
- decide whether a skill is worth installing
- avoid building something that already exists

Do not install a discovered skill automatically.

Before recommending a skill:

1. Check what it does.
2. Check whether it matches the task.
3. Watch for risky install instructions.
4. Prefer simple and reputable skills.
5. Give one best recommendation when possible.

---

## Security Rule

Never commit or sync:

- real API keys
- real tokens
- passwords
- private `.env` values
- secrets
- private customer data
- sensitive personal data

Use placeholders only.

Example:

```text
OPENAI_API_KEY=your_key_here
```

---

## Git Rule

Do not commit directly to `main` unless Mike explicitly says so.

Use a feature branch for edits.

Preserve the original fork structure.

Do not rewrite upstream skill files unless necessary.

---

## Agent Execution Rule

When using this repo, agents must follow this execution order:

1. Identify Mike's actual goal.
2. Decide whether this repo is needed.
3. If needed, choose only one relevant skill:
   - `agentspace`
   - `find-skills`
4. Read only that skill's `SKILL.md`.
5. Ignore unrelated folders and files.
6. Execute the task using the smallest safe command set.
7. Return only:
   - what was done
   - the command used
   - the result or link
   - any security warning
   - the next required step, if any

Do not provide long explanations unless Mike asks.

Do not explain the entire repo.

Do not list every possible option.

Prefer the fastest safe path.

---

## Output Compression Rule

For normal answers, agents should use this format:

```text
Answer:
Steps:
Command:
Result:
Warning:
Next:
```

Skip any section that does not apply.

Keep responses short unless the task is complex or Mike asks for depth.

---

## Absolute Do Nots

- Do not turn this repo into a general command center.
- Do not add unrelated workflows, prompts, or notes.
- Do not default to edit permission.
- Do not upload folders blindly.
- Do not use `curl | bash` unless necessary.
- Do not install skills without explaining why.
- Do not claim a share link exists unless the CLI printed it.
