# Changelog

All notable changes to this project are documented here. Versions follow [Semantic Versioning](https://semver.org/).

## [1.1.0] — 2026-04-13

### Summary

This release is a **structural overhaul** of how the diagnostic runs: the old flat “assessment form” is gone; behavior definition, synthesis, BCW ranking, user feedback, and optional outputs are first-class parts of the pipeline.

### Behavior definition

- **`assets/behavior-canvas.md`** — Single place for the structured behavior definition (who, will do what, to what extent, context, outcome, optional current-state pattern vocabulary).
- **Prior attempts** — New canvas field for what has already been tried and why it did not work, so the diagnosis is not blind to failed interventions.

### Lens navigation and depth

- **`references/lenses/lens-map.md`** (formerly `dimensional-ids.md`) — Entry point: sub-lens shortcodes, diagnostic questions, ID conventions.
- **Pattern guidance + Refs** — Each sub-lens has Pattern guidance blocks with machine-scannable **Refs** lines (BCW, BCT, dimensions, cross-lens shortcodes).

### Practitioner worksheet (replaces assessment form)

- **Removed** `assets/assessment-form-template.md` (flat per-dimension scoring tables).
- **Added** `assets/practitioner-worksheet.md` — Synthesis and intervention design:
  - COM-B **priority ranking** (C / O / M) before sub-lens detail
  - Per-lens synthesis tables + narrative (what to try / what not to try)
  - Cross-lens interactions
  - **BCW function ranking** (top 5 with rationale and top BCTs)
  - Intervention implications
- Step 3’s **explicit output** is the filled worksheet; it can also be delivered as **Phase B — Working analysis**.

### Delivery and templates

- **Phase B** now has three paths: in-depth report, action plan, **working analysis** (filled worksheet).
- **`assets/output-template.md`** — Translation notes so each format turns worksheet depth into readable prose; **feedback prompt** after Phase A before offering Phase B.

### Feedback loop

- After **Phase A** (summary + key insights), the agent pauses for user reaction: resonance, prior tries, missing context.
- **Substantive new information** updates the behavior canvas and **re-runs from Step 2** (fresh worksheet), not a patch on the old conclusion.

### Orchestration docs

- **`SKILL.md`**, **`references/flow.md`**, **`references/guide.md`** — Aligned on the pipeline, worksheet, feedback loop, and guardrails.
- **`scripts/apply_lens_ids.py`** — No longer transforms the removed assessment form.

### Docs and discoverability

- **`README.md`** — Mermaid diagram of the high-level flow (optional feedback branch to re-run lens work).

### Migration note

If you pinned workflows to **`assessment-form-template.md`**, switch to **`practitioner-worksheet.md`** and lens files for dimensions; there is no combined “all dimensions in one table” file anymore.

---

## [1.0.0] — 2026-04-12

Initial tagged release: README positioning, COM-B / BCW / BCT skill layout, lens files, and install paths for Cursor and other agents.

[1.1.0]: https://github.com/johnpcutler/change-lenses-and-actions/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/johnpcutler/change-lenses-and-actions/releases/tag/v1.0.0
