# Delivery and Pull Request Governance

## Classify implementation first

Before creating a branch, the specialist asks whether the implementation is a **feature** or a **hotfix**. Do not infer the classification when the human has not stated it.

The human may provide the branch suffix. The specialist may propose a concise suffix when permitted.

## Feature delivery

1. Start from the permanent lowercase `test` branch unless the human explicitly authorizes another base.
2. Create a temporary branch following `ft/feature-task-name`.
3. Implement with engineer-owned tests.
4. Update technical documentation, changelog, and central context.
5. Push and create one pull request targeting `test` when authorized.
6. Never merge the pull request.

`feature-task-name` is a placeholder for the actual approved or proposed suffix.

## Hotfix delivery

A hotfix corrects a defect affecting the live application.

1. Start from the permanent lowercase `production` branch.
2. Create a temporary branch following `hotfix/task-name`.
3. Implement the smallest safe correction with regression tests.
4. Update technical documentation, changelog, and central context.
5. Push and create two pull requests when authorized: one targeting `test` for validation and UAT, and one targeting `production` for the eventual live correction.
6. Never merge either pull request.

`task-name` is a placeholder for the actual approved or proposed suffix. The production PR remains unmerged until validation is satisfactory and a human separately authorizes its merge.

## Pull-request boundary

Specialists may create, revise, and report on pull requests for the human. No Agent Eco Space specialist may merge a pull request under any circumstance. Implementation, testing, pushing, PR creation, deployment elsewhere, or release preparation is not merge authorization.

## Package delivery

Packages and distributable libraries use their approved release lifecycle rather than application DTAP where appropriate: branch, implement, test compatibility, document, prepare version and release evidence, then stop for human publication and merge decisions.

## Evidence

No work is described as ready when required tests or CI are red. An explicitly accepted exception records the failing check, impact, owner, and human approval.
