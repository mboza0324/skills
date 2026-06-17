# SECURITY.md

## Security Standard

Never commit secrets, tokens, passwords, private keys, production credentials, private user data, or `.env` files.

Use `.env.example` with placeholders only. Apply least privilege, validate server-side inputs, sanitize uploads, protect sensitive routes, and avoid logging secrets or private data.

Security-affecting changes must document the threat, mitigation, residual risk, validation, and rollback path.
