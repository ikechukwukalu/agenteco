# Versioned Governance Snapshots

## Canonical release identity

`VERSION` at the Agent Eco Space repository root is the readable governance version. Every governance-changing pull request must advance it before merge. Use a major increment for incompatible safeguards or schemas, a minor increment for new compatible capabilities, and a patch increment for compatible corrections. A merge does not authorize a tag or publication; the human owner controls those separately.

Record both the version and the exact merged commit. The pair identifies immutable source content; a matching version with a different commit is a conflict, not a cache hit. A context commit is a third, independent version and must never be confused with the governance version.

## Product snapshot

Each central product context may carry a compact, version-controlled `context/governance/` snapshot. Its `manifest.json` records the canonical repository, governance version and commit, generated-at time, snapshot content fingerprint, product-context commit at generation, audience, included specialist sections, and source paths. The snapshot contains `core.md` and only the selected `roles/<specialist>.md` files. It is a local reading aid, not a second authority or permission to change Agent Eco Space.

The snapshot must retain non-negotiable controls: implementation authorization, confidentiality, source and information authority, adapter integrity, test and QA decisions, release and publication gates, and the prohibition on AI merging pull requests. It may omit unrelated role detail. No secret, customer record, protected environment value, or unauthorized proprietary content may be copied. Readers need the permissions required by the Agent Eco Space license and the product context's access classification.

For repository-based sessions, the local adapter and manifest point to the product snapshot and exact repository context. Repository-free Business Context Mode supplies the central-context location and presenter identity in its entry prompt. A fresh chat has no remembered rules; it must load its applicable snapshot or canonical source before answering.

## Fast validation and refresh

1. Read the product snapshot manifest and the small canonical `VERSION` plus merged commit reference. Verify the product snapshot fingerprint and that its recorded version and commit match the canonical pair. Do not reread all canonical pages on a verified match.
2. Load only the applicable specialist section, active scoped product rules, relevant decisions, and task or audience-specific availability records. Fetch live facts only when requested and permitted.
3. If the canonical pair changed, the snapshot is missing or damaged, or applicability is uncertain, use the current canonical governance and reconcile the product snapshot through a product-context pull request. Never treat a stale snapshot as current or silently overwrite it. Local managed adapters follow their existing automatic compliance rule.
4. If canonical access is unavailable, disclose the limitation to an authorized internal user and apply Access-Degraded Mode. Customer-facing Ada gives a natural limitation without revealing governance. Do not use a damaged or conflicting snapshot; do not authorize new repository mutation or a customer claim from unverified release data.

After a human merges an Agent Eco Space change, affected product snapshots become stale until synchronized. The changing Agent Eco specialist records impacted roles, templates, manifest fields, and snapshot migration notes in the release entry. Product specialists update their own central context when authorized; no Agent Eco specialist automatically writes to every product repository.

The snapshot can reduce repeated reading and prompt size, but a remote comparison and initial load still take time. It does not promise an instantaneous first response.

After the governance PR is merged, generate from a clean Agent Eco checkout and copy the output into a temporary branch of the product context:

```text
python3 tools/build_governance_snapshot.py --product '<product>' --context-revision '<context-commit>' --classification '<authorized audience>' --roles Ada Chinedu Dotun --output '<empty-output-directory>'
python3 tools/verify_governance_snapshot.py '<output-directory>'
```

Review the generated files and open a context PR. Never overwrite an existing snapshot directory without reviewing its changes. The verifier checks the file hashes and canonical version/commit against the checked-out Agent Eco source. For a fast remote freshness check, first compare the canonical `VERSION` and merged commit, then run the verifier only when needed.
