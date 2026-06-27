# PRD: Public AI Agent Skills Showcase

## 1. Objective
Create a centralized hub (repository and web showcase) to display, search, and explain all public GitHub skills for AI agents in both English and Chinese. The project aims to explain the "Skill" concept—not as complex vendor-locked features, but as natural-language instructions with optional CLIs following the progressive disclosure paradigm—and list all active public skills with links.

## 2. Target Audience
- **Developers & AI Builders**: Humans who want to understand what skills are available and how to install them in their workspaces.
- **AI Coding Agents** (e.g., Claude Code, Cursor, OpenCode, Codex): Agents that receive instructions to install a specific skill and need to look up documentation and public repo locations.

## 3. Key Requirements
1. **Bilingual Documentation**: Support both English (default) and Chinese versions of documentation, cross-linked at the top of every view.
2. **Double Exposure Formats**:
   - **Markdown Hub (`README.md` / `README_zh.md`)**: Text-first view on GitHub, direct and easy for AI agents to parse.
   - **Visual Showcase (`index.html` / `index_zh.html`)**: Rich visual experience served via GitHub Pages for humans.
3. **Progressive Disclosure Explanation**: Teach users that a skill is just a markdown instruction file + an optional CLI/connector.
4. **Curated Skills Directory**: A clean, categorized list of all public skills, including workflows, best practices, and API guides with working public GitHub URLs.
5. **Premium Web Design**: The visual page on GitHub Pages must feel state-of-the-art:
   - Modern typography (e.g., Outfit or Inter from Google Fonts).
   - Rich color palettes (dark mode by default, gradient borders, subtle neon accents).
   - Dynamic hover animations and micro-interactions.
   - Glassmorphic card layouts.
   - Responsive grid for different screen sizes.

## 4. Scope & Exclusions
- **No Private Data**: Do not list private details, API keys, or private aliases.
- **No Complex Frameworks**: The web pages are built purely with vanilla CSS and JS to ensure fast, zero-dependency deployment on GitHub Pages.
- **No Native Tests Required**: As the project contains only HTML/CSS and Markdown files, no test suite is required at this stage.
