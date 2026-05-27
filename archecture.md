# ARCHITECTURE.md

## System Overview

```text
User / Client
    ↓
Application Layer
    ↓
API / Service Layer
    ↓
Data Layer
    ↓
External Services
```

## Main Components

### Client / Frontend

Purpose:
- User interface
- Input collection
- Display logic
- Basic client-side validation

Rules:
- Do not store secrets in frontend code.
- Do not place sensitive business logic in frontend code.
- Keep components reusable.
- Keep UI logic separate from core business logic.

### Server / Backend

Purpose:
- API routes
- Authentication checks
- Authorization
- Business logic
- External API calls
- Database access

Rules:
- Validate inputs server-side.
- Handle errors clearly.
- Keep API responses consistent.
- Protect sensitive operations.

### Data Layer

Purpose:
- Persistent storage
- User data
- Application data
- Logs or analytics where appropriate

Rules:
- Avoid destructive schema changes without approval.
- Explain migrations before applying them.
- Preserve existing data.
- Add indexes for heavy queries when needed.

### External Services

Purpose:
- Third-party APIs
- AI services
- Payment services
- Email services
- Storage services
- Analytics services

Rules:
- Do not expose API keys.
- Handle rate limits.
- Handle failed responses.
- Log failures safely.

## Data Flow

```text
User submits request
    ↓
Client validates basic input
    ↓
Server validates securely
    ↓
Server performs business logic
    ↓
Server reads/writes data if needed
    ↓
Server calls external services if needed
    ↓
Result returns to client
    ↓
Client displays result
```

## Architecture Change Rule

Do not make major architecture changes without documenting:
- reason
- affected files
- risks
- migration steps
- rollback plan
