# Design Specification: AI Agent Skills Showcase & Registry

This document outlines the architectural, interaction, and visual design decisions for the AI Agent Skills Showcase and Registry.

---

## 1. Conceptual Architecture

The project is built on the belief that AI coding agents require a different interface design than traditional software components.

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
2. **Evaluation**: The developer filters by categories (Tools, Workflows, Best Practices) and reads the descriptions.
3. **Trigger**: The developer clicks the "Copy Prompt" button on a skill card.
4. **Execution**: The developer pastes the installation prompt into the agent's chat interface (e.g., Cursor, Claude Code). The agent executes the prompt, cloning the repository, creating symlinks, and registering the skill.

### AI Agent Flow
1. **Index Parsing**: An agent receives a request to install a skill or search for capabilities. It reads the markdown index (`README.md` or `README_zh.md`).
2. **URL Retrieval**: The agent extracts the public repository URL or the direct markdown file link.
3. **Workspace Integration**: The agent executes a terminal command to clone the repo, creates a symlink in the local rules folder, and appends the path to the workspace's global `INDEX.md`.

---

## 3. Visual Language & Theme System

The visual dashboard employs a futuristic dark slate aesthetic representing intelligent agent workspaces.

### Palette & Styling
* **Background**: Slate Navy (`#0f172a` / HSL `222, 47%, 11%`) providing a dark, high-contrast workspace.
* **Card Material**: Glassmorphic panels (`rgba(30, 41, 59, 0.7)` with `backdrop-filter: blur(12px)` and a thin border `rgba(255, 255, 255, 0.1)`).
* **Accent Gradients**: Vibrant HSL gradients (Cyan to Violet) used for primary hover borders, tag outlines, and call-to-actions, representing the flow of intelligence.

### Micro-Interactions
* **Card Hover**: Cards scale slightly (`scale(1.02)`), lift upward, and cast a neon cyan-to-violet drop shadow.
* **Filter Transition**: Cards animate using CSS transitions when categories are toggled.
* **Copy Feedback**: Clicking the copy button replaces the copy icon with a green checkmark icon, animates the button border, and shows a tooltip saying "Copied!".

---

## 4. File Mapping

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
