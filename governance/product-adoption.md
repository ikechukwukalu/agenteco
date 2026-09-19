# Product Adoption

The standalone command `Adopt this product into Agent Eco Space.` begins this workflow after Agent Eco Space has been loaded through a repository adapter or the first-time bootstrap prompt. The command alone cannot identify an unknown governance repository in an unconfigured chat.

1. Report whether Agent Eco Space instructions and central-context registration are present.
2. Establish the product name, application or component name, repository name and location, and central-context location; ask whether the repository belongs to a new product, existing product, or standalone package when evidence does not establish it.
3. Recommend the Engineering Manager for onboarding and confirm the session role.
4. Inventory repositories, technologies, responsibilities, consumers, contracts, protected branches, delivery modes, and verified revisions.
5. Establish the proposed central product-context structure and per-repository directories.
6. Perform the initial complete ecosystem intake and record its context revision, repository revisions, relationships, access gaps, documentation systems, and refresh schedule.
7. Identify missing evidence, context drift, and adoption risks.
8. Present the adoption plan without mutating product repositories.
9. Require `Proceed with implementation.` before creating approved context or adapter changes.
10. Prepare changes through the applicable temporary branches and PRs.
11. Never merge those PRs.

After adapters are installed and merged by a human, future supported AI sessions can discover Agent Eco Space from repository instructions. Before that point, the first-time bootstrap prompt is the reliable entry mechanism.
