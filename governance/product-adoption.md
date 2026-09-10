# Product Adoption

The standalone command `Adopt this product into Agent Eco Space.` begins this workflow after Agent Eco Space has been loaded through a repository adapter or the first-time bootstrap prompt. The command alone cannot identify an unknown governance repository in an unconfigured chat.

1. Report whether Agent Eco Space instructions and central-context registration are present.
2. Ask whether the repository belongs to a new product, existing product, or standalone package when evidence does not establish it.
3. Recommend the Engineering Manager for onboarding and confirm the session role.
4. Inventory repositories, technologies, responsibilities, consumers, contracts, protected branches, delivery modes, and verified revisions.
5. Establish the proposed central product-context structure and per-repository directories.
6. Identify missing evidence, context drift, and adoption risks.
7. Present the adoption plan without mutating product repositories.
8. Require `Proceed with implementation.` before creating approved context or adapter changes.
9. Prepare changes through the applicable temporary branches and PRs.
10. Never merge those PRs.

After adapters are installed and merged by a human, future supported AI sessions can discover Agent Eco Space from repository instructions. Before that point, the first-time bootstrap prompt is the reliable entry mechanism.
