# Instruction Adapter Integrity

`AGENTS.md`, `CLAUDE.md`, and `.github/copilot-instructions.md` are governed Agent Eco Space adapters. Human edits are permitted, but no edit silently replaces canonical governance.

## Managed and local sections

Each adapter separates its content using these markers:

```text
<!-- AGENT-ECO:CANONICAL-START -->
<!-- AGENT-ECO:CANONICAL-END -->
<!-- AGENT-ECO:LOCAL-START -->
<!-- AGENT-ECO:LOCAL-END -->
```

The canonical section contains the applicable Agent Eco Space adapter. The local section contains repository-specific commands, architecture notes, and other authorized instructions that do not weaken canonical safeguards.

## Preflight validation

The repository manifest records each adapter's expected template version, canonical-section fingerprint, local-section fingerprint, last verified revision, validation state, and any drift or conflict.

The preflight classifies a difference as an authorized local customization, outdated adapter, accidental drift, or conflicting instruction. It preserves valid local additions and rejects local instructions that weaken implementation authorization, source authority, engineer-owned testing, context synchronization, pull-request merge restrictions, security, or release controls.

## Reconciliation

Agent Eco Space never silently overwrites or reverts a human edit. The selected specialist reports the exact difference, preserves history, and presents a reconciliation proposal. Changes require the standalone `Proceed with implementation.` command and are delivered through a pull request that the specialist must not merge.
