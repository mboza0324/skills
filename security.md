# SECURITY.md

## Security Rules

Never commit:
- `.env`
- API keys
- access tokens
- passwords
- private keys
- production credentials
- user private data
- confidential files

## Environment Variables

Use `.env.example` to document required variables.

Real secrets belong in secure environment settings, not the repository.

Examples:
- GitHub Secrets
- hosting provider environment variables
- cloud provider secret managers
- deployment platform variables

## Input Validation

All user input must be validated server-side.

Examples:
- forms
- uploads
- API requests
- query parameters
- user-generated content

## File Upload Safety

For upload features:
- restrict file types
- restrict file size
- sanitize filenames
- avoid executing uploaded files
- store files securely
- scan or validate content where appropriate

## API Security

- Do not expose private API keys to frontend code.
- Use server-side routes for sensitive calls.
- Validate request methods.
- Validate request bodies.
- Return safe error messages.
- Avoid leaking stack traces.

## Authentication and Authorization

- Protect private routes.
- Verify user identity server-side.
- Do not rely only on frontend checks.
- Apply least-privilege access.
- Separate admin actions from normal user actions.

## Logging

Do not log:
- API keys
- passwords
- tokens
- private user data
- sensitive request bodies

## AI Agent Security Rule

If a requested change could expose secrets, weaken authentication, weaken authorization, leak data, or reduce security, stop and explain the risk before proceeding.
