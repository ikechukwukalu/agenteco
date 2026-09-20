# API–Consumer Compatibility Mapping

Agent Eco Space maintains a progressive, product-wide map between APIs and every known web, mobile, SDK, service, administrative, partner, and third-party consumer. The map exists so specialists can detect when work on either side may break an existing integration before the failure reaches users.

## Backend-owned initial baseline

For an existing product, the selected backend specialist initializes the current state before incremental maintenance begins. For each backend—beginning with the designated core backend—the specialist must:

1. inventory every current route from framework and source evidence;
2. record method, URI, name, handler, authentication, middleware, version, purpose, lifecycle, documentation source, and verified backend revision;
3. identify every known consumer and inspect accessible consumer repositories for actual call sites;
4. record request data, response fields relied upon, authentication, error handling, pagination, state, and other behavioural assumptions;
5. distinguish verified relationships from declared, suspected, inaccessible, or drifted relationships;
6. record compatibility risks and existing mismatches; and
7. publish the baseline in the central context using the canonical tables.

The backend specialist must not claim complete consumer coverage when a repository is inaccessible or evidence is missing. Record the gap and confidence explicitly.

The initial baseline is performed once per backend or after an approved material remapping. Later tasks use incremental updates and do not rescan every route or consumer unless a freshness, coverage, or drift trigger justifies it.

## Collaborative progressive ownership

The map is not backend-only documentation:

- Backend specialists own producer truth: route existence, validation, behaviour, responses, errors, authentication, deprecation, and compatibility intent.
- Frontend, mobile, SDK, service, and integration specialists own consumption truth: repository, module, source call site, request sent, response fields used, error handling, assumptions, tests, and consumer revision.
- A consumer specialist that introduces new API use records it immediately as `Consumer Declared`, verifies it against backend evidence, and advances its status as evidence becomes available.
- Any specialist discovering a mismatch or fragile assumption records the risk and alerts the human.
- No second specialist starts automatically. The active specialist recommends the relevant producer or consumer specialist and waits for human approval.

The code repositories remain authoritative for implemented producer and consumer behaviour. Central context records the verified relationship and its evidence.

## Required tabular records

Use [the canonical API–Consumer Compatibility tables](../templates/product-context/api-consumer-compatibility.md):

1. backend route inventory;
2. route-to-consumer map;
3. consumer contract expectations;
4. compatibility and risk register; and
5. Consumer Impact Alerts.

Every row records the backend and consumer revisions used as evidence. Keep historical alerts and superseded relationships; mark their lifecycle instead of deleting the reason they changed.

## Confidence and lifecycle

Relationship confidence uses only these values:

- `Backend Verified`
- `Consumer Verified`
- `Bidirectionally Verified`
- `Declared, Not Verified`
- `Suspected`
- `Drift Detected`

Consumer relationship status uses only these values:

- `Consumer Declared`
- `Contract Verified`
- `Integration Tested`
- `Backend Acknowledged`
- `Compatibility Risk`
- `Update Required`
- `Verified Compatible`
- `Deprecated`

## Consumer Impact Alerts

Before changing an existing API, the backend specialist checks the map and accessible consumer evidence. Prefer a backward-compatible change. When a change may break a consumer, create a Consumer Impact Alert with a stable identifier such as `CIA-2026-001-shipment-quote-response`.

The alert records the previous and new contract, exact breaking difference, affected consumers and source locations, required changes, migration or compatibility options, producer and consumer revisions, branches and PRs, target environment or date, tests, owner, severity, and per-consumer status.

The alert must be visible from the shared API contract area, the backend context directory, and every affected consumer context directory. Every specialist checks unresolved alerts affecting its assigned repository during every preflight, even when the requested task appears unrelated. Backend and consumer specialists check again before related implementation, then promptly alert the human and propose focused work. An unrelated alert need not block otherwise safe scoped work, but it must not be hidden or described as resolved.

An alert remains open until each affected consumer is `Verified Compatible`, deprecated, or covered by an explicit human-approved exception. An agent never marks another repository updated without repository evidence.

## Release protection

A known breaking API change must not be released to production while an affected consumer remains incompatible unless the human explicitly approves and records an exception with impact, duration, owner, mitigation, and rollback or recovery plan.

API documentation, feature documentation, examples, tests, `CHANGELOG.md`, shared contracts, repository context, risks, and Consumer Impact Alerts must remain synchronized.
