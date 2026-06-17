# TESTING.md

## Testing Standard

Do not claim software is working unless verification occurred.

For every meaningful change:
- run relevant tests
- run build checks when available
- run lint and type checks when available
- verify affected behavior
- report failed or unavailable checks
- confirm no secrets or unrelated files were added

When testing is unavailable, state: `Not tested — theoretical implementation only.`
