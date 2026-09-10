# Laravel and Magic Make Standard

## Purpose

This rule defines the default backend engineering standard for Laravel projects managed through Agent Eco Space. It supplements, and never replaces, the global engineering rules and DTAP governance.

## Applicability

Every new Laravel project must install and use Magic Make before feature implementation begins, unless the Project Owner explicitly approves an exception.

For existing Laravel projects, the selected specialist must assess whether Magic Make can be introduced safely and present a migration plan before making changes.

For a non-Laravel technology, Agent Eco Space remains applicable. Before implementation, the team must establish or approve a technology-appropriate equivalent that preserves the relevant architectural principles.

## Magic Make Baseline

Magic Make provides the approved opinionated Laravel feature foundation. Agents must preserve its conventions unless an approved Project Context decision changes them.

Feature generation should use the profile appropriate to the work:

- **Lean** for minimal features.
- **Standard** for normal application features.
- **Enterprise** for a full layered feature structure.

Generated feature code may target a declared path and namespace. When the project uses a modular or domain-oriented structure, all applicable artifacts must stay within the approved feature boundary.

## Response Boundary

Service-facing application operations normally return `ResponseData`, containing:

- success state;
- HTTP status code;
- message;
- data.

Business logic must not choose a view or JSON representation. Controllers and approved response helpers form the presentation boundary.

Small private or pure utility methods may return a simpler value when a `ResponseData` wrapper adds no value.

## Response Mode

Magic Make Laravel projects scaffold an explicit response mode:

- `view`
- `json`
- `auto`

Resolution order:

1. method-level override;
2. controller-level override;
3. application-wide default;
4. request negotiation only in `auto` mode.

This preserves the service layer when an application changes between server-rendered views and API-first delivery.

## selected specialist Responsibilities

Before Laravel implementation, the selected specialist must confirm:

1. Magic Make is installed or a safe adoption plan is approved.
2. The selected generation profile is appropriate.
3. The target path and namespace are explicit for modular features.
4. Response mode and permitted overrides are recorded in Project Context.
5. Generated code is reviewed for the agreed conventions and relevant tests.

## Exceptions

Any exception to this standard must be explicit, scoped, recorded in the Project Context, and must not weaken Agent Eco Space's higher-precedence approval or safety rules.

