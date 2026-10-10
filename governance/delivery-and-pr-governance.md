# Delivery and Pull Request Governance

## Classify implementation first

Before creating a branch, the specialist asks whether the implementation is a **feature** or a **hotfix**. Do not infer the classification when the human has not stated it.

The human may provide the branch suffix. The specialist may propose a concise suffix when permitted.

## Feature delivery

1. Start from the permanent lowercase `test` branch unless the human explicitly authorizes another base.
2. Create a temporary branch following `ft/feature-task-name`.
3. Implement with engineer-owned tests.
4. Update technical documentation, changelog, and central context.
5. Present the evidence and obtain the human's explicit Armstrong QA decision.
6. If approved, have Armstrong independently verify the completed branch and address or record the verdict before PR creation. If declined, record the decision.
7. Push and create one pull request targeting `test` when authorized.
8. Never merge the pull request.

`feature-task-name` is a placeholder for the actual approved or proposed suffix.

## Hotfix delivery

A hotfix corrects a defect affecting the live application.

1. Start from the permanent lowercase `production` branch.
2. Create a temporary branch following `hotfix/task-name`.
3. Implement the smallest safe correction with regression tests.
4. Update technical documentation, changelog, and central context.
5. Present the evidence and obtain the human's explicit Armstrong QA decision.
6. If approved, have Armstrong independently verify the completed branch and address or record the verdict before PR creation. If declined, record the decision.
7. Push and create two pull requests when authorized: one targeting `test` for validation and UAT, and one targeting `production` for the eventual live correction.
8. Never merge either pull request.

`task-name` is a placeholder for the actual approved or proposed suffix. The production PR remains unmerged until validation is satisfactory and a human separately authorizes its merge.

## Pull-request boundary

Specialists may create, revise, and report on pull requests for the human. No Agent Eco Space specialist may merge a pull request under any circumstance. Implementation, testing, pushing, PR creation, deployment elsewhere, or release preparation is not merge authorization.

After creating a PR, check the other open PRs that are visible for the affected product's code and central-context repositories. In the completion report, give the human a short, deduplicated reminder with links to relevant unmerged PRs, prioritizing context PRs and stating which work remains unsynchronized until human merge. Do not imply that a created PR is merged, list unrelated PRs merely to fill a report, or claim there are no other PRs when access or the check failed. Never merge them on the human's behalf.

For testable code or behaviour, PR creation also requires a recorded pre-PR QA decision. This applies to every implementing specialist, explicitly including Chinedu and Dotun. The human may approve Armstrong's independent review or decline it; silence is not a decision, and Armstrong is never invoked automatically.

## Package delivery

Packages and distributable libraries use their approved release lifecycle rather than application DTAP where appropriate: branch, implement, test compatibility, document, obtain the pre-PR QA decision for testable changes, prepare version and release evidence, then stop for human publication and merge decisions.

## Evidence

No work is described as ready when required tests or CI are red. An explicitly accepted exception records the failing check, impact, owner, and human approval.

For DTAP work, the implementing specialist updates the central [feature availability catalogue](feature-availability.md) for their component with branch, commit, dependency, and verification evidence. A merged branch is not a deployment. The release owner records actual environment deployment; the customer-facing state depends on all required components, flags, audience access, customer-journey verification, and communication approval.

An enrolled product's production-source change may independently queue a central documentation PR under its recorded [production-reconciliation standing authorization](production-context-reconciliation.md). This does not promote the feature through DTAP, prove deployment, bypass human PR merge, or authorize workflow repair. Automated central documentation PRs identify their grant, source range, evidence, and unresolved release-state gaps.

## API consumer compatibility gate

Before a known breaking API change is released to production, every mapped affected consumer must be `Verified Compatible`, deprecated with evidence, or covered by an explicit human-approved exception. The exception records affected consumers, impact, duration, owner, mitigation, and rollback or recovery plan. Implementation approval alone is not a production compatibility exception.
