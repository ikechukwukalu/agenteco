# First-Time Agent Eco Space Bootstrap Prompt

Use this in a new AI session when the current product has not installed Agent Eco Space instruction adapters. Replace the placeholders before sending it.

```text
Use Agent Eco Space as the governance system for this work.

Agent Eco Space governance repository:
https://github.com/ikechukwukalu/agenteco

Product or current repository:
<PRODUCT_OR_REPOSITORY_URL_OR_WORKSPACE_PATH>

Central product context repository:
<CONTEXT_REPOSITORY_URL_OR_NONE_YET>

Read the Agent Eco Space README, command catalogue, operating constitution, specialist catalogue, and applicable rules. Then begin the "Adopt this product into Agent Eco Space." workflow.

Do not modify any repository yet. First confirm what sources you can access, recommend the Engineering Manager for onboarding, ask who you are operating as today, inspect the current product evidence, and present an adoption plan. Wait for the standalone "Proceed with implementation." command before creating approved changes. You may create pull requests after authorization, but you must never merge them.
```

## Access requirement

The AI must be able to read the listed sources. In a coding workspace, clone or attach the relevant repositories. In a hosted chat, connect or attach sources when supported. If a private repository is inaccessible, the AI reports that limitation and requests access or supplied context rather than inventing its contents.

## After adoption

Once repository-specific instructions are installed and human-merged, future sessions can discover Agent Eco Space from the repository. The short standalone adoption command is then sufficient within that configured workspace.
