# DEPLOYMENT.md

## Deployment Standard

Projects must document environments, CI/CD flow, required environment variables, release process, health checks, and rollback procedure.

Before production deployment:
- build and tests pass, or limitations are stated
- configuration and required variables are verified
- no secrets are committed
- migrations and API routes are reviewed
- rollback path is understood

Never deploy major changes automatically without documenting what changed, what was verified, what could break, and how to roll back.
