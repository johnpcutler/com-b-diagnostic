# Behavior Diagnosis Framework

A behavioral diagnostic framework built on two established models from behavioral science: the **COM-B model** (Capability, Opportunity, Motivation - Behavior) by Susan Michie and colleagues, and the **Behavior Change Wheel (BCW)** intervention taxonomy. The framework extends these models into organizational behavior adoption, tool design, and change strategy.

The repo includes reference files for COM-B vocabulary, BCW intervention logic, BCT taxonomy links, and tool-level mechanisms, plus a diagnostic cycle that walks through seven behavior states with matched blockers and interventions. The **`lenses/`** folder holds four companion notes that deepen each COM-B branch with numbered dimensions; `scenarios/` holds optional end-to-end pressure tests. It also includes `personas_jobs.md` — a worked example (avalanche safety) and reusable template for profiling actors in any multi-actor behavior system.

## How to apply this framework

This framework works at two levels, and the real power comes from using them together.

### Level 1: Diagnose the behavior

Pick any behavior that matters in your domain — a practice, ritual, process, or habit. Use the **diagnostic cycle** (`behavior-jtbd-maturity-diagnostic-cycle.md`) to classify its current state across seven possibilities: from fully ritualized and stable, through friction-filled or inconsistent, down to aspirational, suppressed, or conceptually undefined. Each state comes with a COM-B blocker profile that explains *why* the behavior looks the way it does, and a set of intervention strategies matched to those specific blockers.

This level answers: **"What is happening with this behavior, why is it stuck, and what interventions fit?"**

### Level 2: Map the actors (optional)

Most important behaviors do not live inside a single person. They span a system of actors — different roles, teams, or personas — each with their own capability, opportunity, and motivation profile. Use `personas_jobs.md` as a template for profiling each actor: what they are trying to do, what COM-B forces shape their behavior, and where they are likely to fail. The file includes a reusable persona structure and a worked example (avalanche safety) you can reference.

The critical insight is at the **interfaces**. Individual actors may each perform well within their own scope, but failures concentrate at the handoffs — where one actor's output becomes another's input. A report that is technically accurate but communicated abstractly fails the person who needs actionable guidance. Strong upstream performance means nothing if the downstream decision-maker misreads the environment.

This level answers: **"Who are the actors, what does COM-B look like for each of them, and where do the breakdowns between actors actually happen?"**

### Combining both levels

For a complete diagnosis:

1. **Name the behavior.** What specific practice or decision are you examining?
2. **Classify its state** using the diagnostic cycle. Identify the COM-B blockers.
3. **Profile the actors** involved. Create your own personas using the template in `personas_jobs.md`. For each, map their capability, opportunity, motivation, and failure modes.
4. **Find the misalignments.** Where do actors optimize for different objectives? Where does one actor's failure mode become another's blocker? Where does automatic motivation (habits, biases, social pressure) override what people know they should do?
5. **Select interventions** that target the specific blockers and misalignments you found — not generic best practices.

The reference files (`com-b-abbreviations-reference.md`, `com-b-to-bcw-intervention-function-mapping.md`, `bct-taxonomy.md`, `com-b-tool-influence-mechanisms-and-levers.md`, `com-b-behavior-states-primary-secondary-blockers.md`, the four lens files under `lenses/`, and optionally `scenarios/`) provide the vocabulary, intervention logic, technique detail, lens depth, and tool mechanisms you need at each step.

---

## How to think about these files

The files form a layered system. Start from the foundational reference tables, then use the diagnostic cycle to apply them.

### Layer 1: Vocabulary

**`com-b-abbreviations-reference.md`**

The glossary. Defines the six COM-B codes (PC, PHC, PO, SO, RM, AM) used across every other file. Each code maps to one dimension of Capability, Opportunity, or Motivation, with real-world examples of the barriers it represents.

Read this first if you encounter an abbreviation you do not recognize. Every blocker, strategy, and lever in the framework traces back to one of these six codes.

### Layer 2: Intervention logic

**`com-b-to-bcw-intervention-function-mapping.md`**

The bridge between diagnosis and action. Contains three tables:

1. Which BCW intervention functions (Education, Training, Persuasion, etc.) are effective for which COM-B problem type (per Michie, Atkins & West, 2014).
2. What each BCW intervention abbreviation (ED, TR, PE, INC, COE, RE, ER, MO, EN) means and does.
3. Which BCT groupings typically implement each intervention function, with links into the full taxonomy (`bct-taxonomy.md`).

This file answers: "Given a COM-B blocker, what categories of intervention are likely to work?" It is the theoretical engine behind the tool levers recommended in the diagnostic cycle.

### Layer 2b: Behaviour Change Techniques (BCT) taxonomy

**`bct-taxonomy.md`**

The full **Behaviour Change Technique Taxonomy (v1)** — granular techniques (93 techniques in 16 groupings) that sit *below* BCW intervention functions. Use it when you need to name specific techniques (e.g. for intervention design, research reporting, or matching tactics to functions).

Referenced from table 3 in `com-b-to-bcw-intervention-function-mapping.md`.

### Layer 2c: Lens files (diagnostic depth per COM-B branch)

In **`lenses/`**, four companion notes unpack each branch of COM-B with overlapping sub-lenses and **numbered dimensions** (stable IDs for shorthand and cross-referencing):

| File | COM-B branch |
|------|----------------|
| [`lenses/capability-lenses.md`](lenses/capability-lenses.md) | `PC`, `PHC` |
| [`lenses/motivation-lenses.md`](lenses/motivation-lenses.md) | `RM`, `AM` |
| [`lenses/physical-opportunity-lenses.md`](lenses/physical-opportunity-lenses.md) | `PO` |
| [`lenses/social-opportunity-lenses.md`](lenses/social-opportunity-lenses.md) | `SO` |

**ID scheme:** Physical and social opportunity lenses use **section.dimension** (e.g. PO **2.1**, SO **4.5**). Capability and motivation lenses use **sub-lens.dimension** (e.g. PC **1.2.3**, RM **1.3.8**).

Use these after you know *which* COM-B codes are in play — they turn a code into a precise diagnosis (mental models vs procedural fluency, norms vs incentives, tool-task mismatch vs feedback latency, and so on).

### Layer 3: Tool-specific mechanisms

**`com-b-tool-influence-mechanisms-and-levers.md`**

Translates the abstract COM-B model into concrete product and tool design. For each COM-B element, it specifies:

- What tools can realistically influence
- The mechanisms through which tools produce that influence (e.g., Clarification, Automation, Social Proof)
- Specific examples of tool levers (e.g., guided workflows, default templates, shared dashboards)

This file answers: "If I am building or evaluating a tool, what design patterns address each type of behavioral barrier?"

### Layer 4: Blocker summary matrix

**`com-b-behavior-states-primary-secondary-blockers.md`**

A compact diagnostic lookup table. Maps seven behavior states (from Fully Realized & Stable through Contested / Undefined) to their primary and secondary COM-B blockers. Each blocker is tagged with its COM-B code so you can trace it back to the abbreviations reference and the intervention mapping.

This file answers: "Given the current state of a behavior, what is most likely blocking it?"

### Layer 5: The full diagnostic cycle

**`behavior-jtbd-maturity-diagnostic-cycle.md`**

The main document. Integrates everything above into a single walkthrough of seven behavior states, presented as a cycle (not a linear ladder). For each state it provides:

- A state signal (short phrase describing what the behavior looks like)
- Characteristics (observable symptoms)
- Primary and secondary COM-B blockers (with full `Domain -> Sub-domain -> Specific barrier` paths)
- High-level tool strategy (what a tool or intervention should aim to do)
- Six tool levers (three primary, three secondary), each annotated with its COM-B code and BCW intervention function

This file answers: "For a behavior in state X, what exactly is going wrong, and what should I do about it?"

### Layer 6: Persona profiles (template + worked example)

**`personas_jobs.md`**

A reusable template and worked example for profiling actors in a multi-actor behavior system using COM-B. The file starts with the persona structure to follow for any domain, then includes a complete worked example applying that structure to avalanche safety (eight personas: Forecaster, Field Observer, Ski Patrol, Highway Control, Mountain Guide, Backcountry Recreationist, Search and Rescue, Educator).

Each persona is described with:

- Target behaviors
- Needs and desires
- COM-B breakdown (Capability, Opportunity, Motivation — with specific sub-dimensions)
- Failure modes

The worked example also demonstrates system-level analysis — the patterns to look for after profiling individual actors:

1. **The "last mile" problem:** failures concentrate at downstream decision points even when upstream actors perform well.
2. **Motivation as weakest link:** automatic motivation (habits, biases, social pressure) overrides capability and opportunity.
3. **Permissive environments:** environmental cues implicitly permit the wrong behavior.
4. **Misaligned optimization:** each actor optimizes for a different objective; no single actor owns end-to-end behavioral alignment.

This file is **optional**. Use it when your situation involves multiple actors and you want to understand where behavior breaks down across a system, not just within a single role. You can use the avalanche example as a reference, replace it with your own domain, or build from the template.

### Layer 7: Worked scenarios (optional)

**`scenarios/`**

Four end-to-end **pressure-test** narratives (product/engineering contexts). Each file walks: behavior state → COM-B blockers → lens deepening (all four lens files + dimension IDs) → BCW functions → BCTs → tool levers → phased intervention. Use them as templates for applying the full stack or as a check that your own diagnosis hangs together.

The exact order and the **digest** block convention are specified in **`flow.md`** (canonical pipeline as pseudocode + step table).

---

## How the files reference each other

```
com-b-abbreviations-reference.md
    Defines: PC, PHC, PO, SO, RM, AM
    Referenced by: every other file

com-b-to-bcw-intervention-function-mapping.md
    Defines: ED, TR, PE, INC, COE, RE, ER, MO, EN; COM-B -> functions; functions -> BCT groupings
    Uses: COM-B codes from abbreviations reference
    Links to: bct-taxonomy.md (table 3)
    Referenced by: diagnostic cycle (tool lever annotations); lens files (BCW pointers)

bct-taxonomy.md
    Full BCT Taxonomy v1 (93 techniques / 16 groupings)
    Linked from: com-b-to-bcw-intervention-function-mapping.md
    Read next from: same file; cross-links to lens files and mapping

lenses/capability-lenses.md | lenses/motivation-lenses.md | lenses/physical-opportunity-lenses.md | lenses/social-opportunity-lenses.md
    Deep diagnosis per COM-B branch; numbered dimension IDs
    Use after: blocker identification; before: detailed intervention design
    Point to: com-b-to-bcw-intervention-function-mapping.md for BCW layer

flow.md
    Canonical pipeline (pseudocode) + digest field spec; scenarios implement steps 1–7

scenarios/*.md (optional)
    End-to-end examples: state -> COM-B -> lenses -> BCW -> BCT -> tools -> phases

com-b-tool-influence-mechanisms-and-levers.md
    Uses: COM-B codes from abbreviations reference
    Parallel to: intervention mapping (same COM-B rows, different lens)
    Informs: tool lever examples in diagnostic cycle

com-b-behavior-states-primary-secondary-blockers.md
    Uses: COM-B codes from abbreviations reference
    Summarizes: blocker data from diagnostic cycle
    Quick-reference version of: diagnostic cycle blocker sections

behavior-jtbd-maturity-diagnostic-cycle.md
    Uses: COM-B codes from abbreviations reference
    Uses: BCW codes from intervention mapping
    Applies: tool mechanisms from tool influence file
    Expands: blocker matrix into full per-state diagnosis + intervention

personas_jobs.md (optional — template + worked example)
    Uses: COM-B categories (C, O, M) from abbreviations reference
    Provides: reusable persona structure for any domain
    Includes: worked example (avalanche safety) as reference
    Complements: diagnostic cycle (cycle diagnoses behavior states;
                  personas file diagnoses actor-level breakdowns)
```

## How an LLM should use this framework

1. **Classify the behavior state.** When someone describes a behavior (a practice, ritual, process, habit), match their description to one of the seven states using the characteristics and state signals in the diagnostic cycle.

2. **Identify the blockers.** Use the blocker matrix or the per-state blocker section to name the primary and secondary COM-B forces holding the behavior in place. Decode any abbreviation using the abbreviations reference.

3. **Deepen diagnosis (optional but high value).** For each relevant COM-B code, open the matching lens file under `lenses/` (`capability-lenses.md`, `motivation-lenses.md`, `physical-opportunity-lenses.md`, `social-opportunity-lenses.md`) and use the numbered dimensions to specify *what kind* of PC/PHC/PO/SO/RM/AM problem it is.

4. **Select interventions.** Use the intervention mapping to find which BCW functions apply to the identified (and optionally lens-specified) COM-B blockers. Use table 3 in the same file to jump into `bct-taxonomy.md` when you need named techniques. Use the tool influence file if the question is specifically about product or tool design.

5. **Recommend tool levers.** Use the per-state tool levers in the diagnostic cycle to suggest specific, actionable changes. Each lever is already annotated with its COM-B target and BCW mechanism, so recommendations are traceable.

6. **Reason about transitions.** The cycle is not a maturity ladder. Behaviors can regress (e.g., a Fully Realized behavior becomes Actively Suppressed after a reorg). Use the cycle flow to reason about what state a behavior might move toward, and what blockers would emerge at that next state.

7. **Profile actors in a system (if applicable).** When the situation involves multiple actors (personas, roles, teams), use the persona template in `personas_jobs.md` to profile each one. For each actor, map their target behaviors, COM-B profile (what they can do, what the environment permits, what drives them), and failure modes. Then look at the interfaces between actors — where one actor's output becomes another's input — because system-level failures often occur at these handoffs, not within a single actor. The avalanche safety example in the same file shows this pattern in detail.

8. **Diagnose system-level dynamics (if applicable).** After profiling actors, check for recurring patterns:
   - Is there a "last mile" problem where upstream performance is strong but downstream decisions still fail?
   - Is automatic motivation (habits, biases, social pressure) overriding capability and opportunity?
   - Is the environment implicitly permitting the wrong behavior?
   - Are different actors optimizing for different objectives with no one owning end-to-end alignment?

9. **Avoid common mistakes.**
   - Do not assume higher states are always better. "Fully Realized & Stable" can mask brittleness and hidden cost.
   - Do not treat the seven states as mutually exclusive within an organization. Different teams may be at different states for the same behavior.
   - Do not skip diagnosis. The framework's value is in matching the intervention to the specific blocker profile, not in applying generic advice.
   - When profiling personas, do not profile them in isolation. The value of multi-actor COM-B analysis is in revealing misalignment between actors, not just within them.

## Theoretical foundations

- **COM-B model:** Michie, S., van Stralen, M. M., & West, R. (2011). The behaviour change wheel: A new method for characterising and designing behaviour change interventions. *Implementation Science*, 6(1), 42.
- **Behavior Change Wheel (BCW):** The intervention function taxonomy that sits on top of COM-B, mapping each behavioral domain to evidence-based intervention categories.

The behavior states, blocker profiles, tool strategies, and tool levers are original extensions of these models, applied to the context of organizational behavior adoption and tool design.
