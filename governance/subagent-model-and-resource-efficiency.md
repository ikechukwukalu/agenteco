# Subagent Model and Resource Efficiency (Mandatory)

Applies to every Agent Eco specialist using a supported agent host, IDE, CLI, or model provider, including Cursor, Claude Code, Codex, Gemini CLI, Grok-powered hosts, and future equivalents. Supported underlying model choices may include Cursor Composer, Claude, GPT/Codex, Gemini, Grok, and others; neither class of example restricts eligibility. Agent Eco defines resource and independence outcomes, not a mandatory execution platform. This policy optimizes approved Tasks/subagents; it does not automatically authorize additional specialist invocations.

## Agent host, model, and specialist are separate concerns

Agent Eco specialist identity (Armstrong, Samuel, Chinedu, etc.) is independent of the agent host and underlying model. A developer may use Cursor with its **Composer** model as the implementing agent, or another supported model/host, without changing specialist authority or governance obligations. Composer is a model choice, not an Agent Eco specialist or a separate required host. Do not assume that selecting Composer, or any other model, creates an independent subagent, grants new permissions, or proves the host supports delegation. Verify the actual host-native isolated execution and attributable evidence before accepting specialist QA.

## Host-agnostic model selection

1. Prefer the active host's supported automatic, default, or balanced model routing where available and consistent with human choice, taking intelligence, speed, and cost into account. If such routing is unavailable, use the host's supported selection and disclose limitations. Never claim a specific cost benefit without evidence.
2. Do not force premium, maximum-context, highest-intelligence, extended-thinking, or fast-priced models by default. Adjust model capability only when warranted by risk, complexity, available host controls, and human authorization.
3. Respect explicit human model and optimization choices, including Composer selected in Cursor. Never silently substitute Auto, another model, or a different provider merely because it seems cheaper. Model inheritance is not automatically balanced routing: a fixed model inherited from the parent remains fixed unless the host demonstrates otherwise.
4. Model flags and default behavior are host-specific. For Cursor custom subagents, `model: inherit` or an omitted model field may be appropriate; for native Task launches, omit explicit model parameters where documented to inherit. **These are Cursor-specific examples, not universal syntax.** Claude Code, Codex, Gemini CLI, and other hosts must use their actual supported equivalent controls without inventing undocumented APIs or selection guarantees.
5. If a required model configuration cannot be honored, explain the constraint; do not silently override human preferences or imply a host capability that was not verified.

## Token and context efficiency

Every invoked subagent MUST receive a focused brief identifying specialist, task, acceptance criteria, verified references, evidence boundaries, independence requirements, expected output, and stopping condition. Fresh independent execution must not inherit the implementing agent's tool history; the reviewer can inspect necessary artifacts while forming its own verdict.

- Load the smallest relevant context slice and expand only for demonstrated dependencies or missing facts. Avoid entire-chat replay, repetitive retrieval, unfocused repository scans, and duplicate analysis.
- Return concise findings with actionable evidence, limitations, and next steps rather than verbose reports that add no review value.
- Use supported execution, context, and token limits appropriately. Do not invent fixed budgets, measured savings, or access to usage metering the host does not expose.
- Stop unnecessary exploration once acceptance and verification criteria are met, but never truncate necessary security investigation, QA, or tests solely to save resources.

## Delegation, speed, and resource scaling

Delegate meaningful, bounded work only with applicable human approval. Avoid duplicate agents, unnecessary nested delegation, repeated vague handoffs, or speculative parallel work. Parallelize independent tasks only when supported and worthwhile, without conflicting writes. Scale context and depth to risk: narrow documentation tasks should be lightweight; architecture, security, failures, and independent QA may require more extensive investigation.

If resources or independent agent capabilities are insufficient for a mandatory gate, report blocked rather than manufacturing evidence.

## Quality, authority, and execution evidence

Resource optimization MUST NOT weaken genuine process isolation, independent Armstrong QA, Samuel review/scoring, engineer-owned tests, security, CI, CAPP, UAT, human authorization, PR creation controls, release approvals, or the prohibition on AI merges. Do not replace independent execution with same-session role-play for speed or cost.

When available, record the host-native execution reference (task/run ID, agent link, or verifiable execution log), actual configured model/routing, and resource constraints. Never claim an actual model identity, Auto routing, token savings, or completed review without host-verifiable evidence. An agent link is not universally required if the host provides another verifiable record.

## Canonical inheritance and host adapters

Mandatory across enrolled product adapters at authorized reconciliation. Adapters translate this policy into real host-native controls; Cursor Auto/Balance and `model: inherit` are examples, not platform requirements. Product-specific `LOCAL` reinforcement may tighten budgets or review scope but MUST NOT weaken canonical independence, evidence, model choice, human approval, or release safeguards.
