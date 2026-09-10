# Source Authority and Reference Governance

This rule governs every source used to understand, design, implement, review, or release a project. A source may be a repository, Project Context, API documentation, Figma file, screenshot, PDF, design system, CSS library, live website, template, production application, or stakeholder instruction. No project is required to provide every source type.

## Source Inventory

At startup, the selected specialist must create or refresh a Source Inventory. For every known source, record:

- name and location
- type
- role and intended usage
- scope and relevant areas
- authority, including domain-specific authority where needed
- mutation policy or read/write permissions
- explicit constraints
- allowed deviations
- freshness or approval status when relevant

The inventory must state which source governs API contracts, UI, UX, architecture, behaviour, business rules, and any other material domain. If no authoritative source exists for a domain, record that gap instead of inventing one.

## Authority Classification

Use the smallest accurate classification. Supported types include:

- **Engineering Operating System:** permanent Agent Eco Space governance.
- **Project Context:** approved project-specific decisions and continuity.
- **API Contract:** authoritative API behaviour and compatibility.
- **Canonical Product or UI:** an existing approved product that must be closely preserved within its stated scope.
- **Design or Behaviour Specification:** approved requirements for a defined domain.
- **Technical Foundation:** an implementation constraint such as Tailwind CSS, Bootstrap, Material UI, or a component library.
- **Reference:** strong direction with permitted adaptation.
- **Inspiration:** ideas only; never a specification.

Authority is scoped, not universal. For example, API documentation may have highest API authority, Figma highest visual authority, an existing application highest behavioural authority, and Tailwind only styling-implementation authority. Record visual and behavioural authority separately when they differ.

## Precedence and Conflict Handling

Apply current explicit Project Owner decisions and approved Project Context first, then the highest authoritative source for the affected domain. Canonical and specification sources govern only their recorded scope. Foundations constrain implementation but do not define unrecorded product design. References and inspiration must not override approved requirements.

When authoritative sources conflict, are stale, or leave a material gap, stop the affected decision, report the conflict, identify its owner, and update Project Context after resolution. Do not silently choose the most convenient source.

## Mandatory Source Utilization

Before presenting architecture, UI, UX, implementation, or review recommendations, each participating specialist must include a concise **Sources Consulted** declaration listing the relevant authoritative sources actually used. The requirement applies only to sources relevant to that specialist. Missing access or an intentionally unused relevant source must be disclosed with its impact.

The selected specialist must provide specialists with the relevant Source Inventory entries and must not accept recommendations that ignore an applicable authoritative source.

## Design and Experience Reference Registry

For work affecting UI or UX, maintain a Design and Experience Reference Registry as the design-specific view of the Source Inventory. For each reference, record:

- source and type
- relevant screens, journeys, components, or behaviours
- visual authority
- behavioural authority
- technical or brand constraints
- mutation policy
- allowed deviations

Existing products, Figma, screenshots, brand guidelines, themes, templates, live websites, Tailwind CSS, Bootstrap, Material UI, and design systems are all valid inputs when classified accurately. A project may record that no external visual reference exists and assign design authority to the accountable UI/UX specialist within approved product and accessibility constraints.

No specialist may treat inspiration as specification or ignore an authoritative design reference.

## Scoped Readiness Evidence

Before implementation, the selected specialist records only the readiness facts relevant to the task:

- Agent Eco Space loaded: Yes/No
- Project Context reviewed: Yes/No
- authoritative sources reviewed: Yes/No
- outstanding questions identified: Yes/No
- discovery complete: Yes/No
- implementation authorized: Yes/No

This record does not grant authorization. When clear implementation authorization is absent, it states **Implementation Authorized: No**.

## Context Drift Detection

At material decision points and before completion or promotion, compare implementation decisions and repository state with approved Project Context and authoritative sources. If drift exists, stop affected work, resolve the discrepancy, and update or supersede Project Context before continuing. GitHub remains the durable project memory; conversation history is not a substitute.

## Cost-aware startup output

The selected specialist reports the chosen role, active repository, relevant authoritative sources, material unknowns, applicable delivery mode, and authorization state. A full source inventory or design-reference registry is created only when scope and risk justify it. Agent rosters and delegation plans are omitted unless the human approves additional participation.
