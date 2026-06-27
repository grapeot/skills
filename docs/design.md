# Design Specification: AI Agent Skills Showcase & Registry

This document outlines the architectural, interaction, and visual design decisions for the AI Agent Skills Showcase and Registry.

---

## 1. Conceptual Architecture

The project is built on the belief that AI coding agents require a different interface design than traditional software components.

### Platform-Agnosticism vs. Codified SDKs
Other editors or plugin systems (e.g. Cursor, Codex, Cloud Code Skills) utilize heavily codified JSON configurations, strict function definitions, and vendor-specific APIs. Our Skill system is **platform-agnostic**:
* **Natural Language Priority**: The core logic is natural language (`SKILL.md`) outlining reasoning steps, checklists, and outcomes. Any agent can parse and follow it.
* **Optional CLI Connectors**: Code execution is wrapped in standalone CLI tools (e.g., Python scripts). The agent executes it through standard terminal interfaces without special IDE integration.
* **Process & Result Certainty**: The documentation explicitly maps execution paths, validation steps, and expected outputs, ensuring the agent performs task segments with absolute certainty.

### Files-as-Interfaces
Traditional AI integrations use REST endpoints, WebSocket servers, or SDK wrappers. This adds setup overhead and makes debugging difficult. Our skills interact with the host environment by reading and writing files in the local workspace.
* **Statefulness**: Files preserve the history of inputs and outputs in plain text.
* **Inspectability**: Human developers can see exactly what files the agent read or wrote.
* **Safety**: Files can be staged, reviewed, and reverted via standard Git control before execution.

### Local-Overlay Separation
Public skill repositories describe generic interfaces and technical contracts. Private configuration stays in the workspace.
* **Symbolic Links (Local)**: In the user's workspace, skills in `rules/skills/` are relative symlinks pointing to `adhoc_jobs/<skill_repo>/skills/<file>.md`. When the agent or human updates the skill guidelines in `rules/skills/`, the changes are automatically tracked in the nested git repository for easy commits and upstream pushes.
* **Flat Reference (Public)**: In the public `context-infrastructure` starter set, these are represented as flat documentation guides. The registry lists the standalone tool repositories so that agents can clone them and set up their own symlinks automatically.

---

## 2. Interaction & UX Flows

The system supports two distinct user flows.

### Human Builder Flow
1. **Discovery**: The developer lands on the visual dashboard served via GitHub Pages.
2. **Evaluation**: The developer scans skills grouped by functional domain, narrows with the type filter (Tools, Workflows, Best Practices), or searches by keyword.
3. **Trigger**: The developer clicks the **copy** button on a skill row.
4. **Execution**: The developer pastes the generated installation prompt into the agent's chat interface (e.g., Cursor, Claude Code). The agent executes the prompt, integrating the skill end-to-end.

### AI Agent Flow
1. **Index Parsing**: An agent receives a request to install a skill or search for capabilities. It reads the markdown index (`README.md` or `README_zh.md`).
2. **URL Retrieval**: The agent extracts the public repository URL or the direct markdown file link.
3. **Workspace Integration**: The agent runs the installation chain appropriate to the skill type (see §3).

---

## 3. One-Click Install Protocol (Two Modes)

The central promise is that **installation is trivial**: no IDE-specific slash commands, no proprietary package manager, and no "invoke a skill in order to install a skill." The human copies one prompt and pastes it into any agent. Because skills ship in two physical forms, the copy button emits one of two prompts, auto-selected by the entry's type (a `.md` link → Doc mode, otherwise → Repo mode).

### Mode A — Repo Skills (`REPO`)
For skills that live in their own GitHub repository (a `SKILL.md` plus optional CLI tooling). The prompt instructs the agent to:
1. Start from the workspace `AGENTS.md`, following any `WORKSPACE.md` routing rules.
2. Clone or vendor the repo under an appropriate directory (e.g. `adhoc_jobs/`).
3. Expose exactly one root skill to `rules/skills/` via a relative symlink and register it in the rules index.
4. Keep private aliases, paths, and credentials in a local overlay — never in the public repo.

### Mode B — Standalone Doc Skills (`DOC`)
For skills that are a single Markdown file inside a larger repo (e.g. the `context-infrastructure` starter set). A flat clone is insufficient — the file must be hooked into the workspace's **skill-discovery chain**. The prompt instructs the agent to:
1. **Explore first**: read the source repo structure and the specific `.md` file to understand what it does.
2. **Trace the discovery chain**: starting at `AGENTS.md` / `CLAUDE.md`, follow each include or reference down to `rules/skills/`, identifying the layer at which skills become discoverable.
3. **Place correctly**: vendor the file and link/register it at the layer where that chain expects it, so the agent will actually surface it later.
4. **Confirm before scaffolding**: if no discovery chain or `rules/skills/` structure exists yet, the agent must NOT create it silently — it proposes the directory structure and asks the user to approve it before writing anything.
5. Keep private paths and credentials in a local overlay.

The full procedure is **enforced inside the copied prompt**, not printed on the page. The dashboard shows only a slim one-line callout ("hit copy, paste into your agent") with two compact mode chips (`REPO` → clone & symlink; `DOC` → place into discovery chain) — enough to convey the mechanism without dumping prompt text the user never needs to read.

---

## 4. Visual Language & Theme System

The dashboard uses a **light, technical, developer-docs** aesthetic — precise, legible, and reference-like rather than promotional. It should read like a well-set man page or API index.

### Palette (cool neutrals, light)
* **Page**: paper-cool off-white `#f7f8fa`; surfaces `#fbfcfd` / `#ffffff`.
* **Ink**: slate `#1c2733`; secondary text `#5b6675` / `#6b7585`; faint mono numerals `#b9c0cb`.
* **Hairlines**: `#e6eaef` / `#edf0f3` for dividers and card borders.
* **Accent (single)**: steel blue `#1f6f8b`, used sparingly for kickers, mono labels, the active filter, and the copy affordance. No gradients.

### Typography
* **IBM Plex Sans** — headings and body. Tight tracking on display sizes (`-.02em`), comfortable 1.55–1.62 line-height on body.
* **IBM Plex Mono** — all metadata: section kickers, type badges (`REPO` / `DOC`), index numbers, counts, filter pills, code blocks. Monospace carries the "technical registry" tone.

### Layout
* **Limited-width single column** (`max-width: 1080px`, registry rows reading comfortably within it) — chosen over a card grid so dozens of entries read as one scannable register, with equal-height rows and clean CJK wrapping.
* **Header**: a mono kicker (`THE REGISTRY · N SKILLS · 5 DOMAINS`) over a large two-line display title and a single supporting sentence.
* **Flow-based grouping**: skills are sectioned by **where they sit in the agent's working flow**, not by what they technically are. Almost any task an agent does runs *intake → process → output*, so the registry follows that spine and adds the two cross-cutting layers that support it. The five sections are **Intake** (bring context in), **Analyze & Research** (turn data/info into insight), **Output & Delivery** (produce artifacts for people), **Infrastructure** (the runtime that runs the agents), and **Best Practices** (how to work well). The `REPO` / `DOC` badge is an orthogonal axis (it only selects the install mode), so a section freely mixes both. A handful of skills genuinely serve two stages (email reads *and* sends; Google Docs is read *and* published); these are listed once in their primary stage and carry a small `↺ also…` marker rather than being duplicated, which keeps the 01–N numbering continuous. The type filter shares this exact taxonomy, so grouping and filtering never present two competing classifications.
* **Skill row**: `[mono index] · [name + bordered type badge] · [one-line description] · [copy + ↗]` on a stable grid, so the action column always aligns.
* **Sticky controls**: a search field plus **bordered box-style** filters, one per flow stage (`ALL / INTAKE / ANALYZE / OUTPUT / INFRA / PRACTICES`), that stick to the top while scrolling. Filtering hides non-matching rows and collapses empty groups; an empty-state line appears when nothing matches.

### Components & Micro-Interactions
* **Type badge**: hairline-bordered mono chip; `DOC` carries a faint steel tint to distinguish it from `REPO`.
* **Copy feedback**: the `copy` chip turns green and reads `copied ✓` for ~1.5s, then reverts. Protocol-card buttons behave the same against the dark bar.
* **Hover**: rows lift to a faint steel wash (`#f3f7f9`); links and read-blog chips brighten their border to the accent. No scaling, glow, or neon.
* **FAQ**: lightweight accordion; the first item is open by default; chevron rotates on toggle.

---

## 5. Bilingual Handling (EN ↔ ZH)

`index.html` (English) and `index_zh.html` (Chinese) share the same structure and visual system, with **per-language type tuning** rather than a pixel-identical swap:
* Latin copy uses IBM Plex Sans; Chinese copy pairs the same mono labels with a CJK-optimized sans stack, with slightly increased line-height and looser letter-spacing for Han legibility.
* Display-title line breaks are set per language (English breaks after "Skills"; Chinese breaks at a natural clause boundary).
* The mono metadata layer (badges, counts, filters, code) stays identical across both, preserving the technical identity.
* A persistent `EN / 中文` toggle sits in the top nav of both pages.

---

## 6. File Mapping

The repository maintains strict bilingual pairing and representation formats:

```text
skills/
├── README.md               # English Markdown Index (Default landing)
├── README_zh.md            # Chinese Markdown Index
├── index.html              # English Dashboard
├── index_zh.html           # Chinese Dashboard
├── styles.css              # Dashboard stylesheet
├── docs/
│   ├── prd.md              # Product Requirements Document
│   ├── rfc.md              # Architectural RFC
│   ├── design.md           # Design Specification (This document)
│   └── working.md          # Project changelog
└── AGENTS.md               # Workspace rules for modifying agents
```
