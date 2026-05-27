# TESTING.md

## Testing Philosophy

No code should be considered working unless it has been verified.

AI agents must not claim success unless tests, builds, or manual verification were actually performed.

If testing was not possible, state:

```text
Not tested — theoretical implementation only.
```

## Standard Commands

Install:

```bash
# replace with project-specific install command
```

Lint:

```bash
# replace with project-specific lint command
```

Build:

```bash
# replace with project-specific build command
```

Test:

```bash
# replace with project-specific test command
```

Type Check:

```bash
# replace with project-specific type-check command
```

## Required Validation

For code changes:
- Check affected files.
- Run relevant tests.
- Run build command if available.
- Run lint/type checks if available.
- Verify no secrets were added.
- Verify no unrelated files changed.

For frontend changes:
- Page renders.
- Responsive behavior works.
- Loading states work.
- Error states work.
- Forms validate properly.
- API responses display correctly.

For backend changes:
- Endpoint returns expected status codes.
- Request validation works.
- Authentication/authorization works if applicable.
- Database queries work if applicable.
- Errors are handled safely.

For database changes:
- Migration impact is explained.
- Existing data is protected.
- Rollback risk is considered.
- Indexes are considered for heavy queries.

For deployment changes:
- Build passes.
- Environment variables are documented.
- Deployment config is valid.
- Rollback path is known.

## Pull Request Testing Checklist

Before merging:
- [ ] Build checked
- [ ] Tests checked
- [ ] Lint/type checks checked
- [ ] No secrets committed
- [ ] No unrelated files changed
- [ ] Documentation updated if needed
- [ ] Deployment impact reviewed
- [ ] Rollback path understood
