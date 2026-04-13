# Behavior Lenses

This file collects behavior-state-oriented lenses for understanding the `B` in COM-B. While the capability, opportunity, and motivation lenses examine the C, O, and M, this lens examines the behavior itself: how reliably it happens, how aligned people are in performing it, and how vulnerable it is to regression.

These lenses overlap with the other COM-B lenses. That is fine. Each behavior state has characteristic blocker profiles that span C, O, and M — but the primary diagnostic focus here is characterizing the *behavior's current lifecycle position*. The blocker profiles are **hypotheses** to test and refine against the C/O/M lenses, not predetermined conclusions.

This lens uses a **cycle** model, not a maturity ladder. Behaviors advance, stall, and regress depending on shifts in incentives, norms, clarity, and operating conditions. Different teams can be at different states for the same behavior.

See [com-b-abbreviations-reference.md](../com-b-bcw-bct/com-b-abbreviations-reference.md) for the shared code system.

## The 7-state behavior cycle

### Suggested cycle flow
`Contested / Undefined` → `Aspirational Only` → `Weakly Realized` → `Partially Realized / Inconsistent` → `Realized but Friction-Filled` → `Fully Realized & Stable` → `Actively Suppressed` → back to `Contested / Undefined`

## Quick-reference: State vs. Blockers

| State | Primary Blockers (COM-B) | Secondary Blockers (COM-B) |
|---|---|---|
| S.1: Fully Realized & Stable | Risk aversion (RM), Env friction (PO), Norm pressure (SO) | Procedural knowledge gaps (PC), Habit inertia (AM), Tool risk (PO) |
| S.2: Realized but Friction-Filled | Tool limits (PO), Time scarcity (PO), Workflow barriers (PO) | Learned helplessness (AM), Cognitive overload (PC), Norms of toleration (SO) |
| S.3: Partially Realized / Inconsistent | Mental-model variation (PC), Procedural gaps (PC), Local norms (SO) | No belief in one method (RM), Insufficient training (PC), Tools not aligned (PO) |
| S.4: Weakly Realized | Time scarcity (PO), Habit competition (AM), High activation energy (PO) | Short-term bias (RM), Lack of triggers (PC), Fire-drill culture (SO) |
| S.5: Aspirational Only | Identity gap (RM), No enabling structure (PO), Skill undefined (PC) | Low emotional reward (AM), Symbolic norms (SO), No clarity of "good" (PC) |
| S.6: Actively Suppressed | Political risk (RM), Punishing norms (SO), Misaligned incentives (SO) | Fear response (AM), Low psych safety (PC), Blocking systems (PO) |
| S.7: Contested / Undefined | Mental-model conflict (PC), No shared language (PC), Identity attachment to definitions (RM) | Semantic drift (SO), Turf battles (SO), Cognitive overload (PC) |

---

## S.1: Fully Realized & Stable

**Core view of the behavior:** The behavior is happening consistently, predictably, and reliably. It has become a ritual, habit, or embedded system.

**Strongest at:** Revealing hidden brittleness, invisible cost, and change-resistance in behaviors that appear healthy.

**State signal:** Ritualized, reliable, trusted.

**Characteristics:**
- Strong norms
- Clear ownership
- Predictable outputs
- Change feels risky
- Pain may exist but does not threaten the ritual

**Dimensions it tends to foreground:**

- **S.1.1** Ritual entrenchment: weakly ritualized → deeply ritualized
- **S.1.2** Change risk perception: change feels safe → change feels threatening
- **S.1.3** Hidden cost: low invisible overhead → high invisible overhead
- **S.1.4** Norm rigidity: norms are flexible → norms resist any deviation
- **S.1.5** Automation gap: manual burden is low → manual burden is high but tolerated
- **S.1.6** Ownership clarity: ambiguous ownership → clear ownership
- **S.1.7** Improvement openness: open to refinement → closed to change

**Primary blocker hypotheses (COM-B):**
- RM: Risk aversion / loss aversion
- PO: Environmental friction (manual, expensive workflows)
- SO: Norm pressure to preserve predictability

**Secondary blocker hypotheses (COM-B):**
- PC: Procedural knowledge gap (how to automate safely)
- AM: Habit inertia (status quo bias)
- PO: Tooling limitations that make change risky

**Intervention direction:**
- Respect ritual; reduce risk of disruption (PO, RM → ER, EN)
- Preserve the ritual while reducing invisible cost
- Safe sandboxes, automation of painful steps, audit trails

**What it sees well:** Why "working" behaviors may still be worth improving, and why change is resisted even when the status quo is costly.

**What it sees less well:** Whether the behavior is actually delivering value — that often requires the capability and opportunity lenses to assess.

---

## S.2: Realized but Friction-Filled

**Core view of the behavior:** The behavior consistently happens, but the environment makes it painful.

**Strongest at:** Revealing when the problem is not motivation or knowledge but environmental hostility.

**State signal:** Mandatory but painful; environment is the enemy.

**Characteristics:**
- Legacy systems
- Workarounds
- Manual effort
- Compliance-driven
- Little joy, lots of necessity

**Dimensions it tends to foreground:**

- **S.2.1** Environmental hostility: environment supports behavior → environment fights behavior
- **S.2.2** Workaround prevalence: few workarounds needed → workarounds are the norm
- **S.2.3** Manual burden: low manual effort → high manual effort
- **S.2.4** Compliance vs. commitment: people do it because they believe in it → people do it because they must
- **S.2.5** Pain visibility: friction is visible and discussed → friction is normalized and invisible
- **S.2.6** Tooling debt: tools match current needs → tools lag behind needs
- **S.2.7** Joy/engagement: behavior feels meaningful → behavior feels like a tax

**Primary blocker hypotheses (COM-B):**
- PO: Tool/system constraints (legacy systems)
- PO: Limited time/resource availability
- PO: Workflow friction (workarounds, manual steps)

**Secondary blocker hypotheses (COM-B):**
- AM: Learned helplessness ("this is just how it is")
- PC: Overload / working memory strain
- SO: Cultural acceptance of inefficiency

**Intervention direction:**
- Remove friction and overhead (PO → ER, EN)
- Streamline, automate, unblock what people already agree on

**What it sees well:** Situations where capable, motivated people are grinding through a hostile environment.

**What it sees less well:** Whether the behavior itself is well-designed — people may be doing the wrong thing efficiently.

---

## S.3: Partially Realized / Inconsistent

**Core view of the behavior:** The behavior happens, but unevenly; different teams or people do it differently.

**Strongest at:** Revealing alignment failures, semantic drift, and local-optimum traps.

**State signal:** Exists in pockets; lacks alignment.

**Characteristics:**
- Process variation
- No canonical method
- Conflicts of interpretation
- Uneven capability across teams
- Local optimizations, not a shared system

**Dimensions it tends to foreground:**

- **S.3.1** Practice variation: consistent across groups → highly variable across groups
- **S.3.2** Canonical method: strong shared method → no agreed method
- **S.3.3** Interpretation alignment: shared interpretation → conflicting interpretations
- **S.3.4** Capability evenness: similar skill levels → wide skill gaps across teams
- **S.3.5** Knowledge codification: tacit knowledge codified → tacit knowledge trapped locally
- **S.3.6** Cross-team visibility: teams can see each other's practice → teams are opaque to each other
- **S.3.7** Convergence trajectory: converging toward shared practice → diverging further

**Primary blocker hypotheses (COM-B):**
- PC: Mental-model variation
- PC: Lack of procedural knowledge ("how to do it correctly")
- SO: Local norms / team-level divergence

**Secondary blocker hypotheses (COM-B):**
- RM: Low belief in a single "right way"
- PC: Insufficient training or shared language
- PO: Tools do not enforce consistency

**Intervention direction:**
- Standardize meaning and flow (PC, SO → ED, MO, ER)
- Define "the way," enforce consistency, unify semantics

**What it sees well:** Why teams that all claim to do the same thing are actually doing different things.

**What it sees less well:** Whether the variation is genuinely problematic or whether local adaptation is appropriate — the capability lenses provide more precision here.

---

## S.4: Weakly Realized

**Core view of the behavior:** Everyone agrees the behavior matters, but it keeps getting displaced.

**Strongest at:** Revealing activation-energy barriers and priority-displacement dynamics.

**State signal:** Agreed and valued, but continually displaced.

**Characteristics:**
- Not a knowledge problem
- Not a commitment problem
- Loses to urgency, fire drills, scarcity
- Creates guilt and a backlog of "shoulds"

**Dimensions it tends to foreground:**

- **S.4.1** Priority displacement: behavior holds its slot → behavior loses to competing urgencies
- **S.4.2** Activation energy: easy to start → hard to initiate
- **S.4.3** Habit competition: behavior has its own cues → other habits crowd it out
- **S.4.4** Guilt accumulation: low guilt about skipping → chronic guilt about not doing it
- **S.4.5** Structural protection: protected time/resources → no protection from displacement
- **S.4.6** Trigger availability: clear triggers exist → no cues remind people to start
- **S.4.7** Short-vs-long-term salience: long-term value is salient → present urgency dominates

**Primary blocker hypotheses (COM-B):**
- PO: Lack of time / competing urgencies
- AM: Habit competition (other habits crowd it out)
- PO: High activation energy (too many steps)

**Secondary blocker hypotheses (COM-B):**
- RM: Short-term focus vs long-term value
- PC: Limited self-regulation structures (no triggers)
- SO: Culture prioritizes fire drills over proactive work

**Intervention direction:**
- Make starting easy; reduce forgetting (PO, AM → ER, EN)
- Provide cues, scaffolds, reminders, nudges, templates

**What it sees well:** The gap between intention and action — why people who genuinely want to do something still don't.

**What it sees less well:** Whether the displaced behavior is actually the right thing to protect — the motivation lenses help assess whether the intention is durable.

---

## S.5: Aspirational Only

**Core view of the behavior:** The behavior is desired or politically valuable, but not practiced.

**Strongest at:** Revealing identity-practice gaps and aspiration without infrastructure.

**State signal:** Identity-level desire without practice.

**Characteristics:**
- Leadership vision statements
- Cultural aspiration
- Branding and identity motives
- Small symbolic attempts
- No actual habit infrastructure

**Dimensions it tends to foreground:**

- **S.5.1** Identity-practice gap: behavior matches practice → aspiration far exceeds practice
- **S.5.2** Infrastructure existence: enabling systems exist → no enabling systems
- **S.5.3** Skill definition: "what good looks like" is clear → "what good looks like" is undefined
- **S.5.4** Symbolic vs. substantive: investment is substantive → investment is purely symbolic
- **S.5.5** Early-win availability: quick wins are accessible → no easy entry point
- **S.5.6** Leadership modeling: leaders practice the behavior → leaders only talk about it
- **S.5.7** Aspiration durability: aspiration is stable → aspiration shifts with trends

**Primary blocker hypotheses (COM-B):**
- RM: Identity gap (aspiration > true commitment)
- PO: No enabling structures or systems
- PC: Undefined skills or knowledge to begin

**Secondary blocker hypotheses (COM-B):**
- AM: Low emotional reward / no habit loop
- SO: Symbolic buy-in without behavioral reinforcement
- PC: Undefined "what good looks like"

**Intervention direction:**
- Turn aspiration into action (PC, RM → ED, TR, EN)
- Make the abstract concrete, enable early wins, bootstrap skill

**What it sees well:** Why organizations declare values they cannot enact, and what it takes to bridge the gap.

**What it sees less well:** Whether the aspiration is authentic or performative — the motivation lenses (especially identity and SDT) go deeper here.

---

## S.6: Actively Suppressed

**Core view of the behavior:** Not only is the behavior not happening; explicit or implicit forces prevent it.

**Strongest at:** Revealing political, structural, and incentive-based suppression.

**State signal:** Systemic forces prevent the behavior.

**Characteristics:**
- Political risk (doing it creates exposure)
- Turf protection ("do not step on toes")
- Misaligned incentives (reward systems punish the behavior)
- Cultural norms against it
- Learned helplessness

**Dimensions it tends to foreground:**

- **S.6.1** Suppression intensity: mild discouragement → active prevention
- **S.6.2** Political risk level: low risk → high risk to attempt
- **S.6.3** Incentive misalignment: incentives are neutral → incentives punish the behavior
- **S.6.4** Turf protection: open boundaries → strong territorial defense
- **S.6.5** Fear level: low fear → pervasive fear about attempting
- **S.6.6** Suppression visibility: suppression is overt and discussable → suppression is covert and undiscussable
- **S.6.7** Safe-channel availability: safe ways to attempt exist → no safe channel

**Primary blocker hypotheses (COM-B):**
- RM: Political risk / threat to status
- SO: Norms that punish or discourage the behavior
- SO: Misaligned incentives

**Secondary blocker hypotheses (COM-B):**
- AM: Fear responses (threat, anxiety)
- PC: Low psychological safety to attempt the behavior
- PO: Systems designed to block the behavior

**Intervention direction:**
- Make safe and depoliticized (SO, RM → ER, MO)
- Create safe channels, depersonalize conflict, legitimize practice

**What it sees well:** Why behaviors fail in politically charged environments even when everyone privately agrees they should happen.

**What it sees less well:** Granular social dynamics — the social opportunity lenses (especially power, norms, legitimacy) go much deeper.

---

## S.7: Contested / Undefined

**Core view of the behavior:** People cannot agree on, or clearly describe, what the behavior actually is.

**Strongest at:** Revealing definitional ambiguity, semantic drift, and conceptual incoherence as root causes.

**State signal:** No shared definition; conceptual ambiguity.

**Characteristics:**
- Fundamental definitional ambiguity
- Competing framings
- No shared language
- Same words used with different meanings
- Meetings derail into debates about definitions
- Extremely high cognitive load
- Alignment is impossible because the conceptual object is unstable

**Dimensions it tends to foreground:**

- **S.7.1** Definitional clarity: shared clear definition → fundamental definitional conflict
- **S.7.2** Semantic stability: stable meaning → meaning drifts across groups
- **S.7.3** Framing convergence: converging on a shared frame → competing frames entrenched
- **S.7.4** Cognitive load from ambiguity: low → overwhelming
- **S.7.5** Identity attachment to definitions: definitions are negotiable → definitions are identity-bound
- **S.7.6** Shared language: common vocabulary exists → same words mean different things
- **S.7.7** Discussability: definitional differences can be surfaced → differences are undiscussable

**Primary blocker hypotheses (COM-B):**
- PC: Mental-model divergence (core definitional conflict)
- PC: Lack of conceptual knowledge / shared language
- RM: Identity-driven attachment to competing definitions

**Secondary blocker hypotheses (COM-B):**
- SO: Semantic drift (same words, different meanings)
- SO: Intergroup friction / turf over ownership of definitions
- PC: Cognitive overload / ambiguity tolerance

**Intervention direction:**
- Create shared clarity (PC, SO → ED, ER)
- Surface differences, reveal mental models, align terminology

**What it sees well:** Why alignment fails at the conceptual level — before you can change a behavior, you have to agree on what it is.

**What it sees less well:** The specific capability gaps or social dynamics driving the conflict — the capability lenses (especially shared representations **PC.1.6**) and social opportunity lenses (norms, legitimacy) go deeper.

---

## From Behavior Lenses To COM-B / BCW

These lenses do not replace COM-B. They help characterize *where the behavior sits in its lifecycle* so the C/O/M lenses can be applied with the right starting hypotheses.

Each state's blocker profile is a hypothesis about which COM-B codes are most likely in play. The intervention directions use BCW function codes:
- ED = Education, TR = Training, PE = Persuasion, INC = Incentivisation, COE = Coercion
- RE = Restriction, ER = Environmental Restructuring, MO = Modelling, EN = Enablement

See [com-b-abbreviations-reference.md](../com-b-bcw-bct/com-b-abbreviations-reference.md) for the full code system.

## How to use these lenses together

One practical way to use these state lenses is to ask a diagnostic question for each:

- **S.1 — Fully Realized & Stable:** Is this behavior ritualized and working, but hiding cost or blocking improvement?
- **S.2 — Realized but Friction-Filled:** Is the behavior happening but painful because the environment fights it?
- **S.3 — Partially Realized / Inconsistent:** Is the behavior happening in pockets but without alignment or consistency?
- **S.4 — Weakly Realized:** Is the behavior endorsed and intended but continually displaced by competing priorities?
- **S.5 — Aspirational Only:** Is the behavior aspirational but lacking practice, infrastructure, or defined skill?
- **S.6 — Actively Suppressed:** Is the behavior blocked by political, structural, or incentive-based forces?
- **S.7 — Contested / Undefined:** Can people even agree on what the behavior is?

Match the situation to the best-fit state, then use the blocker hypotheses and intervention direction as starting points for the C/O/M lens analysis.

## Boundaries of this file

This note is intentionally behavior-lifecycle-first. It does not fully address:

- specific capability gaps (mental models, procedural skill, judgment)
- specific opportunity constraints (tools, time, norms, politics)
- specific motivation dynamics (identity, habit, self-efficacy, reinforcement)

Those belong in the adjacent lens files:
- [capability-lenses.md](capability-lenses.md) for PC and PHC
- [motivation-lenses.md](motivation-lenses.md) for RM and AM
- [physical-opportunity-lenses.md](physical-opportunity-lenses.md) for PO
- [social-opportunity-lenses.md](social-opportunity-lenses.md) for SO

Important distinctions:

- The behavior state is not a permanent classification. It is a snapshot that can change as conditions shift.
- The blocker profiles are hypotheses, not facts. They must be tested against the C/O/M lenses.
- Different actors or teams can be at different states for the same behavior.

Read next:
- [dimensional-ids.md](dimensional-ids.md) for how dimension IDs are prefixed and dotted
- [capability-lenses.md](capability-lenses.md) for PC and PHC dimensions
- [motivation-lenses.md](motivation-lenses.md) for RM and AM dimensions
- [physical-opportunity-lenses.md](physical-opportunity-lenses.md) for PO dimensions
- [social-opportunity-lenses.md](social-opportunity-lenses.md) for SO dimensions
- [com-b-to-bcw-intervention-function-mapping.md](../com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md) for BCW intervention families

## References To Ground These Lenses

- **COM-B and BCW:** Michie, van Stralen, and West on COM-B and the Behaviour Change Wheel.
- **Behavior states and blocker profiles:** Original extensions of COM-B diagnostic work, applying lifecycle thinking to behavioral readiness assessment in organizational and product contexts.
- **Cycle model:** Draws on stage-of-change traditions (Prochaska and DiClemente) reframed as a non-linear cycle rather than a progressive ladder.
