Also available in: [简体中文 (Chinese)](README_zh.md)

# AI Agent Skills Registry

This repository is the central indexing hub for **AI Agent Skills**. 

> [!IMPORTANT]
> **Interactive Showcase & Registry**
> For the full, interactive visual experience—including categorized search, filter tabs, and one-click agent installation prompts—please visit our official dashboard:
> **👉 [https://grapeot.github.io/skills/](https://grapeot.github.io/skills/)**

---

## What is a Skill? (The Philosophy)

Unlike typical editor extensions (like Cursor, Codex, or Cloud Code plugins) which rely on vendor-locked JSON schemas, strict function definitions, or heavy SDK bindings, our ecosystem is built on a different paradigm:

1. **Platform-Agnosticism & Natural Language First**: A skill is fundamentally a Markdown guide (`SKILL.md`) outlining rules, prompts, and reasoning patterns. Any agent can read and follow it. If a task requires execution, we pair it with a lightweight Python CLI tool. It works seamlessly across Claude Code, Cursor, OpenCode, or custom terminal agents.
2. **Process & Result Certainty**: Rather than relying on fuzzy instructions, our skill templates define clear execution boundaries, validation rules, and outcome verification checklists to ensure the agent executes task segments with absolute certainty.
3. **Files-as-Interfaces**: Tools interact with the workspace by reading and writing files. Inputs and outputs are plain-text files (Markdown, JSON, SQLite) rather than remote server endpoints, keeping agent work inspectable, stateful, and revertible via Git.
4. **Local-Overlay Isolation**: Public skill repositories define generic technical interfaces. All private folder paths, credentials, and custom aliases are stored in a local overlay file in the user's private workspace.

### Key Background Reading
* **Methodology**: [Step Two to Using AI Well: Write the Skill Before You Execute](https://yage.ai/skill-first-en.html) (Chinese: [用好AI的第二步：先写Skill再执行](https://yage.ai/skill-first.html))
* **Infrastructure Design**: [Why AI only says correct nonsense, and how to push it out of its comfort zone](https://yage.ai/context-infrastructure.html)

### Maintain or Fork This Registry

The registry includes its own reusable [Skill Registry Lifecycle](skills/skill_registry_lifecycle.md). Read it before adding, removing, forking, or rebuilding a registry. It defines the design principles, required context, success criteria, privacy review, release gates, and known maintenance failures.

---

## Quick Reference (Registry List)

For a quick overview of the codebases, the standalone repository links are listed below:

### API Connectors & Tools
* [tavily-skill](https://github.com/grapeot/tavily-skill) — Web search and HTML scraping optimizer
* [gdocs-skill](https://github.com/grapeot/gdocs-skill) — Google Docs editor integration
* [outlook_skill](https://github.com/grapeot/outlook_skill) — Outlook.com mail and calendar scheduler
* [resend_email_skill](https://github.com/grapeot/resend_email_skill) — Custom domain Resend mailer
* [imessage_skill](https://github.com/grapeot/imessage_skill) — Local iMessage sender CLI
* [pptx.skill](https://github.com/grapeot/pptx.skill) — PPTX presentation generator
* [presentation_skill](https://github.com/grapeot/presentation_skill) — Previewable agent slide decks (Reveal.js); image-rendered by default, HTML modules on request—not PPTX
* [image-generation-skill](https://github.com/grapeot/image-generation-skill) — Upscaler and image generator
* [genai_portrait_skill](https://github.com/grapeot/genai_portrait_skill) — Identity-preserving portrait and headshot editing with photographic coherence
* [tiff-icc-profile](https://github.com/grapeot/tiff-icc-profile) — ICC color profile injector
* [online-media-skill](https://github.com/grapeot/online-media-skill) — Video downloader and Whisper transcriber
* [open_router_data_scraper](https://github.com/grapeot/open_router_data_scraper) — OpenRouter model activity data scraper (token usage, rankings, benchmarks)

### Life Loggers & Quantification
* [health-quantification](https://github.com/grapeot/health-quantification) — Apple Health SQLite regression analysis
* [roest-analysis](https://github.com/grapeot/roest-analysis) — Roest roaster telemetry graphs
* [intake-skill](https://github.com/grapeot/intake-skill) — Audio voice intake diary organizer

### Innovation & Research
* [innovation-assistant-skill](https://github.com/grapeot/innovation-assistant-skill) — Structured innovation engine (SIT + Think Bigger) as executable pipelines

### Agent Daemon & Devops
* [process-launcher](https://github.com/grapeot/process-launcher) — macOS HTTP process launcher bypass
* [opencode_skill](https://github.com/grapeot/opencode_skill) — OpenCode task runner
* [opencode-docker](https://github.com/grapeot/opencode-docker) — OpenCode docker config

*(For the complete list of 27+ built-in workflow guides and detailed copy-paste installation prompts, check the [Interactive Showcase](https://grapeot.github.io/skills/))*
