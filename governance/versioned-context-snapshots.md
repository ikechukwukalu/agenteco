# Versioned Governance Snapshots

## Canonical release identity

`VERSION` at the Agent Eco Space repository root is the readable governance version. Every governance-changing pull request must advance it before merge. Use a major increment for incompatible safeguards or schemas, a minor increment for new compatible capabilities, and a patch increment for compatible corrections. A merge does not authorize a tag or publication; the human owner controls those separately.

Record both the version and the exact merged commit. The pair identifies immutable source content; a matching version with a different commit is a conflict, not a cache hit. A context commit is a third, independent version and must never be confused with the governance version.

## Complete product mirror

An authorized product context stores a version-controlled complete Agent Eco mirror at `context/governance/mirror/`. Its `repository/` directory reproduces every regular Git-tracked file from one merged canonical Agent Eco commit, including `VERSION`, but not `.git`, untracked files, protected environment files, or credentials. Its manifest records the product, audience classification, canonical repository, version, exact commit and tree, file modes, sizes, SHA-256 hashes, and a content fingerprint. This is a read-only distribution, not a second authority or permission to edit Agent Eco.

Before installation, confirm that every reader of the context repository is authorized under the proprietary Agent Eco license and product classification. If not, use a separately approved restricted destination. Never grant access to private governance merely to make the cache convenient.

1. Verify the mirror's manifest, full file inventory, hashes, and `VERSION` before use. This proves internal integrity, not freshness or source authenticity by itself. The human-merged context PR and recorded source commit establish its approved provenance.
2. With canonical access, compare the canonical **version and exact merged commit** to the mirror. On a match, read the mirror; do not re-download unchanged governance. A different commit at the same version is a conflict. A newer canonical version makes the mirror stale. An apparently newer mirror than the accessible checkout is a conflict or stale checkout, not permission to downgrade.
3. Only a specialist with approved canonical read access and product-context write access may prepare a refresh PR, under applicable context-update authorization. Build from the merged canonical commit, verify the complete copy, review the changed files and audience, and preserve version history in the PR. A human merges it. Source read access alone never grants canonical Agent Eco write authority.
4. Without canonical access, use only the last human-approved, internally verified mirror for the authorized audience. Disclose to an authorized internal user that its freshness could not be checked; do not claim it is current or edit it. If damaged, unapproved, conflicting, or missing relevant safeguards, apply Access-Degraded or Governance-Uncertain Mode and stop affected mutation. Customer-facing Ada must not expose this internal check.
5. A new mirror PR is pending, not effective. The previous approved copy remains effective until human merge is verified. A version match without a commit match is never sufficient.

Build from a clean checkout of a merged canonical commit into an empty directory outside Agent Eco, then verify before submitting a product-context PR:

```text
python3 tools/build_governance_mirror.py --product '<product>' --classification '<authorized audience>' --output '<empty-output-directory>'
python3 tools/verify_governance_mirror.py '<output-directory>'
```

The verifier checks offline integrity only and explicitly does not establish the latest canonical version. Existing CI rejects a governance PR unless `VERSION` increases over its base; every governance change, including a small correction, requires this increase.

## Product snapshot

Each central product context may also carry a compact, version-controlled `context/governance/` snapshot. Its `manifest.json` records the canonical repository, governance version and commit, generated-at time, snapshot content fingerprint, product-context commit at generation, audience, included specialist sections, and source paths. The snapshot contains `core.md` and only the selected `roles/<specialist>.md` files. It is a faster local reading aid, not a replacement for the complete mirror or permission to change Agent Eco Space.

The snapshot must retain non-negotiable controls: implementation authorization, confidentiality, source and information authority, adapter integrity, test and QA decisions, release and publication gates, and the prohibition on AI merging pull requests. It may omit unrelated role detail. No secret, customer record, protected environment value, or unauthorized proprietary content may be copied. Readers need the permissions required by the Agent Eco Space license and the product context's access classification.

For repository-based sessions, the local adapter and manifest point to the product snapshot and exact repository context. Repository-free Business Context Mode supplies the central-context location and presenter identity in its entry prompt. A fresh chat has no remembered rules; it must load its applicable snapshot or canonical source before answering.

## Fast validation and refresh

1. Read the product snapshot manifest and the small canonical `VERSION` plus merged commit reference. Verify the product snapshot fingerprint and that its recorded version and commit match the canonical pair. Do not reread all canonical pages on a verified match.
2. Load only the applicable specialist section, active scoped product rules, relevant decisions, and task or audience-specific availability records. Fetch live facts only when requested and permitted.
3. If the canonical pair changed, the snapshot is missing or damaged, or applicability is uncertain, use the current canonical governance and reconcile the product snapshot through a product-context pull request. Never treat a stale snapshot as current or silently overwrite it. Local managed adapters follow their existing automatic compliance rule.
4. If canonical access is unavailable, first verify and use the last approved full mirror for the authorized audience. Disclose the freshness limitation to an authorized internal user and apply Access-Degraded Mode where needed. Customer-facing Ada gives a natural limitation without revealing governance. Do not use a damaged or conflicting mirror or snapshot; do not authorize affected mutation or a customer claim from unverified release data.

After a human merges an Agent Eco Space change, affected product mirrors and snapshots become stale until synchronized. The changing Agent Eco specialist records impacted roles, templates, manifest fields, and mirror/snapshot migration notes in the release entry. Product specialists update their own central context when authorized; no Agent Eco specialist automatically writes to every product repository.

The snapshot can reduce repeated reading and prompt size, but a remote comparison and initial load still take time. It does not promise an instantaneous first response.

After the governance PR is merged, generate from a clean Agent Eco checkout and copy the output into a temporary branch of the product context:

```text
python3 tools/build_governance_snapshot.py --product '<product>' --context-revision '<context-commit>' --classification '<authorized audience>' --roles Ada Chinedu Dotun --output '<empty-output-directory>'
python3 tools/verify_governance_snapshot.py '<output-directory>'
```

Review the generated files and open a context PR. Never overwrite an existing snapshot directory without reviewing its changes. The verifier checks the file hashes and canonical version/commit against the checked-out Agent Eco source. For a fast remote freshness check, first compare the canonical `VERSION` and merged commit, then run the verifier only when needed.
