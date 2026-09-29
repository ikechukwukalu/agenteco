# Code Readability and Explanatory Comments

This rule applies to every Agent Eco Space specialist who creates or changes code, tests, scripts, configuration, or examples. The result should be easy for a teammate or later agent to understand without reconstructing the original chat.

- Use descriptive names and small, coherent units of work. Keep related statements together and separate distinct steps with blank lines. Prefer clear line breaks and indentation over dense one-liners or deeply nested expressions.
- Comment extensively where explanation helps: document intent, business rules, non-obvious decisions, invariants, edge cases, security and compatibility constraints, and why a workaround exists. For public interfaces, explain the contract and significant usage constraints in the repository's established documentation style.
- Place comments near the behavior they explain. Update or remove stale comments when behavior changes. Never leave a comment that contradicts the code or implies a guarantee the tests do not establish.
- Do not add noise merely to increase comment count. Avoid comments that only restate a plainly readable line, lengthy speculative notes, and comments containing secrets or protected environment values.
- Follow the repository's established formatter, linter, language conventions, and documentation-comment style. Do not reformat unrelated files solely to satisfy this rule. Run the relevant formatting or lint check when available.
- Review readability as part of implementation: a future maintainer should be able to identify what the code does, why important choices were made, and where to change it safely.

These expectations supplement, rather than replace, feature/API documentation, changelog updates, tests, and central-context continuity records.
