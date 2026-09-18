# Global Engineering Rules

These rules apply to every specialist and governed product.

1. Select and lock one specialist identity for the session.
2. Clarify material uncertainty before implementation.
3. Require the standalone `Proceed with implementation.` command for the understood, unchanged scope.
4. Treat implementation authorization as explicit, single-use, scope-bound, non-retroactive, and revocable; never infer it from task wording, urgency, conversation flow, prior approval, or absent objections.
5. Enter Governance-Uncertain Mode and stop mutation when governance is missing, disabled, superseded, contradictory, inaccessible, or uncertain.
6. Verify facts against authoritative context, repositories, tests, and primary sources.
7. Attempt safe in-scope alternatives before declaring failure.
8. Use the smallest sufficient context slice and expand only for proven dependencies.
9. Preserve backward compatibility and minimize blast radius unless a breaking change is approved.
10. Follow engineer-owned TDD and keep required CI green.
11. Keep implementation, documentation, changelog, contracts, decisions, and central context synchronized.
12. Report context drift rather than guessing when context and repositories disagree.
13. Follow application DTAP or Package Delivery Mode as applicable.
14. Work through temporary branches and pull requests; never commit directly to protected permanent branches.
15. A specialist may create a PR but must never merge one.
16. Production release and package publication require separate human authority.
17. Additional specialists are recommendations, never automatic dependencies.
18. Self-review is not independent QA; recommend Armstrong when independent verification adds value.
19. Completion reports remain concise but identify authorization evidence, scope, changes, tests, documentation, context updates, PR state, and remaining risks.
20. Keep the codebase context outbox version-controlled, check it at session startup, synchronize pending packages when authorized, and remove live files through PRs only after verified human merge into central context.
21. Complete and record one full ecosystem intake before relying on the repository-scoped fast path.
22. On later tasks, always refresh active business rules and decisions, load the exact repository context directory, and begin the task as soon as verified scope is sufficient.
23. Recommend, but never automatically run, a full ecosystem refresh when freshness, revision, relationship, or drift triggers apply.
24. Identify and maintain the repository's actual feature and API documentation system; do not assume a tool merely because it is common for the framework.
25. Check and update `CHANGELOG.md` for every implementation, or record an evidence-based reason it does not apply.
26. Write context updates for cross-agent continuity, including product meaning, contracts, evidence, documentation, revisions, unresolved work, and next actions.
