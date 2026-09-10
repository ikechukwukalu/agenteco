# UI Replica Mode

## Purpose

UI Replica Mode is an optional, high-fidelity workflow for rebuilding an existing approved interface when visual and behavioural parity—not general design direction—is the objective.

It supplements Agent Eco Space’s Design and Experience Reference Registry. It does not apply by default to normal product design, and it does not grant implementation or release approval.

## Activation

The Project Owner must explicitly request UI Replica Mode and identify the canonical product, page, route, or experience to reproduce. The selected specialist records:

- the canonical visual and behavioural reference;
- scope: routes, breakpoints, themes, states, journeys, and assets;
- allowed deviations, if any;
- ownership and permission to use the reference assets and content;
- visual and behavioural acceptance criteria.

When a source product and source code are both available, the live product is authoritative for observable behaviour and the source code is authoritative for hidden implementation intent only where it does not contradict the observable result.

## Discovery Before Implementation

Before any UI implementation begins, the team must produce auditable reference evidence:

1. full-page captures at desktop (1440px), tablet (768px), and mobile (390px), unless the approved scope defines other breakpoints;
2. an interaction sweep covering scroll, click, hover, focus, keyboard, timing, overlays, loading, empty, error, and success states relevant to the scope;
3. asset and typography inventory, including layered media, icons, fonts, content, themes, and responsive breakpoints;
4. route-by-route and state-by-state parity matrix;
5. component specifications with observed structure, exact computed styling values where practical, interaction model, state transitions, real content/assets, and responsive behaviour;
6. a recorded distinction between observed facts and implementation assumptions.

No builder may receive broad instructions such as “make it look like the reference.” Builders receive a focused component specification and the relevant reference evidence.

## Implementation

- Preserve the reference’s observable experience. Do not substitute a familiar interaction model without proving it matches the reference.
- Build foundation tokens and shared behaviour first; then implement small, independently verifiable components.
- Use the target project’s approved technology. UI Replica Mode does not require React, Next.js, Tailwind, or any particular framework.
- For framework migrations, replace framework internals with idiomatic target-platform mechanisms while retaining the approved observable interface.
- Engineer-owned tests cover interactive behaviour. Browser tests cover customer journeys and state transitions.

## Acceptance Gate

Before calling replica scope complete, the selected specialist must provide:

- side-by-side captures at the approved breakpoints;
- browser-flow evidence for every mapped interaction and state;
- visual-difference findings and their disposition;
- an updated parity matrix showing each item as matched, approved deviation, or unresolved;
- confirmation that no unresolved material parity gap remains.

“Looks similar” is not evidence of parity. A requested 100% clone means no material visual or behavioural difference remains. Rendering-engine variance and deliberate deviations must be individually recorded and explicitly approved.

## Scope Boundary

Use UI Replica Mode only where the Project Owner controls or has permission to reproduce the referenced product, assets, content, and brand expression. It must not be used for impersonation, deceptive cloning, or unauthorized copying.

