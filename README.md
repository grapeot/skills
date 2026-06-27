Also available in: [简体中文 (Chinese)](README_zh.md) | For a visual experience, visit our [Web Showcase](https://grapeot.github.io/skills/).

# AI Agent Skills Registry & Showcase

This repository serves as a centralized showcase and registry for **AI Coding Agent Skills**. 

---

## 1. What is a Skill? (The Philosophy)

Unlike typical editor extensions (like Cursor, Codex, or Cloud Code plugins) which rely on vendor-locked JSON schemas, strict function definitions, or heavy SDK bindings, our ecosystem is built on a different paradigm:

1.  **Platform-Agnosticism & Natural Language First**: A skill is fundamentally a Markdown guide (`SKILL.md`) outlining rules, prompts, and reasoning patterns. Any agent can read and follow it. If a task requires execution, we pair it with a lightweight Python CLI tool. It works seamlessly across Claude Code, Cursor, OpenCode, or custom terminal agents.
2.  **Process & Result Certainty**: Rather than relying on fuzzy instructions, our skill templates define clear execution boundaries, validation rules, and outcome verification checklists to ensure the agent executes task segments with absolute certainty.
3.  **Files-as-Interfaces**: Tools interact with the workspace by reading and writing files. Inputs and outputs are plain-text files (Markdown, JSON, SQLite) rather than remote server endpoints, keeping agent work inspectable, stateful, and revertible via Git.
4.  **Local-Overlay Isolation**: Public skill repositories define generic technical interfaces. All private folder paths, credentials, and custom aliases are stored in a local overlay file in the user's private workspace.

### Key Background Reading
*   **Methodology**: [Step Two to Using AI Well: Write the Skill Before You Execute](https://yage.ai/skill-first-en.html) (Chinese: [用好AI的第二步：先写Skill再执行](https://yage.ai/skill-first.html))
*   **Infrastructure Design**: [Why AI only says correct nonsense, and how to push it out of its comfort zone](https://yage.ai/context-infrastructure.html)

---

## 2. FAQ & Installation Guide

### Q: How do I install a skill?
It is completely prompt-driven. You don't install plugins or compile packages. Simply copy the GitHub URL of the skill and tell your AI Agent (e.g., Cursor or Claude Code):
```text
Install this public skill repo into my workspace:
<GitHub URL of the Skill>

Read the rules in this repo, clone/vendor it under 'adhoc_jobs/', create a relative symlink under 'rules/skills/', and register it in the rules index.
```
The agent will run the git clone, map the files, and configure the local rules by itself.

### Q: Does it work with my editor / LLM?
Yes. Since the interface is just files and standard terminal commands, it works with any coding agent that can read workspace files and execute terminal tasks.

---

## 3. Skills Registry

### 📈 Social Media, Sales & Cost Analytics
| Skill | Type | Description | Link |
|---|---|---|---|
| **typefully-twitter-skill** | Repo | Schedule draft tweets, queue threads, and fetch X (Twitter) statistics | [GitHub](https://github.com/grapeot/typefully-twitter-skill) |
| **stripe-skill** | Repo | Read-only Stripe integrations to extract sales metrics, subscription trends, and logs | [GitHub](https://github.com/grapeot/stripe-skill) |
| **ai_usage_dashboard** | Repo | Track cross-platform API token consumption, estimate costs, and export stats | [GitHub](https://github.com/grapeot/ai_usage_dashboard) |

### 🏠 Everyday Quantification & Life Loggers
| Skill | Type | Description | Link |
|---|---|---|---|
| **health-quantification** | Repo | Ingest Apple Health metrics, track caffeine/sleep logs, and run regressions in local SQLite | [GitHub](https://github.com/grapeot/health-quantification) |
| **roest-analysis** | Repo | Scrape Roest coffee roaster API, detect crack clusters, and chart roasting telemetry | [GitHub](https://github.com/grapeot/roest-analysis) |
| **intake-skill** | Repo | Ingest voice recording notes, run local transcription, and maintain organized audio logs | [GitHub](https://github.com/grapeot/intake-skill) |

### 💼 Office Automation & Creative Media
| Skill | Type | Description | Link |
|---|---|---|---|
| **gdocs-skill** | Repo | Search, publish, share, and manage Google Docs using Markdown and Tab interfaces | [GitHub](https://github.com/grapeot/gdocs-skill) |
| **outlook_skill** | Repo | Download, archive, and send Outlook.com emails, parse calendar invites, and format Markdown | [GitHub](https://github.com/grapeot/outlook_skill) |
| **resend_email_skill** | Repo | Send custom domain emails, check attachments, and retrieve notifications | [GitHub](https://github.com/grapeot/resend_email_skill) |
| **imessage_skill** | Repo | Send macOS iMessages using CLI; maps contacts to local overlay names | [GitHub](https://github.com/grapeot/imessage_skill) |
| **pptx.skill** | Repo | Read, write, and render slide decks with strict design layouts | [GitHub](https://github.com/grapeot/pptx.skill) |
| **image-generation-skill** | Repo | Generate text-to-image prompts, edit images, and upscale resolution via Gemini/GPT | [GitHub](https://github.com/grapeot/image-generation-skill) |
| **tiff-icc-profile** | Repo | Embed default P3-D65 or custom ICC color profiles into unmarked TIFF files | [GitHub](https://github.com/grapeot/tiff-icc-profile) |
| **online-media-skill** | Repo | Download online videos, run ASR transcription, and format query packs | [GitHub](https://github.com/grapeot/online-media-skill) |

### ⚙️ Agent Infrastructure & Local Daemons
| Skill | Type | Description | Link |
|---|---|---|---|
| **process-launcher** | Repo | Local HTTP process daemon to bridge GUI/TCC permissions, logs, and process cancellations | [GitHub](https://github.com/grapeot/process-launcher) |
| **opencode_skill** | Repo | Submit and monitor OpenCode tasks, run cron pipelines, and archive SQLite databases | [GitHub](https://github.com/grapeot/opencode_skill) |
| **opencode-docker** | Repo | Docker deployment configurations to quickly containerize OpenCode execution environments | [GitHub](https://github.com/grapeot/opencode-docker) |

### 🧠 Built-in Cognition, Workflows & Best Practices
| Skill | Type | Description | Link |
|---|---|---|---|
| **AI CLI Agent Guide** | Doc | Architectural rules for designing CLI interfaces and nesting agent-to-agent calls | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/ai_agent_cli_guide.md) |
| **Share Report to Web** | Doc | Converts Markdown to HTML pages and deploys to servers via SSH | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/share_report.md) |
| **Semantic Search Skill** | Doc | Retrives workspace memory and background knowledge using vector database queries | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/semantic_search.md) |
| **Parallel Subagents** | Doc | Orchestrates concurrent background subagents for independent task branches | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/workflow_parallel_subagents.md) |
| **Deep Research & Survey** | Doc | Gathers info using multiple parallel agents with overlapping topics to cross-validate | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/workflow_deep_research_survey.md) |
| **Cognitive Profile Extraction** | Doc | Iteratively extracts predictable cognitive axioms and traits from conversation logs | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/workflow_cognitive_profile_extraction.md) |
| **AI Programming Mindset** | Doc | Strategy detailing the 70% accuracy boundary and script-writing priority | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_ai_programming_mindset.md) |
| **Skill Writing Guide** | Doc | Meta-instructions explaining how to write reusable, outcome-focused Skill files | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_skill_writing.md) |
| **PDF to Markdown** | Doc | Employs Docling parser for high-accuracy tabular and layout extraction from PDFs | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_pdf_to_markdown.md) |
| **Temporal Verification** | Doc | Guidelines to verify information lying past model knowledge cutoff dates | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_temporal_info_verification.md) |
| **Staged Workflow** | Doc | Maintains a strict "isolate-process-validate" loop to execute dry-runs on code changes | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_staged_approach.md) |
| **Project Scaffold & Reorg** | Doc | Scaffolds loose workspaces into organized directories (docs/, src/, tests/) | [View File](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/project_scaffold.md) |
