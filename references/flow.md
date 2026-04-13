# Diagnostic flow (canonical)

Single source of truth for the **ordered pipeline** recommended for any COM-B diagnosis in this repo. The full walkthrough with file pointers is in [`guide.md`](guide.md).

---

## Pipeline (pseudocode)

Treat each step as a function: named inputs, named outputs, explicit file dependencies.

```text
STEP 1  define_behavior()
  IN      user description, artifacts, or follow-up answers
  READ    assets/behavior-canvas.md                        // field definitions + coaching prompts + pattern vocabulary
  OUT     behavior_definition {
            behavior    // summary statement
            who         // actors
            will_do     // specific action
            to_extent   // frequency, depth, observable standard
            in_context  // environment, tools, constraints
            for_outcome // intended result
            current_state  // optional: pattern label (e.g. "aspirational only", "actively suppressed")
          }

STEP 2  research_com()
  READ    lenses/capability-lenses.md                     // C-lens: PC, PHC
          lenses/motivation-lenses.md                     // M-lens: RM, AM
          lenses/physical-opportunity-lenses.md            // O-lens: PO
          lenses/social-opportunity-lenses.md              // O-lens: SO
  METHOD  asking (follow-up questions) + inferring (from description)
  OUT     dimensional_findings                            // per-dimension: relevant?, position, evidence
          follow_up_questions[]                           // surfaced to user during process

STEP 3  synthesize_and_assess()
  IN      dimensional_findings
  READ    assets/practitioner-worksheet.md                // synthesis + BCW ranking template
  OUT     filled_worksheet {
            per_lens_synthesis[]        // tables: sub-lens, dims, pattern guidance conclusions, BCTs
            cross_lens_interactions     // tensions, reinforcements, prerequisites, leverage
            bcw_ranking[]               // top 5 functions with rationale + top 3 BCTs each
            diagnostic_narrative        // coherent picture connecting the dots
          }

STEP 4  convert_to_recommendations()                     // under the hood
  IN      filled_worksheet
  READ    com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md
          com-b-bcw-bct/bct-taxonomy.md
  NOTE    BCW ranking from the worksheet drives function prioritization; refine with taxonomy
  OUT     bcw_functions_prioritized[]   // ordered by leverage, informed by dimensional positions
          bcts_by_function{}            // e.g. ER→BCT.12.1,BCT.12.5 | EN→BCT.1.1,BCT.2.2

STEP 5  frame_recommendations()
  IN      all prior OUTs
  OUT     phase_a {                     // always delivered first
            summary                     // plain-language "what's going on and what to do"
            key_insights[3..5]          // highest-leverage findings
          }
          phase_b_choice {              // user chooses one or both
            in_depth_report             // full diagnostic with dimensional assessments, BCW/BCT reasoning
            action_plan                 // phased rollout: week-by-week, owners, success signals
          }
```

---

## Output delivery

Step 5 delivers in two phases:

| Phase | What | When |
|-------|------|------|
| **A** | Summary + key insights (plain language, no taxonomy codes) | Always delivered first |
| **B — report** | Full diagnostic: dimensional assessments, cross-lens tensions, BCW/BCT reasoning | On request |
| **B — plan** | Phased action plan: concrete changes, owners, success signals, tool/AI recommendations | On request |

The user can ask for both Phase B outputs, but the default is to deliver Phase A and let them pull.

---

## The practitioner worksheet

The practitioner worksheet ([`assets/practitioner-worksheet.md`](../assets/practitioner-worksheet.md)) is the agent's internal working document for synthesis and intervention design. It is used in Steps 3–4 after the lens analysis is complete:

1. **Per-lens synthesis** (Step 3): for each active COM-B branch, the agent records key dimensional findings, Pattern guidance conclusions, and relevant BCTs in a structured table
2. **Cross-lens interactions** (Step 3): tensions, reinforcements, prerequisites, and highest-leverage points across lenses
3. **BCW function ranking** (Steps 3–4): top 5 functions ranked by likelihood of closing the gap, with rationale and top 3 BCTs each

The worksheet is internal by default. It can be surfaced in the Phase B in-depth report if the user asks.

---

## Source files (paths)

| Need | File |
|------|------|
| Behavior definition fields + coaching prompts | [`assets/behavior-canvas.md`](../assets/behavior-canvas.md) |
| Practitioner worksheet: synthesis + BCW ranking template | [`assets/practitioner-worksheet.md`](../assets/practitioner-worksheet.md) |
| C-lens: PC, PHC dimensions | [`lenses/capability-lenses.md`](lenses/capability-lenses.md) |
| M-lens: RM, AM dimensions | [`lenses/motivation-lenses.md`](lenses/motivation-lenses.md) |
| O-lens: PO dimensions | [`lenses/physical-opportunity-lenses.md`](lenses/physical-opportunity-lenses.md) |
| O-lens: SO dimensions | [`lenses/social-opportunity-lenses.md`](lenses/social-opportunity-lenses.md) |
| COM-B → BCW → BCT groupings | [`com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md`](com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md) |
| Full BCT taxonomy | [`com-b-bcw-bct/bct-taxonomy.md`](com-b-bcw-bct/bct-taxonomy.md) |
| COM-B abbreviations | [`com-b-bcw-bct/com-b-abbreviations-reference.md`](com-b-bcw-bct/com-b-abbreviations-reference.md) |
| Repo overview | [`README.md`](../README.md) |

---

## LLM / author notes

- Run steps **in order**; later steps depend on earlier outputs.
- Step 1 is not optional. A vague behavior definition produces a vague diagnosis. Coach the user until the definition is precise.
- Step 2 uses three diagnostic lenses (C, O, M) applied to dimensions in the lens files directly.
- The practitioner worksheet is the agent's working document for Steps 3–4. Use it to synthesize findings, rank BCW functions, and design interventions.
- Step 4 happens under the hood. The user does not need to see BCW/BCT taxonomy unless they request the in-depth report.
- Deliver Phase A first. Wait for the user to choose before producing Phase B content.
