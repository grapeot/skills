# Working Log: AI Agent Skills Showcase

## Changelog

### 2026-06-27
- Initialized repository scaffolding.
- Created `AGENTS.md` and `.gitignore`.
- Drafted Product Requirements Document (`docs/prd.md`).
- Drafted Request for Comments (`docs/rfc.md`).
- Prepared working log (`docs/working.md`).
- Cleaned up link mapping to use the correct `main` branch for `context-infrastructure`.
- Finalized architecture: retain classic template docs (Google Docs, Send Email, Share Report, Growth Analytics, Semantic Search) inside `context-infrastructure/rules/skills/` as reference implementations/overlays.
- Restored Doc links and added Send Email, Share Report, Growth Analytics, and Semantic Search cards to the HTML web dashboards in the `skills` showcase repository.
- Added `opencode-docker` under Agent operations in both showcase dashboards and `docs/SKILL_ECOSYSTEM.md`.


## Lessons Learned
- **Bilingual Consistency**: Ensure updates are mirrored across all four key entrypoints (`README.md`, `README_zh.md`, `index.html`, `index_zh.html`) to prevent documentation drift.
- **Progressive Disclosure Representation**: Clearly explain to users that a "skill" is fundamentally a set of natural language instructions (a markdown file), and optionally accompanied by a helper script or CLI tool.
