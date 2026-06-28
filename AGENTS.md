# AGENTS.md

Welcome! This is the public GitHub repository and showcase for our public AI agent skills ecosystem.

## Project Structure
- `README.md` / `README_zh.md`: The English (default) and Chinese documentation hubs. They list ecosystem skills (standalone repos) and link to the showcase for the full built-in skill list.
- `index.html` / `index_zh.html`: The interactive HTML showcase pages served via GitHub Pages. They list **all** skills — both ecosystem (standalone repo) and built-in (single-file in `context-infrastructure`). Each entry has a copy button for the raw skill URL and a direct link.
- `docs/`: Design documents, requirements, and project logs.
  - `prd.md`: Product Requirements Document outlining goals and scope.
  - `rfc.md`: Request for Comments outlining design decisions (e.g., dual-language setup, directory design).
  - `working.md`: The project changelog and lessons learned.

## Rules for Agents
1. **Bilingual Updates**: Any updates to the list of skills, descriptions, or URLs must be applied to both English and Chinese versions (`README.md` <-> `README_zh.md` and `index.html` <-> `index_zh.html`).
2. **Documenting Work**: Keep `docs/working.md` updated. At the end of each session, log what was accomplished under the `# Changelog` section using simple bullet points.
3. **Commit Frequently**: Commit after completing meaningful stages (e.g., scaffolding, populating READMEs, developing HTML styles).
4. **Git Branching**: Ensure the active branch is `master`. Do not use `main`.

## Skill Categories

The registry contains two types of skills, both displayed in the showcase:

### Ecosystem Skills (standalone repos)
Setup-required connectors and tools (e.g., Google Docs, Typefully, Stripe, Resend). Each lives in its own public GitHub repository. Listed in `README.md`/`README_zh.md` as bullet-point links, and in `index.html`/`index_zh.html` as showcase entries with repo URLs.

### Built-in Skills (single-file in context-infrastructure)
Generic workflows and best practices that require no external API keys or configuration. Each is a single Markdown file in the `context-infrastructure` repo's `rules/skills/` folder. Not individually listed in README (summarized as "N+ built-in workflow guides"), but fully listed in the showcase HTML pages with direct GitHub blob URLs.

## Architectural Conventions

### Local-Overlay Developer Flow
* **Development Workspace**: Link skills via relative symbolic links (`rules/skills/<file>.md -> ../../adhoc_jobs/<skill_repo>/skills/<file>.md`) in the private workspace. This allows editing within the rules directory while tracking edits inside the sub-repository's git tree.
* **Public Infrastructure**: Resolve relative symbolic links into flat reference implementations when copying/publishing to public repositories to prevent broken links for cloning users.

