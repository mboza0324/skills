# DEPLOYMENT.md

## Deployment Overview

Frontend:
- TBD

Backend:
- TBD

Database:
- TBD

Hosting:
- TBD

CI/CD:
- TBD

## Environments

Production:
- stable live version
- connected to main branch or approved release branch

Preview/Staging:
- test deployments
- connected to feature branches or pull requests

Development:
- temporary work environment

## Deployment Flow

```text
Code change
    ↓
Commit
    ↓
Pull request if needed
    ↓
Automated checks if configured
    ↓
Preview/Staging deployment if configured
    ↓
Review
    ↓
Merge
    ↓
Production deployment
```

## Required Pre-Deployment Checks

Before production deployment:
- Build passes.
- Tests pass or limitation is stated.
- Environment variables are configured.
- No secrets are committed.
- Database migrations are reviewed.
- API routes are verified.
- Rollback path is known.

## Rollback

If deployment fails:
1. Identify the failed commit or change.
2. Revert the commit or redeploy prior successful version.
3. Confirm environment variables were not changed incorrectly.
4. Confirm database was not damaged.
5. Document the incident in `CHANGELOG.md`.

## Agent Rule

Never deploy major changes automatically without confirming:
- what changed
- what was tested
- what could break
- how to roll back
