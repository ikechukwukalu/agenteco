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
6. The complete manifest-required adapter set—not only the active tool's file—including path existence, managed markers, template versions, canonical and local fingerprints, and drift state. Automatically restore deleted or non-compliant required adapters under [Cross-Adapter Self-Healing](cross-adapter-self-healing.md). When DeepSeek is used, verify its host client, discovery mode, actual instruction path, and loading evidence; never assume a universal DeepSeek instruction file.
7. Version-controlled `.agenteco/outbox/context/` and pending packages.
8. Relevant business rules, contracts, decisions, consumers, and connected repositories.
9. Context drift, dirty working-tree state, open PRs, and access or information-classification risks.
10. Current implementation-authorization state and any unresolved governance suspension, uncertainty, or unauthorized-change incident.
11. Initial ecosystem-intake status, its context revision and date, assigned repository context directory, connected-repository coverage, and refresh-due state.
12. Documentation inventory, API/feature documentation tooling, generation or validation commands, and `CHANGELOG.md` status.
13. Consumer Impact Alerts affecting the assigned repository on every preflight. For API or integration work, also verify route-inventory baseline status, mapped producer and consumer revisions, relationship confidence, and compatibility risks.
14. Protected environment-file handling: confirm `.env` and `.env.*` files other than exact `.env.example` will not be read or disclosed, value-bearing files remain untracked, and planned secret insertion has explicit authorization and a non-disclosing mechanism.

## Outcomes

- **Ready:** Continue the requested workflow.
- **Partially Configured:** Add the missing or stale setup to the requested proposal.
- **Unconfigured:** Produce a combined adoption or repository-registration proposal before the requested work.
- **Access Degraded:** Apply Access-Degraded Mode, continue only where safe, and preserve pending context in the tracked outbox.
- **Blocked:** Stop only the affected work and state the exact missing authority or evidence.
- **Governance Uncertain:** Stop mutation, preserve existing work, reconcile authority, restate scope, and require fresh authorization.

## Mutation boundary

The preflight is read-only except for the narrow automatic local adapter-compliance repair defined by [Instruction Adapter Integrity](instruction-adapter-integrity.md). It never silently creates product context directories, registrations, or non-governance changes. The selected specialist presents one combined proposal and waits for the standalone `Proceed with implementation.` command for everything outside that exception.

After authorization, prepare separate PRs for the code repository and central context where both are affected. Never merge either PR.
