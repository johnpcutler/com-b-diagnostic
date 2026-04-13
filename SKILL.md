# COM-B Diagnostic Skill

## Purpose

Run a structured behavioral diagnosis using COM-B, the Behavior Change Wheel, and BCT Taxonomy v1. Given a description of a stuck or problematic behavior, produce a traceable chain: structured behavior definition → dimensional lens analysis across B, C, O, M → cross-lens assessment → intervention functions → named techniques → actionable recommendations.

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

Before any analysis, establish a precise behavior definition. Extract from the user's description and artifacts, or coach them through it with follow-up questions.

**Structured output:**
- **Behavior:** summary statement
- **Who:** actors
- **Will do what:** specific action
- **To what extent:** frequency, depth, observable standard
- **In what context:** environment, tools, constraints
- **For what outcome:** intended result

If the user provides enough detail to fill this out, do so and confirm. If critical fields are missing (especially "will do what" and "to what extent"), ask before proceeding. A vague behavior definition produces a vague diagnosis.

### Step 2 — Research behavior, capability, opportunity, and motivation

Read [`assets/assessment-form-template.md`](assets/assessment-form-template.md). This is your primary working document for the diagnosis. It lists every dimension from every lens file, with intervention bias annotations baked in.

Apply four peer lenses to the defined behavior:

- **Behavior state** (B-lens): read [`references/lenses/behavior-lenses.md`](references/lenses/behavior-lenses.md). Match to one of seven states (**S.1**–**S.7**). These are a **cycle**, not a ladder — behaviors regress.
- **Capability** (C-lens): PC, PHC dimensions from the form; deep definitions in [`references/lenses/capability-lenses.md`](references/lenses/capability-lenses.md) if needed.
- **Opportunity** (O-lens): PO, SO dimensions from the form; deep definitions in [`references/lenses/physical-opportunity-lenses.md`](references/lenses/physical-opportunity-lenses.md) and [`references/lenses/social-opportunity-lenses.md`](references/lenses/social-opportunity-lenses.md) if needed.
- **Motivation** (M-lens): RM, AM dimensions from the form; deep definitions in [`references/lenses/motivation-lenses.md`](references/lenses/motivation-lenses.md) if needed.

For each relevant dimension on the form, note: relevance, position on the scale, and evidence. Skip dimensions that don't apply — most situations activate a subset.

**This is a good place to ask follow-up questions.** The lens dimensions often surface distinctions the user hasn't considered — e.g. whether a capability gap is about mental models or procedural fluency, whether motivation is about identity or habit, whether opportunity constraints are about tooling or norms. If the initial description doesn't give enough signal to choose between competing dimensions, ask.

### Step 3 — Synthesize and assess

Read back the filled-out assessment form. Build a cross-lens assessment:

- Where do lenses **tension** against each other? (e.g. capability is present but motivation doesn't support it)
- Where do lenses **reinforce** each other? (e.g. both opportunity and motivation point to the same bottleneck)
- Which dimensional findings are **highest-leverage** for this specific situation?

Produce a coherent diagnostic picture that connects the dots across all four lenses.

### Step 4 — Convert to BCW and BCT recommendations

This step runs **under the hood**. The user does not need to see the taxonomy chain unless they request the in-depth report.

Use the filled-out form's intervention bias annotations to prioritize BCW functions. Read [`references/com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md`](references/com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md) for the base mapping and [`references/com-b-bcw-bct/bct-taxonomy.md`](references/com-b-bcw-bct/bct-taxonomy.md) for named techniques.

### Step 5 — Frame recommendations (phased delivery)

Deliver in two phases:

**Phase A — always deliver first:**
- **Summary:** Plain-language "here's what's going on and what to do." No taxonomy codes. Write as a trusted advisor would speak.
- **Key insights:** 3–5 most important findings — tensions, surprises, or highest-leverage points.

After delivering Phase A, offer the user two paths:

**Phase B — user chooses one or both:**
- **In-depth report:** Full diagnostic with dimensional assessments, cross-lens tensions, BCW/BCT reasoning visible. Can include the assessment form.
- **Action plan:** Concrete phased plan — week-by-week — with specific changes, owners, success signals, tool/AI recommendations.

Follow the output skeleton in [`assets/output-template.md`](assets/output-template.md) for structure.

## Guardrails

1. **Start with behavior definition (Step 1).** Do not skip to analysis without a structured definition. Coach the user if needed.
2. **Follow the pipeline order.** Later steps depend on earlier outputs. Do not jump to interventions without researching through lenses first.
3. **Use the assessment form.** Read [`assets/assessment-form-template.md`](assets/assessment-form-template.md) as your primary working document. It contains all dimensions and intervention bias annotations in one place.
4. **Treat all four lenses as peers.** The behavior-state lens is not a gateway or prerequisite. It is one diagnostic frame among four.
5. **Do not assume higher states are better.** "Fully Realized & Stable" can mask brittleness and hidden cost.
6. **Reason about transitions.** The cycle is not a maturity ladder. Behaviors regress when incentives, norms, or operating conditions shift. Different teams can be at different states for the same behavior.
7. **Multi-actor situations:** do not stop at per-role analysis — trace handoffs and where one actor's output becomes another's input; failures often concentrate at interfaces.
8. **Deliver Phase A first.** Do not produce the full report or action plan until the user asks. Let them pull.
9. **Trace everything.** In the in-depth report, every intervention function should trace back to a dimensional position, every dimensional position to observed signals. If the chain breaks, the diagnosis is incomplete.
10. **Name your sources.** When citing BCTs, use **`BCT.n.m`** IDs (see [`references/lenses/dimensional-ids.md`](references/lenses/dimensional-ids.md)). When citing lens dimensions, use the stable `PC` / `PHC` / `RM` / `AM` / `PO` / `SO` / `S` IDs.
