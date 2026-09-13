# Repository Readiness Preflight

Every Agent Eco Space entry workflow runs this compact preflight before assuming a repository is configured. This includes first-time bootstrap, normal calls, product adoption, adding a repository, synchronizing existing work, and refreshing Agent Eco Space understanding.

## Fast path

Read `.agenteco/manifest.yml` first. When it exists, validate its recorded governance version, product context, repository identity, adapters, work mode, delivery model, and last verified repository revision. Inspect deeper only when the manifest is missing, stale, inconsistent, or insufficient for the requested work.

## Checks

1. Agent Eco Space governance location, access, and recorded version.
2. Product name, application or component name, and central-context location and access.
3. Repository registration and per-repository context directory.
4. Repository identity, visibility, classification, current revision, and default specialist.
5. Application or Package work mode, operating profile, topology, permanent branches, and release model.
6. Current `AGENTS.md`, `CLAUDE.md`, and Copilot instruction adapters, including template versions, canonical and local fingerprints, and drift state.
7. Version-controlled `.agenteco/outbox/context/` and pending packages.
8. Relevant business rules, contracts, decisions, consumers, and connected repositories.
9. Context drift, dirty working-tree state, open PRs, and access or information-classification risks.

## Outcomes

- **Ready:** Continue the requested workflow.
- **Partially Configured:** Add the missing or stale setup to the requested proposal.
- **Unconfigured:** Produce a combined adoption or repository-registration proposal before the requested work.
- **Access Degraded:** Apply Access-Degraded Mode, continue only where safe, and preserve pending context in the tracked outbox.
- **Blocked:** Stop only the affected work and state the exact missing authority or evidence.

## Mutation boundary

The preflight is read-only. It never silently creates adapters, manifests, context directories, or registrations. The selected specialist presents one combined proposal and waits for the standalone `Proceed with implementation.` command.

After authorization, prepare separate PRs for the code repository and central context where both are affected. Never merge either PR.
