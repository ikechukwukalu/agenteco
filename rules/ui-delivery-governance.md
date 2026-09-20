# UI Delivery Governance

This rule applies whenever work creates or materially changes a user interface. It establishes design ownership, implementation boundaries, and visual acceptance without changing Agent Eco Space's implementation, DTAP, or release gates.

## Required Delivery Sequence

UI work follows this sequence:

1. approved requirements and applicable Design and Experience Reference Registry entries;
2. Samuel's UX/UI design and testable visual acceptance criteria;
3. Project Owner design approval when the proposed design introduces or materially changes visual direction;
4. the standalone `Proceed with implementation.` command for the understood scope;
5. Dotun's implementation of the approved design;
6. Armstrong's functional and regression QA;
7. Samuel's visual-fidelity and experience review;
8. the Project Owner's separate UAT decision.

An already approved canonical UI or approved design specification may satisfy the design-approval step when the registry records that authority and no new visual direction is introduced. A technical foundation such as Tailwind CSS does not satisfy it.

## Design-Ready Gate

Before requesting implementation authorization, Samuel must provide or validate:

- the relevant journeys, screens, components, and responsive behaviour;
- layout, hierarchy, interaction, state, accessibility, and design-system direction;
- loading, empty, error, validation, permission, and success states that apply;
- visual acceptance criteria and allowed deviations;
- the authoritative references actually consulted.

The selected specialist must report the design as `Ready`, `Approval Required`, or `Blocked`. Dotun must not invent missing visual direction to make a design appear complete.

## Implementation Boundary

Dotun owns frontend architecture and faithful implementation, not unapproved visual direction. During implementation, Dotun must:

- implement the approved design and recorded deviations;
- preserve the authoritative visual and behavioural references;
- escalate material gaps or conflicts to Samuel through the selected specialist;
- provide representative evidence for desktop, tablet, and mobile where applicable;
- include applicable loading, empty, error, validation, permission, and success states in the evidence.

Material design changes return to Samuel and, when required, the Project Owner before implementation continues. The existing implementation authorization is invalidated when the approved scope or design direction materially changes.

## Visual Acceptance Review

The implementing specialist must compare the implementation with the approved design and authoritative references and record:

- breakpoints and states reviewed;
- visual, interaction, accessibility, and responsive findings;
- every approved deviation;
- unresolved material differences;
- a verdict of `Accepted`, `Changes Required`, or `Blocked`.

After testable UI implementation and Dotun's engineer-owned verification—but before implementation PR creation—Dotun must ask whether the human approves Armstrong's independent functional QA or declines it. Armstrong is invoked only with human approval. Samuel remains a recommended independent visual reviewer when that would materially improve confidence. When the human requires either review for the current scope, unresolved blocking findings prevent readiness. UI Replica Mode adds stricter parity evidence when activated.

## Project Owner UAT

Any requested visual-acceptance verdict does not replace the Project Owner's UAT decision or authorize Production, merge, deployment, or publication.
