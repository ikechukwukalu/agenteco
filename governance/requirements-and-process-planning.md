# Requirements and process planning

## Purpose and entry

Use linked PRD, 2A and FARS records to improve usability, visibility, stability and productivity across every governed product. Keep them understandable to business reviewers, design, engineering and QA. This is a portfolio-wide standard, not a product-specific permission model.

After the existing session and role selection, establish the task if it has not already been supplied. Locate the product's current planning index, actor/action register and relevant records before asking for documents. Recognize a PRD by its content, not its filename. If no linked 2A exists, ask whether the human has one or wants help preparing it. Do not ask again for accessible records. An uploaded document is not implementation authorization.

Use the [planning templates](../templates/planning/README.md). Agents may assist with drafting and normalize incoming material into the standard format while preserving the original submission or source link. Record gaps and proposed reinterpretations; do not silently change business meaning or redesign the template during product work. Repository writes still require the applicable scope-bound authorization.

## Sequence and authority

1. **PRD:** the stakeholder describes the business need, expected outcomes, requirements and boundaries. Retain its source, stable ID, owner, version and approval evidence.
2. **2A — Actors and Actions:** the team explains its understanding for stakeholder agreement. Define objective, multiple success points, actors, each actor's actions and dependencies, roles and permissions, key actions grouped under each success point, and complete cross-actor process flows. Process flows stay inside 2A.
3. **FARS:** derive the failure/frustration, avoidance, recovery and verification review from the agreed 2A. Review every action, including optional and post-success actions. Record reviewed actions with no material risk found rather than omitting them.
4. **Resolve decisions:** if FARS changes business behaviour, update the proposed 2A and obtain stakeholder agreement. An unresolved decision blocks dependent implementation, not safe independent work.
5. **Implement only after separate authorization:** document agreement and FARS approval never replace the standalone `Proceed with implementation.` command, engineer-owned evidence, applicable specialist reviews, QA, UAT or release controls. Never merge.

Scale the paperwork to the change: reuse existing records and update only affected sections for small fixes. An urgent hotfix follows existing hotfix authorization and delivery rules with proportionate linked analysis; urgency does not waive gates. Missing historical documents are recorded as gaps, not fabricated approval. A separate process receives a new linked 2A; an extension to the same process revises its existing 2A.

## Traceability and ownership

Each document has its own stable ID, owner, dates, version, status and approver evidence. Row numbers count entries and are not references. 2A cites the PRD name, ID, version and link. FARS cites both PRD and 2A, including the 2A version, and uses the same actor, action and success-point references. Keep links to implementation, tests and relevant contracts through the product [planning index](../templates/product-context/planning-index.md).

Maintain one authoritative Markdown content record in CPI and clearly labelled Word exports. Word masters define presentation, not competing business truth. Keep sources and earlier approvals accessible. Record document agreement separately from implementation, verification and confirmed live availability. A merged PR is not deployment evidence.

The accountable specialist maintains the affected records. Business owners decide meaning and approve behaviour; design reviews clarity and awareness; engineering checks feasibility, dependencies and contracts; QA derives observable tests from agreed outcomes, permissions and recovery. These responsibilities do not automatically invoke any specialist or replace existing engagement approvals.

## Awareness and designs

Every key action must be obvious to the responsible actor at the right time. Each flow states who acts next, who is waiting on whom or what, and how and when each person is informed. Notification may be an on-screen next step, status, email or another agreed channel; do not prescribe broadcast for private events.

Record a module wireframe/design link and version or date, plus exact frame links per flow where available. Do not invent links or assume a linked design is approved, implemented or accessible. Record inaccessible designs as gaps. Keep optional actions discoverable without making them false prerequisites to success.

## Actor-confirmation checkpoint

Before finalizing a 2A, present the actors for its exact product, application and process scope to the human and obtain explicit confirmation. Agents may recommend actors with reasons and evidence; recommendations, model names, source-code discovery and assumed industry conventions are not confirmation. Keep the 2A in Draft while the applicable actor list is unconfirmed or disputed.

Consult the product's approved actor register first. Cite any existing explicit confirmation for the same unchanged scope; it may be reused without repeatedly asking the human. A broad product inventory alone does not confirm which actors belong in a specific application's 2A. Any addition, omission, rename, reclassification or changed scope requires renewed clarification and confirmation. Record the confirmed list, scope, confirmer, date and decision reference in 2A. General implementation approval does not settle an unresolved actor decision.

Distinguish actors using the scoped application from actors participating through connected applications. Record cross-application handoffs without assigning the receiving actor access to the originating application. Do not silently convert an agreed actor into a role or collapse distinct actor categories. Product owners define their product's taxonomy; canonical governance must not impose one product's actor names, user models or application mapping on another.

## Product register and older features

Use the [product actor, action and process register](../templates/product-context/actor-action-register.md) as the stable reference. Distinguish actor groups, subtypes, aliases and permission-bearing roles. A broad group name does not grant every member every permission. Record which role may perform which action, under what conditions, and the source and decision owner.

Agents may discover and propose additions, renames and retirements with evidence. Separate intended business behaviour, observed implementation and unknowns; code does not silently redefine approved intent. Human agreement is required for uncertain semantics and permissions. Retiring a registry entry never deletes accounts or changes application access. Never reuse retired IDs.

For older products, consult existing ecosystem intake first and propose a bounded backfill: repositories, processes, revision, evidence, missing coverage and decision owner. Inspect only the approved scope, including relevant contracts, tests and consumers. Do not fabricate a historical PRD or retroactive approval. A reconstructed requirement remains proposed until agreed. Do not automatically repair application behaviour or repeat full discovery each session.

Product-specific actor names and application mappings belong in that product’s approved register, not in canonical examples used as default actor inventories.

## Process conflicts and change history

During 2A drafting, changes to requirements or connected processes, and new implementation/testing findings, follow affected references into connected actions, prerequisites, permissions, notifications, contracts and FARS. Check code and tests before claiming actual behaviour. Record conflicts in the 2A **Connections to other processes** section: reference, clashing rules and source references, effect, decision owner, resolution and date. FARS links the consequence and recovery to that decision rather than creating a competing decision record.

Distinguish confirmed conflict, possible impact requiring verification, missing information, and no conflict found within the reviewed scope. This is an evidence-based review, not a guarantee of exhaustive automatic conflict detection. Unresolved business choices remain visible and pause dependent changes.

Version a process in place with the same document ID. Preserve prior versions, the reason for change, approval and effective-date evidence. Identify the current agreed version separately from the confirmed live version. Keep action IDs when identity remains the same; give genuinely new actions new IDs and mark removed ones retired. Explicitly decide how work already in progress uses old or new rules; do not assume migration. Refresh linked PRD, 2A, FARS, tests and affected guidance after an approved change.

## Agent contributions and recovery features

Before adding agent-discovered findings or solutions to an agreed FARS, display them for discussion and obtain human approval. Keep provenance in a short note keyed by finding ID: human-provided, agent-proposed or joint; approval reference/date; and whether controls are proposed, implemented or verified. Do not bury unapproved proposals among agreed entries. The simple six-column action table stays unchanged.

A recovery can require a new feature. Link it to a scoped requirement, affected action and 2A flow; identify dependencies, permissions, open business decisions and verification. FARS approval is not permission to implement that feature. Never describe a proposed fallback as available.

For example, cached carrier quotes and deferred waybill retries are potential recovery designs, not evidence that a provider permits or supports them. Before proposing them as usable, verify quote freshness and coverage, price-change handling, payment consent, duplicate-charge/booking prevention, pending-state awareness, safe retry ownership and escalation. This example authorizes no carrier integration or product change.

## Adoption and maintenance

Pilot this workflow on one human-selected process before a broader backfill. Evaluate whether stakeholders understand outcomes, QA can derive tests, handoffs are visible, conflicts surface earlier and maintenance effort is proportionate. Record remaining gaps instead of expanding the templates indefinitely. Approved record changes follow the normal documentation PR process; updating canonical governance does not automatically rewrite product contexts or roll out new product behaviour.

Use the separate [case reporting and classification guidance](case-management-and-help-knowledge.md) for operational reports and audience-specific help knowledge. Those records inform planning but do not authorize implementation.
