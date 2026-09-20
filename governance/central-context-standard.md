# Central Context Standard

## One context repository per product

A product uses one central context repository across customer and internal applications, mobile apps, backends, microservices, SDKs, packages, and infrastructure repositories.

## Required structure

```text
context/
  README.md
  product/
    overview.md
    glossary.md
    architecture.md
    repository-map.md
    ecosystem-intake.md
  business-rules/
    index.md
  contracts/
    apis/
      route-inventory.md
      consumer-map.md
      consumer-expectations.md
      impact-alerts.md
    events/
    data/
  decisions/
    index.md
  handoffs/
  synchronization/
    processed-packages.md
  repositories/
    <repository-name>/
      README.md
      current-state.md
      roadmap.md
      decisions.md
      documentation.md
      task-history.md
  releases/
  risks/
```

The structure may expand, but shared truth and per-repository ownership must remain distinguishable.

API records use the canonical [API–Consumer Compatibility Map](../templates/product-context/api-consumer-compatibility.md). A backend specialist initializes the route and known-consumer baseline. Every producer and consumer specialist then progressively maintains the rows affected by its work. Shared alerts are linked from the producer and every affected consumer context directory.

The synchronization ledger records every accepted offline Context Update Package using its identifier, fingerprint, source repository and commit, destination records, context PR, merge commit, and synchronization date. This prevents another specialist from publishing the same offline update twice.

## Business-rule lifecycle

When a rule changes, do not erase it. Mark it superseded or deprecated; record its effective period, replacement, reason, decision owner, and affected repositories; then update affected contracts and repository context.

## Repository evidence and drift

Implementation context records the commit, release, or dated repository state against which it was verified. The code repository is authoritative for code that exists. Approved business context is authoritative for intended product meaning.

If these disagree, record context drift, determine what must change, and never silently choose one.

## Specialist responsibility

The active specialist updates the active repository context, changed shared contracts, API-consumer relationships, affected business rules and decisions, cross-repository handoffs, documentation inventory, task history, verification references, and the pre-PR Armstrong QA decision and verdict when applicable. A consumer specialist records newly implemented API use; a backend specialist records producer changes and consumer impact. The record must be detailed enough for another specialist to continue without reconstructing the work from conversation history, but it must never contain protected `.env` or `.env.*` values.

The first verified product session loads the complete accessible ecosystem and records its coverage in `context/product/ecosystem-intake.md`. Later tasks use the repository-scoped fast path while always refreshing active business rules and decisions. Full ecosystem refreshes require human approval and are recommended when freshness or drift triggers apply.
