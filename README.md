# AI Agent Skills Ecosystem

Also available in: [简体中文 (Chinese)](README_zh.md) | For a more visual experience, visit our [Visual Showcase](https://grapeot.github.io/skills/).

> **The Progressive Disclosure Paradigm for AI Agents.**
> A "Skill" is not a proprietary vendor API or a rigid schema. It is a natural language markdown instruction file that explains goals, success standards, and edge cases to an agent, accompanied by optional CLI tools or connectors. 

This repository is a central registry showcasing all public GitHub skills in our ecosystem. You can share this URL with any coding agent (like Claude Code, Cursor, Codex, or OpenCode) to help it understand and install these capabilities.

---

## The Philosophy: What is a Skill?

Most AI agents struggle with "hallucinating correct-sounding garbage" or repeating errors because they start each conversation blind.
A **Skill** solves this by externalizing knowledge and rules into markdown files that agents can discover and read.

We use **Progressive Disclosure**:
1. **L1 (Global Entry)**: An agent begins by reading `AGENTS.md` or `CLAUDE.md`, which routes it to a central index.
2. **L2 (Index Router)**: A simple file like `rules/skills/INDEX.md` lists available skills and mapping criteria.
3. **L3 (Detail Skill)**: The specific skill file (e.g., `skill_imessage.md`) detailing the exact CLI commands, parameters, boundaries, and safety rules.
4. **Local Overlays**: Keep private configurations (like contact aliases or API credentials) in local settings, while linking to public skill repositories for technical code and CLIs.

---

## Curated Skills Directory

### 🛠️ Connected Tools & API Guides

Specialized CLIs and connectors that extend an agent's capability to read/write external systems.

| Skill / Repo Name | Type | Description | Link |
|---|---|---|---|
| **tavily-skill** | Repo | Search & web extraction optimized for AI agents, returning clean JSON | [GitHub](https://github.com/grapeot/tavily-skill) |
| **gdocs-skill** | Repo | Google Docs creation, modification, sharing, and tab management | [GitHub](https://github.com/grapeot/gdocs-skill) |
| **outlook_skill** | Repo | Outlook.com email retrieval, rendering, and archiving | [GitHub](https://github.com/grapeot/outlook_skill) |
| **resend_email_skill** | Repo | Resend email sender, inbound parser, and MD exporter | [GitHub](https://github.com/grapeot/resend_email_skill) |
| **imessage_skill** | Repo | macOS send-only iMessage CLI with contact alias support | [GitHub](https://github.com/grapeot/imessage_skill) |
| **process-launcher** | Repo | Local HTTP process launcher for bridging TCC & GUI permissions | [GitHub](https://github.com/grapeot/process-launcher) |
| **ai_usage_dashboard** | Repo | Multi-platform AI token usage aggregator and dashboard | [GitHub](https://github.com/grapeot/ai_usage_dashboard) |
| **typefully-twitter-skill** | Repo | Typefully integration CLI for draft scheduling and X analytics | [GitHub](https://github.com/grapeot/typefully-twitter-skill) |
| **stripe-skill** | Repo | Stripe sales, growth, and transaction analysis CLI | [GitHub](https://github.com/grapeot/stripe-skill) |
| **pptx.skill** | Repo | AI-first presentation reader, editor, and renderer | [GitHub](https://github.com/grapeot/pptx.skill) |
| **image-generation-skill** | Repo | Gemini/GPT text-to-image generator and upscaler CLI | [GitHub](https://github.com/grapeot/image-generation-skill) |
| **tiff-icc-profile** | Repo | Color profile embedding tool for unmarked TIFF images | [GitHub](https://github.com/grapeot/tiff-icc-profile) |
| **health-quantification** | Repo | Apple Health ingestion server and health data CLI analyzer | [GitHub](https://github.com/grapeot/health-quantification) |
| **roest-analysis** | Repo | Roest coffee roaster API scraping and roast log analysis | [GitHub](https://github.com/grapeot/roest-analysis) |
| **intake-skill** | Repo | Audio recording parser and transcription intake CLI | [GitHub](https://github.com/grapeot/intake-skill) |
| **opencode-docker** | Repo | Docker deployment helper for OpenCode server instances | [GitHub](https://github.com/grapeot/opencode-docker) |
| **opencode_skill** | Repo | OpenCode session management, scheduling, and archiving tool | [GitHub](https://github.com/grapeot/opencode_skill) |
| **AI CLI Agent Guide** | Doc | Core guidelines on files-as-interface design and AI-to-AI calls | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/ai_agent_cli_guide.md) |

---

### 🔄 Workflows

Step-by-step methodologies guiding AI agents through complex multi-agent or multi-step tasks.

| Skill / File Name | Description | Link |
|---|---|---|
| **Parallel Subagents** | How to delegate subtasks to concurrent subagents without polling | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/workflow_parallel_subagents.md) |
| **Deep Research & Survey** | Scanning, dividing topics with overlap, and cross-validating research | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/workflow_deep_research_survey.md) |
| **Analytical Writing** | Translating facts into structured, high-opinion, translation-free texts | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/workflow_analytical_writing.md) |
| **Cognitive Profile Extraction** | Extracting predictable cognitive axioms from conversational history | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/workflow_cognitive_profile_extraction.md) |
| **Presentation Slide Deck** | 8-way parallel PowerPoint rendering and verification workflow | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/workflow_presentation_slides.md) |
| **Knowledge Flywheel** | Iteratively turning raw data into structured knowledge schemas | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/workflow_knowledge_flywheel.md) |
| **Online Media Ingestion** | Whisper transcribing, video downloading, and source parsing | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/workflow_bilibili_whisper_transcription.md) |
| **Delayed Execution** | Orchestrating deferred tasks and automated cron schedules | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/delayed_execution.md) |

---

### 💡 Best Practices

Conceptual frameworks and diagnostic tools for software development, debugging, and systems engineering.

| Skill / File Name | Description | Link |
|---|---|---|
| **AI Programming Mindset** | Core philosophy of agentic workflows vs reasoning chat models | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_ai_programming_mindset.md) |
| **Skill Writing Guide** | Meta-skill detailing how to write reusable skill documentation | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_skill_writing.md) |
| **1Password CLI Management** | Safeguarding keys and injecting credentials safely without hardcoding | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_api_key_management_1password_cli.md) |
| **Interview Evaluation** | AI cheat detection and evaluating technical candidate traits over skill lists | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_interview_evaluation.md) |
| **Markdown to HTML** | Structuring assets and publishing configurations safely | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_markdown_html_conversion.md) |
| **PDF to Markdown** | Leveraging Docling for highly accurate tabular and semantic PDF parsing | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_pdf_to_markdown.md) |
| **Temporal Verification** | Techniques to verify information lying past model knowledge cutoffs | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_temporal_info_verification.md) |
| **Staged Workflow** | Maintaining an isolated edit-validate feedback loop for safety | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_staged_approach.md) |
| **Multi-Agent Analysis** | Coordinating multiple agents on overlapping tasks to find contradictions | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_multi_agent_analysis.md) |
| **GUI Automation Method** | Mapping visual states into CLI scripts for tools lacking official APIs | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_gui_automation.md) |
| **AI Debugging & Diagnosis** | Systemic decision tree to resolve stuck, repeating, or buggy code edits | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_ai_debugging_diagnosis.md) |
| **AI Product Design** | Decoupling systems, designing rules, and chat vs workspace design | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_ai_product_design.md) |
| **Reverse Engineering Decisions** | Deconstructing trade-offs, constraints, and spaces of external designs | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_product_decision_analysis.md) |
| **Project Scaffolding** | Reorganizing scattered scripts into robust, modular repository templates | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/project_scaffold.md) |

---

## Installation Protocol

To let your coding agent install any skill, simply feed it the following instructions:

```text
Install this public skill repo into my workspace:
<Skill Repo GitHub URL or file URL>

Start from my workspace AGENTS.md or CLAUDE.md. Follow any WORKSPACE.md or skills/INDEX.md routing rules. Clone or vendor the repo under an appropriate project directory. Expose exactly one root skill to my global skill index or agent instructions. Keep private aliases, local paths, credentials, endpoint defaults, and business context in a local overlay, not in the public repo.
```

## Privacy & Safety

All repositories here are built with the **Publishable with Fake Data** principle.
- No real credentials, emails, or phone numbers are checked into public versions.
- Workspace-specific settings (e.g., recipient emails, contact aliases, API tokens) must live in a local overlay (like a local `.env` or `rules/skills/` config) and are never pushed upstream.
