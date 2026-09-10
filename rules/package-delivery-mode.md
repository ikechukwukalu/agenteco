# Package Delivery Mode

## Purpose

Package Delivery Mode governs reusable libraries, frameworks, boilerplates, plugins, and developer tooling. It is a work mode, not an operating profile.

At startup, the selected specialist must establish two independent choices:

1. **Work mode:** Application or Package.
2. **Operating profile:** Lite, Standard, or Enterprise.

For most packages, the default is **Package mode + Lite profile**. The profile may be raised when compatibility, consumer impact, security, or release risk requires more rigor.

## Package Workflow

Package work does not use application-only DTAP environment promotion. Instead, the selected specialist must:

1. load the package and its Project Context repositories;
2. inspect the package, existing public package, supported versions, and current release state;
3. agree objectives, scope, and a precise roadmap;
4. plan and implement through a temporary branch and pull request after explicit approval;
5. verify tests, static analysis or linting where available, dependency/security posture, supported framework/runtime versions, and backward compatibility;
6. update public package documentation, examples, changelog, upgrade notes, and support matrix as applicable;
7. recommend a Semantic Versioning release number;
8. obtain explicit Project Owner approval before tagging, creating a release, or publishing to a registry.

## Required Package Context

Project Context for a package must identify:

- development/source repository, public package repository, and context repository where they are separate;
- package purpose, consumers, supported versions, dependencies, and release channels;
- public API or command surface;
- compatibility and deprecation policy;
- current roadmap, release history, and known risks.

## UI Replica Work

When a package includes a reference implementation, demonstration site, or playground that must be faithfully rebuilt across frameworks, activate [UI Replica Mode](ui-replica-mode.md). The package Project Context must retain the parity matrix, specifications, and acceptance evidence.

## Scope Boundary

Do not require application-only concerns unless they are genuinely relevant: DTAP environments, customer interfaces, internal administration surfaces, production operations, and Ada capability are normally out of scope for a package.

Package mode never removes higher-precedence requirements for approval, security, privacy, documentation, or release authorization.

## Rigor Escalation

The selected specialist must recommend raising the operating profile when a package has material consumer impact, breaking changes, broad support-matrix changes, security-sensitive behavior, complex integrations, or coordinated releases across dependent products.

