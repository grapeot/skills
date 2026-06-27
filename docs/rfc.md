# RFC: Architectural Design for AI Agent Skills Showcase

## 1. Project Organization
The repository will contain the following public-facing components:
- `README.md`: English documentation hub.
- `README_zh.md`: Chinese documentation hub.
- `index.html`: English visual showcase page.
- `index_zh.html`: Chinese visual showcase page.
- `styles.css`: Shared styling sheet for the visual showcase.
- `docs/`: PRD, RFC, and project logs.

## 2. Multi-Language Linking Flow
To prevent fragmentation and ensure a seamless experience:
- **English Default**: `README.md` and `index.html` serve as the root page.
- **Top Bar Prompts**:
  - English files begin with: *"Also available in: [简体中文 (Chinese)](README_zh.md) | For a more visual experience, visit our [Web Showcase](https://grapeot.github.io/skills/)."*
  - Chinese files begin with: *"本文档也有英文版：[English Version](README.md) | 想要获得更直观的视觉体验，请访问我们的 [网页展示端](https://grapeot.github.io/skills/index_zh.html)。"*
- This ensures both human readers and AI agents can navigate directly to their preferred language and format.

## 3. UI/UX & Web Design Decisions
The visual showcase will be styled as a premium dashboard matching high aesthetic standards:
- **Theme**: Futuristic dark theme with glassmorphism (translucent white card overlays, backdrop-filter blur).
- **Typography**: Imports Google Font "Outfit" for headers and "Inter" for body text to create a clean, modern aesthetic.
- **Color Palette**:
  - Background: Dark slate/navy (`#0f172a` / HSL `222, 47%, 11%`).
  - Cards: Semi-transparent gray (`rgba(30, 41, 59, 0.7)`).
  - Accents: Vibrant gradients (Cyan to Violet / HSL `190, 90%, 50%` to `270, 90%, 60%`).
- **Layout**: CSS Grid representing skill cards categorized by:
  - 🛠️ **API Guides & CLI Tools**: Connectors and utilities.
  - 🔄 **Workflows**: Comprehensive multi-step agent behaviors.
  - 💡 **Best Practices**: Methodology and AI programming rules.
- **Interactions**:
  - Hover effects on cards (slight lift, scaling, gradient border glow).
  - Instant category filtering (using inline JavaScript).
  - Direct copy-to-clipboard for installation commands or repo URLs.

## 4. Skills Directory Strategy
We aggregate skills from two main vectors into a single structured list:
1. **Generic Skills**: Residing inside the public `context-infrastructure` rules/skills directory. These must be generic methodologies (Workflows or Best Practices) that work out-of-the-box without external API keys or configurations. Link format points directly to `https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/<filename>`.
2. **Technical Skills with Code**: Standalone repositories representing setup-required tools (e.g. `tavily-skill`, `gdocs-skill`). Link format points to `https://github.com/grapeot/<repo-name>`.

Any skills requiring custom accounts, credentials, or complex configurations are kept strictly out of the core `context-infrastructure` folder to maintain it as a clean, out-of-the-box reference.

