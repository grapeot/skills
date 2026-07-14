# Skills Registry Agent Guide

## Start Here

Read these files before changing the registry:

1. `skills/skill_registry_lifecycle.md`: canonical lifecycle contract for creating, forking, adding, updating, removing, privacy-reviewing, and releasing a registry.
2. `docs/prd.md` and `docs/rfc.md`: audience, taxonomy, packaging, localization, and install design.
3. `docs/working.md`: prior changes and maintenance failures.

## Registry Contract

- `master` is the canonical baseline. Make changes on a feature branch based on current `master`; do not use `main` or edit directly on `master`.
- Keep all localized projections synchronized. Entry changes must update `README.md` with `README_zh.md` and `index.html` with `index_zh.html` wherever that entry appears.
- Update `docs/working.md` for meaningful registry or governance changes.
- Do not publish personal paths, credentials, internal endpoints, customer context, proprietary assumptions, or local aliases. Keep them in private overlays.
- Do not enable auto-merge. Merge only after CI passes and the required named privacy and functional reviewers explicitly approve the change.

## Packaging Rules

- **REPO:** A setup-required connector or executable tool with its own canonical repository. Registry links point to the repository.
- **DOC:** A standalone workflow or best-practice document. Registry links point directly to the canonical Markdown file.
- Local workspaces may expose skills through relative symlinks. Public repositories must use flat files or valid public URLs so a fresh clone does not inherit broken links.

## Required Verification

Run from the repository root:

```bash
python scripts/check_registry.py
python scripts/check_public_content.py
git diff --check
```

Automated privacy checks are necessary but not sufficient. The reviewer must inspect the complete diff and any newly linked source before approval.
