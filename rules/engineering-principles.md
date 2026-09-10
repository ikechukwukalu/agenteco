# Engineering Principles

All agents operate at high senior/staff-level standard.

## Core Principles

- SOLID
- DRY
- KISS
- YAGNI
- Clean Architecture where useful
- Secure by default
- Performance-aware design
- Maintainability over cleverness
- Clear naming conventions
- Testability
- Observability
- Backward compatibility where required
- Minimal blast radius

## Laravel/PHP Defaults

- Prefer Form Requests for validation.
- Prefer service classes for business logic.
- Keep controllers thin.
- Avoid N+1 queries.
- Use queues for slow or external operations.
- Use transactions for multi-step database writes.
- Use policies/gates for authorization.
- Use migrations carefully and reversibly.
- Avoid breaking API contracts without versioning.

## Frontend Defaults

- Accessible UI by default.
- Responsive design.
- Clear component boundaries.
- Predictable state management.
- Avoid duplicated API logic.
- Handle loading, empty, success, and error states.

## Delivery Defaults

- Every feature needs acceptance criteria.
- Every critical flow needs tests.
- Every deployment should include rollback thinking.
- Every major decision should be documented.

