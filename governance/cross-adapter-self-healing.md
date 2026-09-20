# Cross-Adapter Self-Healing

Every Agent Eco-aware specialist validates the complete adapter set declared in `.agenteco/manifest.yml`, not only the adapter used by the active AI tool. A surviving Codex, Claude, Copilot, Gemini, or verified DeepSeek session must therefore detect and repair another required adapter that was deleted or damaged.

## Manifest authority

Each adapter record declares its expected repository path and whether it is required. Self-healing restores only required adapters. An available canonical template does not by itself authorize installation of an unapproved tool adapter.

The manifest records the governance revision, canonical fingerprint, local fingerprint, validation state, reconciliation time, and reconciliation-history path. Missing or placeholder evidence is treated as incomplete configuration rather than proof of compliance.

## Startup and preflight behaviour

After the active tool loads any surviving Agent Eco adapter, preflight must:

1. enumerate every manifest-required adapter;
2. verify that each expected path exists;
3. verify managed markers and the canonical fingerprint;
4. classify deletion, truncation, stale content, drift, and conflict;
5. automatically restore missing or non-compliant canonical content under Instruction Adapter Integrity;
6. inspect Git history for the most recent compliant local section when the file was deleted;
7. restore that local section only when it remains compatible with current governance;
8. otherwise restore the canonical adapter with an empty local placeholder and report the unrecoverable customization;
9. update manifest evidence and reconciliation history; and
10. verify the complete required set again.

Recovery from Git history never promotes an old canonical section over current Agent Eco Space. Canonical content always comes from the current verified governance revision.

## Total-loss boundary

If every repository adapter is deleted, a newly opened AI may have no instruction telling it that Agent Eco Space exists. Agent intelligence cannot overcome undiscoverable governance. Recovery then requires at least one external signal:

- the complete governance-upgrade prompt;
- the first-time bootstrap prompt; or
- the repository's adapter-integrity CI check.

The CI check detects missing files, malformed managed sections, and canonical fingerprint mismatches. It fails closed and reports remediation; it must not commit, push, open a pull request, or rewrite files automatically.

## Boundaries

Cross-adapter repair uses the narrow automatic local compliance authorization. It never authorizes product changes, context changes, installation of optional adapters, or writes to Agent Eco Space. A specialist may create a product-repository pull request containing the repair but must never merge it.
