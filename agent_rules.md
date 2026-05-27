# AGENT_RULES.md

Read this file completely before taking action.

## Primary Directive

Build reliable, maintainable, production-quality software.

Do not:
- invent APIs, packages, files, commands, or features
- claim something works unless verified
- remove working functionality without approval
- rewrite architecture unnecessarily
- expose secrets or credentials
- make broad changes when a small fix is enough

If uncertain, say so clearly.

## Universal Agent Rules

Before making changes:
1. Identify the repository.
2. Identify the current branch.
3. Identify the files likely affected.
4. State whether the change affects code, docs, tests, security, deployment, data, or infrastructure.
5. Prefer the smallest safe change that solves the problem.

## Environment Rules

- Use GitHub web workflow for simple file edits, documentation, commits, branches, pull requests, and reviews.
- Use a cloud development environment only when terminal execution, dependency installation, app preview, or testing is required.
- Never assume local machine access.
- Never require local installs unless explicitly requested.
- Use repo-relative paths only.
- Use environment variables for secrets.
- Never hardcode credentials.

## Branch Rules

- `main` must remain stable.
- Use branches for risky changes, feature work, refactors, infrastructure changes, database changes, dependency changes, and bug fixes.
- Documentation-only foundation updates may be committed directly to `main` when appropriate.
- Never commit risky application code directly to `main`.

Branch name examples:

```text
feature/new-feature
fix/specific-bug
refactor/specific-area
docs/update-docs
test/add-tests
chore/repo-maintenance
```

## Commit Rules

Before committing:
- Summarize changed files.
- Confirm no unrelated files were modified.
- Confirm no secrets are included.
- Confirm no generated junk files are included.
- Confirm testing status.

Good commit messages:

```text
Add universal repository documentation
Fix authentication redirect handling
Add validation tests for API input
Refactor shared utility functions
Update deployment instructions
```

Bad commit messages:

```text
fix
stuff
changes
update
latest
```

## Pull Request Rules

Before opening or merging a pull request:
- Explain what changed.
- Explain why it changed.
- List affected files.
- State testing performed.
- State risks.
- State deployment impact.
- State environment variable impact.
- State rollback plan if relevant.

## Code Rules

- Keep code modular.
- Avoid giant files.
- Use descriptive names.
- Prefer readable code over clever code.
- Add comments for non-obvious logic.
- Reuse existing utilities before adding new ones.
- Avoid unnecessary dependencies.
- Preserve backward compatibility when possible.
- Do not change public interfaces without explaining impact.

## Dependency Rules

Before adding or upgrading dependencies:
- Explain why the dependency is needed.
- Check whether the project already has a suitable package.
- Avoid duplicate functionality.
- Avoid package bloat.
- Avoid unnecessary version upgrades.
- Explain breaking-change risks.

## Testing Rules

Never say:
- “fixed”
- “working”
- “tested”
- “production ready”

unless verification actually occurred.

If unable to test, state:

```text
Not tested — theoretical implementation only.
```

Before claiming success:
- Run relevant tests.
- Run build checks.
- Run lint/type checks when available.
- Verify affected behavior.
- Report any commands that failed.

## Debugging Rules

When debugging:
1. Show the exact error or symptom.
2. Identify likely root cause.
3. Identify affected files.
4. Apply the smallest safe fix first.
5. Avoid unrelated rewrites.
6. Explain how to verify the fix.

## Security Rules

- Never expose API keys.
- Never commit `.env` files.
- Never hardcode credentials.
- Validate all user input.
- Sanitize uploaded files.
- Protect server-side routes.
- Keep sensitive logic off the frontend.
- Use least-privilege access.
- Avoid leaking stack traces or private data to users.

## Deployment Rules

Before deployment:
- Confirm build passes.
- Confirm tests pass or limitation is stated.
- Confirm environment variables exist.
- Confirm API routes work.
- Confirm database connectivity if applicable.
- Confirm no secrets are exposed.
- Confirm rollback path is understood.

## Documentation Rules

Update documentation when changing:
- setup steps
- environment variables
- commands
- architecture
- deployment
- testing
- security
- public APIs
- major workflows

## AI Honesty Rule

If something is unknown, incomplete, untested, assumed, or risky, state that clearly.

Do not fake certainty.
