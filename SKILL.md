# COM-B Diagnostic Skill

## Purpose

Run a structured behavioral diagnosis using COM-B, the Behavior Change Wheel, and BCT Taxonomy v1. Given a description of a stuck or problematic behavior, produce a traceable chain: behavior state → COM-B blockers → dimensional lens analysis → intervention functions → named techniques → tool/design levers → phased rollout.

## When to activate

The user describes a behavior that is stuck, inconsistent, failing to adopt, regressing, or contested — in any domain (product, team, organizational, individual). Activation phrases include:

- "Why aren't people doing X?"
- "How do we get people to start/stop/change X?"
- "Diagnose this behavior"
- "Run a COM-B analysis"
- "What's blocking adoption of X?"

## Intake

Ask the user for (or extract from context):

1. **Target behavior** — what should people be doing, specifically?
2. **Current reality** — what are people actually doing instead?
3. **Context** — who are the actors, what's the environment, what changed recently?
4. **Scope** — single behavior or multi-actor system?

See [`assets/intake-template.md`](assets/intake-template.md) for a structured intake form.

## Pipeline

Follow [`references/flow.md`](references/flow.md) steps 1–7 in order. The full walkthrough with file pointers is in [`references/guide.md`](references/guide.md).

### Step 1 — Classify the behavior state

Read [`references/com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md`](references/com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md). Match to one of seven states (S1–S7). Name the state and say which signals matched. These are a **cycle**, not a ladder — behaviors regress.

### Step 2 — Identify COM-B blockers

Read [`references/com-b-bcw-bct/com-b-behavior-states-primary-secondary-blockers.md`](references/com-b-bcw-bct/com-b-behavior-states-primary-secondary-blockers.md). Decode codes via [`references/com-b-bcw-bct/com-b-abbreviations-reference.md`](references/com-b-bcw-bct/com-b-abbreviations-reference.md). Output primary and secondary COM-B codes.

### Step 3 — Deepen with lenses

**Do not skip this step.** It is where the framework adds the most value over intuition.

For each COM-B code, open the matching lens file:

- `PC`, `PHC` → [`references/lenses/capability-lenses.md`](references/lenses/capability-lenses.md)
- `RM`, `AM` → [`references/lenses/motivation-lenses.md`](references/lenses/motivation-lenses.md)
- `PO` → [`references/lenses/physical-opportunity-lenses.md`](references/lenses/physical-opportunity-lenses.md)
- `SO` → [`references/lenses/social-opportunity-lenses.md`](references/lenses/social-opportunity-lenses.md)

Output dimensional IDs and short tags (e.g. "PC 1.2.3 — mental-model gap in cue interpretation").

### Step 4 — Map to BCW intervention functions

Read [`references/com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md`](references/com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md). The lens-specified blockers drive the function ordering — a PC blocker rooted in mental-model gaps calls for different functions than one rooted in procedural fluency.

### Step 5 — Select BCTs

Read [`references/com-b-bcw-bct/bct-taxonomy.md`](references/com-b-bcw-bct/bct-taxonomy.md). Name specific techniques per function. The taxonomy acts as a checklist against narrow interventions.

### Step 6 — Choose tool levers

Read per-state levers in [`references/com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md`](references/com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md) and product patterns in [`references/com-b-bcw-bct/com-b-tool-influence-mechanisms-and-levers.md`](references/com-b-bcw-bct/com-b-tool-influence-mechanisms-and-levers.md). Each lever is annotated with COM-B target and BCW mechanism.

### Step 7 — Design the intervention

Combine into a phased rollout with ownership and success signals.

## Output format

See [`assets/output-template.md`](assets/output-template.md) for the structured output format. At minimum, every diagnosis should produce:

1. **State classification** — state ID, name, matched signals
2. **COM-B blockers** — primary and secondary codes with rationale
3. **Lens analysis** — dimensional IDs with short descriptions
4. **Intervention functions** — ordered by lens-driven priority
5. **BCTs** — named techniques keyed by function
6. **Tool levers** — concrete changes keyed by COM-B branch
7. **Phased rollout** — timeboxed phases with ownership and signals

## Guardrails

1. **Follow the pipeline order.** Later steps depend on earlier outputs. Do not jump to interventions without diagnosing blockers first.
2. **Do not skip lens deepening (Step 3).** Generic COM-B codes produce generic interventions.
3. **Do not assume higher states are better.** "Fully Realized & Stable" can mask brittleness and hidden cost.
4. **Reason about transitions.** The cycle is not a maturity ladder. Behaviors regress when incentives, norms, or operating conditions shift. Different teams can be at different states for the same behavior.
5. **Multi-actor situations:** do not stop at per-role blockers—trace handoffs and where one actor's output becomes another's input; failures often concentrate at interfaces.
6. **Trace everything.** Every intervention function should trace back to a COM-B code, every COM-B code to a lens dimension, every lens dimension to observed signals. If the chain breaks, the diagnosis is incomplete.
7. **Name your sources.** When citing BCTs, use taxonomy numbers. When citing lens dimensions, use the stable IDs.
