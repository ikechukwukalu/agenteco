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

### GitHub Copilot code-review handoff

For a governed GitHub repository with Copilot code review available, request a GitHub Copilot review when a pull request is created. Prefer an organization or repository ruleset that automatically requests one review on PR opening. A personal automatic-review preference covers only its owner's PRs, so it does not satisfy a product-wide policy. Enabling a ruleset, connecting repositories, changing billing or review effort, and granting Copilot access require the appropriate GitHub administrator's approval; this governance text does not perform or authorize those changes. Start with one review per PR, not every push or draft PR, unless the repository owner approves the additional cost and noise.

At PR handoff, verify whether Copilot review is configured for that repository and whether a review was requested or posted. If automatic review is unavailable, request Copilot as reviewer through GitHub when permitted; otherwise tell the human exactly what setup or permission is missing. Do not claim a review occurred merely because the PR exists or a ruleset is expected. On later pushes, check whether material changes warrant a fresh review and request it when appropriate and available.

Copilot review is an additional code-review pass, not Armstrong's independent functional QA, Victor's optional specialist review, CI, security review, human approval, or merge authority. Keep the pre-PR Armstrong decision checkpoint unchanged. Treat Copilot findings as actionable evidence: address or explicitly record unresolved material findings before calling a PR ready. Do not allow Copilot approval to count as the human's merge decision or required human approval. Keep review instructions scoped, concise, and consistent with canonical governance; never expose secrets or confidential context in PR comments.

After creating a PR, check the other open PRs that are visible for the affected product's code and central-context repositories. In the completion report, give the human a short, deduplicated reminder with links to relevant unmerged PRs, prioritizing context PRs and stating which work remains unsynchronized until human merge. Do not imply that a created PR is merged, list unrelated PRs merely to fill a report, or claim there are no other PRs when access or the check failed. Never merge them on the human's behalf.

For testable code or behaviour, PR creation also requires a recorded pre-PR QA decision. This applies to every implementing specialist, explicitly including Chinedu and Dotun. The human may approve Armstrong's independent review or decline it; silence is not a decision, and Armstrong is never invoked automatically.

## Package delivery

Packages and distributable libraries use their approved release lifecycle rather than application DTAP where appropriate: branch, implement, test compatibility, document, obtain the pre-PR QA decision for testable changes, prepare version and release evidence, then stop for human publication and merge decisions.

## Evidence

No work is described as ready when required tests or CI are red. An explicitly accepted exception records the failing check, impact, owner, and human approval.

For DTAP work, the implementing specialist updates the central [feature availability catalogue](feature-availability.md) for their component with branch, commit, dependency, and verification evidence. A merged branch is not a deployment. The release owner records actual environment deployment; the customer-facing state depends on all required components, flags, audience access, customer-journey verification, and communication approval.

A production-branch merge triggers a [changelog closeout check](../rules/documentation-and-continuity.md#production-and-publication-closeout), not an automatic claim that every `Unreleased` entry shipped. Once the release owner verifies deployment, the responsible specialist prepares the scoped changelog and central-context update by PR; the human reviews and merges it. Package changelogs close only after verified publication. Record a pending closeout when deployment or entry mapping is not yet proven.

An enrolled product's production-source change may independently queue a central documentation PR under its recorded [production-reconciliation standing authorization](production-context-reconciliation.md). This does not promote the feature through DTAP, prove deployment, bypass human PR merge, or authorize workflow repair. Automated central documentation PRs identify their grant, source range, evidence, and unresolved release-state gaps.

## API consumer compatibility gate

Before a known breaking API change is released to production, every mapped affected consumer must be `Verified Compatible`, deprecated with evidence, or covered by an explicit human-approved exception. The exception records affected consumers, impact, duration, owner, mitigation, and rollback or recovery plan. Implementation approval alone is not a production compatibility exception.
