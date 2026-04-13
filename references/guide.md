# Framework Guide

A detailed walkthrough of the five-step diagnostic pipeline and how the reference files connect.

Built on the **COM-B model** (Michie, van Stralen & West), the **Behavior Change Wheel** (Michie, Atkins & West), and the **BCT Taxonomy v1** (Michie, Richardson, Johnston et al.). The diagnostic lenses draw from Deci & Ryan, Bandura, Klein, Kahneman & Tversky, Endsley, Norman, Cialdini, Edmondson, Beer, Vygotsky, and others across behavioral science, human factors, and organizational theory. The dimensional lens IDs and product-level levers are original extensions. Full credits and sources in [`credits.md`](../credits.md).

---

## The pipeline

Every diagnosis follows the same ordered steps. Later steps depend on earlier outputs. The canonical pseudocode and field spec live in [`flow.md`](flow.md).

```
Step 1  DEFINE BEHAVIOR              (user-facing, interactive)
Step 2  RESEARCH C, O, M             (user-facing, interactive, dimension-level)
Step 3  SYNTHESIZE and ASSESS         (cross-lens topology)
Step 4  CONVERT TO BCW/BCT RECS      (under the hood)
Step 5  FRAME RECOMMENDATIONS         (user-facing, phased delivery)
```

### Step 1 — Define the behavior

**Input:** a user description, artifacts (one-pager, goal doc, data), or a coaching conversation.

This step establishes a structured, precise behavior definition that all later steps operate on. Without it, everything downstream reasons about a fuzzy target.

**Two entry paths:**
- The user provides artifacts — the agent extracts and structures
- The agent coaches the user through describing the behavior until it's clear

**Structured output format:** see [`assets/behavior-canvas.md`](../assets/behavior-canvas.md) for fields, coaching prompts, and an example. The canvas also includes optional pattern vocabulary for describing the behavior's current state.

The canvas includes a "Prior attempts" field. Actively ask what has been tried before and why it didn't work -- this is some of the most diagnostic information available. Failed attempts often reveal which COM-B branches are not the real bottleneck.

**Output:** a canonical behavior definition that Steps 2–5 reference.

### Step 2 — Research capability, opportunity, and motivation

This is the core analytical step.

Then three diagnostic lenses are applied. For each, the agent forms a perspective on specific dimensional scales through a mix of inference from the description and follow-up questions.

**Three diagnostic lenses:**

| Lens | What it examines | Source file |
|------|-----------------|-------------|
| **Capability** (C-lens) | What people must know, perceive, judge, and physically do — PC and PHC | [`lenses/capability-lenses.md`](lenses/capability-lenses.md) |
| **Opportunity** (O-lens) | Material/temporal conditions (PO) and social/political conditions (SO) | [`lenses/physical-opportunity-lenses.md`](lenses/physical-opportunity-lenses.md), [`lenses/social-opportunity-lenses.md`](lenses/social-opportunity-lenses.md) |
| **Motivation** (M-lens) | Reflective endorsement, identity, intentions (RM) and habits, affect, reinforcement (AM) | [`lenses/motivation-lenses.md`](lenses/motivation-lenses.md) |

**Working with the lens files:**

The agent reads the lens files directly during this step. For each relevant sub-lens, the agent notes which dimensions are active, their positions on the scale, and the evidence that supports each position. Most situations will only activate a subset of dimensions — skip those that don't apply.

**Methods:** Asking (follow-up questions to probe ambiguous dimensions) and Inferring (from the behavior description and any provided artifacts). The lens dimensions often surface distinctions the user hasn't considered — e.g. whether a capability gap is about mental models or procedural fluency, whether motivation is about identity or habit, whether opportunity constraints are about tooling or norms.

**ID scheme:** PO and SO use **PO.n.m** / **SO.n.m** (e.g. PO.2.1, SO.4.5). PC, PHC, RM, AM use dotted prefixes **PC.1.x.y**, **PHC.2.x.y**, **RM.1.x.y**, **AM.2.x.y**. See [lenses/lens-map.md](lenses/lens-map.md).

**Output:** dimensional findings from the lens analysis (internal), plus any follow-up questions surfaced to the user.

### Step 3 — Synthesize and assess the situation

The output of this step is a filled-out [`assets/practitioner-worksheet.md`](../assets/practitioner-worksheet.md). The agent works through it section by section:

1. **COM-B priority ranking** — rank C, O, M by contribution to the gap
2. **Per-lens synthesis** — for each active branch, fill the table and write a narrative synthesis that surfaces what to try and what not to try
3. **Cross-lens interactions** — tensions, reinforcements, prerequisites, highest leverage
4. **BCW function ranking** — top 5 functions with rationale and top 3 BCTs each
5. **Intervention implications** — connect BCTs to concrete actions

The filled worksheet is both the agent's internal reasoning artifact and a deliverable the user can request ("working analysis").

**Output:** the filled practitioner worksheet — a situational assessment naming the key forces, their interactions, and where intervention would have the most leverage.

### Step 4 — Convert assessment to BCW and BCT recommendations

This step runs under the hood. The agent converts the dimensional assessment into formal intervention recommendations using the COM-B → BCW → BCT chain. The user doesn't need to see this unless they request the in-depth report.

**How dimensions guide conversion:**

The practitioner worksheet's BCW function ranking (Section 3) drives this step. The agent uses the dimensional findings and Pattern guidance conclusions from the per-lens synthesis to rank BCW functions by likelihood of closing the gap, then selects specific BCTs for each. The ranking refines within the set of functions the base COM-B → BCW mapping provides — it prioritizes, not replaces.

**Source files:**

| File | Role |
|------|------|
| [`com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md`](com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md) | Base mapping: COM-B code → BCW functions → BCT groupings |
| [`com-b-bcw-bct/bct-taxonomy.md`](com-b-bcw-bct/bct-taxonomy.md) | Full BCT Taxonomy v1 — 93 techniques in 16 groupings |

**Output:** prioritized BCW functions and named BCT techniques keyed by function.

### Step 5 — Frame recommendations

Delivers recommendations progressively in two phases.

**Phase A — always delivered first:**
- **Summary:** Plain-language "here's what's going on and what to do." No taxonomy codes. Answers the question a trusted advisor would answer.
- **Key insights:** The 3–5 most important findings — tensions, surprises, or highest-leverage points the diagnosis surfaced.

**Feedback loop:**

After delivering Phase A, pause and ask for the user's reaction. Prompt specifically for:
- Whether the diagnosis resonates with what they're seeing
- Whether they've already tried any of the implied approaches (and what happened)
- Missing context -- political dynamics, past failures, constraints

If the user provides substantive new information, update the behavior canvas (especially Prior attempts and any refined fields) and re-run from Step 2. The re-run produces a fresh worksheet; do not patch the old one. If the diagnosis lands, proceed to the Phase B offer.

**Phase B — user chooses one or more:**

After the feedback loop, the agent offers three paths:

- **In-depth report:** Full diagnostic with dimensional assessments per lens, cross-lens tensions, BCW/BCT reasoning made visible. For understanding the "why" deeply or sharing with stakeholders.
- **Action plan:** Concrete, phased plan — week-by-week or phase-by-phase — with specific changes, owners, success signals. Includes tool/AI recommendations and mapping to relevant frameworks. For acting now.
- **Working analysis:** The practitioner worksheet showing how the agent got from lens findings to ranked interventions. For inspecting the reasoning chain or reusing the analysis.

**Output structure for each:** see [`assets/output-template.md`](../assets/output-template.md).

---

## How the files connect

```
assets/practitioner-worksheet.md
    Synthesis scaffold (Step 3), BCW ranking (Step 4), intervention design
    Per-lens synthesis, cross-lens interactions, BCW function ranking with BCTs

com-b-bcw-bct/com-b-abbreviations-reference.md
    Defines: PC, PHC, PO, SO, RM, AM
    Referenced by: every other file

com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md
    Bridges: COM-B codes → BCW functions → BCT groupings
    Used in Step 4

com-b-bcw-bct/bct-taxonomy.md
    Full BCT Taxonomy v1 (93 techniques / 16 groupings)
    Used in Step 4

lenses/capability-lenses.md
    Source of truth for PC and PHC dimension definitions and academic grounding

lenses/motivation-lenses.md
    Source of truth for RM and AM dimension definitions and academic grounding

lenses/physical-opportunity-lenses.md
    Source of truth for PO dimension definitions and academic grounding

lenses/social-opportunity-lenses.md
    Source of truth for SO dimension definitions and academic grounding

flow.md
    Canonical pipeline pseudocode + delivery spec
```
