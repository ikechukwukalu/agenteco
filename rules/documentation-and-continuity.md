# Documentation and Continuity

Implementation is incomplete until another authorized specialist can understand what changed, why it changed, how it was verified, and what must happen next.

## Continuity record

For every completed task, update the assigned repository context directory and any affected shared records with:

- task objective and business reason;
- verified before-and-after behaviour;
- success path, credible failure points, implemented recovery or escalation, and verification status for meaningful feature or integration work, using the [feature-path record](../templates/product-context/feature-paths-and-recovery.md);
- implementation approach and significant files or components;
- decisions created, changed, corrected, deprecated, or superseded;
- contracts produced or consumed and affected sibling repositories;
- database, configuration, infrastructure, security, compatibility, and migration effects;
- tests, commands, evidence, and known coverage gaps;
- the pre-PR Armstrong QA decision and, when performed, verdict and findings disposition;
- feature, API, operational, README, migration, and release documentation changed;
- `CHANGELOG.md` entry or an explicit, evidence-based reason it does not apply;
- branch, commit, pull request, release, and source revisions;
- unresolved risks, deferred work, and the clearest next action.

Never record a value from `.env` or any `.env.*` file other than safe placeholders in exact `.env.example`. Configuration continuity records use variable names, purpose, environment, ownership, and sanitized status only.

Do not write vague notes such as `feature completed` or duplicate code diffs without explaining their product and contract meaning. Separate verified facts from proposals and uncertainty.

## Feature and API documentation

Backend and frontend specialists must identify the repository's current documentation system before changing documented behaviour. Record, where applicable:

- documentation tool and version;
- configuration and source locations;
- generation or validation command;
- generated or published destination;
- ownership and update workflow;
- last verified revision.

Examples include Knuckles/Scribe for Laravel, OpenAPI or Swagger, Storybook, Compodoc, Typedoc, JSDoc, generated SDK references, or a verified repository-specific system. Examples are not defaults: inspect the repository and use what is actually installed.

When behaviour, contracts, examples, errors, authentication, parameters, responses, components, or user flows change, update the applicable feature and API documentation in the same authorized scope. Generated documentation must be regenerated or validated according to repository policy.

Document relevant error and recovery behaviour alongside the happy path. Customer-facing guidance must explain safe next actions without exposing provider internals, private state, or secrets. The central-context feature-path record distinguishes verified behaviour from proposed or unsupported recovery.

For APIs, documentation includes the shared route inventory, route-to-consumer map, consumer expectations, compatibility risks, and unresolved Consumer Impact Alerts. Backend agents initialize the current-state baseline. Each consumer agent records new API usage and the exact source and contract assumptions introduced by its implementation.

## Changelog

`CHANGELOG.md` is a required release and continuity artefact. Check it during preflight and update it for user-visible changes, contracts, security, compatibility, configuration, migration, deprecation, operational behaviour, fixes, and releases. Preserve the repository's existing format and release convention.

If no changelog entry applies, state why in completion evidence. Do not silently omit the check.

### Production and publication closeout

When a change is merged into a production branch, the release owner must check whether its `Unreleased` changelog entries have actually been deployed. A merge alone is not deployment evidence. The release or DevOps owner verifies the running artifact, environment, rollout, and affected component against the [feature-availability record](../governance/feature-availability.md) or equivalent package-release evidence. If deployment is pending, failed, partial, or unverified, keep the entries under `Unreleased` and record the blocker and follow-up owner.

After verified production deployment, the responsible specialist prepares a changelog closeout on a temporary branch and human-reviewed PR. Move **only** the entries supported by the deployed commit or artifact range into a release section using the repository's established version and date convention. Continuously deployed applications without a release version use a dated section with a traceable deployment or artifact reference. Leave unshipped work under a fresh `Unreleased` section. Do not invent a version or move every entry merely because the branch advanced. Package entries close only after verified publication under the approved package-release process.

Record the release section, source range, deployment evidence, affected audience and components, context update, and PR in the repository's central-context task or release history. Check the feature-availability catalogue separately: a deployed backend component does not make an unfinished frontend journey customer-available. If entry-to-deployment mapping is ambiguous, flag it and keep those entries `Unreleased` until resolved. A rollback or withdrawn release is recorded as a dated correction, not hidden by silently rewriting prior release history. No AI specialist merges the closeout PR.

## Cross-repository handoff

When another repository is affected, update the shared contract, API–Consumer Compatibility Map, or handoff record with the producer revision, consumer impact, adoption status, compatibility constraints, and required follow-up. The implementer does not claim the consumer was updated without repository evidence. Known breaking changes create a Consumer Impact Alert linked from every affected repository context.
