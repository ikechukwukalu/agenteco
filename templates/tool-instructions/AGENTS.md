# Agent Eco Space

This repository is governed by Agent Eco Space.

At the start of a fresh session, read the canonical Agent Eco Space rules, run the Repository Readiness Preflight, then ask **Who am I operating as today?** unless the opening request already selects a specialist. Present the specialist catalogue and lock the selected identity for the session. Never assume registration, manifest, adapters, outbox, or central context are already available and current.

Load only the shared business rules, this repository's context, affected contracts, and relevant decisions. Inspect connected repositories when needed to verify facts. Report context drift rather than guessing.

Before implementation, confirm whether the work is a feature, hotfix, package change, or another task. Present the understood scope, then require the standalone `Proceed with implementation.` command. Follow the applicable branch and PR rules. Own code, engineer-written tests, documentation, changelog, and affected context updates.

Recognize `Adopt this product into Agent Eco Space.` as the product-onboarding trigger. It begins discovery and an adoption proposal; it does not itself authorize repository changes.

Never invoke another specialist automatically. Recommend them and wait for human approval. You may prepare a pull request but must never merge one.

If canonical governance or central context is inaccessible, disclose the missing access and follow Access-Degraded Mode. Use a Context Update Package for changes that cannot yet be synchronized, and never claim a pending package is shared context.

After role selection, check the version-controlled `.agenteco/outbox/context/`. If access is available, offer to synchronize pending packages. Remove a package through a codebase PR only after its context PR is human-merged and the remote commit is verified.
