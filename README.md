# Behavior Diagnosis Framework

This collection of files encodes a behavioral diagnostic framework built on top of two established models from behavioral science: the **COM-B model** (Capability, Opportunity, Motivation - Behavior) by Susan Michie and colleagues, and the **Behavior Change Wheel (BCW)** intervention taxonomy. The framework extends these models into the domain of organizational behavior adoption, tool design, and change strategy. It also includes an applied example showing how to use COM-B to profile personas within a multi-actor behavior system.

## How to think about these files

The files form a layered system. Start from the foundational reference tables, then use the diagnostic cycle to apply them.

### Layer 1: Vocabulary

**`com-b-abbreviations-reference.md`**

The glossary. Defines the six COM-B codes (PC, PHC, PO, SO, RM, AM) used across every other file. Each code maps to one dimension of Capability, Opportunity, or Motivation, with real-world examples of the barriers it represents.

Read this first if you encounter an abbreviation you do not recognize. Every blocker, strategy, and lever in the framework traces back to one of these six codes.

### Layer 2: Intervention logic

**`com-b-to-bcw-intervention-function-mapping.md`**

The bridge between diagnosis and action. Contains two tables:

1. Which BCW intervention functions (Education, Training, Persuasion, etc.) are effective for which COM-B problem type.
2. What each BCW intervention abbreviation (ED, TR, PE, INC, COE, RE, ER, MO, EN) means and does.

This file answers: "Given a COM-B blocker, what categories of intervention are likely to work?" It is the theoretical engine behind the tool levers recommended in the diagnostic cycle.

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

### Layer 6: Applied example — persona-level COM-B profiles

**`personas_jobs.md`**

A worked example applying COM-B to a real multi-actor behavior system: avalanche safety. Profiles eight personas (Forecaster, Field Observer, Ski Patrol, Highway Control, Mountain Guide, Backcountry Recreationist, Search and Rescue, Educator), each described with:

- Target behaviors
- Needs and desires
- COM-B breakdown (Capability, Opportunity, Motivation — with specific sub-dimensions)
- Failure modes

Beyond individual profiles, the file surfaces four system-level insights:

1. **The "last mile" problem:** failures concentrate at the decision point (Guide / Recreationist) even when upstream actors perform well.
2. **Motivation is the weakest link:** automatic motivation (powder fever, social pressure, familiarity) overrides capability and opportunity.
3. **Opportunity shapes behavior:** environmental cues (easy access, existing tracks, open terrain) implicitly permit risk.
4. **Misaligned optimization:** each persona optimizes for a different objective; no single persona owns end-to-end behavioral alignment.

The core framing: avalanche safety is not a knowledge problem — it is a distributed behavior system where capability is uneven, opportunity is often permissive, and motivation is frequently misaligned. Failure occurs when these do not align at the moment of decision.

This file demonstrates how the abstract COM-B vocabulary (Layer 1) can be applied to profile real actors, diagnose where behavior breaks down across a system, and identify the interfaces between personas where interventions matter most.

---

## How the files reference each other

```
com-b-abbreviations-reference.md
    Defines: PC, PHC, PO, SO, RM, AM
    Referenced by: every other file

com-b-to-bcw-intervention-function-mapping.md
    Defines: ED, TR, PE, INC, COE, RE, ER, MO, EN
    Uses: COM-B codes from abbreviations reference
    Referenced by: diagnostic cycle (tool lever annotations)

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

personas_jobs.md
    Uses: COM-B categories (C, O, M) from abbreviations reference
    Applies: COM-B as a persona profiling lens (not abbreviated codes)
    Demonstrates: how to decompose a multi-actor system using COM-B
    Complements: diagnostic cycle (cycle diagnoses behavior states;
                  personas file diagnoses actor-level breakdowns)
```

## How an LLM should use this framework

1. **Classify the behavior state.** When someone describes a behavior (a practice, ritual, process, habit), match their description to one of the seven states using the characteristics and state signals in the diagnostic cycle.

2. **Identify the blockers.** Use the blocker matrix or the per-state blocker section to name the primary and secondary COM-B forces holding the behavior in place. Decode any abbreviation using the abbreviations reference.

3. **Select interventions.** Use the intervention mapping to find which BCW functions apply to the identified COM-B blockers. Use the tool influence file if the question is specifically about product or tool design.

4. **Recommend tool levers.** Use the per-state tool levers in the diagnostic cycle to suggest specific, actionable changes. Each lever is already annotated with its COM-B target and BCW mechanism, so recommendations are traceable.

5. **Reason about transitions.** The cycle is not a maturity ladder. Behaviors can regress (e.g., a Fully Realized behavior becomes Actively Suppressed after a reorg). Use the cycle flow to reason about what state a behavior might move toward, and what blockers would emerge at that next state.

6. **Profile actors in a system.** When the situation involves multiple actors (personas, roles, teams), use the personas file as a template. For each actor, map their target behaviors, COM-B profile (what they can do, what the environment permits, what drives them), and failure modes. Then look at the interfaces between actors — where one actor's output becomes another's input — because system-level failures often occur at these handoffs, not within a single actor.

7. **Diagnose system-level dynamics.** After profiling actors, check for the patterns surfaced in the personas file:
   - Is there a "last mile" problem where upstream performance is strong but downstream decisions still fail?
   - Is automatic motivation (habits, biases, social pressure) overriding capability and opportunity?
   - Is the environment implicitly permitting the wrong behavior?
   - Are different actors optimizing for different objectives with no one owning end-to-end alignment?

8. **Avoid common mistakes.**
   - Do not assume higher states are always better. "Fully Realized & Stable" can mask brittleness and hidden cost.
   - Do not treat the seven states as mutually exclusive within an organization. Different teams may be at different states for the same behavior.
   - Do not skip diagnosis. The framework's value is in matching the intervention to the specific blocker profile, not in applying generic advice.
   - Do not profile personas in isolation. The value of multi-actor COM-B analysis is in revealing misalignment between actors, not just within them.

## Theoretical foundations

- **COM-B model:** Michie, S., van Stralen, M. M., & West, R. (2011). The behaviour change wheel: A new method for characterising and designing behaviour change interventions. *Implementation Science*, 6(1), 42.
- **Behavior Change Wheel (BCW):** The intervention function taxonomy that sits on top of COM-B, mapping each behavioral domain to evidence-based intervention categories.

The behavior states, blocker profiles, tool strategies, and tool levers are original extensions of these models, applied to the context of organizational behavior adoption and tool design.
