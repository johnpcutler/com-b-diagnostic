# Physical Opportunity Lenses

This file collects physical-opportunity-oriented lenses for understanding `PO` in COM-B. It treats physical opportunity as the material, temporal, infrastructural, and environmental conditions that make a behavior practically feasible in real work settings.

These lenses overlap. That is fine. The goal is to make `PO` more diagnostically useful without losing the organizing simplicity of COM-B.

Within this repo's COM-B vocabulary:

- `PO` covers time, tools, systems, workflows, and local physical conditions.
- `PO` often interacts with `PC` and `AM` when friction, overload, or poor fit crowd out capable or well-intended behavior.

See [com-b-abbreviations-reference.md](../com-b-bcw-bct/com-b-abbreviations-reference.md) for the shared code system.

## PO-1-WorkSys: Work-System Configuration and Constraints

**Core view of opportunity:** Opportunity is shaped by how person, task, tools, physical setting, and organizational arrangements interact as a local system.

**Use when:** Revealing structural mismatches across the work system that make the target behavior hard to enact even when people are capable and motivated -- especially multi-factor constraints that cannot be explained by a single missing tool or skill.

**Diagnostic question:** Where is the local work system misaligned for this behavior?

**Academic grounding:** Draws on `SEIPS` and work-system/human-factors models, especially Carayon and colleagues, plus sociotechnical systems traditions in ergonomics.

**Dimensions it tends to foreground:**

- **PO.1.1** Work-system coherence: coherent and mutually supportive -> fragmented and conflicting
- **PO.1.2** Tool-task fit: tools match task demands -> tools force workarounds
- **PO.1.3** Process reliability: predictable process -> frequent breakdown and recovery
- **PO.1.4** Local adaptability: local adjustment possible -> brittle, hard-to-adapt setup
- **PO.1.5** Feedback-loop strength: rapid learning loops -> delayed or weak learning loops
- **PO.1.6** Safety-productivity balance: low tradeoff pressure -> chronic tradeoff pressure
- **PO.1.7** Constraint load: manageable constraints -> compounding constraints

#### Pattern guidance

**Refs:** BCW: EN, ER, PE, TR | BCT: 1.2, 2.2, 2.7, 12.1, 12.2, 12.5 | Dims: PC.1.2.1, PO.1.1, PO.1.2, PO.1.5, PO.1.6, PO.2.3, SO.7.5 | Cross: PC-1.2-Models, PO-2-Resource, PO-7-Control, SO-7-Governance

**Primary BCW linkage:** ER and EN. ER addresses system-level misalignment via BCT.12.1 (restructuring the physical environment) and BCT.12.2 (restructuring the social environment) holistically. EN supports local adaptation via BCT.12.5 (adding objects to the environment) and BCT.1.2 (problem solving) to identify which misfits most strongly block the behavior.

**Shaping notes:**
- When PO.1.1 (work-system coherence) is low, multiple elements conflict. ER via BCT.12.1 and BCT.12.2 addressing the system holistically, not individual components. BCT.1.2 (problem solving) to identify which misfits most strongly block the behavior.
- When PO.1.2 (tool-task fit) is poor, tools force workarounds. ER via BCT.12.1 or BCT.12.5 (adding objects) to improve fit. If the tool is fixed, EN to create bridging aids.
- When PO.1.5 (feedback-loop strength) is weak, learning loops are delayed or absent. EN via BCT.2.2 (feedback on behaviour) and BCT.2.7 (feedback on outcomes) to shorten the loop -- see also PO-7-Control.
- When PO.1.6 (safety-productivity balance) shows chronic tradeoff pressure, people cut corners because the system demands it. ER to redesign so safety and productivity are not competing. Don't address this with TR or PE -- the system is the problem.

**Redirecting notes:**
- If SO.7.5 (policy-operational coherence) is poor, work-system redesign may conflict with policy constraints. Address SO-7-Governance.
- If PO.2.3 (slack margin) is zero, there's no capacity to implement system changes. Address PO-2-Resource.
- If PC.1.2.1 (model accuracy) is low, people may misdiagnose which system elements are causing problems. Address PC-1.2-Models to improve system understanding.

## PO-2-Resource: Resource and Capacity Conditions

**Core view of opportunity:** Opportunity depends on whether people have enough time, staffing, material resources, and slack to perform the behavior without sacrificing critical adjacent work.

**Use when:** Revealing scarcity-driven displacement, chronic urgency competition, and hidden capacity ceilings -- especially when endorsed, understood behaviors still fail under real resource pressure.

**Diagnostic question:** Is capacity/scheduling scarcity displacing the behavior?

**Academic grounding:** Draws on workload/capacity and operations-management traditions, including demand-capacity fit, queueing effects, and human-factors workload research.

**Dimensions it tends to foreground:**

- **PO.2.1** Time availability: protected time -> constant time scarcity
- **PO.2.2** Staffing adequacy: adequate coverage -> chronic understaffing
- **PO.2.3** Slack margin: healthy slack -> no slack / constant firefighting
- **PO.2.4** Competing urgency: stable prioritization -> frequent priority collisions
- **PO.2.5** Resource reliability: resources dependable -> frequent resource outages
- **PO.2.6** Variability absorption: variability absorbed -> variability destabilizes flow
- **PO.2.7** Activation overhead: low startup burden -> high startup burden

#### Pattern guidance

**Refs:** BCW: ED, EN, ER, TR | BCT: 1.1, 1.2, 1.4, 7.1, 11.3, 12.1, 12.5 | Dims: AM.2.1.1, PO.1.1, PO.2.1, PO.2.3, PO.2.4, PO.2.6, PO.2.7, SO.4.4 | Cross: AM-2.1-Habit, PO-1-WorkSys, SO-4-Incentives

**Primary BCW linkage:** EN and ER. EN protects capacity via BCT.1.4 (action planning) for time protection and BCT.11.3 (conserving mental resources). ER embeds behavior into existing flows via BCT.12.1 (restructuring the physical environment) to reduce additional demand.

**Shaping notes:**
- When PO.2.1 (time availability) is scarce, behavior is displaced by urgency. EN via BCT.1.4 (action planning) to protect time. ER via BCT.12.1 to embed the behavior into existing routines rather than adding it as separate work.
- When PO.2.4 (competing urgency) is high, frequent priority collisions occur. BCT.1.2 (problem solving) for priority negotiation. BCT.1.1 (goal setting, behavior) to establish non-negotiable minimums.
- When PO.2.7 (activation overhead) is high, high startup burden displaces the behavior. ER via BCT.12.1 and BCT.12.5 (adding objects) to reduce startup cost. BCT.7.1 (prompts/cues) to trigger action before activation overhead builds.
- When PO.2.6 (variability absorption) is low, variability destabilizes flow. EN via BCT.1.2 (problem solving) for contingency planning. ER for buffers and slack in the system.
- Resource scarcity often makes other interventions impractical: if PO.2.1 and PO.2.3 are very low, don't attempt TR programs, lengthy ED interventions, or complex ER redesigns. Start with high-leverage EN that reduces demands.

**Redirecting notes:**
- If SO.4.4 (short-vs-long horizon) pressure dominates, resource allocation is driven by short-term metrics. Address SO-4-Incentives to protect long-term resource allocation.
- If AM.2.1.1 (automaticity) is low for the target behavior, it requires deliberate effort and therefore consumes more resource. Invest in AM-2.1-Habit to reduce resource demand over time.
- If PO.1.1 (work-system coherence) is fundamentally fragmented, adding resources to a broken system produces diminishing returns. Address PO-1-WorkSys.

## PO-3-Workflow: Workflow and Process Architecture

**Core view of opportunity:** Opportunity is created or blocked by process topology: handoffs, dependencies, sequence constraints, queue points, and coordination latency.

**Use when:** Revealing where workflow design adds activation energy, delays, or breakdowns that suppress behavior -- especially operational friction that silently prevents behavior from becoming routine.

**Diagnostic question:** Where do handoffs, dependencies, and queues suppress execution?

**Academic grounding:** Draws on process-engineering and resilience-in-work traditions, plus human-factors work on handoffs, coordination burden, and process reliability.

**Dimensions it tends to foreground:**

- **PO.3.1** Path complexity: simple path -> branching and exception-heavy path
- **PO.3.2** Handoff burden: few clean handoffs -> many fragile handoffs
- **PO.3.3** Dependency depth: shallow dependencies -> deep dependency chain
- **PO.3.4** Queue friction: low wait and rework -> high wait and rework
- **PO.3.5** Sequence rigidity: flexible order -> rigid order with failure cascades
- **PO.3.6** Recovery ease: easy recovery -> recovery is costly and slow
- **PO.3.7** Activation energy: easy to begin -> hard to initiate

#### Pattern guidance

**Refs:** BCW: EN, ER | BCT: 1.2, 1.4, 2.7, 7.1, 12.1, 12.5 | Dims: PC.1.1.3, PO.1.1, PO.3.2, PO.3.4, PO.3.5, PO.3.7, SO.2.7 | Cross: AM-2.1-Habit, PC-1.1-Knowledge, PO-1-WorkSys, PO-4-Visibility, SO-2-Roles

**Primary BCW linkage:** ER and EN. ER simplifies process architecture via BCT.12.1 (restructuring the physical environment). EN reduces friction at key points via BCT.12.5 (adding objects to the environment), BCT.7.1 (prompts/cues), and BCT.1.4 (action planning) for handoff protocols.

**Shaping notes:**
- When PO.3.2 (handoff burden) is high, many fragile handoffs accumulate. ER via BCT.12.1 to simplify handoff points. EN via BCT.7.1 (prompts/cues) at handoff moments. BCT.1.4 (action planning) for explicit handoff protocols.
- When PO.3.7 (activation energy) is high, behavior is hard to initiate. ER to reduce startup steps. BCT.12.5 (adding objects) to pre-stage materials. BCT.7.1 (prompts/cues) at the natural initiation point. This dimension often gates AM-2.1-Habit formation -- if starting is hard, repetition can't build.
- When PO.3.4 (queue friction) is high, wait and rework accumulate. ER to restructure queue points. BCT.2.7 (feedback on outcomes) to make queue costs visible -- crosses into PO-4-Visibility.
- When PO.3.5 (sequence rigidity) is high with failure cascades, EN via BCT.1.2 (problem solving) for alternative sequences. ER to build recoverable branch points.

**Redirecting notes:**
- If SO.2.7 (handback reliability) is poor, workflow improvements will fail at organizational handoff boundaries. Address SO-2-Roles.
- If PO.1.1 (work-system coherence) is fundamentally fragmented, optimizing individual process steps won't help. Address PO-1-WorkSys holistically.
- If PC.1.1.3 (sequence clarity) is vague, people may not execute the workflow correctly even after redesign. Address PC-1.1-Knowledge.

## PO-4-Visibility: Information and State Visibility in the Environment

**Core view of opportunity:** Opportunity depends on whether the environment surfaces the right signals, system states, and consequences at the point of action.

**Use when:** Revealing observability and feedback failures that prevent timely, accurate action -- especially when people fail because critical information is not legible in the environment.

**Diagnostic question:** Are relevant states and consequences visible at point of action?

**Academic grounding:** Draws on situation-awareness and ecological-interface traditions, especially Endsley and related CSE/HFE work on observability and projection.

**Dimensions it tends to foreground:**

- **PO.4.1** Signal surfacing: key signals obvious -> key signals buried
- **PO.4.2** State visibility: system state visible -> state must be inferred
- **PO.4.3** Feedback latency: immediate feedback -> delayed feedback
- **PO.4.4** Feedback diagnosticity: clear meaning -> ambiguous meaning
- **PO.4.5** Projection support: next state anticipatable -> next state hard to foresee
- **PO.4.6** Representation coherence: coherent displays/artifacts -> fragmented representations
- **PO.4.7** Alert quality: useful alerts -> noisy, fatiguing alerts
- **PO.4.8** Cost visibility: overhead costs are visible and tracked -> overhead costs are invisible and tolerated
- **PO.4.9** Friction visibility: friction is visible and discussed -> friction is normalized and invisible

#### Pattern guidance

**Refs:** BCW: EN, ER | BCT: 2.2, 2.4, 2.7, 5.3, 7.1, 12.1, 12.5, 13.2 | Dims: PC.1.4.3, AM.2.3.1, PO.4.1, PO.4.3, PO.4.7, PO.4.8, PO.5.2 | Cross: AM-2.3-Affect, PC-1.4-Signal, PO-5-Tooling, PO-7-Control

**Primary BCW linkage:** ER and EN. ER surfaces information via BCT.12.1 (restructuring the physical environment) and BCT.12.5 (adding objects to the environment) such as dashboards and visual cues. EN shortens feedback loops via BCT.2.2 (feedback on behaviour), BCT.2.7 (feedback on outcomes of behavior), and BCT.7.1 (prompts/cues).

**Shaping notes:**
- When PO.4.1 (signal surfacing) is poor, key signals are buried. ER via BCT.12.5 (adding objects) such as dashboards, status boards, or visual cues. BCT.7.1 (prompts/cues) to surface signals at point of action.
- When PO.4.3 (feedback latency) is high, delayed feedback prevents timely correction. EN via BCT.2.2 (feedback on behaviour) with shortened loop. BCT.2.7 (feedback on outcomes) brought forward in time -- crosses into PO-7-Control.
- When PO.4.8 (cost visibility) is low, overhead costs are invisible and tolerated. BCT.2.4 (self-monitoring of outcomes) to make costs trackable. BCT.5.3 (information about social and environmental consequences) to make hidden costs salient.
- When PO.4.7 (alert quality) is noisy, alert fatigue sets in. ER via BCT.12.1 to reduce false-positive alerts. Fewer, better signals outperform more signals.

**Redirecting notes:**
- If PC.1.4.3 (detection sensitivity) is low, making signals visible won't help if the person can't interpret them. Address PC-1.4-Signal.
- If PO.5.2 (state transparency) is opaque at the tool level, environmental visibility improvements are undermined by tool opacity. Address PO-5-Tooling.
- If AM.2.3.1 (valence) is aversive for the information being surfaced (e.g. bad-news dashboards), people will avoid looking. Address AM-2.3-Affect or use BCT.13.2 (framing/reframing) to make the information less threatening.

## PO-5-Tooling: Tooling and Interface Affordances

**Core view of opportunity:** Opportunity is shaped by whether tools and interfaces make the desired behavior easy, reliable, and recoverable in context of use.

**Use when:** Revealing friction, mode confusion, brittleness, and usability debt that suppress desired behavior -- especially when well-intended users avoid or abandon behaviors because the interface makes them costly.

**Diagnostic question:** Do tools make the behavior easy and recoverable in context?

**Academic grounding:** Draws on HCI/usability and affordance traditions, including Norman, `ISO 9241-11`, and human-centered design in context of use.

**Dimensions it tends to foreground:**

- **PO.5.1** Affordance clarity: obvious action possibilities -> unclear action possibilities
- **PO.5.2** State transparency: visible mode/status -> opaque mode/status
- **PO.5.3** Core-path efficiency: efficient frequent path -> high interaction overhead
- **PO.5.4** Error tolerance: easy recovery -> brittle failure paths
- **PO.5.5** Consistency: predictable interaction patterns -> inconsistent patterns
- **PO.5.6** Learnability in context: low onboarding burden -> high onboarding burden
- **PO.5.7** Automation fit: automation supports work -> automation adds new friction

#### Pattern guidance

**Refs:** BCW: EN, ER, TR | BCT: 4.1, 6.1, 7.1, 8.7, 12.1, 12.5 | Dims: PC.1.2.1, PO.1.2, PO.2.1, PO.5.1, PO.5.4, PO.5.6, PO.5.7 | Cross: PC-1.2-Models, PO-1-WorkSys, PO-2-Resource

**Primary BCW linkage:** ER and EN. ER redesigns interfaces via BCT.12.1 (restructuring the physical environment) and BCT.12.5 (adding objects to the environment). EN bridges usability gaps via BCT.4.1 (instruction on how to perform a behavior) and BCT.7.1 (prompts/cues).

**Shaping notes:**
- When PO.5.1 (affordance clarity) is low, action possibilities are unclear. ER via BCT.12.1 to redesign the interface for clearer affordances. EN via BCT.7.1 (prompts/cues) and BCT.4.1 (instruction) as bridging measures.
- When PO.5.4 (error tolerance) is low, brittle failure paths discourage use. ER to add undo, confirmation, and recovery mechanisms. BCT.12.5 (adding objects) for safety nets.
- When PO.5.6 (learnability in context) is high burden, tools are hard to learn. TR via BCT.8.7 (graded tasks) and BCT.6.1 (demonstration). EN via BCT.12.5 (adding objects) such as inline help or guided workflows.
- When PO.5.7 (automation fit) is poor, automation adds friction. ER to reconfigure automation boundaries. The fix is not training people to work around bad automation -- it's redesigning the automation.

**Redirecting notes:**
- If PO.1.2 (tool-task fit) is fundamentally poor, patching the interface won't help when the tool is wrong for the task. Address PO-1-WorkSys tool selection.
- If PC.1.2.1 (model accuracy) is low, people may misuse well-designed tools because they misunderstand the system. Address PC-1.2-Models.
- If PO.2.1 (time availability) is scarce, people will use the fastest path regardless of good design. Address PO-2-Resource.

## PO-6-PhysEnv: Physical Environment and Ergonomic Conditions

**Core view of opportunity:** Opportunity depends on whether the physical setting supports safe, sustainable, and efficient execution.

**Use when:** Revealing environmental strain, sensory load, and layout barriers that reduce feasible performance -- especially local constraints that make behavior physically inconvenient or unsafe.

**Diagnostic question:** Does the physical setting support sustainable execution?

**Academic grounding:** Draws on physical ergonomics and occupational human-factors traditions focused on posture, reach, lighting, noise, layout, and environmental stressors.

**Dimensions it tends to foreground:**

- **PO.6.1** Layout support: layout enables flow -> layout creates detours and delays
- **PO.6.2** Space adequacy: sufficient workspace/access -> constrained workspace/access
- **PO.6.3** Sensory load: manageable sensory conditions -> distracting/fatiguing conditions
- **PO.6.4** Posture and reach demand: neutral demand -> awkward demand
- **PO.6.5** Mobility burden: low searching/movement burden -> high searching/movement burden
- **PO.6.6** Environmental hazard load: low exposure -> persistent hazard exposure
- **PO.6.7** Physical comfort sustainability: sustainable comfort -> accumulating discomfort

#### Pattern guidance

**Refs:** BCW: EN, ER | BCT: 1.4, 12.1, 12.5, 12.6 | Dims: PHC.2.5.1, PO.2.1, PO.6.1, PO.6.3, PO.6.5, PO.6.7, SO.4.4 | Cross: PHC-2.5-Ergo, PO-2-Resource, SO-4-Incentives

**Primary BCW linkage:** ER and EN. ER redesigns the physical setting via BCT.12.1 (restructuring the physical environment) for layout, lighting, noise, and access. EN augments via BCT.12.5 (adding objects to the environment) and BCT.12.6 (body changes) for conditioning or equipment.

**Shaping notes:**
- When PO.6.1 (layout support) creates detours and delays, ER via BCT.12.1 to redesign layout for flow.
- When PO.6.3 (sensory load) is high with distracting or fatiguing conditions, ER via BCT.12.1 to reduce noise, improve lighting, or control temperature. BCT.12.5 (adding objects) such as noise-cancelling equipment or task lighting.
- When PO.6.5 (mobility burden) is high with excessive movement, ER via BCT.12.1 to co-locate frequently used items. BCT.12.5 (adding objects) to bring materials to point of use.
- When PO.6.7 (physical comfort sustainability) is low, accumulating discomfort degrades performance over time. ER via BCT.12.1 for better seating, workstation height, or climate. BCT.1.4 (action planning) for rest intervals.

**Redirecting notes:**
- If PHC.2.5.1 (posture demand) is driven by the environment, fix the environment (PO) before attributing the problem to the body (PHC). PO-6-PhysEnv and PHC-2.5-Ergo often need to be addressed together.
- If PO.2.1 (time availability) is scarce, environmental improvements get deprioritized. Address PO-2-Resource to create capacity for change.
- If SO.4.4 (short-vs-long horizon) pressure dominates, environmental investment (long-term payoff) loses to short-term targets. Realign SO-4-Incentives.

## PO-7-Control: Control Loops and Adaptive Regulation (Cybernetics)

**Core view of opportunity:** Opportunity depends on whether the system has usable feedback loops, effective control actions, and sufficient damping to self-correct under disturbance.

**Use when:** Revealing delay, oscillation, and over/under-correction dynamics that keep behavior unstable even when tools and intent exist -- especially when enough resources exist but control architecture and adaptation loops still fail.

**Diagnostic question:** Can the system sense, decide, and correct fast enough to stay stable?

**Academic grounding:** Draws on cybernetics and control traditions, especially Wiener, Ashby, and later systems-dynamics and sociotechnical control-loop work.

**Dimensions it tends to foreground:**

- **PO.7.1** Feedback latency: short loop delay -> long loop delay
- **PO.7.2** Signal fidelity: accurate control signal -> noisy/misaligned signal
- **PO.7.3** Corrective authority: actors can correct locally -> correction requires slow escalation
- **PO.7.4** Loop closure quality: actions close loops -> actions fail to close loops
- **PO.7.5** Damping quality: stable correction -> oscillation and over-correction
- **PO.7.6** Disturbance handling: disturbances absorbed -> disturbances destabilize performance
- **PO.7.7** Variety handling: control responses match variability -> variability exceeds control capacity

#### Pattern guidance

**Refs:** BCW: EN, ER | BCT: 2.2, 2.7, 4.1, 12.1, 12.2 | Dims: PC.1.3.6, PO.4.2, PO.7.1, PO.7.3, PO.7.5, PO.7.7, SO.7.1 | Cross: PC-1.3-Judgment, PO-4-Visibility, SO-7-Governance

**Primary BCW linkage:** ER and EN. ER restructures control architecture via BCT.12.1 (restructuring the physical environment) and BCT.12.2 (restructuring the social environment) for faster loops and local authority. EN improves loop quality via BCT.2.2 (feedback on behaviour) and BCT.2.7 (feedback on outcomes of behavior).

**Shaping notes:**
- When PO.7.1 (feedback latency) is long, delayed loops prevent timely correction. EN via BCT.2.2 (feedback on behaviour) with shortened cycle. ER to restructure information flow for faster sensing.
- When PO.7.5 (damping quality) is poor with oscillation and over-correction, ER to add damping mechanisms (e.g. decision thresholds, response delays for non-emergencies). BCT.4.1 (instruction on how to perform a behavior) on proportional response.
- When PO.7.7 (variety handling) is exceeded, variability exceeds control capacity. EN to add response options (Ashby's law of requisite variety). ER to reduce incoming variability where possible. Don't try to control what can't be controlled -- increase the system's adaptive range.
- When PO.7.3 (corrective authority) requires slow escalation, actors can't correct locally. ER via BCT.12.2 (restructuring social environment) to push authority to the point of action -- crosses into SO-7-Governance.

**Redirecting notes:**
- If PO.4.2 (state visibility) is poor, the control loop lacks input. Address PO-4-Visibility before tuning the control mechanism.
- If SO.7.1 (local autonomy fit) is low, control loops stall because actors lack authority to act. Address SO-7-Governance.
- If PC.1.3.6 (time-pressure competence) is low, fast control loops overwhelm the decision-maker. Address PC-1.3-Judgment or slow the loop to match human capacity.

## From Physical Opportunity Lenses To COM-B / BCW

These lenses do not replace COM-B. They help specify what kind of `PO` problem is inside the broad `Opportunity` branch.

- Most of these lenses primarily refine `PO`.
- Secondary effects often appear in `PC` (when friction blocks practice) and `AM` (when high activation energy prevents initiation).

Once dominant physical-opportunity patterns are clearer, the next step is usually to move into [com-b-to-bcw-intervention-function-mapping.md](../com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md):

- `PO` is most often paired with `RE`, `ER`, and `EN`.
- In some cases, paired `TR` helps when environmental redesign and capability-building must be coordinated.

The goal is not to duplicate that mapping here, but to make it easier to move from physical-opportunity diagnosis to intervention family.

## Boundaries of this file

This note is intentionally physical-opportunity-first. It does not fully address:

- social permission, norms, incentives, and political safety
- identity, value, and other motivation dynamics
- internal cognitive skill, judgment, and mental-model capability

Those belong more naturally in adjacent notes such as [social-opportunity-lenses.md](social-opportunity-lenses.md), [motivation-lenses.md](motivation-lenses.md), and [capability-lenses.md](capability-lenses.md).

Read next:
- [social-opportunity-lenses.md](social-opportunity-lenses.md) for `SO` conditions
- [capability-lenses.md](capability-lenses.md) for `PC` and `PHC`
- [com-b-to-bcw-intervention-function-mapping.md](../com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md) for BCW intervention families

## References To Ground These Lenses

- **COM-B and BCW:** Michie, van Stralen, and West on COM-B and the Behaviour Change Wheel.
- **Work-System Configuration and Constraints:** Carayon et al. on `SEIPS`; sociotechnical systems and macroergonomics traditions.
- **Resource and Capacity Conditions:** workload and demand-capacity fit traditions in HFE; queueing and flow management traditions in operations.
- **Workflow and Process Architecture:** process reliability and resilience-in-work traditions; handoff and interdependence work in safety-critical domains.
- **Information and State Visibility in the Environment:** Endsley on situation awareness; CSE/ecological-interface traditions on observability and projection.
- **Tooling and Interface Affordances:** Norman on affordances and design; `ISO 9241-11` on usability in context.
- **Physical Environment and Ergonomic Conditions:** physical ergonomics and occupational human-factors traditions on layout, posture, reach, noise, lighting, and hazard exposure.
- **Control Loops and Adaptive Regulation (Cybernetics):** Wiener on cybernetics; Ashby on requisite variety; control-loop and systems-dynamics traditions for delay, damping, and stability.
