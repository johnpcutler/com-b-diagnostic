# Scenario: "We should be doing continuous discovery"

This narrative follows the canonical pipeline in [`flow.md`](../flow.md). The fenced block below is the **digest**: a code-like summary of outputs for steps 1–7.

```
state      = S5: Aspirational Only
blockers   = PC* RM* PO* | AM SO                         (* = primary)
lenses.PC  = [1.1.2 procedural-fluency-gap, 1.2.1 model-accuracy, 1.5.1 calibration,
              1.6.1 shared-language, 1.7.2 scaffold-sensitivity]
lenses.RM  = [1.3.5 effort-cost, 1.3.8 present>future, 1.4.4 difficulty-as-mismatch,
              1.5.3 plan-specificity, 1.5.4 cue-linkage]
lenses.AM  = [2.1.2 weak-cues, 2.2.1 reward-immediacy, 2.2.7 goal-directed-control]
lenses.PO  = [2.1 time-scarcity, 2.7 activation-overhead, 3.1 path-complexity,
              3.7 activation-energy, 5.1 affordance-gap, 5.3 core-path-friction]
lenses.SO  = [1.4 norm-inconsistency, 4.1 reward-misaligned, 4.5 recognition-invisible,
              5.1 legitimacy, 5.3 identity-safety, 6.3 political-threat, 7.4 governance-recursion]
functions  = EN >> ED > TR > MO > PE                      COE↓ RE↓
bcts       = ED→4.1,5.3 | TR→8.1,8.7 | EN→1.4,1.1,3.2 | MO→6.1 | PE→9.1,13.3
tools      = PC:template | PO:scheduling,synthesis | AM:weekly-prompt | RM:dashboard | SO:feed
phases     = [wk1-4] ED+TR+EN → [wk5-12] MO+PE+AM → [wk13+] EN+sustain
```

## The situation

A mid-size B2B SaaS company has eight product teams, each with a PM, a designer, and 4-6 engineers. Eighteen months ago, the VP of Product declared "we are a discovery-driven organization" after attending a conference. The phrase appears in the product org's mission statement, in the hiring page, and in two OKRs ("increase customer insight velocity" and "validate top-3 assumptions per quarter"). Leadership genuinely believes this is the direction they want to go.

In practice, two of the eight PMs do occasional customer interviews, roughly one every few weeks, usually triggered by a specific feature bet that feels risky. One PM has a small panel of friendly customers she taps for feedback. The other six PMs have never conducted a discovery interview. Their customer contact consists of sitting in on sales demos, reading support tickets, and occasionally watching a Fullstory session. No team has a shared synthesis practice. No team has a recruiting pipeline for finding non-customers or churned users. There is no shared interview guide, no consent template, no repository for insights, and no protected time in anyone's calendar for discovery work.

The gap between identity and practice is wide. Sprint ceremonies, stakeholder reviews, and backlog grooming fill the calendar. When a PM is asked "how do you know this is the right thing to build?" the answer is usually a mix of stakeholder request, competitive analysis, and intuition. Discovery appears in OKRs but not in weekly rhythms. The few PMs who do interview feel unsupported; the rest feel vaguely guilty but don't know where to start.

## Step 1: Classify the behavior state

Using the diagnostic cycle in [../com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md](../com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md), this organization sits squarely in **State 5: Aspirational Only**.

The state signal for Aspirational Only is "identity-level desire without practice," and the characteristics are:

- **Leadership vision statements** — "we are a discovery-driven org" is a declared identity, not a description of current behavior.
- **Cultural aspiration** — discovery is positioned as something the org values and wants to be known for.
- **Branding and identity motives** — the hiring page and mission statement use discovery language to signal a certain kind of product culture.
- **Small symbolic attempts** — two PMs doing occasional interviews constitute token practice, not systematic behavior.
- **No actual habit infrastructure** — no cadence, no templates, no recruiting, no synthesis, no protected time.

This is not Weakly Realized (State 4), because Weakly Realized requires that "everyone agrees it matters" and that the behavior "keeps getting displaced." Here, most PMs have never attempted the behavior at all. There is no displacement of an existing practice; there is an absence of practice altogether. The behavior has not been displaced by urgency — it was never instantiated in the first place.

It is also not Contested/Undefined (State 7), because there is no active definitional conflict. People are not arguing about what discovery means. They simply are not doing it. The definitional vagueness (what counts as "discovery"?) is a secondary issue that sits inside the Aspirational Only pattern rather than being the primary blocker.

## Step 2: Identify COM-B blockers

Referencing [../com-b-bcw-bct/com-b-behavior-states-primary-secondary-blockers.md](../com-b-bcw-bct/com-b-behavior-states-primary-secondary-blockers.md) for the quick lookup and grounding in the Aspirational Only state from [../com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md](../com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md):

### Primary blockers

- **RM: Identity gap — aspiration exceeds true commitment.** Leadership says "discovery" but hasn't invested in structure, hasn't reallocated time, and hasn't changed what gets rewarded. The aspiration is sincere but shallow. When forced to choose between protecting discovery time and hitting a sprint commitment, every team chooses the sprint. The identity is adopted at the narrative level but has not been translated into resource allocation or behavioral commitment.

- **PO: No enabling structures.** There is no recruiting pipeline for finding research participants. No interview guide templates. No consent scripts. No synthesis tools or shared insight repository. No protected calendar time. No budget for incentives. The physical infrastructure required to perform discovery simply does not exist. A PM who wanted to do an interview tomorrow would have to build everything from scratch.

- **PC: Undefined skill.** Most PMs don't know what a good discovery interview looks like. They cannot distinguish between a discovery conversation (testing assumptions, understanding context and motivation) and a sales demo or a feature-request conversation. They lack procedural knowledge of how to recruit, how to write a discussion guide, how to synthesize, and how to connect insights to product decisions.

### Secondary blockers

- **AM: Low emotional reward / no habit loop.** There is no positive reinforcement for doing discovery. Sprint velocity and shipped features get celebrated in demos and all-hands. Insight generation is invisible. No one has experienced the reward of a discovery insight changing a product decision, so there is no appetitive pull toward the behavior.

- **SO: Symbolic buy-in without behavioral reinforcement.** Leadership talks about discovery, but peer behavior signals that it is optional. When PMs look at what their colleagues actually do, no one is doing discovery. The social norm is to fill time with delivery activities. The two PMs who do interview are seen as having a personal interest, not as following an organizational expectation.

- **PC: Undefined "what good looks like."** There are no shared exemplars. No one has seen a well-run discovery interview, a strong synthesis artifact, or a product decision that was visibly improved by discovery. Without concrete models, the behavior remains abstract.

## Step 3: Deepen with lenses

*Dimensional IDs below reference [../lenses/capability-lenses.md](../lenses/capability-lenses.md) (PC `1.x.y`), [../lenses/motivation-lenses.md](../lenses/motivation-lenses.md) (RM/AM `1.x.y` / `2.x.y`), [../lenses/physical-opportunity-lenses.md](../lenses/physical-opportunity-lenses.md) (PO `n.m`), [../lenses/social-opportunity-lenses.md](../lenses/social-opportunity-lenses.md) (SO `n.m`).*

### Capability lenses ([../lenses/capability-lenses.md](../lenses/capability-lenses.md))

**1.1 Declarative and Procedural Knowledge** — *PC **1.1.1**, **1.1.2** (emphasis):* Most PMs have read about continuous discovery — they can name Teresa Torres, they know the phrase "opportunity solution tree." But they lack procedural fluency. They could not recruit a participant, write a discussion guide, conduct a 30-minute interview that tests a specific assumption, and synthesize the result into an actionable insight. The gap is between declarative knowledge ("discovery is important, here are some concepts") and procedural capability ("I can execute this, step by step, right now"). This is a classic case where people have heard the material but cannot execute the behavior reliably.

**1.2 Mental Models** — *PC **1.2.1** (model accuracy):* Many PMs hold a flawed mental model of what discovery is. The most common misconception is "discovery = asking customers what they want" or "discovery = validating our ideas with users." A more accurate model would emphasize assumption identification, evidence triangulation, understanding of context and motivation, and distinguishing between what people say and what they do. Without correcting this mental model, even PMs who start interviewing will do it badly — they'll run feature-validation sessions rather than genuine discovery.

**1.5 Metacognition** — *PC **1.5.1** (calibration):* The two PMs who have done some interviews may overestimate their skill. They have done the behavior but have received no feedback on quality, so their confidence may be poorly calibrated. They may not recognize that their interviews are leading, that they are confirming rather than testing, or that their synthesis is thin. Meanwhile, the PMs who haven't tried at all may underestimate their potential — they assume discovery requires a level of expertise they don't have, when in fact a scaffolded first attempt is quite achievable.

**1.6 Shared Representations** — *PC **1.6.1**, **1.6.2** (shared language / alignment):* There is no common language for what "discovery" means across teams. For one PM, discovery means "talking to the sales team about what customers are asking for." For another, it means "watching a user try our prototype." For a third, it means "ethnographic observation." These are not the same activity, and the lack of a shared definition makes it impossible to set expectations, measure progress, or learn from each other. The word "discovery" has become a floating signifier that each person fills with their own meaning.

**1.7 Supported Performance** — *PC **1.7.2**, **1.7.6** (scaffolding / transfer under support):* This is the most optimistic lens. With the right templates (interview guide, recruiting script, synthesis template) and light coaching (a research-trained person sitting in on the first few interviews), most PMs could likely perform competently. The capability gap is more about scaffolding than about fundamental cognitive limitation. This suggests that heavy upfront training is less important than providing good tools and paired practice.

### Motivation lenses ([../lenses/motivation-lenses.md](../lenses/motivation-lenses.md))

**1.3 Expectancy-Value-Cost** — *RM **1.3.5**, **1.3.7**, **1.3.8** (effort / opportunity / present cost):* The reflective calculus is unfavorable. The effort cost of discovery is high and front-loaded: recruiting participants (who? how?), scheduling calls (when? calendar is full), preparing a discussion guide (what questions?), synthesizing results (into what format? for whom?). The payoff is uncertain and delayed: insights may or may not change a product decision, and even if they do, the connection is hard to demonstrate. Present cost dominates future value. This is a textbook expectancy-value-cost problem where the behavior fails not because people don't value it in the abstract, but because the cost-benefit ratio in the moment is terrible.

**1.4 Identity-Based Motivation** — *RM **1.4.1**, **1.4.4** (congruence / interpretation of difficulty):* "Discovery-driven PM" is an aspirational identity that most PMs in this org have adopted at the narrative level. But when they encounter the difficulty of actually doing discovery (recruiting is hard, scheduling is hard, synthesis is ambiguous), the difficulty is interpreted as "this isn't practical for our context" rather than as a meaningful challenge worth overcoming. In Oyserman's terms, difficulty is being read as identity-incongruent ("people like us don't have time for this") rather than identity-congruent ("this is hard because it matters"). The identity has not been anchored to concrete behaviors, so it provides aspiration without traction.

**1.5 Goal/Implementation Intentions** — *RM **1.5.3**, **1.5.4** (plan specificity / cue linkage):* The intention exists at a high level ("we should do discovery") but there are zero implementation intentions. No one has specified: "Every Tuesday at 2pm I will conduct a 25-minute discovery call with a customer recruited from our panel." There are no if-then plans, no triggers, no cue linkage. The goal is a floating aspiration with no action plan attached. This is the classic intention-action gap: strong goal intention, zero implementation intention.

**2.1 Habit Formation (AM)** — *AM **2.1.1**, **2.1.2** (automaticity / context dependence):* There is zero automaticity. Discovery is not cued by anything in the weekly workflow. No context-response association exists. Sprint planning does not trigger "what assumption should we test?". Release planning does not trigger "what did we learn from customers this cycle?". The behavior has no cue, no routine, and no reward — all three components of a habit loop are absent.

**2.2 Reinforcement (AM)** — *AM **2.2.1**, **2.2.5**, **2.2.7** (immediacy / cue-wanting / control):* There is no reward for discovery. The organizational reward system celebrates velocity (stories shipped), predictability (hit the sprint commitment), and stakeholder satisfaction (built what was requested). Insight generation is invisible in every performance artifact: sprint demos, quarterly reviews, promotion packets. A PM who spends 3 hours a week on discovery has nothing to show for it in the systems that matter for recognition and advancement.

### Physical opportunity lenses ([../lenses/physical-opportunity-lenses.md](../lenses/physical-opportunity-lenses.md))

**2. Resource and Capacity** — *PO **2.1** (time availability), **2.7** (activation overhead):* There is no protected time for discovery. PM calendars are packed with sprint ceremonies (standup, planning, retro, review), stakeholder meetings, cross-team syncs, and backlog grooming. Discovery competes with all of these for the same scarce resource: unstructured PM time. Time scarcity is severe and structural. Even a motivated PM would struggle to find 3 hours a week for recruiting, interviewing, and synthesizing without something else being explicitly deprioritized. The activation overhead is high because there is no slack margin — every hour is already allocated.

**3. Workflow and Process Architecture** — *PO **3.1** (path complexity), **3.7** (activation energy):* No discovery workflow exists. There is no step in any team's operating rhythm that includes discovery. Sprint planning does not include "identify assumptions to test." Release planning does not include "synthesize what we learned." There is no recruiting step, no scheduling step, no synthesis step. The activation energy is enormous because you would have to build the entire workflow from scratch, with no organizational precedent to follow. The path complexity is high for a first-time practitioner: recruit a participant, schedule a time, prepare questions, conduct the interview, capture notes, synthesize, share findings, connect to decisions — and none of these steps has an established process.

**5. Tooling and Interface Affordances** — *PO **5.1**, **5.3** (affordance clarity / core-path efficiency):* There is no recruiting tool (no customer panel platform, no way to find non-customers), no interview guide template, no consent script template, no note-taking template, no synthesis repository, and no way to connect insights to product decisions in existing tools. The behavior has no infrastructure. The tooling gap means that every instance of discovery requires high manual overhead, which compounds the time scarcity problem. There are no affordances that make discovery easy, and the existing tool landscape (Jira, Confluence, Slack) is optimized for delivery, not discovery.

### Social opportunity lenses ([../lenses/social-opportunity-lenses.md](../lenses/social-opportunity-lenses.md))

**1. Norms and Normative Climate** — *SO **1.1**, **1.2**, **1.4** (descriptive/injunctive norms / consistency).* The descriptive norm is clear: PMs do not do discovery. Six of eight PMs have never interviewed a customer. The two who do are seen as having a personal interest, not as following an organizational norm. The injunctive norm is contradictory: leadership says discovery matters (strong injunctive signal), but peer behavior and calendar allocation say it doesn't (strong descriptive counter-signal). Norm consistency is very low — the message from above and the behavior around you point in opposite directions. When PMs look at what gets rewarded, recognized, and discussed, it is delivery velocity, not insight generation.

**4. Incentives, Accountability, and Reinforcement Architecture** — *SO **4.1**, **4.5** (reward alignment / recognition visibility).* The formal reinforcement system actively works against discovery. PMs are evaluated on feature throughput, stakeholder satisfaction, and sprint predictability. None of these reward discovery — and discovery can actively harm all three by consuming time, surfacing inconvenient truths that challenge stakeholder requests, and introducing uncertainty into sprint plans. Recognition visibility for discovery work is near zero: there is no artifact, metric, or ritual that makes discovery contribution legible in performance conversations. A PM who spends 3 hours a week on discovery has nothing to show for it in the systems that matter.

**5. Legitimacy, Meaning, and Identity Safety** — *SO **5.1**, **5.2**, **5.3** (legitimacy / meaning / identity safety).* Discovery occupies an ambiguous legitimacy position. It is rhetorically endorsed but operationally unsupported, which sends a mixed signal about whether it is truly legitimate work. A PM who blocks an afternoon for customer calls may face implicit pushback: "shouldn't you be grooming the backlog?" or "we have a stakeholder review to prepare for." The behavior is not forbidden, but neither is it protected. Meaning is thin — without a visible connection between discovery insights and product decisions, the activity can feel like academic exercise rather than real work. Identity safety is moderate: PMs who do discovery risk being seen as "not focused on delivery" in a culture that rewards output.

**6. Power, Politics, and Psychological Safety** — *SO **6.1**, **6.3** (voice safety / political threat).* Discovery can be politically risky. Insights from customers sometimes contradict stakeholder assumptions or leadership's product vision. A PM who surfaces evidence that the current roadmap is misaligned with user needs is delivering an unwelcome message. In organizations where the roadmap is politically negotiated, discovery can threaten the equilibrium. Psychological safety to share disconfirming evidence is variable across teams — some PMs may suppress discovery findings that would create conflict rather than risk the political exposure.

**7. Governance Viability and Recursion** — *SO **7.2**, **7.4** (coordination / governance recursion).* Discovery requires coordination across levels: individual PMs need time, tools, and coaching; team-level operating rhythms need to incorporate discovery cadence; organizational-level resource allocation needs to fund recruiting infrastructure and protect PM time. Currently, none of these coordination layers exist. The behavior is viable only at the individual level (a motivated PM working alone) and breaks down at every higher level. This is the core SO diagnostic for this scenario: the governance structure does not support discovery at any level above the individual.

## Step 4: Map to intervention functions

Referencing [../com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md](../com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md) Table 1:

From COM-B blockers to intervention functions:
- **PC** → ED (Education), TR (Training), EN (Enablement)
- **RM** → ED (Education), PE (Persuasion), INC (Incentivisation), COE (Coercion)
- **PO** → RE (Restriction), ER (Environmental Restructuring), EN (Enablement)
- **AM** → PE (Persuasion), INC (Incentivisation), COE (Coercion), TR (Training), ER (Environmental Restructuring), MO (Modelling), EN (Enablement)

Priority functions for this scenario, ranked by leverage:

1. **EN (Enablement)** — the single highest-leverage function. Remove the PO barriers that make the behavior structurally impossible. Provide templates, protected time, and a recruiting pipeline. Without EN, no amount of education or motivation will produce sustained behavior.

2. **ED (Education)** — teams need to understand what discovery actually is, how it differs from sales validation, and why it matters for product quality. This addresses the PC blocker (wrong mental models, missing procedural knowledge) and the RM blocker (shallow understanding of value).

3. **TR (Training)** — teams need to practice doing discovery in a safe setting before attempting it with real customers. This addresses the PC blocker (procedural fluency) and builds AM through rehearsal.

4. **MO (Modelling)** — show what good looks like via internal exemplars. The two PMs who already practice discovery can demonstrate the behavior. This addresses the PC secondary blocker (no exemplars) and the SO blocker (no visible peer behavior).

5. **PE (Persuasion)** — make the value of discovery visible and connect it to outcomes teams already care about (reducing rework, increasing confidence in bets, shipping things customers actually use). This addresses RM (identity gap, expectancy-value) and AM (emotional reward).

COE (Coercion) and RE (Restriction) are deprioritized. Coercing discovery would undermine the autonomous motivation needed for it to be done well. Restriction has limited application here — we want to add behaviors, not restrict competing ones (though protecting time from meetings could be framed as restriction).

## Step 5: Select BCTs

Referencing [../com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md](../com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md) Table 3 to navigate into [../com-b-bcw-bct/bct-taxonomy.md](../com-b-bcw-bct/bct-taxonomy.md):

### Via ED → Grouping 4 (Shaping Knowledge) and Grouping 5 (Natural Consequences)

- **4.1 Instruction on how to perform a behavior** — Teach the actual mechanics of a discovery interview: how to write a discussion guide organized around assumptions rather than features, how to ask open-ended questions, how to probe without leading, how to close and capture. This directly addresses the PC blocker of missing procedural knowledge.

- **5.3 Information about social and environmental consequences** — Show what happens to product quality, rework rates, and customer satisfaction when teams skip discovery. Use internal data: "Team X shipped Feature Y without discovery; 30% of users never activated it. Team Z tested their top assumption first; they pivoted the design and saw 2x activation." Making consequences concrete and local is more persuasive than abstract industry arguments.

### Via TR → Grouping 8 (Repetition and Substitution)

- **8.1 Behavioral practice/rehearsal** — Run practice interviews in a safe setting. PMs interview each other or interview willing internal stakeholders using a real discussion guide. The goal is to build procedural fluency before the stakes are real. Practice in a low-consequence context reduces the anxiety of a first real interview and builds the muscle memory of the conversational flow.

- **8.7 Graded tasks** — Start with lightweight discovery (a 10-minute assumption-check call using a 3-question script) before progressing to full 30-minute contextual interviews. Graduated difficulty prevents overwhelm and gives early wins. The first task should be achievable in a single afternoon with no special tooling.

### Via EN → Grouping 1 (Goals and Planning) and Grouping 3 (Social Support)

- **1.4 Action planning** — Create specific if-then implementation intentions: "Every sprint planning includes identifying one assumption to test this sprint" and "Every Thursday at 2pm is protected discovery time." Converting the vague goal into concrete cue-linked plans directly addresses the RM blocker (intention without implementation) and begins building AM (context-response associations).

- **1.1 Goal setting (behavior)** — Set a team-level behavior goal: "Conduct 2 discovery conversations per sprint." The goal is defined in terms of the behavior (conversations), not the outcome (insights), to keep it actionable and measurable. This makes the aspiration concrete and trackable.

- **3.2 Social support (practical)** — Pair each PM with a discovery coach (internal research-trained person or one of the two experienced PMs) for the first 4 sprints. The coach helps recruit the first participants, co-facilitates the first interview, and reviews the first synthesis. This directly addresses the 1.7 Supported Performance finding: the capability gap is about scaffolding, not fundamental limitation.

### Via MO → Grouping 6 (Comparison of Behaviour)

- **6.1 Demonstration of the behavior** — Have the two PMs who already practice discovery run a live demo interview with the broader PM team watching. Make the behavior observable and concrete. Follow the demo with a debrief: what was the assumption being tested, how was the guide structured, what was learned, how did it change a product decision. This converts "discovery" from an abstract concept to a visible, imitable practice.

### Via PE → Grouping 9 (Comparison of Outcomes) and Grouping 13 (Identity)

- **9.1 Credible source** — Bring in a respected external practitioner (or a senior internal leader who has practiced discovery in a previous role) to present concrete examples of discovery-informed product decisions. Credibility matters because the internal culture currently lacks proof that discovery works in their context.

- **13.3 Incompatible beliefs** — Draw attention to the discrepancy between the org's stated identity ("we are discovery-driven") and its actual behavior (6 of 8 PMs have never talked to a customer). This creates productive discomfort. The goal is not shame but honest confrontation of the gap, which can energize commitment to close it.

## Step 6: Tool levers

Referencing [../com-b-bcw-bct/com-b-tool-influence-mechanisms-and-levers.md](../com-b-bcw-bct/com-b-tool-influence-mechanisms-and-levers.md):

- **PC: Guided interview template in the team's existing tool.** A Notion or Confluence template with a structured discussion guide format: assumption statement, 3-5 open questions, probing prompts, and a synthesis section. This uses the Clarification and Instruction mechanisms to make the behavior procedurally clear without requiring separate training. The template encodes "what good looks like" directly into the workflow.

- **PO: One-click scheduling integration for customer calls.** A Calendly-style link connected to a customer panel or opt-in list, reducing the recruiting and scheduling overhead from hours to minutes. This uses the Automation and Streamlining mechanisms to collapse the highest-friction step in the discovery workflow.

- **PO: Pre-built synthesis template that auto-captures notes.** A structured template (assumption tested, key quotes, confidence shift, next action) that can be filled during or immediately after the call. Uses Reduction of Resource Cost to make synthesis feel like 5 minutes of structured capture rather than a separate research artifact.

- **AM: Weekly prompt/reminder to schedule next discovery session.** An automated Slack message every Monday: "What assumption is your team testing this week? Book your discovery call." This uses the Cues & Reminders mechanism to create a context-response trigger where none exists. Over time, the prompt becomes a cue for the habit.

- **RM: Dashboard showing discovery cadence alongside product outcomes.** A simple dashboard: discovery conversations per team per sprint, plotted alongside feature activation rates and rework rates. This uses Feedback Loops and Persuasion mechanisms to make the value of discovery visible and to connect the behavior to outcomes leadership already tracks.

- **SO: Shared feed showing which teams did discovery this week.** A weekly Slack digest or Notion board: "This week, Team Alpha tested assumption X and learned Y. Team Beta spoke with 3 customers about Z." This uses Social Proof and Shared Visibility mechanisms to make discovery a visible, normal peer behavior rather than an invisible individual choice.

## Step 7: Intervention design

### Phase 1: Bootstrap (weeks 1-4)

**Focus:** ED, TR, EN — build minimum capability and remove the biggest PO barriers.

- **Workshop (2 hours):** What discovery is, what it isn't, how to run a 20-minute assumption-testing interview. Include a live demo by one of the two experienced PMs (6.1 Demonstration of the behavior). Follow with a practice round where PMs pair up and interview each other using a provided guide (8.1 Behavioral practice/rehearsal). End with a concrete internal example of a discovery insight that changed a product decision (5.3 Information about social and environmental consequences).

- **Starter kit deployment:** Distribute a discovery starter kit — interview guide template, consent script, synthesis template, and a 1-page "how to recruit" guide (4.1 Instruction on how to perform a behavior). Embed these in the team's existing Notion/Confluence workspace so they are findable without a separate tool.

- **Recruiting infrastructure:** Set up a shared recruiting channel. Options include: a customer opt-in panel (email to existing customers asking if they'd be willing to do 20-minute calls), a Slack channel where PMs can post recruiting requests, and Calendly links for easy scheduling (PO → ER, EN). The goal is to reduce recruiting from a multi-hour effort to a 10-minute task.

- **Behavior goal setting:** Each team sets a behavior goal: conduct 2 customer discovery conversations in the next 2 sprints (1.1 Goal setting (behavior)). The goal is intentionally modest — achievability matters more than ambition at this stage.

- **Discovery buddies:** Pair each team's PM with one of the two experienced PMs or a research-trained designer for their first 4 discovery sessions (3.2 Social support (practical)). The buddy co-facilitates the first interview, reviews the synthesis, and provides calibration feedback.

### Phase 2: Build the habit (weeks 5-12)

**Focus:** MO, PE, AM — make discovery visible, rewarding, and progressively automatic.

- **Biweekly "discovery show and tell":** A 30-minute session where one team shares: what assumption they tested, what they heard, what they decided as a result. Combines 6.1 (Demonstration of the behavior) with 10.4 (Social reward) — the team gets recognition for the practice, not just the insight. Rotate across teams to normalize the behavior.

- **Weekly automated prompt:** Every Monday, an automated Slack message to each team channel: "What assumption is your team testing this sprint? Tag your discovery call in the shared tracker" (7.1 Prompts/cues). This creates a recurring contextual cue that begins building a context-response association (AM).

- **Discovery cadence dashboard:** A lightweight dashboard (even a shared spreadsheet) tracking discovery conversations per team per sprint. Visible to all teams and to leadership. This uses social comparison (6.2) and feedback on behavior (2.2) to make the behavior legible and to create gentle peer accountability without coercion.

- **Graded complexity:** Weeks 5-8, teams focus on short assumption-check calls (10-15 minutes, scripted questions). Weeks 9-12, teams attempt longer contextual interviews (25-30 minutes, open-ended exploration with probing) (8.7 Graded tasks). The progression prevents overwhelm and gives teams time to build fluency before increasing difficulty.

- **Credible source talk:** In week 6 or 7, bring in a respected external practitioner or internal senior leader to present concrete cases where discovery changed outcomes (9.1 Credible source). Timing matters: by this point teams have attempted discovery and have enough experience to engage meaningfully with the examples.

### Phase 3: Sustain and integrate (weeks 13+)

**Focus:** EN, habit consolidation — embed discovery into the operating rhythm so it persists without special effort.

- **Discovery as a standing sprint-planning item:** Add "What assumption are we testing this sprint?" as a required agenda item in sprint planning (8.3 Habit formation). This creates a structural cue that fires every sprint, embedding the behavior into an existing ritual rather than requiring a separate one.

- **Quarterly discovery practice retro:** Review discovery practice quality, not just quantity. Are teams testing real assumptions or going through the motions? Are insights changing decisions? Is synthesis improving? (1.5 Review behavior goals). This prevents the behavior from becoming performative compliance.

- **Coaching fade:** Gradually reduce buddy support as teams self-correct. By week 13, most PMs should be able to recruit, interview, and synthesize independently. Buddies shift from co-facilitation to occasional review (7.3 Reduce prompts/cues — fading scaffolding).

- **Connect discovery to product reviews:** In quarterly product reviews, require teams to present: "What did we learn from customers this quarter, and how did it influence what we shipped?" This connects discovery insights to shipped outcomes (5.3 Information about social and environmental consequences, 9.2 Pros and cons) and makes discovery visible in the artifact that leadership pays most attention to.

- **Insight repository maturation:** As volume grows, invest in a shared insight repository where teams can search and build on each other's discovery work. This creates a compounding return on discovery effort and reinforces the value of the practice over time.

## Framework observations

- **What worked: The behavior-state classification immediately focused the diagnosis.** "Aspirational Only" correctly predicted that the blockers would be a mix of PC (undefined skill), RM (identity gap), and PO (no structure) — which matched the scenario perfectly. The state label gave a fast entry point into the right blocker pattern without having to diagnose from scratch. The cycle framework's distinction between Aspirational Only and Weakly Realized was particularly useful: it prevented the common mistake of treating this as a "competing priorities" problem (Weakly Realized) when it is actually a "never started" problem (Aspirational Only).

- **What worked: The lenses added diagnostic precision beyond the state label.** The capability lenses distinguished between "hasn't been taught" (1.1 procedural knowledge), "holds the wrong mental model" (1.2), "can't calibrate own skill" (1.5), "no shared language" (1.6), and "could perform with scaffolding" (1.7). These are five different PC problems that require different interventions. Without the lenses, the diagnosis would have been a flat "PMs lack capability" that leads to a flat "train them" response. With the lenses, the intervention can be more surgical: correct the mental model first, provide scaffolding rather than extensive upfront training, and build shared language early.

- **What worked: The BCT taxonomy forced specificity.** Instead of vaguely saying "train people on discovery," the framework pushed toward concrete techniques: graded tasks (8.7) to manage difficulty progression, behavioral practice/rehearsal (8.1) to build fluency before real stakes, action planning (1.4) to convert intention into implementation. The taxonomy also surfaced techniques that would not have been obvious, such as 13.3 (Incompatible beliefs) — using the gap between stated identity and actual behavior as a motivational lever.

- **What worked: The social opportunity lenses surfaced the organizational layer that the initial diagnosis underweighted.** The SO lenses — particularly Incentives/Reinforcement Architecture (SO **4.x**, especially **4.1**, **4.5**), Legitimacy (SO **5.x**, especially **5.1–5.3**), and Governance Viability (SO **7.x**, especially **7.2**, **7.4**) — revealed that this is not just a PM-level behavior problem. The organizational reinforcement system actively works against discovery: PMs are measured on throughput, discovery findings can be politically inconvenient, and the governance structure does not coordinate discovery support across any level above the individual. Without the SO lenses, the diagnosis would have stayed at "PMs lack capability and structure," missing the systemic forces that explain why that capability and structure were never built. The SO lenses make the causal chain visible: leadership's shallow RM commitment (SO lens 4 — no incentive alignment) produces the absent PO (no infrastructure) which produces the absent PC (no skill development) which confirms the absent AM (no reward). The lenses connect the organizational system to the individual behavior.

- **Gap: The framework doesn't have a strong way to represent sequencing dependencies between organizational enablement and individual behavior change.** Protected time, recruiting infrastructure, and synthesis tools are all PO problems. But they require RM-level commitment from leadership before they can be solved — someone has to decide to invest in them. The intervention design implicitly handled this (Phase 1 starts with EN and ER, which presupposes leadership buy-in), but the framework itself does not make this dependency explicit. In practice, the first intervention target is not any individual PM's behavior; it is leadership's resource-allocation behavior. That meta-level behavior change (leadership committing real resources) is a precondition for the individual-level behavior change (PMs doing discovery), and the framework treats them as separate analyses rather than as a linked sequence.
