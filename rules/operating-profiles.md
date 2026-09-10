# Operating Profiles

## Purpose

Operating profiles set the required delivery rigor for a project. They are not technology choices, feature restrictions, or Magic Make generation modes.

A project may use full-stack Laravel or a Laravel REST API with separate frontend applications at any profile. A capability such as multiple interfaces, Ada, APIs, phone support, or formal security controls may be used at any profile when the Project Owner requires it. The profile defines the default planning depth, evidence, and release controls.

## Selection and Default

At startup, the selected specialist must first establish whether the work mode is **Application** or **Package**, then ask the Project Owner to select **Lite**, **Standard**, or **Enterprise**.

For this Project Owner, **Enterprise is the default**. Do not downgrade a project without explicit Project Owner approval. The selected specialist may recommend a different profile with reasons, but must record the selected profile and rationale in Project Context.

## Universal Baseline

Every profile requires:

- approved Project Context;
- explicit approval before implementation;
- clear ownership and scope;
- proportionate testing and security review;
- current documentation;
- controlled delivery through lowercase `test`, `staging`, and `production`;
- at least one authenticated internal administration or back-office interface.

## Startup Checklist

Before feature planning, the selected specialist must capture:

1. product purpose, users, and business outcome;
2. operating profile;
3. delivery topology: full-stack Laravel or API-core with separate SPA interfaces;
4. repositories and declared interfaces, including their roles;
5. internal administration/back-office requirements;
6. material capabilities and constraints, including integrations, sensitive data, compliance, payments, Ada, customer channels, and release dependencies.

The checklist is a concise start, not a substitute for Project Context. The selected profile determines how much detail and evidence is required next.

## Lite

Lite is for low-risk, tightly scoped work.

Required delivery bar:

- concise Project Context with purpose, scope, owners, key decisions, risks, and release notes;
- a single application repository by default; additional repositories are allowed when declared;
- one primary interface and a minimal internal administration surface;
- focused tests for changed behavior;
- concise API or integration notes where relevant;
- compact operational documentation and controlled release evidence.

Not automatically required unless scope demands it:

- component contexts;
- formal architecture decision records;
- a cross-repository delivery matrix;
- full observability design;
- formal Ada knowledge governance.

## Standard

Standard is for normal production applications and integrations.

Required delivery bar:

- full Project Context covering product, technical, delivery, security, and operational decisions;
- clear roles, permissions, integrations, and API contracts;
- documented test strategy and regression evidence;
- maintained operational, support, and release documentation;
- explicit interface and repository mapping when more than one component exists;
- readiness review appropriate to the application’s risk.

Not automatically required unless scope demands it:

- enterprise-wide interface registry;
- formal cross-repository release coordination;
- comprehensive audit, observability, or Ada governance controls.

## Enterprise

Enterprise is for products with material customer, operational, regulatory, security, integration, or multi-interface complexity. It is this Project Owner’s default.

Required delivery bar:

- a shared platform Project Context and component contexts where useful;
- an explicit platform map, interface registry, API contracts, and consumer mapping;
- a feature delivery matrix showing backend and affected interface work;
- role-based access, auditability, security/privacy assessment, and observability expectations;
- documented integrations, operational runbooks, support readiness, and formal release evidence;
- cross-repository planning and coordinated promotion through DTAP;
- formal architecture decisions for material trade-offs;
- when Ada is enabled: approved resource registry, handoff policy, knowledge governance, and readiness review.

## Escalation

If the chosen profile cannot safely cover the discovered scope, the selected specialist must recommend raising the profile before implementation. No profile permits bypassing a higher-precedence governance, safety, privacy, or approval rule.

