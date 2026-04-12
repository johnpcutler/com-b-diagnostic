# Behavior Diagnosis Framework

A seven-step diagnostic pipeline for understanding why a behavior is stuck and choosing interventions that match the specific blockers—not generic best practices.

Built on the **COM-B model** (Michie, van Stralen & West), the **Behavior Change Wheel** (Michie, Atkins & West), and the **BCT Taxonomy v1** (Michie, Richardson, Johnston et al.). The diagnostic lenses draw from Deci & Ryan, Bandura, Klein, Kahneman & Tversky, Endsley, Norman, Cialdini, Edmondson, Beer, Vygotsky, and others across behavioral science, human factors, and organizational theory. The behavior states, blocker profiles, dimensional lens IDs, and product-level levers are original extensions. Full credits and sources in [`credits.md`](credits.md).

---

## The pipeline

Every diagnosis follows the same ordered steps. Later steps depend on earlier outputs. The canonical pseudocode and field spec live in [`flow.md`](flow.md); worked examples in [`scenarios/`](scenarios/).

### Step 1 — Classify the behavior state

**Input:** a description of what people actually do or fail to do, in context.

Read [`com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md`](com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md). Match the situation to one of **seven states** (Fully Realized & Stable → Realized but Friction-Filled → Partially Realized / Inconsistent → Weakly Realized → Aspirational Only → Actively Suppressed → Contested / Undefined). These are a **cycle**, not a ladder—behaviors regress when incentives, norms, or operating conditions shift.

**Output:** state id (S1–S7) and a rationale grounded in the state signals and characteristics.

### Step 2 — Identify COM-B blockers

Read [`com-b-bcw-bct/com-b-behavior-states-primary-secondary-blockers.md`](com-b-bcw-bct/com-b-behavior-states-primary-secondary-blockers.md) for a fast lookup of primary and secondary blockers per state. Decode codes with [`com-b-bcw-bct/com-b-abbreviations-reference.md`](com-b-bcw-bct/com-b-abbreviations-reference.md):

| Code | Branch | Covers |
|------|--------|--------|
| **PC** | Psychological Capability | Mental models, skills, shared definition |
| **PHC** | Physical Capability | Physical skill, stamina, coordination |
| **PO** | Physical Opportunity | Time, tools, systems, workflows |
| **SO** | Social Opportunity | Norms, politics, incentives, culture |
| **RM** | Reflective Motivation | Intentions, beliefs, identity, political risk |
| **AM** | Automatic Motivation | Habits, fear, autopilot, learned helplessness |

**Output:** primary and secondary COM-B codes for this situation.

### Step 3 — Deepen with lenses

This is the highest-leverage step. A COM-B code like "PC" is too broad to act on; the lens files turn it into a precise diagnosis.

| Lens file | COM-B branch | What it unpacks |
|-----------|-------------|-----------------|
| [`lenses/capability-lenses.md`](lenses/capability-lenses.md) | `PC`, `PHC` | Mental models, procedural skill, judgment under uncertainty, distributed cognition, learning transfer |
| [`lenses/motivation-lenses.md`](lenses/motivation-lenses.md) | `RM`, `AM` | Self-determination, identity, habit loops, self-efficacy, temporal discounting, emotion regulation |
| [`lenses/physical-opportunity-lenses.md`](lenses/physical-opportunity-lenses.md) | `PO` | Work-system fit, tool-task match, feedback latency, resource constraints, workflow friction |
| [`lenses/social-opportunity-lenses.md`](lenses/social-opportunity-lenses.md) | `SO` | Norms, power dynamics, institutional legitimacy, coordination cost, psychological safety |

Each lens file contains multiple sub-lenses drawn from established research traditions (SDT, NDM, CTA, SEIPS, social-norms theory, etc.) and breaks each COM-B branch into **numbered dimensions** with stable IDs for shorthand and cross-referencing.

**ID scheme:** PO and SO use **section.dimension** (e.g. PO 2.1, SO 4.5). PC, PHC, RM, AM use **sub-lens.dimension** (e.g. PC 1.2.3, RM 1.3.8).

**Output:** dimensional IDs and short tags for the specific forces in play (e.g. "PC 1.2.3 — mental-model gap in cue interpretation" rather than just "PC").

### Step 4 — Map to BCW intervention functions

Read [`com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md`](com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md). Three tables bridge COM-B blockers to intervention categories:

1. Which of the nine BCW functions (Education, Training, Persuasion, Incentivisation, Coercion, Restriction, Environmental Restructuring, Modelling, Enablement) apply to each COM-B code.
2. Abbreviation definitions (ED, TR, PE, INC, COE, RE, ER, MO, EN).
3. Which BCT groupings typically implement each function (links into Step 5).

**Output:** ordered list of intervention functions for this case, with the lens-specified blockers driving the priority.

### Step 5 — Select BCTs

Read [`com-b-bcw-bct/bct-taxonomy.md`](com-b-bcw-bct/bct-taxonomy.md). The full **Behaviour Change Technique Taxonomy v1** — 93 techniques in 16 groupings. Pick named techniques that implement the functions from Step 4.

**Output:** techniques keyed by function (e.g. ER → 12.1, 12.5 | EN → 1.1, 2.2).

### Step 6 — Choose tool levers

Read the per-state tool levers in [`com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md`](com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md) and the product-design patterns in [`com-b-bcw-bct/com-b-tool-influence-mechanisms-and-levers.md`](com-b-bcw-bct/com-b-tool-influence-mechanisms-and-levers.md). Each lever is annotated with its COM-B target and BCW mechanism so choices stay traceable back to diagnosis.

**Output:** concrete tool or design changes keyed by COM-B branch.

### Step 7 — Design the intervention

Combine all prior outputs into a **phased rollout**: what changes when, who owns it, which BCW functions and BCTs are active in each phase, and what signals tell you to advance or adjust.

**Output:** timeboxed phases tying functions + techniques + levers to sequence and ownership.

### Optional — Profile actors

When the behavior spans **multiple roles or handoffs**, run [`personas_jobs.md`](personas_jobs.md) in parallel with or after Steps 1–2. For each actor, map target behaviors, COM-B breakdown, and failure modes. Then look at the **interfaces** — where one actor's output becomes another's input — because system-level failures concentrate at handoffs, not within single roles.

Patterns to check after profiling actors:
- **Last mile:** upstream performance is strong but downstream decisions still fail.
- **Motivation override:** automatic motivation (habit, bias, social proof) overrides reflective intent.
- **Permissive environment:** cues implicitly allow the wrong behavior.
- **Misaligned optimization:** actors optimize for different objectives; no one owns end-to-end alignment.

---

## Repo structure

```
com-b-bcw-bct/
    com-b-abbreviations-reference.md          # Step 2: COM-B code glossary (PC, PHC, PO, SO, RM, AM)
    com-b-behavior-states-primary-secondary-blockers.md  # Step 2: blocker cheat sheet per state
    behavior-jtbd-maturity-diagnostic-cycle.md # Steps 1 & 6: seven-state cycle + per-state tool levers
    com-b-to-bcw-intervention-function-mapping.md  # Step 4: COM-B → BCW functions → BCT groupings
    bct-taxonomy.md                            # Step 5: full BCT Taxonomy v1 (93 techniques / 16 groupings)
    com-b-tool-influence-mechanisms-and-levers.md  # Step 6: product/tool design patterns per COM-B element

lenses/
    capability-lenses.md                       # Step 3: PC, PHC dimensional depth
    motivation-lenses.md                       # Step 3: RM, AM dimensional depth
    physical-opportunity-lenses.md             # Step 3: PO dimensional depth
    social-opportunity-lenses.md               # Step 3: SO dimensional depth

scenarios/
    scenario-code-review.md                    # Worked example: S2 Realized but Friction-Filled
    scenario-writing-tests.md                  # Worked example: S4 Weakly Realized
    scenario-continuous-discovery.md           # Worked example: S5 Aspirational Only
    scenario-definition-of-ready.md            # Worked example: S7 Contested / Undefined

flow.md                                        # Canonical pipeline pseudocode + digest field spec
personas_jobs.md                               # Optional: multi-actor COM-B profiles (template + avalanche-safety example)
credits.md                                     # Full credits and source lineages
```

---

## How the files connect

```
com-b-bcw-bct/com-b-abbreviations-reference.md
    Defines: PC, PHC, PO, SO, RM, AM
    Referenced by: every other file

com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md
    Uses: COM-B codes, BCW codes
    Applies: tool mechanisms from tool influence file
    Expands: blocker matrix into full per-state diagnosis + intervention

com-b-bcw-bct/com-b-behavior-states-primary-secondary-blockers.md
    Quick-reference version of the diagnostic cycle's blocker sections

com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md
    Bridges: COM-B codes → BCW functions → BCT groupings
    Links to: com-b-bcw-bct/bct-taxonomy.md (table 3)

com-b-bcw-bct/bct-taxonomy.md
    Full BCT Taxonomy v1 (93 techniques / 16 groupings)
    Linked from: intervention mapping table 3

com-b-bcw-bct/com-b-tool-influence-mechanisms-and-levers.md
    Translates: COM-B → product/tool design patterns

lenses/*.md
    Deepen each COM-B branch into numbered dimensions
    Use after: blocker identification; before: intervention design
    Point to: intervention mapping for BCW layer

flow.md
    Canonical pipeline + digest field spec; scenarios implement steps 1–7

scenarios/*.md
    End-to-end examples: state → COM-B → lenses → BCW → BCT → tools → phases

personas_jobs.md
    Multi-actor COM-B profiles; template + worked example (avalanche safety)
    Complements the diagnostic cycle (cycle diagnoses behavior states;
    personas diagnose actor-level breakdowns and interface failures)

credits.md
    Full credits and source lineages for core models and all lens traditions
```

---

## How an LLM should use this framework

Follow [`flow.md`](flow.md) steps 1–7 in order. Specific guidance:

1. **Classify the behavior state** (Step 1). Match the description to one of seven states using signals and characteristics in the diagnostic cycle. Name the state and say which signals matched.

2. **Identify blockers** (Step 2). Use the blocker matrix or the per-state section. Decode abbreviations. Output primary and secondary COM-B codes.

3. **Deepen with lenses** (Step 3). For each COM-B code in play, open the matching lens file and identify which numbered dimensions apply. This step turns a generic code into a precise, actionable diagnosis. Do not skip it — it is where the framework adds the most value over intuition.

4. **Map to BCW functions** (Step 4). Use the intervention mapping tables. The lens-specified blockers should drive the function ordering — a PC blocker rooted in mental-model gaps (PC 1.2.x) calls for different functions than one rooted in procedural fluency (PC 1.5.x).

5. **Select BCTs** (Step 5). Use the taxonomy to name specific techniques per function. The taxonomy acts as a checklist against narrow interventions.

6. **Choose tool levers** (Step 6). Use the per-state levers in the diagnostic cycle and the product/tool file. Each lever is annotated with COM-B target and BCW mechanism.

7. **Design the intervention** (Step 7). Combine into phased rollout with ownership and success signals.

8. **Profile actors if multi-actor** (optional). Use `personas_jobs.md`. Profile each actor, then diagnose interface failures — last-mile gaps, motivation overrides, permissive environments, misaligned optimization.

9. **Reason about transitions.** The cycle is not a maturity ladder. Behaviors regress (a Fully Realized behavior becomes Actively Suppressed after a reorg). Different teams can be at different states for the same behavior.

10. **Avoid common mistakes.**
    - Do not skip lens deepening (Step 3). Generic COM-B codes produce generic interventions.
    - Do not assume higher states are better. "Fully Realized & Stable" can mask brittleness and hidden cost.
    - Do not profile personas in isolation. The value is in revealing misalignment between actors, not just within them.

