# Universal AI Agent Repository Control System

A reusable repository-control system for AI-assisted software development.

This repo contains standard files that can be copied into the root of any project to help AI agents work more safely, efficiently, and consistently.

---

## Purpose

Use this repository as the source of truth for AI agent operating rules, repository safety rules, testing expectations, security practices, deployment checks, and project documentation structure.

Agents can copy these files into any new or existing repository:

```text
AGENT_RULES.md
README.md
ARCHITECTURE.md
TESTING.md
SECURITY.md
DEPLOYMENT.md
.env.example
.gitignore
```

Optional files:

```text
ROADMAP.md
CHANGELOG.md
DECISIONS.md
CONTRIBUTING.md
```

---

## AI Agent Instructions

Before making meaningful changes, all AI agents must read the repository control files in this order:

1. `AGENT_RULES.md`
2. `README.md`
3. `ARCHITECTURE.md`
4. `TESTING.md`
5. `SECURITY.md`
6. `DEPLOYMENT.md`

If `AGENT_USAGE_RULES.md` exists, agents must also read it immediately after `AGENT_RULES.md`.

Agents must follow `AGENT_RULES.md` before:

- editing code
- creating branches
- opening pull requests
- changing dependencies
- modifying deployment settings
- changing architecture
- installing packages
- generating artifacts
- sharing files or workspace links

Agents must preserve existing project-specific content and must not overwrite working files unless explicitly instructed.

Agents must not expose secrets, credentials, private keys, tokens, `.env` files, or sensitive user data.

---

## How to Use This Repo

When starting or updating another repository, tell the agent:

```text
Use my universal AI agent repository control system as the source of truth.

Copy the standard control files from this repo into the root of the target repository.

Preserve existing project-specific content.

Merge README.md, .gitignore, and .env.example instead of blindly replacing them.

Do not change application code.

Do not install packages.

Do not refactor anything.

After copying or merging the files, summarize what changed.
```

---

## Files Included

### `AGENT_RULES.md`

Defines mandatory behavior for AI agents, including environment rules, branch rules, commit rules, testing rules, security rules, and deployment rules.

### `README.md`

Provides the project overview and links to the repository-control files.

### `ARCHITECTURE.md`

Documents the system architecture, major components, data flow, and architecture-change rules.

### `TESTING.md`

Defines testing expectations, validation rules, build checks, and pull-request testing checklist.

### `SECURITY.md`

Defines rules for secrets, credentials, user data, uploads, APIs, authentication, authorization, and logging.

### `DEPLOYMENT.md`

Defines deployment environments, deployment flow, pre-deployment checks, and rollback rules.

### `.env.example`

Documents required environment variables without exposing real secrets.

### `.gitignore`

Prevents common junk files, secrets, environment files, build artifacts, and caches from being committed.

---

## Optional Files

### `ROADMAP.md`

Tracks current goals, priorities, backlog, and features that should not be built yet.

### `CHANGELOG.md`

Tracks meaningful changes over time.

### `DECISIONS.md`

Records important technical, product, and process decisions.

### `CONTRIBUTING.md`

Defines development workflow, branch naming, commit rules, pull-request rules, and code-review checklist.

---

## Recommended Target Repo Placement

All copied files should go at the root of the target repository:

```text
/
├── AGENT_RULES.md
├── README.md
├── ARCHITECTURE.md
├── TESTING.md
├── SECURITY.md
├── DEPLOYMENT.md
├── .env.example
└── .gitignore
```

Optional:

```text
/
├── ROADMAP.md
├── CHANGELOG.md
├── DECISIONS.md
└── CONTRIBUTING.md
```

---

## Important Merge Rules

When applying this system to another repository:

- Do not overwrite an existing `README.md` blindly.
- Merge the AI Agent Instructions section into the existing README.
- Do not overwrite an existing `.gitignore` blindly.
- Append missing ignore rules only.
- Do not overwrite an existing `.env.example` blindly.
- Merge missing environment variable placeholders only.
- Do not delete existing project-specific documentation.
- Do not change application code unless explicitly instructed.

---

## Standard Commit Message

Use this commit message when adding these files to a repo:

```text
Add universal AI agent repository control system
```

---

## License

MIT
