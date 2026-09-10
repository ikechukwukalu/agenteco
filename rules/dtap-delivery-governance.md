# DTAP Delivery Governance

Application delivery uses permanent lowercase `test`, `staging`, and `production` branches where those environments apply. Development happens on temporary branches.

## Mandatory classification

Before branching, ask whether implementation is a feature or hotfix unless the user already stated it clearly.

## Feature

- Base: `test`, unless the user explicitly chooses another base.
- Branch: `ft/feature-task-name`.
- PR: one pull request targeting `test`.

## Hotfix

A hotfix addresses a live production defect.

- Base: `production`.
- Branch: `hotfix/task-name`.
- PRs: one targeting `test` for verification and UAT, and one targeting `production` for eventual release.

The suffixes are placeholders supplied by the user or proposed by the specialist when permitted.

## Protections

- Never commit directly to a permanent DTAP branch.
- Never merge a pull request.
- Never infer production authorization from implementation, testing, UAT, PR creation, or branch state.
- Record relevant tests, context updates, exclusions, and release risks.

See [Delivery and Pull Request Governance](../governance/delivery-and-pr-governance.md) for the full flow.
