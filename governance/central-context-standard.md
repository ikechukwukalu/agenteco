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
  business-rules/
    index.md
  contracts/
    apis/
    events/
    data/
  decisions/
    index.md
  handoffs/
  repositories/
    <repository-name>/
      README.md
      current-state.md
      roadmap.md
      decisions.md
  releases/
  risks/
```

The structure may expand, but shared truth and per-repository ownership must remain distinguishable.

## Business-rule lifecycle

When a rule changes, do not erase it. Mark it superseded or deprecated; record its effective period, replacement, reason, decision owner, and affected repositories; then update affected contracts and repository context.

## Repository evidence and drift

Implementation context records the commit, release, or dated repository state against which it was verified. The code repository is authoritative for code that exists. Approved business context is authoritative for intended product meaning.

If these disagree, record context drift, determine what must change, and never silently choose one.

## Specialist responsibility

The active specialist updates the active repository context, changed shared contracts, affected business rules and decisions, cross-repository handoffs, and verification references. Every specialist may read across central context but initially loads only the relevant slice.
