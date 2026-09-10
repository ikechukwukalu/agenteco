# Internal Administration Interface Standard

## Purpose

Every application managed by Agent Eco Space must include one or more authenticated internal administration or back-office interfaces. This is a permanent product-design baseline, not an optional afterthought.

The interface may be a dedicated admin area, an internal operations portal, or clearly separated internal modules within the application. Its design must fit the product's users and operational needs.

## Baseline Responsibilities

Before implementation, the selected specialist must identify and record:

1. the internal user roles and their least-privilege permissions;
2. the operational workflows staff must perform;
3. the required administration interfaces or modules;
4. audit, monitoring, reporting, and support needs;
5. internal-versus-customer-facing route and access boundaries;
6. authentication, step-up verification, session, privacy, retention, and incident requirements.

The Project Context must contain the approved internal-interface scope and ownership.

## Access and Safety

- Internal administration functions must require authenticated, authorized staff access.
- Customer-facing pages, guest sessions, public APIs, and customer phone/chat channels must not expose internal administration actions.
- Administrative actions that change sensitive customer, financial, operational, policy, or knowledge data must be auditable and use the relevant confirmation/approval workflow.
- Interfaces must be designed for staff operations, not assumed to be safe merely because a route is hidden.

## Ada Relationship

The Ada Support Capability remains optional. When a project selects it, the internal administration interface is where staff manage Ada's settings, presenter identity, knowledge sources, knowledge governance, approvals, handoff routing, and monitoring. Customer-facing chat and phone interfaces may consume published Ada capability but may never administer it.

## selected specialist Readiness Review

Before a feature enters `test`, the selected specialist must report the internal-interface status: required modules, completed and pending workflows, role coverage, access boundaries, audit evidence, and open risks. The report must be repeated for production-release readiness.

