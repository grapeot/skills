# AGENTS.md

Welcome! This is the public GitHub repository and showcase for our public AI agent skills ecosystem.

## Project Structure
- `README.md` / `README_zh.md`: The English (default) and Chinese documentation hubs detailing the skills and how to use them.
- `index.html` / `index_zh.html`: The HTML pages served via GitHub Pages for a highly visual, premium showcase of the skills.
- `docs/`: Design documents, requirements, and project logs.
  - `prd.md`: Product Requirements Document outlining goals and scope.
  - `rfc.md`: Request for Comments outlining design decisions (e.g., dual-language setup, directory design).
  - `working.md`: The project changelog and lessons learned.

## Rules for Agents
1. **Bilingual Updates**: Any updates to the list of skills, descriptions, or URLs must be applied to both English and Chinese versions of the README and GitHub Pages (`README.md` <-> `README_zh.md` and `index.html` <-> `index_zh.html`).
2. **Documenting Work**: Keep `docs/working.md` updated. At the end of each session, log what was accomplished under the `# Changelog` section using simple bullet points.
3. **Commit Frequently**: Commit after completing meaningful stages (e.g., scaffolding, populating READMEs, developing HTML styles).
4. **Git Branching**: Ensure the active branch is `master`. Do not use `main`.

## Architectural Conventions for Skills

### 1. Ecosystem Segmentation
* **Built-in Skills**: Keep strictly to generic, out-of-the-box workflows and best practices in the core `context-infrastructure` rules folder. They must not require external API keys or configurations.
* **Ecosystem Skills**: Keep setup-required connectors (like Google Docs, Typefully, Stripe) in standalone public repositories. List them in `docs/SKILL_ECOSYSTEM.md` and the visual showcase. Do not copy their configurations as flat files into the public大仓 to avoid broken references.

### 2. Local-Overlay Developer Flow
* **Development Workspace**: Link skills via relative symbolic links (`rules/skills/<file>.md -> ../../adhoc_jobs/<skill_repo>/skills/<file>.md`) in the private workspace. This allows editing within the rules directory while tracking edits inside the sub-repository's git tree.
* **Public Infrastructure**: Resolve relative symbolic links into flat reference implementations when copying/publishing to public repositories to prevent broken links for cloning users.

