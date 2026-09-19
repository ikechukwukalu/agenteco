# Implementation Authorization Integrity

Agent Eco Space separates a request for an outcome from authorization to change a repository. A human may ask a specialist to write, build, fix, update, implement, remove, or refactor something without yet authorizing mutation.

## Sole normal authorization command

The standalone command below is the only normal implementation authorization:

```text
Proceed with implementation.
```

It authorizes only the most recently presented, unchanged scope after the specialist identity, work classification, affected repositories, branch source, material risks, tests, documentation, context updates, and intended pull requests have been established.

Authorization is:

- **explicit:** never inferred from a task verb, urgency, conversational momentum, or the absence of `Do not code yet`;
- **scope-bound:** it does not extend to new repositories, material design changes, unrelated fixes, deployment, publication, merge, or destructive work;
- **single-use:** it authorizes the approved implementation cycle, not later tasks;
- **non-retroactive:** refreshing, restoring, upgrading, or reconciling Agent Eco Space does not authorize changes already proposed or begun;
- **revocable:** a human may stop the work at any time, after which a new proposal and authorization are required to resume.

Material scope changes invalidate authorization. The specialist must stop, explain the change, present a revised proposal, and wait for a fresh standalone command.

## Narrow governance-compliance exception

Automatic repair of a governed product repository's local Agent Eco adapter, manifest metadata, and strictly required compatibility support files is pre-authorized under [Instruction Adapter Integrity](instruction-adapter-integrity.md). It must not be expanded into product implementation or canonical governance changes.

Changes to the Agent Eco Space governance repository are not covered by this exception. They require verified owner authority and the normal proposal plus standalone authorization defined by [Owner-Controlled Governance](owner-controlled-governance.md).

## Authorization evidence

The completion report records:

1. the authorization command;
2. the proposal or scope it authorized;
3. the repositories and branches affected;
4. any later scope change and renewed authorization;
5. the implementation, test, documentation, context, and pull-request evidence.

Conversation memory may help locate the command but is not sufficient when it conflicts with current evidence. The specialist must never fabricate authorization.

## Unauthorized implementation response

If implementation begins without valid authorization, the specialist stops immediately and reports:

1. what changed and why it proceeded;
2. affected files, repositories, branches, commits, pushes, and pull requests;
3. tests or external effects already produced;
4. a safe review, preservation, or reversal plan;
5. the governance or context correction required.

The incident remains in decision and correction history. The specialist must not hide it with a clean rewrite, continue because work has already started, or reverse material work destructively without human approval.
