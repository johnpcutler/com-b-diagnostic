# Diagnostic flow (canonical)

Single source of truth for the **ordered pipeline** used in [`scenarios/`](scenarios/) and recommended for any COM-B diagnosis in this repo. Scenario narratives implement this flow as **Step 1** … **Step 7**; the **digest** block at the top of each scenario is a compressed, code-like view of the same outputs.

---

## Pipeline (pseudocode)

Treat each step as a function: named inputs, named outputs, explicit file dependencies.

```text
INPUT
  behavior_in_context   // what people do or fail to do, with enough texture to reason about COM-B

STEP 1  classify_state()
  READ    com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md
  OUT     state_id                      // S1..S7; full name from cycle
          state_rationale               // which characteristics / state signals matched

STEP 2  identify_blockers()
  READ    com-b-bcw-bct/com-b-behavior-states-primary-secondary-blockers.md
          com-b-bcw-bct/com-b-abbreviations-reference.md   // decode PC, PHC, PO, SO, RM, AM
  OUT     primary_blockers[]        // COM-B codes; * in digest
          secondary_blockers[]

STEP 3  deepen_with_lenses()
  READ    lenses/capability-lenses.md          // PC, PHC
          lenses/motivation-lenses.md          // RM, AM
          lenses/physical-opportunity-lenses.md
          lenses/social-opportunity-lenses.md
  OUT     lens_hits.{PC|PHC|PO|SO|RM|AM}   // dimensional IDs + short tags
          // PO/SO: section.dimension  (n.m)
          // PC/PHC/RM/AM: sublens.dimension (x.y.z)

STEP 4  map_intervention_functions()
  READ    com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md   // tables 1–3
  OUT     bcw_order                 // ED, TR, PE, …; >> / > for emphasis in digest

STEP 5  select_bcts()
  READ    com-b-bcw-bct/bct-taxonomy.md           // technique IDs; groupings from mapping table 3
  OUT     bct_by_function           // e.g. ER→12.1,12.5 | EN→1.1,2.2

STEP 6  tool_levers()
  READ    com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md   // per-state levers
          com-b-bcw-bct/com-b-tool-influence-mechanisms-and-levers.md  // product/tool lens
  OUT     tool_notes_by_com_b       // digest: PO:foo, PC:bar, …

STEP 7  intervention_design()
  IN      all prior OUTs
  OUT     phases[]                  // timeboxed rollout + sustainment
          // ties BCW + BCT + levers to sequence and ownership
```

---

## Digest block (scenario header convention)

Immediately after the scenario title, a **fenced code block** holds the digest: **outputs only**, no prose. Same field names across scenarios so diffs and skims stay predictable.

| Field | Role |
|--------|------|
| `state` | State shorthand, e.g. `S2: Realized but Friction-Filled` |
| `blockers` | COM-B codes; `*` = primary |
| `lenses.PC` … `lenses.AM` | Lists of `id short-tag` from the lens files (only branches in play) |
| `functions` | BCW function ordering for this case |
| `bcts` | `FUNCTION→n.n,n.n` groups, `|` between functions |
| `tools` | Short tokens keyed by COM-B branch |
| `phases` | Rollout sequence, e.g. `[wk1-3] A+B → [wk4-8] C` |

---

## Narrative sections ↔ steps

| Section heading | Step |
|-----------------|------|
| **Step 1:** Classify the behavior state | 1 |
| **Step 2:** Identify COM-B blockers | 2 |
| **Step 3:** Deepen with lenses | 3 |
| **Step 4:** Map to intervention functions | 4 |
| **Step 5:** Select BCTs | 5 |
| **Step 6:** Tool levers | 6 |
| **Step 7:** Intervention design | 7 |

Body text under **The situation** is context only; it is not a numbered pipeline step.

---

## Source files (paths)

| Need | File |
|------|------|
| States, per-state blockers, tool levers | [`com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md`](com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md) |
| Primary/secondary blocker cheat sheet | [`com-b-bcw-bct/com-b-behavior-states-primary-secondary-blockers.md`](com-b-bcw-bct/com-b-behavior-states-primary-secondary-blockers.md) |
| COM-B abbreviations | [`com-b-bcw-bct/com-b-abbreviations-reference.md`](com-b-bcw-bct/com-b-abbreviations-reference.md) |
| COM-B → BCW → BCT groupings | [`com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md`](com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md) |
| Full BCT taxonomy | [`com-b-bcw-bct/bct-taxonomy.md`](com-b-bcw-bct/bct-taxonomy.md) |
| Tool mechanisms | [`com-b-bcw-bct/com-b-tool-influence-mechanisms-and-levers.md`](com-b-bcw-bct/com-b-tool-influence-mechanisms-and-levers.md) |
| Lenses | [`lenses/capability-lenses.md`](lenses/capability-lenses.md), [`lenses/motivation-lenses.md`](lenses/motivation-lenses.md), [`lenses/physical-opportunity-lenses.md`](lenses/physical-opportunity-lenses.md), [`lenses/social-opportunity-lenses.md`](lenses/social-opportunity-lenses.md) |
| Repo overview | [`README.md`](../README.md) |

---

## LLM / author notes

- Run steps **in order**; later steps assume earlier outputs. Lens deepening (step 3) is where ambiguous COM-B codes become precise enough for BCT and tool choices.
- Do not treat the seven **behavior states** as a maturity ladder; see step 6 / cycle text on regressions.
