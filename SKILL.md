# COM-B Diagnostic Skill

## Purpose

Run a structured behavioral diagnosis using COM-B, the Behavior Change Wheel, and BCT Taxonomy v1. Given a description of a stuck or problematic behavior, produce a traceable chain: structured behavior definition → dimensional lens analysis across C, O, M → cross-lens assessment → intervention functions → named techniques → actionable recommendations.

## When to activate

The user describes a behavior that is stuck, inconsistent, failing to adopt, regressing, or contested — in any domain (product, team, organizational, individual). Activation phrases include:

- "Why aren't people doing X?"
- "How do we get people to start/stop/change X?"
- "Diagnose this behavior"
- "Run a COM-B analysis"
- "What's blocking adoption of X?"

## Pipeline

Follow [`references/flow.md`](references/flow.md) steps 1–5 in order. The full walkthrough with file pointers is in [`references/guide.md`](references/guide.md).

### Step 1 — Define the behavior

Before any analysis, establish a precise behavior definition using [`assets/behavior-canvas.md`](assets/behavior-canvas.md). Extract from the user's description and artifacts, or coach them through it with follow-up questions. The canvas lists every field, coaching prompts for ambiguous cases, and optional pattern vocabulary for describing the behavior's current state.

If critical fields are missing (especially "will do what" and "to what extent"), ask before proceeding. A vague behavior definition produces a vague diagnosis.

### Step 2 — Research capability, opportunity, and motivation

Apply three diagnostic lenses by reading the lens files directly:

- **Capability** (C-lens): [`references/lenses/capability-lenses.md`](references/lenses/capability-lenses.md) — PC, PHC dimensions.
- **Opportunity** (O-lens): [`references/lenses/physical-opportunity-lenses.md`](references/lenses/physical-opportunity-lenses.md) and [`references/lenses/social-opportunity-lenses.md`](references/lenses/social-opportunity-lenses.md) — PO, SO dimensions.
- **Motivation** (M-lens): [`references/lenses/motivation-lenses.md`](references/lenses/motivation-lenses.md) — RM, AM dimensions.

For each relevant dimension, note: relevance, position on the scale, and evidence. Skip dimensions that don't apply — most situations activate a subset.

**This is a good place to ask follow-up questions.** The lens dimensions often surface distinctions the user hasn't considered — e.g. whether a capability gap is about mental models or procedural fluency, whether motivation is about identity or habit, whether opportunity constraints are about tooling or norms. If the initial description doesn't give enough signal to choose between competing dimensions, ask.

### Step 3 — Synthesize and assess

Use [`assets/practitioner-worksheet.md`](assets/practitioner-worksheet.md) to synthesize your findings. Build a cross-lens assessment:

- Where do lenses **tension** against each other? (e.g. capability is present but motivation doesn't support it)
- Where do lenses **reinforce** each other? (e.g. both opportunity and motivation point to the same bottleneck)
- Which dimensional findings are **highest-leverage** for this specific situation?

Produce a coherent diagnostic picture that connects the dots across all three lenses.

### Step 4 — Convert to BCW and BCT recommendations

This step runs **under the hood**. The user does not need to see the taxonomy chain unless they request the in-depth report.

Use the BCW function ranking from the practitioner worksheet to prioritize intervention functions. Read [`references/com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md`](references/com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md) for the base mapping and [`references/com-b-bcw-bct/bct-taxonomy.md`](references/com-b-bcw-bct/bct-taxonomy.md) for named techniques.

### Step 5 — Frame recommendations (phased delivery)

Deliver in two phases:

**Phase A — always deliver first:**
- **Summary:** Plain-language "here's what's going on and what to do." No taxonomy codes. Write as a trusted advisor would speak.
- **Key insights:** 3–5 most important findings — tensions, surprises, or highest-leverage points.

After delivering Phase A, offer the user two paths:

**Phase B — user chooses one or both:**
- **In-depth report:** Full diagnostic with dimensional assessments, cross-lens tensions, BCW/BCT reasoning visible. Can include the practitioner worksheet.
- **Action plan:** Concrete phased plan — week-by-week — with specific changes, owners, success signals, tool/AI recommendations.

Follow the output skeleton in [`assets/output-template.md`](assets/output-template.md) for structure.

## Guardrails

1. **Start with behavior definition (Step 1).** Do not skip to analysis without a structured definition. Coach the user if needed.
2. **Follow the pipeline order.** Later steps depend on earlier outputs. Do not jump to interventions without researching through lenses first.
3. **Use the practitioner worksheet.** After lens analysis, use [`assets/practitioner-worksheet.md`](assets/practitioner-worksheet.md) to synthesize findings, rank BCW functions, and design interventions.
4. **The real diagnosis comes from the C, O, and M lenses.** Pattern labels in the behavior canvas are orientation, not findings.
5. **Multi-actor situations:** do not stop at per-role analysis — trace handoffs and where one actor's output becomes another's input; failures often concentrate at interfaces.
6. **Deliver Phase A first.** Do not produce the full report or action plan until the user asks. Let them pull.
7. **Trace everything.** In the in-depth report, every intervention function should trace back to a dimensional position, every dimensional position to observed signals. If the chain breaks, the diagnosis is incomplete.
8. **Name your sources.** When citing BCTs, use **`BCT.n.m`** IDs (see [`references/lenses/lens-map.md`](references/lenses/lens-map.md)). When citing lens dimensions, use the stable `PC` / `PHC` / `RM` / `AM` / `PO` / `SO` IDs.
