# Product Governance Snapshot Manifest

Use this as a human-readable guide alongside the required complete `context/governance/mirror/` copy and any optional compact `context/governance/manifest.json`, `core.md`, and `roles/<specialist>.md`. Generate the complete copy with `tools/build_governance_mirror.py` from a clean, merged Agent Eco checkout after audience and license review. Use `tools/verify_governance_mirror.py` to check offline integrity. Generate optional role snapshots with `tools/build_governance_snapshot.py`. Neither local check proves canonical freshness without source access.

| Field | Value |
| --- | --- |
| Product | `<product>` |
| Canonical governance repository | `https://github.com/ikechukwukalu/agenteco` |
| Governance version | `<VERSION>` |
| Exact merged governance commit | `<commit>` |
| Snapshot generated at | `<date and time>` |
| Snapshot fingerprint | `<hash of included files>` |
| Complete mirror path and fingerprint | `context/governance/mirror/` at `<content_sha256>` |
| Product context commit at generation | `<commit>` |
| Authorized audience and classification | `<audience/classification>` |
| Included role sections | `<paths>` |
| Canonical source paths | `<paths>` |
| Active rule-index path and revision | `context/rules/index.md` at `<revision>` |
| Availability catalogue path and revision | `context/releases/feature-availability.md` at `<revision>` |
| Last verification result | `<matched/stale/conflicting/unavailable>` |

Each role section summarizes applicable canonical controls and points to current product records. It must retain the safeguards listed in [Versioned Governance Snapshots](../../governance/versioned-context-snapshots.md). Never interpret this file alone as a current customer release or an installed live tool.
