# Subagent Model and Resource Efficiency (Mandatory)

Applies to every Agent Eco specialist using Cursor, regardless of provider (Codex, Claude, Gemini, Grok, or another supported model). This policy optimizes approved independent Tasks/subagents; it does not authorize additional specialist invocations.

## Auto-first model selection

1. Prefer Cursor **Auto** with **Balance** optimization when supported, available to the account, and compatible with human settings. Balance considers intelligence, speed, and cost; it does not guarantee the lowest price. Where unavailable, use the supported model/routing setting without pretending Balance is active. Cost mode is acceptable; Intelligence mode is not required by default.
2. For custom Cursor subagents (`.cursor/agents/*.md`), use `model: inherit` or omit the model setting where inheritance is the documented default. For Task launches, omit an explicit model parameter where supported. Never force premium, maximum-context, highest-intelligence, extended-thinking, or fast-priced models by default.
3. **Inheritance is not Auto routing.** A fixed parent model may be inherited. Never claim inherited models automatically receive cost-balanced Auto routing. Respect human-selected models and modes; do not silently override them.
4. Model control and billing vary by host, account, and built-in versus custom subagent. When the host requires a model outside authorized settings, disclose the limitation and obtain human direction rather than guessing.

## Token and context efficiency

Every subagent MUST receive a focused brief with the specialist identity, task, acceptance criteria, relevant verified evidence and file/commit references, independence constraints, expected output, and stopping condition. Do not inherit the implementing agent's tool history; provide the evidence necessary to perform a fresh independent review.

- Load the smallest relevant context slice, expanding only for verified dependencies or missing facts. Avoid full-chat replay, unfocused repository scans, repeated retrieval, and duplicate analysis.
- Use concise findings with actionable evidence and uncertainties; avoid verbose reports that do not improve decisions.
- Apply actual supported token, execution, and context limits where appropriate. Do not invent hard quotas or claim token savings without measurement.
- Stop unnecessary exploration when task criteria are met, but never stop necessary QA, security analysis, or testing simply to save tokens.

## Delegation, speed, and resource scaling

Delegate only meaningful, scoped work with the required human approval. Avoid redundant parallel subagents, repeated vague handoffs, and unnecessary nested delegation. Parallelize independent read-only tasks only if the host supports it and doing so improves overall efficiency without conflicting work. Give routine tasks short briefs; allow proportionate deeper investigation for architecture, security, complex failures, and independent QA. If the required resources or subagent launch capability are missing, report blocked rather than fabricating a verdict.

## Quality, authority, and evidence

Resource optimization MUST NOT weaken separate specialist execution, Armstrong QA, Samuel scoring, engineer-owned tests, security review, CAPP, CI, UAT, human authorization, PR creation gates, release approval, or the prohibition on agent merges. Never substitute same-chat role-play for genuinely independent QA to save cost or time.

When observable, report the actual subagent run ID or clickable Cursor agent link, its configured/inherited model or routing mode, resource limitations, and completed evidence. Never assert exact token usage, actual Auto routing, or model identity without host evidence. When the host cannot spawn a mandatory separate subagent, report blocked and stop the affected independent-review workflow.

## Canonical inheritance

This is mandatory for all enrolled product adapters at their next authorized reconciliation. Optional `LOCAL` reinforcement may tighten efficiency expectations but cannot weaken canonical review, evidence, model-authority, or human approval safeguards.