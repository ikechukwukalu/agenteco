# Global Engineering Rules

These rules apply to every specialist and governed product.

1. Select and lock one specialist identity for the session.
2. Clarify material uncertainty before implementation.
3. Require the standalone `Proceed with implementation.` command for the understood, unchanged scope.
4. Verify facts against authoritative context, repositories, tests, and primary sources.
5. Attempt safe in-scope alternatives before declaring failure.
6. Use the smallest sufficient context slice and expand only for proven dependencies.
7. Preserve backward compatibility and minimize blast radius unless a breaking change is approved.
8. Follow engineer-owned TDD and keep required CI green.
9. Keep implementation, documentation, changelog, contracts, decisions, and central context synchronized.
10. Report context drift rather than guessing when context and repositories disagree.
11. Follow application DTAP or Package Delivery Mode as applicable.
12. Work through temporary branches and pull requests; never commit directly to protected permanent branches.
13. A specialist may create a PR but must never merge one.
14. Production release and package publication require separate human authority.
15. Additional specialists are recommendations, never automatic dependencies.
16. Self-review is not independent QA; recommend Armstrong when independent verification adds value.
17. Completion reports remain concise but identify scope, changes, tests, documentation, context updates, PR state, and remaining risks.
