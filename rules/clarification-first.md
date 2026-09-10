# Rule: Clarification First

All agents must clarify before implementation.

## Mandatory Behavior

Before producing implementation code, migration files, infrastructure configuration, UI changes, tests, or deployment steps, agents must:

1. Restate the user's request briefly.
2. Identify missing, vague, risky, or conflicting details.
3. Ask only necessary clarification questions.
4. Suggest safe defaults only as options, not assumptions.
5. Require the standalone `Proceed with implementation.` command for the understood scope.

## Forbidden Behavior

Agents must not:

- Assume business rules.
- Invent database fields.
- Invent API contracts.
- Invent UI flows.
- Proceed to production implementation without approval.
- Hide uncertainty.
- Skip security, QA, performance, or deployment impact when relevant.

## Exception

Agents may provide:

- Explanations.
- Analysis.
- Architecture options.
- Review comments.
- Pseudocode.
- Clarifying question lists.
- Risk assessments.

But they must not implement until the user sends the standalone `Proceed with implementation.` command.
