# Diagnostic flow (canonical)

Single source of truth for the **ordered pipeline** recommended for any COM-B diagnosis in this repo. The full walkthrough with file pointers is in [`guide.md`](guide.md).

---

## Pipeline (pseudocode)

Treat each step as a function: named inputs, named outputs, explicit file dependencies.

```text
STEP 1  define_behavior()
  IN      user description, artifacts, or follow-up answers
  OUT     behavior_definition {
            behavior    // summary statement
            who         // actors
            will_do     // specific action
            to_extent   // frequency, depth, observable standard
            in_context  // environment, tools, constraints
            for_outcome // intended result
          }

STEP 2  research_com()
  READ    assets/assessment-form-template.md              // situational orientation + all dimensions + intervention bias annotations
          lenses/capability-lenses.md                     // C-lens: PC, PHC
          lenses/motivation-lenses.md                     // M-lens: RM, AM
          lenses/physical-opportunity-lenses.md            // O-lens: PO
          lenses/social-opportunity-lenses.md              // O-lens: SO
  METHOD  asking (follow-up questions) + inferring (from description)
  OUT     filled_assessment_form                          // per-dimension: relevant?, position, evidence
          follow_up_questions[]                           // surfaced to user during process

STEP 3  synthesize_and_assess()
  IN      filled_assessment_form
  OUT     situational_assessment {
            cross_lens_tensions[]       // e.g. capability present but motivation absent
            highest_leverage_points[]   // which dimensions matter most
            diagnostic_narrative        // coherent picture connecting the dots
          }

STEP 4  convert_to_recommendations()                     // under the hood
  IN      situational_assessment, filled_assessment_form
  READ    com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md
          com-b-bcw-bct/bct-taxonomy.md
  NOTE    dimension-level intervention bias annotations on the form guide function prioritization
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

## The assessment form

The dimensional assessment form ([`assets/assessment-form-template.md`](../assets/assessment-form-template.md)) is the agent's internal working document. It serves triple duty:

1. **Research scaffold** (Step 2): situational orientation plus all dimensions with intervention bias annotations; agent fills in relevance, position, evidence
2. **Synthesis input** (Step 3): agent reads back the form to spot cross-lens patterns
3. **Intervention lookup** (Step 4): co-located bias annotations guide BCW function prioritization

The form is internal by default. It can be surfaced in the Phase B in-depth report if the user asks.

---

## Source files (paths)

| Need | File |
|------|------|
| Assessment form scaffold + intervention bias annotations | [`assets/assessment-form-template.md`](../assets/assessment-form-template.md) |
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
- Step 2 uses three diagnostic lenses (C, O, M) preceded by a situational orientation step at the top of the assessment form.
- The assessment form is the agent's primary working document for Steps 2–4. Read it once; fill it out during Step 2; read it back for Steps 3–4.
- Step 4 happens under the hood. The user does not need to see BCW/BCT taxonomy unless they request the in-depth report.
- Deliver Phase A first. Wait for the user to choose before producing Phase B content.
