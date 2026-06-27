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

### Flow-Based Skill Taxonomy
Earlier drafts grouped skills by their technical form (tool vs. workflow vs. best-practice, or repo vs. doc). We deliberately moved away from that, because form is not how a user thinks — it conflates a *hierarchy* (how a thing is packaged) with a *category* (what a thing is for), and it makes the `REPO`/`DOC` label feel redundant.

Instead, skills are organized around the **agent's working flow**. Almost anything a user asks an agent to do follows the same spine:

> **Intake → Process → Output**

The user (or agent) first has to **pull the relevant context in**, then **process it into something useful**, then **deliver an artifact** a human can consume. Two further layers cut across that flow: the **infrastructure** that actually runs the agents, and the **best practices** that guide how the work is done. This yields five sections:

1. **Intake — Context In**: gets the outside world into the agent's context (voice notes, email, online media, PDFs, semantic recall of prior workspace memory).
2. **Analyze & Research — Data Into Insight**: the "process" stage — turning raw data and sources into metrics, charts, and validated findings (Stripe/health/roast/token analytics, deep research, cognitive-profile extraction).
3. **Output & Delivery — Artifacts For People**: produces and ships the result (docs, slides, images, color-finished stills, web reports, email, iMessage, social posts).
4. **Infrastructure — Run The Agents**: the runtime that everything above depends on (process daemons, OpenCode task control & containers, CLI-design rules, multi-agent orchestration).
5. **Best Practices — Work Well**: the craft of working with agents (programming mindset, skill-writing, staged dry-runs, temporal verification, project scaffolding).

**Orthogonal type badge.** Whether a skill ships as a cloneable **Repo** or a single standalone **Doc** is a *separate* axis from where it sits in the flow, so each section freely mixes both. The badge is meaningful because it selects the install mode (see below), not because it implies a category.

**Skills that span two stages.** A few skills genuinely serve more than one stage — email both reads (intake) and sends (output); Google Docs is both read and published. These are listed once in their primary stage and carry a small `↺ also…` marker, rather than being duplicated, so the registry stays clean and the continuous 01–N numbering holds.

### Two-Mode One-Click Install
The central promise is that **installation is trivial**: no IDE-specific slash commands, no proprietary package manager, and no "invoke a skill in order to install a skill." A human copies one prompt and pastes it into any agent. The copy button emits one of two prompts, auto-selected by the entry's type:

1. **Repo mode** (`REPO`) — clone/vendor the repo under `adhoc_jobs/`, expose one root skill to `rules/skills/` via a relative symlink, register it in the rules index, and keep private config in a local overlay.
2. **Doc mode** (`DOC`) — for a single Markdown file inside a larger repo, a flat clone is not enough. The agent must first **explore the source and read the file**, then **trace the local skill-discovery chain** (from `AGENTS.md` / `CLAUDE.md` down to `rules/skills/`) and place the skill at the layer where it will actually be discovered. If no such chain or structure exists yet, the agent must **propose the directory structure and get user approval before creating anything**.

The dashboard does not print the full prompt text; the procedure is enforced inside the copied prompt, and the page shows only a slim one-line callout plus two mode chips.

---

## 4. Scope & Exclusions

- **Zero-Dependency Hosting**: The visual dashboard is implemented as a single streaming page with inline styles to ensure fast loads and zero-build deployment on GitHub Pages.
- **No Credentials**: No private endpoints, tokens, or credentials will be stored in the public repositories.
- **Copy Stays Fixed**: The skill names and descriptions are sourced verbatim from the README registry; design work reorganizes and restyles, it does not rewrite copy.
