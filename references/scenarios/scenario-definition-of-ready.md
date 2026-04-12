# Scenario: "What does 'ready for dev' actually mean?"

This narrative follows the canonical pipeline in [`flow.md`](../flow.md). The fenced block below is the **digest**: a code-like summary of outputs for steps 1–6.

```
state      = S7: Contested / Undefined
blockers   = PC* RM* | SO                                 (* = primary)
lenses.PC  = [1.2.2 causal-understanding, 1.6.1-1.6.4 shared-representations,
              1.5.1 calibration, 1.1.1-1.1.3 declarative/procedural/sequence]
lenses.SO  = [2.1-2.2 ownership+decision-rights, 4.1-4.4 incentive-structure,
              5.3 identity-safety, 6.6 status-asymmetry]
lenses.PO  = [3.7 activation-energy, 5.1-5.2 tooling-affordance, 4.3 feedback-latency]
lenses.RM  = [1.4.1-1.4.4 identity-framing, 1.3.1-1.3.3 expectancy+value-cost]
functions  = ED >> ER > MO > EN > PE
bcts       = ED→4.2,4.1 | ER→12.1,12.2 | MO→6.1 | PE→13.2,9.2 | EN→1.2
phases     = [wk1-2] ED → [wk3-6] ER+EN → [wk7+] MO+PE+feedback
```

## The situation

A mid-size product organization runs four cross-functional teams, each composed of a product manager, a designer, and a squad of engineers. The teams operate in two-week sprints with a shared sprint planning cadence. Almost every planning session derails into the same argument: is this story "ready for dev"? The PM presents a user story with acceptance criteria and considers it ready. The lead engineer pushes back — where's the technical design? What about the API contract? Have edge cases been documented? The designer interjects — the user flow isn't finalized, and the interaction states haven't been reviewed. Each role brings a different implicit checklist to the table, and each believes their version is the obvious, correct one.

The pattern recurs every sprint, across all four teams. Two of the teams have attempted written "definitions of ready" in the past. One team produced a twelve-item checklist that became stale within a month — nobody updates it, nobody reads it, and when someone does cite it, the response is "that doesn't apply to this kind of story." The other team wrote a three-bullet definition so vague ("story is well-understood, design is sufficient, technical approach is clear") that it resolved nothing; every word in the definition is itself contested. The word "ready" has become a floating signifier — it means different things to each role, and everyone uses it as if it has a single, shared meaning.

The downstream consequences are significant. Stories enter sprints underspecified, leading to mid-sprint scope negotiations, blocked engineers waiting on design decisions, rework when technical constraints surface late, and a growing sense of frustration across roles. PMs feel engineers are being obstructionist. Engineers feel PMs are being reckless. Designers feel excluded from the conversation entirely. The same argument absorbs hours of meeting time every two weeks, and the emotional residue persists between sprints.

## Step 1: Classify the behavior state

Referencing the diagnostic cycle in [../com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md](../com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md), this situation maps to **State 7: Contested / Undefined** — "No shared definition; conceptual ambiguity."

The defining characteristics of this state are present in full:

- **Fundamental definitional ambiguity.** There is no agreement on what "ready" actually contains. It is not a disagreement about how to execute a known standard — it is a disagreement about what the standard even is.
- **Competing framings.** PMs frame readiness as problem clarity ("Is the user need well-articulated?"). Engineers frame it as solution clarity ("Is the implementation path unambiguous?"). Designers frame it as experience coherence ("Is the user journey reviewable?"). These are three distinct framings of the same word.
- **No shared language.** The components of readiness — risk assessment, technical feasibility, design completeness, scope boundaries — are not named or structured in a way that all three roles can reference. People talk past each other using the same vocabulary.
- **Same words, different meanings.** "Acceptance criteria," "design complete," and "technically feasible" all carry role-specific definitions that are never surfaced or reconciled.
- **Meetings derail into definitional debates.** Sprint planning becomes a recurring forum for re-litigating the meaning of readiness rather than evaluating specific stories against a stable standard.
- **Extremely high cognitive load.** Every sprint planning session requires each participant to re-negotiate the frame from scratch. There is no shared conceptual infrastructure to build on.
- **Alignment is impossible because the conceptual object is unstable.** You cannot align on whether a story meets a definition when the definition itself shifts depending on who is speaking.

This is not a State 3 (Partially Realized / Inconsistent) situation, because the issue is not that different teams execute a known practice differently. It is that the practice itself has no shared conceptual foundation. The object of alignment does not yet exist in a stable, shared form.

## Step 2: Identify COM-B blockers

Referencing [../com-b-bcw-bct/com-b-behavior-states-primary-secondary-blockers.md](../com-b-bcw-bct/com-b-behavior-states-primary-secondary-blockers.md), State 7 (Contested / Undefined) identifies the following blocker profile, which maps precisely to this scenario:

### Primary blockers

- **PC: Mental-model divergence.** Each role holds a different internal model of what "ready" requires, shaped by their own downstream needs. The PM's model is built around problem-space clarity because ambiguity in the user need creates wasted effort. The engineer's model is built around solution-space clarity because ambiguity in the technical approach creates rework and bugs. The designer's model is built around experience-space coherence because ambiguity in the user journey creates inconsistent interactions. Each model is internally valid — and mutually incompatible with the others when presented as "the" definition. The divergence is not about carelessness; it is about different causal models of what predicts successful sprint execution.

- **PC: No shared language.** The word "ready" is used as though it has a single referent, but it does not. There is no shared vocabulary for naming the distinct dimensions of readiness — problem clarity, technical feasibility, design completeness, risk tolerance, scope boundaries. Without named dimensions, every conversation collapses into a monolithic yes/no debate ("Is it ready or not?") rather than a dimensional assessment ("Which aspects are clear and which are uncertain?").

- **RM: Identity attachment to competing definitions.** PMs identify professionally with momentum and customer focus — their implicit value is "don't over-specify, move fast, stay close to the user." Engineers identify with rigor and reliability — their implicit value is "reduce ambiguity before committing, protect quality." Designers identify with user experience coherence — their implicit value is "don't ship fragmented journeys." Each definition of "ready" is an expression of professional identity. Challenging someone's definition feels like challenging their professional values. Convergence requires identity flexibility that feels threatening.

### Secondary blockers

- **SO: Semantic drift.** Even when a team reaches a temporary agreement on what "ready" means, the definition drifts within weeks. New story types surface that don't fit the template. People revert to their default mental models under time pressure. Without reinforcing structures, any agreed-upon definition is unstable.

- **SO: Turf battles.** Defining "ready" is implicitly about defining who has authority over the sprint boundary. If the PM's definition wins, PMs control when work enters the sprint. If the engineering definition wins, engineers have veto power. The conversation is not purely about quality — it is about workflow governance and decision rights. Whoever's definition prevails controls the gate.

- **PC: Cognitive overload.** The ambiguity itself imposes overhead. Every sprint planning is a fresh negotiation conducted without stable reference points. Participants must hold their own definition, infer others' definitions, argue for their position, and evaluate stories simultaneously. The cognitive load of the conversation is much higher than it would be if a shared framework existed.

## Step 3: Deepen with lenses

*Dimensional IDs: [../lenses/capability-lenses.md](../lenses/capability-lenses.md) `x.y.z` (PC); [../lenses/social-opportunity-lenses.md](../lenses/social-opportunity-lenses.md) `n.m` (SO); [../lenses/physical-opportunity-lenses.md](../lenses/physical-opportunity-lenses.md) `n.m` (PO); [../lenses/motivation-lenses.md](../lenses/motivation-lenses.md) `x.y.z` (RM).*

### Capability lenses ([../lenses/capability-lenses.md](../lenses/capability-lenses.md))

**1.2 Mental Models / Situation Models** — *PC **1.2.2**, **1.2.3** (causal / structural understanding).* This lens asks whether people hold a workable internal model of how the system or situation operates. In this scenario, each role holds a different causal model of what predicts sprint success:

- PMs model readiness as "Is the problem clear enough to start?" Their causal chain: clear user need → focused engineering effort → valuable delivery. Under-specification of the problem is the risk they optimize against.
- Engineers model readiness as "Is the solution clear enough to build?" Their causal chain: clear technical approach → predictable implementation → low rework. Under-specification of the solution is the risk they optimize against.
- Designers model readiness as "Is the user journey clear enough to evaluate?" Their causal chain: coherent experience design → consistent interactions → user satisfaction. Under-specification of the experience is the risk they optimize against.

Each model is internally coherent — the problem is that all three are correct for their respective risk domains, but each is incomplete. No single role's causal model captures the full set of antecedent conditions for successful sprint execution. The mental-model divergence is not a knowledge deficit; it is a framing conflict between valid but partial situation models.

**1.6 Shared Representations and Conceptual Alignment** — *PC **1.6.1**–**1.6.7** (shared language through cross-role interpretability).* This is the central diagnostic lens for this scenario. Evaluating its dimensions:

- *Shared language:* near zero. The word "ready" carries different conceptual loads for each role. There is no shared vocabulary for readiness dimensions.
- *Conceptual alignment:* low. The concept of "readiness" is not a shared object — it is three overlapping but distinct objects wearing the same name.
- *Representation compatibility:* fragmented. Each role's mental checklist is an internal representation that does not travel well across role boundaries. A PM's "acceptance criteria" is not readable as a completeness check by an engineer; an engineer's "technical design" is not parseable as a readiness signal by a designer.
- *Common ground:* weak. Mutual understanding of what the other roles need from a "ready" story is low. Each role assumes their needs are obvious and shared.
- *Definition stability:* very low. Even when a team agrees on a definition, it drifts within weeks because the underlying mental models have not converged. The definition is a surface agreement without deep conceptual alignment.
- *Cross-role interpretability:* poor. Representations created by one role (e.g., a PM's user story, an engineer's technical spike, a designer's prototype) do not function as shared readiness signals across all three roles.

**1.5 Metacognition and Calibration** — *PC **1.5.1**, **1.5.5** (calibration / uncertainty awareness).* People do not realize that their definition of "ready" is one of several valid framings. Each role believes their version is "obviously correct" — a calibration failure. The PM does not think "my definition prioritizes problem clarity because that's my role-shaped perspective." They think "this is what ready means." The metacognitive insight that "my definition of ready is role-shaped, not universal" is missing. This is overconfidence in one's own framing, combined with poor monitoring of the framing itself.

**1.1 Declarative and Procedural Knowledge** — *PC **1.1.1**–**1.1.3** (cross-role procedural picture of readiness).* There is a secondary knowledge gap about what a well-structured, multi-perspective readiness assessment actually contains. Most participants have never seen or used a readiness framework that explicitly names dimensions from all three perspectives. Their procedural knowledge is limited to their own role's checklist. They lack declarative knowledge about how other roles' readiness criteria connect to sprint outcomes.

### Social opportunity lenses ([../lenses/social-opportunity-lenses.md](../lenses/social-opportunity-lenses.md))

**2. Roles, Authority, and Boundary Clarity** — *SO **2.1**, **2.2** (ownership / decision-right clarity).* The "ready" boundary is fundamentally a jurisdiction question. Who decides when a story crosses the threshold from "not ready" to "ready for sprint"? Ownership is ambiguous. When a PM says "ready" and engineering says "not ready," there is no clear arbitration mechanism. The decision right is contested, not because it hasn't been assigned, but because the assignment would require resolving the definitional conflict first — and that is the very thing the team cannot do. The readiness gate sits at the intersection of three role boundaries, and no one has explicit authority over the intersection.

**4. Incentives, Accountability, and Reinforcement Architecture** — *SO **4.1**, **4.3**, **4.4** (reward alignment / accountability / horizon).* The incentive structures create a structural disagreement that is independent of individual intentions:

- PMs are implicitly rewarded for getting stories into sprints — throughput, velocity, feature delivery, and stakeholder responsiveness all incentivize moving work forward.
- Engineers are implicitly penalized for starting unclear work — rework, bugs, missed estimates, and quality incidents are attributed to engineering even when they originate from upstream ambiguity.
- Designers are often measured on user experience quality outcomes that require upstream clarity they do not control.

The PM's incentive is to push the readiness boundary earlier; engineering's incentive is to push it later; design's incentive is to push for more specificity in a dimension neither PM nor engineering prioritizes. These are not personality conflicts — they are rational responses to misaligned reinforcement structures.

**5. Legitimacy, Meaning, and Identity Safety** — *SO **5.3**, **5.4** (identity safety / reputational risk).* Challenging someone's definition of "ready" can feel like challenging their competence. A PM told "this isn't ready" may hear "you didn't do your job." An engineer who demands more specificity may be perceived as obstructing progress or being "too slow." A designer who raises user-flow concerns may be seen as adding unnecessary process. The conversation is identity-loaded: each pushback carries an implicit judgment about role performance. This makes the negotiation emotionally expensive and incentivizes avoidance or capitulation rather than genuine convergence.

**6. Power, Politics, and Psychological Safety** — *SO **6.6** (status asymmetry).* In teams where PM has higher organizational status or closer access to leadership, the PM's definition tends to win by default — stories enter the sprint under-specified, and engineers absorb the rework cost silently. In teams where engineering has higher status, the engineering definition prevails — PMs feel blocked and escalate stories as "engineering is being slow." The "correct" definition of ready in any given team is often a power outcome rather than a quality outcome. Psychological safety to name this dynamic is low, because naming it requires challenging the implicit authority structure.

### Physical opportunity lenses ([../lenses/physical-opportunity-lenses.md](../lenses/physical-opportunity-lenses.md))

PO is not a primary blocker in this scenario — the problem is conceptual, not environmental. But the PO lenses reveal how the physical environment perpetuates the definitional conflict.

**3. Workflow and Process Architecture** — *PO **3.7** (activation energy — no readiness step).* The sprint planning workflow has no structural support for a multi-perspective readiness assessment. The ceremony is a single meeting where stories are discussed sequentially, with no structured step for evaluating readiness across dimensions. There is no readiness gate in the workflow — stories move from "backlog" to "committed" in a single decision that collapses all readiness dimensions into a single yes/no. The absence of a structured readiness step means that every sprint planning is a fresh negotiation with no process scaffolding. The activation energy for a productive readiness conversation is high because the workflow provides no support for it.

**5. Tooling and Interface Affordances** — *PO **5.1**, **5.2** (affordance / state transparency — ticket lacks readiness dimensions).* The ticket tool (Jira, Linear, etc.) does not encode readiness dimensions. A ticket has fields for assignee, story points, acceptance criteria, and labels — but no structured field for technical design status, design review status, or risk assessment. The tool treats "ready" as an implicit property rather than an explicit, multi-dimensional assessment. This means the tool cannot scaffold the readiness conversation, cannot enforce a multi-perspective review, and cannot track readiness trends over time. The absence of tooling support forces the entire readiness assessment into verbal negotiation, which is exactly where the definitional conflict lives.

**4. Information and State Visibility** — *PO **4.3** (feedback latency — rework signal not at planning).* The consequences of entering a sprint with under-specified stories are not visible at the point of the readiness decision. Rework rates, mid-sprint scope changes, and blocked time are tracked (if at all) in retrospectives, not in sprint planning. The feedback loop between "this story wasn't ready" and "we should have caught that" is delayed by two weeks. Engineers experience the downstream cost but PMs may not see it directly. The information that would resolve the definitional conflict — data showing which readiness gaps predict which sprint problems — is not surfaced at the moment when the readiness decision is made.

### Motivation lenses ([../lenses/motivation-lenses.md](../lenses/motivation-lenses.md))

**1.4 Identity-Based Motivation** — *RM **1.4.1**, **1.4.3** (congruence / identity conflict).* Each role's definition of "ready" is identity-congruent. Asking a PM to add technical design documentation feels like asking them to be an engineer — it conflicts with their identity as a customer-focused problem framer. Asking an engineer to accept vague requirements feels like asking them to abandon professional rigor — it conflicts with their identity as a quality-focused builder. Asking a designer to accept that user flows can be "figured out during the sprint" feels like asking them to accept fragmented experience design — it conflicts with their identity as a user advocate. The behavior change required (converging on a shared, multi-perspective definition) demands identity flexibility that each role experiences as threatening. The difficulty is interpreted as a signal of identity mismatch rather than as a meaningful challenge worth engaging.

**1.3 Expectancy-Value-Cost** — *RM **1.3.1**, **1.3.5**, **1.3.6** (expectancy / effort & emotional cost of convergence).* The expected cost of negotiating a shared definition is high: difficult cross-role conversations, identity threat, significant time investment, and the discomfort of acknowledging that one's own definition is partial. The perceived value is uncertain — "We've tried written checklists before and they didn't stick." Past failures with definitions of ready have trained the teams to expect low returns from definitional work. Expectancy of success is low: people believe this is an unsolvable personality or culture problem rather than a solvable framing problem. The cost-to-expected-value ratio discourages investment in convergence.

## Step 4: Map to intervention functions

Referencing [../com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md](../com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md), the COM-B blockers map to the following intervention functions:

From COM-B blockers:
- PC → ED, TR, EN
- RM → ED, PE, INC, COE
- SO → RE, ER, MO, EN

### Priority functions

1. **ED (Education)** — Make the mental-model divergence visible so people can see that this is a framing problem, not a competence problem. The goal is not to teach people "what readiness is" but to help them see that they are each holding a valid partial model, and that the divergence itself is the problem. ED here means surfacing assumptions, not lecturing.

2. **ER (Environmental Restructuring)** — Restructure the sprint boundary to encode a shared multi-perspective definition into the workflow itself. Replace the implicit, contested gate with an explicit, structured readiness conversation that makes all three perspectives visible by design. Change the environment so that convergence is the path of least resistance.

3. **MO (Modelling)** — Show exemplars of teams that have working, multi-perspective definitions of ready. Demonstrate that this problem is solvable and that the solution looks like collaborative sensemaking, not one role winning the definitional battle.

4. **EN (Enablement)** — Provide a convergence process that goes beyond a document. A facilitated workshop, a structured readiness conversation format, and an embedded artifact that scaffolds the new behavior. Remove the barrier of "we don't know how to have this conversation productively."

5. **PE (Persuasion)** — Reframe "ready" from a gatekeeping mechanism (binary pass/fail, one role's checklist) to a shared risk conversation (what's clear, what's uncertain, what's the plan for managing uncertainty). Shift the emotional valence of the readiness discussion from adversarial to collaborative.

## Step 5: Select BCTs

Referencing the full taxonomy in [../com-b-bcw-bct/bct-taxonomy.md](../com-b-bcw-bct/bct-taxonomy.md):

### Via ED → Grouping 4 (Shaping Knowledge)

- **4.2 Information about antecedents.** Help teams identify what conditions reliably predict successful sprint execution versus mid-sprint rework. Present data linking specific readiness gaps (missing technical design, unfinished user flow, vague acceptance criteria) to specific downstream problems (blocked engineers, scope creep, late design changes). Make the antecedent pattern visible: "When stories enter the sprint without X, Y tends to happen." This shifts the conversation from opinion-based ("I think we need more detail") to evidence-based ("Stories missing technical approach had 3x the rework rate").

- **4.1 Instruction on how to perform a behavior.** Teach a structured "readiness conversation" format that surfaces each role's needs without defaulting to a single perspective. This is procedural knowledge: how to run a 10-minute multi-perspective readiness review, how to name dimensions rather than argue about a monolithic yes/no, how to distinguish "clear," "uncertain but manageable," and "blocking" across different readiness dimensions.

### Via ER → Grouping 12 (Antecedents)

- **12.1 Restructuring the physical environment.** Create a shared readiness artifact — not a flat checklist but a multi-perspective canvas with named dimensions (problem clarity, technical approach, design completeness, risk assessment, scope boundaries) — and embed it in the sprint planning workflow. The artifact becomes part of the ticket template, making the multi-perspective assessment the default path rather than an optional add-on.

- **12.2 Restructuring the social environment.** Change who participates in the readiness decision and how. Establish PM, lead engineer, and designer as co-owners of the "ready" assessment, with each responsible for evaluating their domain's dimensions. The social structure of the decision shifts from adversarial (one role asserts, another challenges) to collaborative (three roles each contribute their perspective to a shared view).

### Via MO → Grouping 6 (Comparison of Behaviour)

- **6.1 Demonstration of the behavior.** Invite a team that has a working definition-of-ready practice — ideally from within the organization or a peer company — to present their process and their artifact. Show what a productive readiness conversation looks like in practice: how long it takes, what the artifact looks like, how disagreements are surfaced and resolved, what the sprint outcomes look like. Demonstration is more powerful than description for a practice that people have only experienced as dysfunctional.

### Via PE → Grouping 13 (Identity) and Grouping 9 (Comparison of Outcomes)

- **13.2 Framing/reframing.** Reframe "ready" from a gate (binary pass/fail, one role's standard imposed on others) to a risk conversation (what's clear, what's uncertain, what's the plan for handling uncertainty). This reframe changes the emotional structure of the discussion: a gate creates winners and losers; a risk conversation creates shared ownership of uncertainty. It also resolves the identity threat — no one's definition "loses" because the frame is no longer "whose checklist wins" but "what do we collectively know and not know."

- **9.2 Pros and cons.** Facilitate a structured exercise: what happens when we start work that isn't ready (rework, blocked engineers, mid-sprint scope changes, frustrated designers) versus what happens when we over-specify (slow throughput, stale requirements, wasted documentation effort). Make the tradeoff explicit and shared rather than implicit and role-specific. Both sides of the tradeoff are real — the goal is to find the right balance collaboratively, not to prove one side wrong.

### Via EN → Grouping 1 (Goals and Planning)

- **1.2 Problem solving.** Run a facilitated session where the team maps their actual rework patterns back to specific readiness gaps. Analyze the last 8-10 sprints: which stories caused the most rework, what was missing at sprint entry, what would have changed if that information had been surfaced earlier? Generate solutions collaboratively from the evidence rather than from abstract principles. This grounds the readiness definition in the team's own experience rather than imposing an external standard.

## Step 6: Intervention design

### Tool and design levers

- **PC → Clarification, Sensemaking Support.** Multi-perspective readiness canvas embedded in the ticket template. Each role's readiness dimensions are visible as named sections (not a single flat checklist). The canvas makes the multi-perspective structure of readiness visible and navigable. When a PM fills out "Problem Clarity" and an engineer fills out "Technical Approach," the structure itself teaches the team that readiness is multi-dimensional.

- **PC → Cognitive Offloading, Error Reduction.** Required fields in the ticket tool that surface specific readiness dimensions before a story can be committed to a sprint. Constraint-based inputs that prevent the "is it ready?" question from collapsing into a monolithic yes/no. The tool enforces dimensionality: you cannot mark a story "ready" without explicitly assessing each dimension, even if that assessment is "uncertain — plan: [X]."

- **SO → Shared Visibility, Depoliticization.** A shared "readiness score" or readiness map visible to all roles, showing which dimensions are assessed as clear, which are flagged as uncertain, and which are gaps. This depoliticizes the conversation: the artifact shows the state of readiness across all dimensions neutrally, rather than one role asserting and another challenging. The discussion moves from "Is it ready?" to "What does the readiness map show?"

- **RM → Feedback Loops, Persuasion.** Before/after metrics tracking the relationship between readiness scores at sprint entry and sprint outcomes (rework rate, mid-sprint scope changes, blocked time, velocity stability). This creates an evidence-based feedback loop: teams can see that stories with high readiness scores across all dimensions have measurably better outcomes. The data does the persuasion work, reducing reliance on authority or assertion.

### Phase 1: Surface the divergence (weeks 1-2)

**Focus: ED — make the problem visible before trying to solve it.**

- Run a "mental model mapping" workshop with all four teams. Each role independently writes their top 5 criteria for "ready for dev" on separate cards. Then the teams compare across roles: where do they overlap? Where do they diverge? The visual comparison makes the mental-model divergence undeniable and depersonalizes it — the divergence is a structural fact, not anyone's fault. (4.2 Information about antecedents, ED)

- Present sprint rework data from the past quarter. Categorize rework by root cause: missing technical design, unclear acceptance criteria, unfinished user flow, late-surfacing edge cases, scope ambiguity. Show how much time was spent on "stories that entered the sprint with specific readiness gaps." Connect specific gaps to specific downstream costs. (5.3 Information about social and environmental consequences, ED)

- Deliver the core reframe in the workshop debrief: "We don't have a readiness problem — we have an alignment problem. Each of your definitions is valid for your role. The issue is that we don't have a definition that integrates all three perspectives. We're going to build one together." (13.2 Framing/reframing, PE)

### Phase 2: Build the shared artifact (weeks 3-6)

**Focus: ER, EN — create a convergence structure.**

- Co-create a multi-perspective readiness canvas in a facilitated workshop with representatives from all three roles across the four teams. The canvas names 5-7 readiness dimensions drawn from the mental-model mapping exercise (e.g., Problem Clarity, Technical Approach, Design Completeness, Edge Cases and Risks, Scope Boundaries, Dependencies). Each dimension has a simple rubric: Clear / Uncertain-with-plan / Blocking. The canvas is a conversation scaffold, not a compliance checklist. (12.1 Restructuring the physical environment, 1.2 Problem solving, ER/EN)

- Embed the canvas in the ticket tool as a structured template. Every story entering sprint consideration gets a readiness canvas. The tool enforces the multi-perspective structure without requiring anyone to remember it. Required fields make dimensionality the default, not an afterthought. (12.1 Restructuring the physical environment, ER)

- Define the "readiness conversation" format: a 10-minute structured review of each story's canvas before sprint commitment. PM speaks to problem clarity and scope. Engineer speaks to technical approach, edge cases, and dependencies. Designer speaks to design completeness and user flow. The conversation is structured by the canvas dimensions, not by role hierarchy. Each role has explicit ownership of their dimensions. (4.1 Instruction on how to perform a behavior, 12.2 Restructuring the social environment, TR/ER)

- Bring in an exemplar team — either internal or from a peer company — to demonstrate their working readiness practice. Show the artifact, walk through a real readiness conversation, and discuss how they handle disagreements and stories that are partially ready. (6.1 Demonstration of the behavior, MO)

### Phase 3: Stabilize and refine (weeks 7+)

**Focus: MO, PE, feedback — make the new practice self-reinforcing.**

- Implement monthly review of readiness scores versus sprint outcomes. Track the correlation between canvas completeness at sprint entry and sprint-level rework rates, blocked time, and scope change frequency. Share results across all four teams. The data provides ongoing evidence that the readiness canvas predicts sprint health. (2.2 Feedback on behaviour, 5.3 Information about social and environmental consequences)

- Add a recurring retrospective question: "Which readiness gaps caused the most rework this sprint?" This embeds problem-solving into the cadence and keeps the canvas evolving based on real experience. Teams update the canvas dimensions based on what they learn about which gaps actually predict problems. (1.2 Problem solving, iterative)

- Gradually evolve the canvas as teams build pattern recognition about what actually predicts successful execution. Initial dimensions may shift — some may prove irrelevant for certain story types, new dimensions may emerge. The canvas is a living artifact, not a fixed standard. Concept stability increases as teams accumulate shared evidence and shared language. (1.5 Review behavior goal(s))

- Celebrate teams that improve their rework-to-readiness ratio. Recognize teams publicly — not for "following the process" but for demonstrating that multi-perspective readiness assessment leads to better sprint outcomes. Social reward reinforces the behavior and makes the practice identity-positive rather than process-burdensome. (10.4 Social reward)

## Framework observations

- **What worked: State classification was precisely right.** "Contested / Undefined" was exactly the correct state for this scenario. The framework correctly predicted that the primary blockers would be PC (mental-model divergence, no shared language) and RM (identity attachment to competing definitions), with SO (semantic drift, turf battles) as a secondary force. The diagnostic cycle's characterization — "alignment is impossible because the conceptual object is unstable" — captures the situation with unusual precision. This is not a practice execution problem; it is a conceptual infrastructure problem.

- **What worked: The capability lenses added significant diagnostic depth.** Lenses **1.6** (Shared Representations — e.g. **1.6.1**–**1.6.7**) and **1.2** (Mental Models — e.g. **1.2.2**, **1.2.3**) were the most productive. They made it clear that this is not a training problem — people do not need to learn "what readiness is" — but a conceptual alignment problem. People need to see that they are holding different valid models and that the models must be integrated, not adjudicated. Without these lenses, the temptation would be to "educate" people about readiness, which would reproduce the problem (whose version of readiness gets taught?). The lenses redirect the intervention toward surfacing and integrating mental models rather than imposing a single one.

- **What worked: The social opportunity lenses revealed the political layer.** Without SO **2** (Roles/Authority — e.g. **2.1**, **2.2**) and **5** (Legitimacy — e.g. **5.3**, **5.4**), this looks like a pure knowledge problem: people just need to agree on a definition. With those lenses, you see that converging on a definition redistributes power over the sprint boundary, that challenging someone's definition threatens their professional identity, and that the "correct" definition in any given team is often a power outcome rather than a quality outcome. This explains why past written definitions failed — they were technical solutions to a political problem.

- **What worked: The physical opportunity lenses, though not a primary blocker, explained why the definitional conflict persists.** The PO lenses (workflow **3.7**, tooling **5.1**–**5.2**, information visibility **4.3**) showed that the sprint planning workflow has no structural support for a multi-perspective readiness assessment, the ticket tool does not encode readiness dimensions, and the consequences of under-specified stories are not visible at the point of the readiness decision. These are not the *cause* of the conflict (PC mental-model divergence is), but they are the reason the conflict recurs unchanged sprint after sprint. The environment provides no scaffolding for convergence and no feedback that would let the team learn from its own readiness failures. The PO lenses strengthened the intervention design: the multi-perspective readiness canvas (ER) and the embedded ticket template (EN) are direct responses to PO findings about missing workflow structure and tooling support.

- **Tension: The intervention function mapping stretches when applied to Contested/Undefined.** PC maps to ED, TR, EN — but ED (Education) in this context is not "teach people facts." It is "help people see their own assumptions." The BCT taxonomy accommodates this through 4.2 (Information about antecedents) and 13.2 (Framing/reframing), but the fit requires interpretation. In the original clinical behavior-change context, ED typically means providing health information to patients. Here, it means facilitating metacognitive awareness in professionals. The function label is the same, but the mechanism is significantly different.

- **Gap: The framework underserves multi-stakeholder definitional convergence as a behavior change pattern.** This scenario is less about changing individual behavior and more about facilitating collective sensemaking — getting three roles to co-construct a shared conceptual object that none of them currently holds. The lenses diagnose this extremely well (**1.6** Shared Representations — e.g. **1.6.2**, **1.6.4** — is almost purpose-built for it). But the intervention layer — BCTs and intervention functions — is architectured for individual behavior change and has to be adapted for group-level conceptual work. There is no BCT for "facilitate shared mental-model construction" or "co-create a boundary object." The closest tools are 12.1 (Restructuring the physical environment) and 1.2 (Problem solving), but neither was designed to describe the kind of facilitated inter-role sensemaking this scenario requires. The framework would benefit from an explicit extension for collective conceptual alignment as a distinct behavior change target.
