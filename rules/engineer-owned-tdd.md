# Engineer-Owned Test-Driven Development

This is a permanent Agent Eco Space delivery rule for backend, frontend, mobile, AI, and any other implementation specialist.

## Principle

Testing is owned first by the engineer who changes the behaviour. QA, security, code review, and operations provide independent verification; they do not substitute for automated tests written and maintained with the implementation.

## Required engineering loop

For every meaningful behaviour change:

1. State the intended observable behaviour and acceptance criteria.
2. Add or update the automated test before, with, or immediately alongside the implementation. Prefer red → green → refactor where practical.
3. Implement the smallest change that satisfies the behaviour.
4. Run the focused tests, then the relevant regression suite.
5. Refactor only while tests remain green.
6. Report evidence, gaps, and deliberately untested boundaries.

“Tests later” is not an acceptable completion state for a finished feature, defect fix, security change, or regression fix.

## Backend expectations

Backend engineers own the appropriate unit, feature, API, integration, database, queue/job, and contract tests. New or changed endpoints must verify success, validation, authorization, error, and compatibility paths. Security-sensitive behaviour requires negative tests.

## Frontend expectations

Frontend engineers own the appropriate unit, component, accessibility, state, API-contract, and user-journey tests. A visual implementation is not complete merely because it renders. Tests must prove loading, empty, error, permission, interaction, and responsive states relevant to the change.

## Independent specialist responsibilities

- **Armstrong (QA):** independently verifies acceptance criteria, integration flows, regressions, exploratory risks, and release evidence.
- **Busola (Security):** independently assesses security threats, authorization, data handling, dependencies, and security regressions.
- **Victor (Code Review):** checks implementation and test quality, maintainability, and coverage of the agreed behaviour.
- **selected specialist:** makes engineer-owned test evidence and independent verdicts visible in the release decision.

## Narrow exceptions

A spike, one-off operational investigation, or purely cosmetic change may justify a documented reduced-test exception. The selected specialist must record the reason, risk, follow-up, and owner. An exception never waives required CI checks or an independent QA/security review that the human has explicitly made a gate for the scope.

For testable implementation, engineer-owned tests are completed first. Before the implementation PR is created, the implementer must ask whether the human approves Armstrong's independent QA or declines it. The decision is recorded; Armstrong never starts automatically.
