# Capability Lenses

This file collects capability-oriented lenses for understanding the `C` in COM-B. It treats `Psychological Capability` (`PC`) and `Physical Capability` (`PHC`) as the two top-level buckets, then uses established sub-lenses to unpack what each one may contain. These lenses overlap. That is fine. The goal is to make capability more descriptively useful without losing the organizing simplicity of COM-B.

This note also absorbs the full value of the earlier task-diagnostic material by translating it into capability language rather than preserving a separate task-first layer. In rough terms:

- `HTA` sharpens procedural structure, sequence, repetition, and execution demands.
- `CTA` sharpens cue use, tacit expertise, mental models, and judgment.
- `CSE` sharpens control-relevant understanding, observability, and adaptation demands.
- `NDM` sharpens judgment under uncertainty, time pressure, and high stakes.
- `Distributed Cognition / Team Cognition` sharpens shared representations and distributed expertise.
- `Learning Sciences` sharpens acquisition, transfer, feedback, and scaffolded performance.

Within this repo's COM-B vocabulary:

- `PC` covers knowledge, mental models, judgment, psychological skill, conceptual clarity, and self-regulatory capability.
- `PHC` covers bodily skill, strength, stamina, coordination, and reliable physical execution.

See [com-b-abbreviations-reference.md](../com-b-bcw-bct/com-b-abbreviations-reference.md) for the shared code system.

## 1. Psychological Capability

Psychological capability concerns what a person must be able to understand, perceive, judge, remember, monitor, and mentally coordinate in order to perform the behavior. It is strongest when the diagnostic question is some version of:

- Do people know what to do?
- Do they understand how the situation works?
- Can they detect and interpret the right signals?
- Can they make sound judgments under the conditions of the task?
- Can they monitor and regulate their own performance?

### 1.1 Declarative and Procedural Knowledge / Skill Acquisition

**Core view of capability:** Capability depends not only on knowing facts or concepts, but also on procedural fluency: knowing how to carry out the behavior in sequence and with sufficient coordination and repetition.

**Strongest at:** Revealing the difference between missing knowledge, missing procedural know-how, and insufficient fluency.

**Academic grounding:** Draws on declarative/procedural knowledge distinctions, stage models of skill acquisition, and expertise-development work, especially Anderson, Fitts and Posner, and later learning-science traditions on fluency and transfer.

**Dimensions it tends to foreground:**

- **PC.1.1.1** Declarative knowledge: thin factual understanding -> rich conceptual understanding
- **PC.1.1.2** Procedural fluency: stepwise and effortful -> smooth and well-practiced
- **PC.1.1.3** Sequence clarity: vague or inconsistent sequence -> clear and executable sequence
- **PC.1.1.4** Skill stage: novice -> practiced -> increasingly automatic
- **PC.1.1.5** Repeatability: brittle performance -> stable repeated performance
- **PC.1.1.6** Exception handling: normal cases only -> adaptable procedure across cases
- **PC.1.1.7** Transfer readiness: narrow context competence -> competence that transfers

**What it sees well:** Situations where the person has heard the material but still cannot execute the behavior reliably.

**What it sees less well:** Value alignment, identity fit, and cue-triggered or hot-state behavior unless paired with [motivation-lenses.md](motivation-lenses.md); it mainly refines `PC`.

### 1.2 Mental Models / Situation Models

**Core view of capability:** Capability depends on whether people hold a workable internal model of how the system, domain, or situation operates.

**Strongest at:** Revealing faulty causal understanding, incomplete structural understanding, and reasoning from the wrong model of the world.

**Academic grounding:** Draws on mental-model traditions and applied work on situation models in complex systems, especially Johnson-Laird, Gentner and Stevens, and adjacent human-factors work on understanding dynamic environments.

**Dimensions it tends to foreground:**

- **PC.1.2.1** Model accuracy: misaligned mental model -> well-aligned mental model
- **PC.1.2.2** Causal understanding: weak sense of causality -> strong causal understanding
- **PC.1.2.3** Structural understanding: fragmented picture -> coherent system picture
- **PC.1.2.4** Dynamical understanding: static understanding -> understanding of change over time
- **PC.1.2.5** Model completeness: important factors omitted -> relevant factors integrated
- **PC.1.2.6** Framing quality: poor framing -> appropriate framing
- **PC.1.2.7** Updateability: rigid model -> revisable and adaptive model

**What it sees well:** Why people make coherent-seeming but wrong decisions because they are reasoning from the wrong internal representation.

**What it sees less well:** Physical skill limits and purely emotional or habit-driven failure modes; it mainly refines `PC`.

### 1.3 Judgment and Decision Competence

**Core view of capability:** Capability includes the ability to make workable judgments under uncertainty, pressure, incomplete information, and competing demands.

**Strongest at:** Revealing whether people have the judgmental competence to select, prioritize, and adapt actions well, especially outside routine cases.

**Academic grounding:** Draws on both judgment-and-decision-making and naturalistic decision-making traditions, especially Tversky and Kahneman on heuristics and biases, and Klein on recognition-primed decision making in real settings.

**Dimensions it tends to foreground:**

- **PC.1.3.1** Judgment demand: few consequential choices -> many consequential choices
- **PC.1.3.2** Uncertainty tolerance: low ability to reason under uncertainty -> high ability
- **PC.1.3.3** Heuristic quality: misleading shortcuts dominate -> useful decision heuristics
- **PC.1.3.4** Recognition competence: weak pattern-based recognition -> strong recognition competence
- **PC.1.3.5** Rule dependence: rigid rule following -> flexible, context-sensitive judgment
- **PC.1.3.6** Time-pressure competence: quality collapses under pressure -> quality is sustained
- **PC.1.3.7** Tradeoff handling: poor tradeoff reasoning -> strong tradeoff reasoning

**What it sees well:** Situations where the issue is not missing facts, but poor judgment, poor decision rules, or lack of experience in applying them.

**What it sees less well:** Whether the person is motivated to use those judgments, and whether the environment gives them time or support to do so.

### 1.4 Signal Detection and Pattern Recognition

**Core view of capability:** Capability often depends on whether people can perceive weak, noisy, rare, or ambiguous signals and recognize meaningful patterns quickly enough to act.

**Strongest at:** Revealing the perceptual and recognition demands of the behavior.

**Academic grounding:** Draws on signal detection theory and expertise research on perceptual discrimination and pattern recognition, especially Green and Swets, plus expertise traditions that study how experts encode and discriminate meaningful patterns.

**Dimensions it tends to foreground:**

- **PC.1.4.1** Signal strength: obvious signal -> subtle or weak signal
- **PC.1.4.2** Signal ambiguity: clean signal -> noisy or conflicting signal
- **PC.1.4.3** Detection sensitivity: low sensitivity -> high sensitivity
- **PC.1.4.4** False-alarm balance: overcautious threshold -> overliberal threshold
- **PC.1.4.5** Pattern repertoire: few usable patterns -> rich pattern repertoire
- **PC.1.4.6** Case familiarity: unfamiliar cases dominate -> familiar patterns are recognized quickly
- **PC.1.4.7** Comparison burden: little comparison needed -> many comparisons needed

**What it sees well:** Why subtle-signal tasks, anomaly detection, and expert pattern recognition are often capability problems even when motivation is high.

**What it sees less well:** Broader workflow and tool design factors that make signals more or less visible; those drift toward `PO`.

### 1.5 Metacognition and Calibration

**Core view of capability:** Capability includes the ability to monitor one's own understanding, detect uncertainty, regulate effort, and calibrate confidence against actual performance.

**Strongest at:** Revealing overconfidence, underconfidence, poor self-monitoring, and failure to notice one's own knowledge gaps.

**Academic grounding:** Draws on metacognition and monitoring-control traditions, especially Flavell, Nelson and Narens, and later calibration research on the fit between confidence and performance.

**Dimensions it tends to foreground:**

- **PC.1.5.1** Calibration: confidence poorly tracks accuracy -> confidence tracks accuracy well
- **PC.1.5.2** Monitoring quality: weak self-monitoring -> strong self-monitoring
- **PC.1.5.3** Error detection: misses own errors -> catches own errors
- **PC.1.5.4** Effort allocation: effort is poorly targeted -> effort is well targeted
- **PC.1.5.5** Uncertainty awareness: uncertainty is hidden from self -> uncertainty is noticed
- **PC.1.5.6** Help-seeking readiness: rarely seeks correction -> seeks correction appropriately
- **PC.1.5.7** Reflective control: poor regulation of strategy -> strong regulation of strategy

**What it sees well:** The difference between someone who lacks knowledge and someone who also does not know that they lack it.

**What it sees less well:** Hot emotional reactions, reinforced habits, and some shared-language issues unless paired with other lenses.

### 1.6 Shared Representations and Conceptual Alignment

**Core view of capability:** Capability is sometimes individual, but often depends on whether people share compatible concepts, definitions, representations, and frames of reference.

**Strongest at:** Revealing conceptual drift, incompatible meanings, and team-level capability failures that masquerade as individual ignorance.

**Academic grounding:** Draws on distributed cognition, common-ground, shared-mental-model, and transactive-memory traditions, especially Hutchins, Clark, Cannon-Bowers and Salas, and Wegner.

**Dimensions it tends to foreground:**

- **PC.1.6.1** Shared language: divergent terminology -> common terminology
- **PC.1.6.2** Conceptual alignment: conflicting concepts -> aligned concepts
- **PC.1.6.3** Representation compatibility: fragmented representations -> compatible shared representations
- **PC.1.6.4** Common ground: little mutual understanding -> strong common ground
- **PC.1.6.5** Coordination literacy: weak understanding of who knows what -> strong distributed understanding
- **PC.1.6.6** Definition stability: unstable definitions -> stable definitions
- **PC.1.6.7** Cross-role interpretability: representations travel poorly -> representations travel well

**What it sees well:** Situations where people are not simply untrained, but are working from different meanings and incompatible conceptual objects.

**What it sees less well:** Incentive conflict, legitimacy, and permission structures that make alignment politically hard; that drifts toward `SO`.

### 1.7 Supported Performance and Scaffolding

**Core view of capability:** Capability can exist partially or conditionally: a person may not be able to perform independently yet, but may perform competently with prompts, examples, checklists, or guidance.

**Strongest at:** Revealing the difference between `cannot perform` and `cannot yet perform alone`.

**Academic grounding:** Draws on scaffolding, the zone of proximal development, and cognitive apprenticeship traditions, especially Vygotsky, Wood, Bruner, and Ross, and Collins, Brown, and Newman.

**Dimensions it tends to foreground:**

- **PC.1.7.1** Independence: requires continuous support -> performs independently
- **PC.1.7.2** Scaffold sensitivity: only strong support works -> light support is enough
- **PC.1.7.3** Prompt dependence: action needs explicit prompting -> action self-initiates
- **PC.1.7.4** Example dependence: requires worked examples -> can generalize beyond examples
- **PC.1.7.5** Feedback dependence: needs constant correction -> self-corrects reliably
- **PC.1.7.6** Transfer under support: support works only locally -> support generalizes capability
- **PC.1.7.7** Fading readiness: support cannot be reduced -> support can be faded

**What it sees well:** Learning-in-progress situations, guided workflows, job aids, and cases where capability is emerging but not yet consolidated.

**What it sees less well:** Whether the support exists in the environment at all; that availability question often belongs to `PO` even when the capability question belongs to `PC`.

## 2. Physical Capability

Physical capability concerns what the body must be able to do reliably to enact the behavior: move, coordinate, sustain, manipulate, tolerate load, and execute motor actions safely enough for the task.

It is strongest when the diagnostic question is some version of:

- Can the person physically perform the behavior?
- Is the issue skillful bodily execution or lack of fluency?
- Is fatigue, recovery, or physical decline limiting performance?
- Is the person capable in principle, but only briefly or inconsistently?

### 2.1 Motor Learning and Psychomotor Skill Acquisition

**Core view of capability:** Physical capability depends on practice-based acquisition of bodily skill, not just raw strength or willingness.

**Strongest at:** Revealing whether physical performance is novice, emerging, fluent, or automated.

**Academic grounding:** Draws on psychomotor learning and stage-based skill-acquisition work, especially Fitts and Posner, Schmidt's schema tradition, and later motor-learning research on retention and transfer.

**Dimensions it tends to foreground:**

- **PHC.2.1.1** Skill stage: novice -> practiced -> increasingly automatic
- **PHC.2.1.2** Execution fluency: effortful and segmented -> smooth and integrated
- **PHC.2.1.3** Accuracy: inconsistent movement -> accurate movement
- **PHC.2.1.4** Retention: weak retention -> stable retained skill
- **PHC.2.1.5** Transfer: context-bound skill -> transferable skill
- **PHC.2.1.6** Consistency: variable execution -> reliable execution
- **PHC.2.1.7** Error correction: repeated uncorrected errors -> adaptive correction

**What it sees well:** Why a person may understand the task but still fail at the bodily execution of it.

**What it sees less well:** Broader environmental mismatch, tool inadequacy, and layout problems unless paired with opportunity or ergonomic analysis; it mainly refines `PHC`.

### 2.2 Motor Control and Coordination

**Core view of capability:** Physical capability includes how well movement is organized, stabilized, and coordinated under the actual demands of the task.

**Strongest at:** Revealing dexterity limits, coordination breakdowns, interference, and poor motor organization.

**Academic grounding:** Draws on motor-control and coordination traditions, especially Bernstein on movement coordination, Newell on constraints, and coordination-dynamics work such as Kelso.

**Dimensions it tends to foreground:**

- **PHC.2.2.1** Coordination quality: poorly coordinated -> well coordinated
- **PHC.2.2.2** Dexterity demand: low dexterity -> high dexterity
- **PHC.2.2.3** Movement stability: unstable execution -> stable execution
- **PHC.2.2.4** Variability: high variability -> controlled variability
- **PHC.2.2.5** Dual-task interference: strong interference -> low interference
- **PHC.2.2.6** Timing precision: rough timing -> precise timing
- **PHC.2.2.7** Fine-vs-gross motor demand: mostly gross -> heavily fine-motor

**What it sees well:** Execution-quality problems that are not primarily about strength or motivation.

**What it sees less well:** Whether the surrounding tools or layout are making coordination harder than necessary; that often belongs to `PO`.

### 2.3 Work Physiology, Fatigue, and Recovery

**Core view of capability:** Physical capability depends not only on whether someone can perform the behavior once, but whether they can sustain it, recover from it, and repeat it reliably over time.

**Strongest at:** Revealing endurance limits, fatigue effects, recovery deficits, and performance drift.

**Academic grounding:** Draws on occupational physiology, fatigue, and work-capacity traditions, including classic ergonomics and exercise-physiology work on workload, recovery, and cumulative strain.

**Dimensions it tends to foreground:**

- **PHC.2.3.1** Endurance: short-lived capacity -> sustained capacity
- **PHC.2.3.2** Fatigue load: low fatigue burden -> high fatigue burden
- **PHC.2.3.3** Recovery speed: fast recovery -> slow recovery
- **PHC.2.3.4** Performance drift: stable over time -> degrades over time
- **PHC.2.3.5** Acute-vs-chronic strain: low cumulative burden -> high cumulative burden
- **PHC.2.3.6** Freshness requirement: performance robust when fatigued -> performance requires freshness
- **PHC.2.3.7** Shift tolerance: stable across shifts -> strong decline across shifts

**What it sees well:** Situations where the person can do the task at first, but not sustainably or repeatedly.

**What it sees less well:** Whether scheduling, staffing, breaks, or workload design are causing the fatigue; that part often belongs to `PO`.

### 2.4 Functional Motor Performance

**Core view of capability:** Physical capability can be assessed in terms of whether someone can complete bounded, concrete physical actions safely and reliably.

**Strongest at:** Revealing whether the person can perform the required bodily actions at all.

**Academic grounding:** Draws on rehabilitation, occupational-performance, and functional-assessment traditions, including the `ICF` family of thinking about functioning, activity, and participation.

**Dimensions it tends to foreground:**

- **PHC.2.4.1** Functional adequacy: cannot meet minimum requirement -> can meet requirement
- **PHC.2.4.2** Strength demand: low force requirement -> high force requirement
- **PHC.2.4.3** Range-of-motion demand: low range demand -> high range demand
- **PHC.2.4.4** Balance and stability: low balance demand -> high balance demand
- **PHC.2.4.5** Manual handling demand: light handling -> heavy handling
- **PHC.2.4.6** Safety margin: narrow safety margin -> strong safety margin
- **PHC.2.4.7** Reliability of execution: inconsistent performance -> dependable performance

**What it sees well:** The can/cannot boundary, especially for concrete physical tasks.

**What it sees less well:** Nuanced issues of meaning, planning, or complex environmental fit.

### 2.5 Physical Ergonomics as Demand Analysis

**Core view of capability:** Physical capability is partly about the body, but it is best understood relative to the physical demands imposed by the task.

**Strongest at:** Revealing when task demands exceed bodily reach, posture tolerance, force tolerance, repetition tolerance, or movement efficiency.

**Academic grounding:** Draws on physical ergonomics and human-task-fit traditions, especially work on posture, force, repetition, anthropometric fit, and biomechanical exposure in human factors and ergonomics.

**Dimensions it tends to foreground:**

- **PHC.2.5.1** Posture demand: neutral posture -> awkward posture
- **PHC.2.5.2** Reach demand: comfortable reach -> extreme reach
- **PHC.2.5.3** Force demand: low exertion -> high exertion
- **PHC.2.5.4** Repetition load: infrequent repetition -> high repetition
- **PHC.2.5.5** Biomechanical sustainability: sustainable -> risky or degrading
- **PHC.2.5.6** Handling complexity: simple manipulation -> complex manipulation
- **PHC.2.5.7** Bodily fit: strong fit between body and task -> mismatch between body and task

**What it sees well:** Cases where the bodily demands of the task are simply too high or too poorly matched to the actor.

**What it sees less well:** Whether layout, tools, space, or scheduling should be redesigned instead; that broader redesign question often belongs to `PO`.

## From Capability Lenses To COM-B / BCW

These lenses do not replace COM-B. They help specify what kind of capability problem is sitting inside the broad `C` branch.

- The psychological lenses mainly refine `PC`.
- The physical lenses mainly refine `PHC`.
- Some situations blend both. For example, a difficult surgical procedure can involve `PC` burdens in signal interpretation and judgment, while also placing `PHC` burdens on dexterity, posture, and fatigue tolerance.

Once the dominant capability pattern is clearer, the next step is usually to move into the BCW mapping in [com-b-to-bcw-intervention-function-mapping.md](../com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md):

- `PC` is most often paired with `ED`, `TR`, and `EN`.
- `PHC` is most often paired with `TR` and `EN`.

The goal is not to duplicate that mapping here, but to make it easier to move from capability diagnosis to intervention family.

## How to use these lenses together

One practical way to use these lenses is to ask a different kind of question with each:

- Declarative and Procedural Knowledge / Skill Acquisition: Is the issue facts, concepts, procedures, or fluency?
- Mental Models / Situation Models: Are people reasoning from the right model of the system or situation?
- Judgment and Decision Competence: Can they make workable judgments under the real conditions of the task?
- Signal Detection and Pattern Recognition: Can they perceive and recognize the right signals in time?
- Metacognition and Calibration: Do they know when they do not know, and can they regulate accordingly?
- Shared Representations and Conceptual Alignment: Are people working from compatible concepts and definitions?
- Supported Performance and Scaffolding: Can they perform only with support, or independently?
- Motor Learning and Psychomotor Skill Acquisition: How practiced and fluent is the bodily skill?
- Motor Control and Coordination: How well organized and stable is the movement?
- Work Physiology, Fatigue, and Recovery: Can the behavior be sustained over time?
- Functional Motor Performance: Can the person perform the required bodily actions at all?
- Physical Ergonomics as Demand Analysis: Do the bodily demands of the task exceed the actor's sustainable capacity?

Used together, these lenses can help turn the broad COM-B label of `capability` into a more precise diagnosis.

## Boundaries of this file

This note is intentionally capability-first. It does not fully address:

- beliefs about capability, value, or identity
- habits, affect, or other motivation dynamics
- time, tools, workflow, and other opportunity conditions
- broad legitimacy, politics, or institutional context

Those belong more naturally in adjacent notes such as [motivation-lenses.md](motivation-lenses.md), [physical-opportunity-lenses.md](physical-opportunity-lenses.md), [social-opportunity-lenses.md](social-opportunity-lenses.md), and broader practice or institutional analysis.

Important distinctions:

- `PC` is not `RM`
  Actual knowledge, judgment, and psychological skill are different from belief about capability or willingness to act.
- `PHC` is not `PO`
  Bodily limits are different from missing time, tools, layout support, or environmental resources.
- capability is not the whole task
  This note asks what the actor must be able to know, perceive, judge, and physically do; it does not try to preserve task analysis as a separate first-class layer.

Read next:
- [motivation-lenses.md](motivation-lenses.md) for `RM` and `AM`
- [physical-opportunity-lenses.md](physical-opportunity-lenses.md) for `PO` diagnosis of time, tools, workflow, and local environment
- [social-opportunity-lenses.md](social-opportunity-lenses.md) for `SO` diagnosis of norms, incentives, legitimacy, and politics
- [behavior-lenses.md](behavior-lenses.md) for how `PC` appears in states such as `Partially Realized / Inconsistent`, `Aspirational Only`, and `Contested / Undefined`
- [com-b-to-bcw-intervention-function-mapping.md](../com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md) for BCW intervention families after capability diagnosis

## References To Ground These Lenses

- **COM-B and BCW:** Michie, van Stralen, and West on COM-B and the Behaviour Change Wheel.
- **Declarative and Procedural Knowledge / Skill Acquisition:** Anderson on declarative and procedural knowledge; Fitts and Posner on stages of skill acquisition; later learning-science and expertise-development work on fluency, practice, and transfer.
- **Mental Models / Situation Models:** Johnson-Laird on mental models; Gentner and Stevens on mental models; adjacent human-factors work on understanding dynamic systems.
- **Judgment and Decision Competence:** Tversky and Kahneman on heuristics and biases; Klein and the `NDM` tradition on recognition-primed decision making.
- **Signal Detection and Pattern Recognition:** Green and Swets on signal detection theory; expertise work on perceptual discrimination, chunking, and pattern recognition.
- **Metacognition and Calibration:** Flavell on metacognition; Nelson and Narens on monitoring and control; later calibration research on confidence and accuracy.
- **Shared Representations and Conceptual Alignment:** Hutchins on distributed cognition; Clark on common ground; Cannon-Bowers, Salas, and Converse on shared mental models; Wegner on transactive memory.
- **Supported Performance and Scaffolding:** Vygotsky on the zone of proximal development; Wood, Bruner, and Ross on scaffolding; Collins, Brown, and Newman on cognitive apprenticeship.
- **Motor Learning and Psychomotor Skill Acquisition:** Fitts and Posner on stages of psychomotor learning; Schmidt on schema theory; later motor-learning research on retention, feedback, and transfer.
- **Motor Control and Coordination:** Bernstein on coordination and degrees of freedom; Newell on constraints; Kelso on coordination dynamics.
- **Work Physiology, Fatigue, and Recovery:** occupational physiology, fatigue science, and classic ergonomics work on work capacity, recovery, and cumulative strain.
- **Functional Motor Performance:** rehabilitation and occupational-performance traditions; `ICF`-oriented work on function, activity, and participation.
- **Physical Ergonomics as Demand Analysis:** physical ergonomics and human factors work on posture, force, repetition, anthropometry, and biomechanical fit.
