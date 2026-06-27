# PRD: AI Agent Skills Showcase & Registry

## 1. Objective & Target Audience

This project provides a centralized, high-aesthetic hub (both a markdown-first repository and a visual web showcase) to register, explain, and install public skills for AI coding agents.

### Target Audience
The system is designed for two first-class citizens:
1. **AI Builders & Developers (Humans)**: Creators who want to understand the philosophy of skills, browse available tools, and quickly install them in their personal workspaces.
2. **AI Coding Agents (Agents)**: Autonomous agents (e.g., Claude Code, Cursor, OpenCode) that navigate the repository to find skill registries, fetch repo URLs, read documentation, and execute installation instructions.

---

## 2. Core Philosophy (Our Differentiation)

Unlike industry-standard integrations (like LangChain Tools, OpenAI Actions, or ChatGPT Plugins) and specific editor plugins (like Cursor, Codex, or Cloud Code Skills) which enforce vendor-locked bindings, strict JSON-typed declarations, or specialized SDK configurations, our ecosystem is built on a different paradigm:

### Platform-Agnosticism & Natural Language First
Our skills are completely independent of any single IDE or LLM vendor. At its core, a skill is a set of natural language instructions (`SKILL.md`) that any agent can read, understand, and execute. When manual repetition becomes tedious, we append a lightweight Python CLI tool. The system operates on natural language reasoning, making it portable across Cursor, Claude Code, OpenCode, or any custom terminal agent.

### Process & Result Certainty
Because agents can easily drift or make assumptions, our skills are written to define strict boundaries, error-handling heuristics, and explicit verification steps. Rather than relying on simple "system prompts," a skill specifies *exactly* what the output files should look like and how to verify correctness. This ensures high certainty in both execution processes and final outcomes.

### Progressive Disclosure
A skill is not a complex piece of code. It starts as a simple text file (`SKILL.md`) outlining natural language instructions for the agent. Only when operations require automation do we append a lightweight CLI tool. There is no SDK lock-in; the core capability is the instruction set.

### Files-as-Interfaces
Skills interact with the workspace by reading and writing files rather than calling remote network endpoints or database sockets. Files are inspectable, recoverable, stateful, and naturally match the file-reading nature of coding agents.

### Key Background Reading
*   **Conceptual Strategy**: [用好AI的第二步：先写Skill再执行](https://yage.ai/skill-first.html) (English: [Step Two to Using AI Well: Write the Skill Before You Execute](https://yage.ai/skill-first-en.html))
*   **Infrastructure Design**: [为什么AI只会说正确的废话，以及怎么把它逼出舒适区](https://yage.ai/context-infrastructure.html)


---

## 3. Core Features

### Bilingual Showcase Hub
The repository serves two representations of the registry:
- **Markdown Index (`README.md` / `README_zh.md`)**: A text-first representation structured for AI agents to easily parse.
- **Visual Dashboard (`index.html` / `index_zh.html`)**: A premium, responsive web experience served via GitHub Pages for human builders.

### Categorized Skills Directory
Skills are classified into three types:
1. **API Guides & Connectors**: Tools interacting with external services (e.g., Google Docs, Outlook, Stripe, Typefully).
2. **Workflows**: Comprehensive, multi-step procedures (e.g., Parallel Subagents, Deep Research, Slide Generation).
3. **Best Practices**: Mindsets, debugging trees, and general principles (e.g., AI Programming Mindset, Skill Writing Guide).

### One-Click Agent Installation Prompt
Each card in the dashboard and entry in the README provides a copy-to-clipboard button generating a standardized prompt. A human builder copies this prompt and pastes it to their agent (e.g., Cursor or Claude Code). The agent then automatically:
1. Clones/vendors the skill repository under `adhoc_jobs/`.
2. Creates the local symbolic link in `rules/skills/` pointing to the public repository's skill guide.
3. Configures local parameters or environment files.
4. Registers the new skill in the workspace `INDEX.md`.

---

## 4. Scope & Exclusions

- **Zero-Dependency Hosting**: The visual dashboard is implemented strictly with vanilla HTML, CSS, and JS to ensure fast loads and zero-build deployment on GitHub Pages.
- **No Credentials**: No private endpoints, tokens, or credentials will be stored in the public repositories.
