# Product Context Template

Use this template to create the single central context repository for a governed product.

## Product declaration

- Product name:
- Purpose:
- Industry or domain:
- Context owner:
- Default delivery model:
- Repositories covered:

## Repository map

For every repository, record its name and location, classification, framework and runtime, audience, responsibilities, contracts produced and consumed, connected repositories, default specialist, delivery model, protected branches, and current verified commit or release.

Record one complete ecosystem intake with its date, central-context revision, repository revisions reviewed, relationship coverage, access gaps, and next reminder date. Later specialists use this as a durable baseline rather than repeating full discovery.

## Shared catalogues

Create catalogues for business rules, vocabulary, architecture, API/event/data contracts, decisions, risks, releases, and cross-repository handoffs.

Create the [scoped product rule index](scoped-rules.md), preserving existing authoritative business-rule files and recording who each rule applies to. For DTAP products, create the shared [feature availability catalogue](feature-availability.md) with evidence for each required component and environment. After audience and license review, install a [complete versioned governance mirror](governance-snapshot.md) in `context/governance/mirror/`; the compact role snapshot remains an optional faster reading aid. Match version, exact commit, and fingerprint against Agent Eco Space when canonical access exists.

Create the tabular [API–Consumer Compatibility Map](api-consumer-compatibility.md). The backend specialist initializes every current route and known consumer using verified revisions. Consumer specialists progressively add and verify new usage, call sites, request and response dependencies, tests, risks, and compatibility status.

Products opting into automatic production-to-context reconciliation add a human-reviewed [registration and authorization record](production-reconciliation-registration.json) or map an existing equivalent registry to its fields. It records the central destination, source allowlist and production branches, separate setup and documentation grants, and secret **names**, never credential values. The source workflow is rendered from that registration using the [canonical notification template](../production-context-notification.yml).

## Per-repository context

Each repository directory includes current state, roadmap, decisions, documentation tooling, task history, produced and consumed contracts, sibling relationships, last verified revision, and continuity records. Task history must explain what changed and why, not merely link to a diff.

Each repository directory records purpose, current state, setup, interfaces, dependencies, decisions, roadmap, known risks, testing, deployment, and the repository revision against which it was verified.
