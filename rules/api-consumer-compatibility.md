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
4. form-to-API validation comparisons for user-facing consumers;
5. compatibility and risk register; and
6. Consumer Impact Alerts.

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

Before changing an existing API, the backend specialist checks the map and accessible consumer evidence. Prefer a backward-compatible change. When a change may break a consumer—or a new or changed validation requirement may make a form insufficient—create a Consumer Impact Alert with a stable identifier such as `CIA-2026-001-shipment-quote-response`. Record a verified no-impact finding when the evidence shows consumers remain compatible; do not create an alert for every harmless producer edit.

The backend specialist updates the producer contract and the affected validation-comparison rows when the API changes. The alert records the previous and new contract, exact difference, affected consumers and source locations, required changes, migration or compatibility options, producer and consumer revisions, branches and PRs, target environment or date, tests, owner, severity, and **separate status for each consumer**. If a consumer repository cannot be inspected, mark it `Unverified`; never infer compatibility from silence. Do not copy private server-only rules, customer data, or protected payloads into the shared map.

The alert must be visible from the shared API contract area, the backend context directory, and every affected consumer context directory. Every specialist checks unresolved alerts affecting its assigned repository during every preflight, even when the requested task appears unrelated. Backend and consumer specialists check again before related implementation, then promptly alert the human and propose focused work. An unrelated alert need not block otherwise safe scoped work, but it must not be hidden or described as resolved.

At **each task preflight, affected implementation proposal, PR handoff, and release-readiness check**, the backend specialist and each affected consumer specialist remind the human of still-open alerts relevant to their repositories. Give the alert link or ID, affected API and form/module, concrete consumer action, owner, environment, latest verification, and blocker or target. Combine repeated alerts into one concise status report; do not interrupt every unrelated message. A specialist with no central-context access uses the version-controlled Context Update Package flow and reports that the alert is pending, not shared. New or changed evidence updates the alert rather than generating a duplicate reminder record.

An alert remains open until **every** affected consumer is verified compatible at the relevant revisions and environment, or is demonstrably retired. A human-approved, time-bounded exception may allow a release under the release-protection rule, but does **not** assert compatibility or remove the alert; keep its risk, expiry, mitigation, and reminders visible until the underlying consumer issue is resolved or retired. Resolve through a human-reviewed context PR only after checking consumer code and tests, producer contract, affected deployment/version state, and any outstanding validation gaps. Preserve the alert's history as `Resolved` rather than deleting it. An agent never marks another repository updated without repository evidence.

## Form-to-API validation comparison

For every affected user-facing form or native-mobile input flow, the consumer specialist compares the **current backend validation contract** with what the interface collects, explains, checks, submits, and does when the server rejects a value. Check required and conditionally required fields, types, ranges, formats, cross-field and business-state conditions, file constraints, and customer-safe error identifiers where relevant. Record producer and consumer revisions, the form location, evidence, and the status of each gap in the canonical table. Repeat the comparison when a mapped backend rule changes, an alert is raised, or a new form starts using the API; do not re-audit unrelated forms without a freshness trigger.

Flag a gap when the form omits a required input, allows an avoidable rejection, hides a conditional requirement until submit, sends the wrong payload, or cannot guide a person to correct a backend rejection. Present known safe requirements early, preserve permissible entries, and map stable server errors to the correct visible field or step. Backend validation remains authoritative; client checks cannot replace it. A condition that only the backend can evaluate needs an approved safe requirements/eligibility response or honest server-side correction path, not a guessed client rule. Link material gaps to the Consumer Impact Alert and the feature's FARS record until verified corrected.

## Release protection

A known breaking API change must not be released to production while an affected consumer remains incompatible unless the human explicitly approves and records an exception with impact, duration, owner, mitigation, and rollback or recovery plan.

API documentation, feature documentation, examples, tests, `CHANGELOG.md`, shared contracts, repository context, risks, and Consumer Impact Alerts must remain synchronized.
