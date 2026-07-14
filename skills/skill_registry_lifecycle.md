# Skill Registry Lifecycle

## Metadata

- **Type:** Workflow
- **Use when:** Creating, forking, extending, removing from, or maintaining an AI agent skill registry
- **Canonical example:** `https://github.com/grapeot/skills`
- **Last updated:** 2026-07-14

## Objective

Maintain a discoverable registry of reusable agent capabilities without turning the registry into an unreviewed copy of personal context. The finished registry must let humans and agents answer four questions: what capability exists, where its canonical source lives, how it is installed or read, and what review made it eligible for promotion.

This skill governs the registry lifecycle. It does not define the domain behavior of every listed skill, approve private material for publication, or replace a human owner, security reviewer, or compliance reviewer.

## Design Principles

### The registry is an index, not the source of truth

Each entry points to one canonical source. A standalone tool should keep its code, tests, and root skill in its own repository. A document-only skill may point to one canonical Markdown file. Do not silently fork skill content into the registry because duplicated copies drift.

### Promotion is selective

A useful personal workflow is not automatically a reusable skill. Promote only the generalizable core. Keep private paths, credentials, personal preferences, customer data, proprietary assumptions, and local aliases in a private overlay or the original workspace.

### One record may have several synchronized projections

Markdown indexes, visual pages, localized pages, search metadata, and counters are views of the same registry record. A change is incomplete if one projection disagrees with another. If the registry grows beyond hand-maintained projections, replace repeated markup with a canonical data file and generated views rather than adding more manual synchronization rules.

### Removal is a first-class operation

Deleting a stale, unsafe, or superseded entry is as important as adding one. Remove all public projections, aliases, counts, and install links while preserving an auditable explanation in version history. Do not keep a broken entry merely to preserve numbering.

### Results must be checkable

Define success through observable registry state: canonical links resolve, localized views agree, counts are correct, install mode matches packaging, tests pass, and privacy review leaves no unresolved findings. Process conventions support these outcomes but do not substitute for them.

### Human approval remains the promotion gate

Agents may prepare changes, run checks, open a pull request, and respond to review. They must not infer approval from silence. Keep platform auto-merge disabled. After all required named human reviewers explicitly approve, an authorized human may merge, or an agent may execute the merge only when the accountable human has explicitly instructed it to do so.

## Required Context

Read the following before changing a registry. Use the repository's equivalents when names differ.

| Context | Why it is required |
|---|---|
| Repository-level agent instructions, such as `AGENTS.md` | Branch, language, documentation, and review policy |
| Registry architecture, such as `docs/prd.md` and `docs/rfc.md` | Audience, taxonomy, packaging model, and intentional exclusions |
| Current human and agent entrypoints, such as `README*` and `index*` | Every projection that must remain synchronized |
| Validation code and CI configuration | Existing machine-checkable invariants and the command CI will run |
| Working log or changelog | Previous drift, failures, and decisions that should not be rediscovered |
| Canonical source of each affected skill | Exact name, URL, packaging type, public description, tests, and license |
| Public/private boundary for the deployment | What may be published, what stays in a local overlay, and who can approve promotion |
| Live Git state and branch protection | Baseline branch, existing changes, required checks, and reviewer requirements |

If any required context is missing, do not invent it. Record the missing input and stop before publication or merge. A local draft may still be prepared when it is clearly marked as unapproved.

## Success Criteria

A registry lifecycle change is complete only when every applicable criterion below is true.

### Registry integrity

- Every entry has one canonical name, source URL, packaging type, category, and concise capability description.
- The source exists and the listed skill or root instructions are actually discoverable at that source.
- Repo entries point to cloneable repositories. Doc entries point to readable files rather than repository landing pages.
- English, Chinese, visual, Markdown, search, count, and sequence projections agree where the registry supports them.
- Additions create no duplicate capability or duplicate canonical URL without an explicit reason.
- Removals leave no stale copy button, direct link, count, alias, or localized entry.
- Forks replace upstream identity, URLs, governance, and deployment assumptions while retaining required attribution and license notices.
- A registry created from scratch documents its taxonomy, canonical record fields, installation modes, public/private boundary, ownership, and validation contract before accepting entries.

### Skill quality and reuse boundary

- The promoted artifact states its objective, boundaries, required context, outputs, and testable acceptance criteria.
- Examples use synthetic or explicitly public data. They do not expose personal filesystem paths, credentials, internal hostnames, customer identifiers, private correspondence, or proprietary desk assumptions.
- Local configuration is represented as an overlay contract or placeholder, not embedded operational data.
- The source skill's focused tests or documented verification command pass when executable code is involved.

### Verification and governance

- Registry consistency checks, privacy checks, and `git diff --check` pass locally.
- The final diff contains only intended files and includes the project working log when required.
- Work occurs on a review branch based on the canonical baseline, not directly on the protected branch.
- The pull request explains the capability, source, affected projections, tests, privacy boundary, and removal or migration impact.
- CI passes and all privacy findings are resolved or explicitly blocked from merge.
- A named human owner gives the required functional approval. Security or compliance approval is also present when the registry policy or content requires it.
- The pull request records each required reviewer's name or account, review role, disposition, and review time. CI success does not substitute for any approval.
- Platform auto-merge remains disabled. An agent merges only under explicit instruction issued after all required approvals are recorded.

## Standard Practice

Choose the smallest operation that matches the requested outcome.

### Add or update an entry

Inspect the canonical source before writing registry copy. Classify the entry by user workflow and packaging, generalize any personal material, update every registry projection, then run source-focused tests and registry checks. Open a reviewable pull request that makes the promotion boundary visible.

### Remove or supersede an entry

Identify every projection and alias before editing. Remove the entry consistently, fix counts and ordering, and state whether a replacement exists. Preserve the reason in the pull request and changelog rather than leaving a tombstone in the user-facing registry unless users need a migration notice.

### Fork an existing registry

Treat the upstream repository as a reference implementation, not as the new organization's policy. Replace identity, canonical URLs, taxonomy assumptions, language requirements, reviewer roles, and public/private boundaries. Remove entries that the new owner cannot verify or support. Keep license and attribution obligations intact.

### Build a registry from scratch

Start with the minimum canonical record needed to render all intended views. Establish ownership, privacy boundaries, promotion gates, removal behavior, and automated invariants before scaling the catalog. Prefer generated projections once manual duplication becomes a recurring source of drift.

### Review and release

Use deterministic checks for structure and an independent reviewer for meaning. A privacy scan can detect likely secrets and local paths but cannot determine whether a research rule, customer name, or operational detail is proprietary. Keep the pull request open at `CI passed · Human review pending` until the accountable reviewer approves it. Record functional and privacy reviewers separately; one approval does not imply the other.

## Privacy Review

The privacy reviewer must inspect the complete diff and any new source material, not only the rendered registry card.

Check for:

- credentials, tokens, private keys, connection strings, and secret-manager references;
- personal home-directory paths, usernames, email addresses, device names, and local aliases;
- private IP addresses, internal domains, VPN or tailnet hostnames, and non-public endpoints;
- customer, employee, portfolio, account, meeting, or correspondence identifiers;
- proprietary procedures, assumptions, prompts, review history, or examples that reveal internal operations;
- metadata in copied files, screenshots, fixtures, and generated artifacts;
- combinations of otherwise harmless details that can re-identify a person or organization.

For this reference repository, run:

```bash
python scripts/check_registry.py
python scripts/check_public_content.py
git diff --check
```

Passing these commands is necessary but not sufficient. Record each named reviewer's account, role, disposition, and review time in the pull request.

## Known Pitfalls

These failure modes come from prior registry maintenance rather than hypothetical edge cases.

| Failure | Observable symptom | Prevention |
|---|---|---|
| Localized views drift | English and Chinese pages expose different skills or URLs | Update all projections together and compare canonical URL sets in CI |
| Counts become stale | Header total or group counter disagrees with rendered rows | Derive and validate counts instead of asserting a historical literal |
| Sequence numbers duplicate or skip | Several cards share one ordinal or numbering jumps | Validate a contiguous one-based sequence |
| A local symlink is published | The skill works in the author's workspace but breaks when cloned | Publish a flat file or a valid repository URL; keep symlinks only in local overlays |
| Branch names are assumed | A valid source is linked through a nonexistent `main` or `master` path | Verify the canonical source branch before publishing a Doc URL |

## Preventive Safeguards

The following controls address high-impact risks even when this repository has not recorded a corresponding incident:

- Inspect and validate the canonical source before promotion so registry copy cannot outrun source quality.
- Combine automated scanning with independent semantic review; secret scanning alone cannot identify proprietary context.
- Keep merge permission separate from execution. CI success is evidence, not approval, and platform auto-merge stays disabled.

## Output Contract

For any registry lifecycle task, leave behind:

- the updated canonical skill or registry projections;
- machine-checkable validation results;
- a changelog entry explaining the operation;
- a pull request or local review packet describing source, scope, privacy boundary, tests, and reviewer state;
- no merge when required approval remains pending.
