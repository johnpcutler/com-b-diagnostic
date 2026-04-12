# Scenario: "Code review is a bottleneck everyone dreads"

This narrative follows the canonical pipeline in [`flow.md`](../flow.md). The fenced block below is the **digest**: a code-like summary of outputs for steps 1–7.

```
state      = S2: Realized but Friction-Filled
blockers   = PO* | AM SO PC                               (* = primary)
lenses.PO  = [1.2 tool-task-mismatch, 1.5 weak-feedback-loops, 2.1 time-scarcity,
              2.7 activation-overhead, 3.2 handoff-burden, 3.7 activation-energy,
              4.1 signal-surfacing, 4.2 state-visibility, 5.1 affordance, 5.3 core-path]
lenses.SO  = [1.1-1.4 descriptive-injunctive-norms, 4.1 reward-misaligned, 4.5 recognition,
              5.3 identity-safety, 5.5 professional-congruence, 6.1 voice, 6.6 status]
lenses.PC  = [1.1.2 procedural-review-skill, 1.3.4 recognition-judgment, 1.5.1 calibration,
              1.6.1 shared-language]
lenses.AM  = [2.1.2-2.1.5 habit-loop, 2.4.1 helplessness, 2.2.1-2.2.2 reinforcement-inverted]
functions  = ER >> EN > MO > TR > PE
bcts       = ER→12.1,12.5,7.1 | EN→1.1,2.2 | MO→6.1 | TR→8.1 | PE→5.3
tools      = PO:ci-size-limit,review-dashboard | PC:inline-checklist | SO:team-feed |
             AM:auto-assign | RM:impact-summary
phases     = [wk1-3] ER+EN → [wk4-8] TR+MO+PE → [wk9+] INC+AM+sustain
```

## The situation

A mid-sized engineering organization of roughly 60 engineers across 6 teams ships a microservices-based product on a two-week sprint cadence. Code review is mandatory: the CI pipeline blocks merge without at least one approval. On paper, this is a healthy engineering practice. In reality, the average review turnaround is 24-48 hours. PRs sit in a queue while authors context-switch to other work, then context-switch back when comments arrive. Large PRs (300-800 lines across a dozen files) are common because nobody has established conventions around PR size, and the tooling does nothing to discourage it.

Most review comments are superficial: style nits, naming preferences, minor formatting issues that a linter could catch. Substantive feedback on logic correctness, test coverage gaps, or architectural implications is rare. Reviewers report that they skim large diffs because they lack the time and cognitive bandwidth to reconstruct the author's intent across 12 changed files. The path of least resistance is a quick scan and an approval. Rubber-stamping is widespread but unspoken. Nobody brags about it, but nobody calls it out either, because everyone understands the implicit pressure: the sprint velocity dashboard counts PRs merged, not PRs thoughtfully reviewed.

Engineers have internalized the idea that reviews should catch real bugs and spread architectural knowledge. They feel guilty about shallow reviews. But the guilt does not change the behavior because the environment punishes depth. A thorough review that takes 45 minutes and raises architectural concerns will delay the author's PR, create tension in the sprint, and produce no visible credit for the reviewer. Over time, engineers have learned that effort invested in review is disconnected from outcomes. The few who once left detailed comments found their feedback ignored or argued away, and they stopped trying. The organization is left with a ritual that consumes time without delivering the value it was designed to produce.

## Step 1: Classify the behavior state

Using the diagnostic cycle in [../com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md](../com-b-bcw-bct/behavior-jtbd-maturity-diagnostic-cycle.md), this scenario maps to **State 2: Realized but Friction-Filled**.

The state signal for State 2 is "mandatory but painful; environment is the enemy." That is an exact match. Code review consistently happens -- CI enforcement guarantees that. There is no question about whether the behavior occurs. The problem is that the environment makes it painful and shallow. The characteristics of State 2 align precisely:

- **Legacy systems / workarounds:** The PR tooling is not legacy in the traditional sense, but it functions like one. The diff view, the queue structure, the lack of risk indicators -- these are inherited defaults that nobody has deliberately designed for review quality. Engineers have developed workarounds: batching PRs, rubber-stamping, skimming headers only.
- **Manual effort:** Reconstructing author intent from a raw diff is manual cognitive labor. There are no summaries, no risk annotations, no test-coverage deltas surfaced inline. The reviewer does all the integration work in their head.
- **Compliance-driven:** The behavior persists because CI requires it, not because anyone experiences it as valuable in its current form.
- **Little joy, lots of necessity:** Engineers describe review as a tax, not a learning opportunity. The emotional signature is obligation and mild resentment, not professional engagement.

This classification matters because it points the intervention toward friction reduction (PO) rather than education (PC) or persuasion (RM). Engineers already know what good review looks like. They already believe it matters. The environment prevents them from doing it.

## Step 2: Identify COM-B blockers

Using [../com-b-bcw-bct/com-b-behavior-states-primary-secondary-blockers.md](../com-b-bcw-bct/com-b-behavior-states-primary-secondary-blockers.md), State 2 predicts primary blockers in PO and secondary blockers in AM, PC, and SO. Grounding these in the code review scenario:

### Primary blockers

- **PO: Tool/system constraints.** The PR tooling shows raw diffs but does not surface what matters. There is no indication of which files carry the most risk, no test-coverage delta, no architectural-impact annotation. The reviewer must reconstruct context by navigating the full codebase. The tool treats every changed line as equally important, which means nothing is important.
- **PO: Limited time / resource scarcity.** There is no protected time for review. Reviews compete directly with feature work, and feature work wins because it is tracked on the sprint velocity dashboard. Engineers who spend 45 minutes on a thorough review have nothing to show for it in any visible metric. The time cost is real; the reward is invisible.
- **PO: Workflow friction.** PRs are too large because there is no convention or enforcement around size. The review queue is unmanaged -- first-come-first-served regardless of urgency, risk, or reviewer expertise. There is no structured review protocol: no checklist, no required sections in the PR description, no guidance on what to focus on. Every review starts from zero.

### Secondary blockers

- **AM: Learned helplessness.** Repeated experience of investing effort in review and seeing it ignored or argued away has trained passivity. Engineers have learned that the environment does not reward depth, so they default to the low-effort response. This is not laziness; it is an adaptive response to a broken feedback loop.
- **PC: Cognitive overload.** A 500-line PR across 12 files exceeds working memory. Even a motivated reviewer cannot hold the full change in their head. The lack of structure (no summary, no risk annotation, no sequenced walkthrough) means the cognitive load falls entirely on the reviewer, making depth physically impossible for large PRs.
- **AM/SO: Cultural acceptance of inefficiency.** Rubber-stamping has become the descriptive norm. Everyone does it, nobody discusses it, and calling it out would violate an implicit social contract. This is partly SO (norm pressure) and partly AM (habituated response to the PR notification cue).

## Step 3: Deepen with lenses

*Dimensional IDs: [../lenses/physical-opportunity-lenses.md](../lenses/physical-opportunity-lenses.md) `n.m` (PO); [../lenses/social-opportunity-lenses.md](../lenses/social-opportunity-lenses.md) `n.m` (SO); [../lenses/capability-lenses.md](../lenses/capability-lenses.md) `x.y.z` (PC); [../lenses/motivation-lenses.md](../lenses/motivation-lenses.md) `x.y.z` (AM).*

### Physical opportunity lenses ([../lenses/physical-opportunity-lenses.md](../lenses/physical-opportunity-lenses.md))

**1. Work-System Configuration and Constraints** — *PO **1.2**, **1.5** (tool-task fit / feedback-loop strength).* The core mismatch is between the task demands of thoughtful code review and the tool support available. Code review requires understanding intent, assessing risk, evaluating test coverage, and checking architectural consistency. The tool provides a line-by-line diff. This is a tool-task mismatch on the "tools force workarounds" end of the dimension. The reviewer must leave the diff view, open the codebase, trace dependencies, check test files, and mentally reconstruct the change narrative. The work system is fragmented: the review interface, the codebase, the CI results, and the architectural context live in different places with no integration. Feedback-loop strength is weak -- the reviewer rarely learns whether their comments led to better code or were ignored.

**2. Resource and Capacity Conditions** — *PO **2.1**, **2.7** (time availability / activation overhead).* Chronic time scarcity is the dominant resource constraint. Review work is invisible in sprint accounting: no story points, no velocity credit, no recognition in performance reviews. Engineers are measured on code shipped, which creates a structural incentive to minimize time spent on someone else's code. There is no slack margin for thoughtful review. When sprint pressure increases, review quality is the first casualty because it has no organizational defender. Activation overhead is high: picking up a review means loading a new mental context, understanding the feature, reading the diff, and then writing comments that may or may not be acted on. The startup cost alone is 15-20 minutes for a non-trivial PR.

**3. Workflow and Process Architecture** — *PO **3.2**, **3.4**, **3.7** (handoffs / queue friction / activation energy).* The activation energy to do a good review is high and the process design does nothing to lower it. PRs are too large because there is no size convention. The queue is unmanaged: a critical security fix sits behind three cosmetic changes. There is no routing logic -- a backend specialist may be assigned a frontend PR. No structured review protocol means every reviewer invents their own approach each time, which increases variance and cognitive cost. Handoff burden is significant: the author writes a PR, a reviewer picks it up hours later with no shared context, leaves comments, the author responds a day later having lost their own context. Each handoff degrades information.

**4. Information and State Visibility** — *PO **4.1**, **4.2** (signal surfacing / state visibility).* Key review signals are buried or absent. Test results may be visible in CI but are not surfaced inline in the diff. Coverage changes are not shown. Architectural diagrams do not exist in the review interface. The reviewer cannot see which files are most frequently changed (churn risk), which functions have had recent bugs, or which changes touch shared infrastructure versus isolated modules. The diff view treats a one-line config change and a fundamental algorithm rewrite as visually equivalent. Signal surfacing is at the "key signals buried" end of the dimension. The reviewer must infer system state rather than observe it.

**5. Tooling and Interface Affordances** — *PO **5.1**, **5.3** (affordance clarity / core-path efficiency).* The diff view does not highlight what is important. There is no mechanism for the author to annotate "this is the tricky part -- please look carefully here." There is no way to sequence the review ("read this file first, then this one"). The review interface does not support progressive disclosure: the reviewer sees everything at once, with no way to prioritize. Core-path efficiency is low: the most common review action (understand the change, assess risk, approve or request changes) requires extensive navigation and context reconstruction that the tool does not support.

### Social opportunity lenses ([../lenses/social-opportunity-lenses.md](../lenses/social-opportunity-lenses.md))

**1. Norms and Normative Climate** — *SO **1.1**, **1.4**, **1.7** (descriptive/injunctive / consistency / deviance cost).* The descriptive norm is rubber-stamping: most reviews are shallow, and everyone knows it. The injunctive norm is mixed -- leadership says reviews matter, engineering values espouse quality, but peer behavior signals that speed matters more than depth. Norm consistency is low: the message from above ("reviews are important") conflicts with the behavior around you ("everyone skims and approves"). Deviance cost is asymmetric: the cost of doing a shallow review is zero (nobody tracks review quality), while the cost of doing a thorough review is tangible (delayed PRs, sprint friction, social tension with the author). This asymmetry stabilizes the shallow-review norm.

**4. Incentives, Accountability, and Reinforcement Architecture** — *SO **4.1**, **4.5** (reward alignment / recognition visibility).* Sprint velocity metrics reward shipping: PRs merged per sprint is a visible team metric. Review quality is unmeasured. Time spent reviewing is invisible in all performance discussions. There is no accountability for review depth -- no one asks "did your review catch anything substantive?" Recognition visibility is near zero for review work: an engineer who catches a critical bug in review gets no credit comparable to the engineer who wrote the feature. Reward alignment is strongly misaligned: the stated behavior (thorough review) is penalized by the actual reinforcement system (velocity metrics).

**5. Legitimacy, Meaning, and Identity Safety** — *SO **5.3**, **5.5** (identity safety / professional congruence).* Thorough reviewing carries identity risk. An engineer who raises architectural concerns in a PR review may be perceived as a gatekeeper, a nitpicker, or someone who slows the team down. This is especially true when the reviewer is questioning a design decision made by a more senior engineer or a tech lead. Professional congruence is ambiguous: is a thorough reviewer a principled craftsperson or an obstructionist? The narrative depends on the team culture, and in a velocity-driven culture, the obstructionist frame is more available. Reputational risk is real: blocking a PR has social consequences that approving it does not.

**6. Power, Politics, and Psychological Safety** — *SO **6.1**, **6.6** (voice safety / status asymmetry).* Status asymmetry suppresses voice in reviews. Junior engineers reviewing senior engineers' code face a steep power gradient. Questioning an architectural decision made by a staff engineer requires courage that the environment does not reliably reward. Even among peers, leaving a critical comment creates a micro-conflict that most people would rather avoid. Voice safety is low for substantive feedback: style nits are safe (they are impersonal), but "I think this architecture is wrong" is risky. The review interface does not depersonalize disagreement -- comments are attached to names and visible to the team.

### Capability lenses ([../lenses/capability-lenses.md](../lenses/capability-lenses.md))

PC is a secondary blocker here, not a primary one — but the capability lenses still surface issues the other lenses miss.

**1.1 Declarative and Procedural Knowledge** — *PC **1.1.2** (procedural fluency for review-as-skill).* Engineers know how to read code. But most have never been explicitly taught how to *review* code — how to prioritize what to look at, how to assess risk from a diff, how to distinguish style concerns from logic concerns, how to phrase architectural feedback constructively. Code review is a distinct skill from code writing, and it is almost never formally taught. Most engineers learned review by osmosis in an environment where the dominant model was rubber-stamping. Their procedural knowledge of review is shallow: skim the diff top to bottom, flag anything that looks wrong, approve. A more skilled reviewer would start from the PR description, identify the riskiest files, check test coverage for those files, assess architectural implications, and then skim the rest. That procedure is rarely modeled or taught.

**1.3 Judgment and Decision Competence** — *PC **1.3.4**, **1.3.6** (recognition competence / time-pressure judgment).* Good review requires judgment under ambiguity: which changes are high-risk? Which comments are worth making? When does a style preference cross into a real concern? When should I block a PR versus approve with comments? These are judgment calls that novice reviewers make poorly — they either flag everything (creating noise) or flag nothing (rubber-stamping). The judgment skill develops with practice and feedback, but the current environment provides neither: there is no feedback on review quality, no calibration against expert reviewers, and no discussion of what makes a good review comment.

**1.5 Metacognition and Calibration** — *PC **1.5.1** (calibration).* Engineers who rubber-stamp may not recognize that they are doing it. The skim-and-approve habit is fast enough that it feels like "reviewing." Calibration is poor: engineers may believe they are doing adequate reviews because they occasionally catch a typo, without recognizing that they are systematically missing logic errors, test gaps, and architectural drift. The metacognitive insight — "I am not actually reviewing this, I am just looking at it" — is often absent.

**1.6 Shared Representations** — *PC **1.6.1** (shared language for review quality).* Teams lack a shared vocabulary for review quality. There is no common language for distinguishing categories of review feedback (style, correctness, architecture, test coverage, security). Without shared categories, teams cannot discuss whether their reviews are improving, what kind of feedback is missing, or what a high-quality review looks like. The absence of shared representations makes review quality invisible and undiscussable.

### Motivation lenses ([../lenses/motivation-lenses.md](../lenses/motivation-lenses.md))

AM is the key secondary blocker. The relevant sub-lenses:

**2.1 Habit Formation (AM)** — *AM **2.1.2**, **2.1.5**, **2.1.7** (cueing / goal independence / competing habits).* The current habit loop is: cue (PR notification) -> routine (quick skim, check for obvious errors, approve) -> reward (notification cleared, colleague unblocked, sense of completion). This loop is deeply grooved through hundreds of repetitions. Context dependence is strong: the PR notification itself triggers the skim-and-approve response. The habit runs largely on autopilot and is goal-independent -- even engineers who consciously want to review more deeply find themselves clicking "approve" before they have really thought about it. Competing habit strength is high: the rubber-stamp habit competes directly with the desired thorough-review habit, and it wins because it is faster, easier, and better reinforced.

**2.4 Learned Helplessness and Perceived Uncontrollability** — *AM **2.4.1**, **2.4.3** (controllability / generalization).* Engineers who once invested effort in thorough review experienced a repeated pattern: they left detailed comments, the author pushed back or ignored them, the PR merged anyway, and the next review cycle was the same. Effort felt disconnected from outcomes. Over time, this produced passivity -- not anger, but resignation. "Reviews are just like this" is a helplessness statement. Perceived controllability is low: individual engineers feel they cannot change the review culture alone, and nobody has proposed a systemic intervention. Generalization has occurred: helplessness about review quality has spread to a broader cynicism about process improvement in the organization.

**2.2 Reinforcement, Reward, and Wanting (AM)** — *AM **2.2.1**, **2.2.2**, **2.2.4** (immediacy / magnitude / negative reinforcement).* The reinforcement contingencies are inverted. Approving quickly is immediately rewarded: the author thanks you, the PR ships, your notification queue shrinks, you feel a small sense of completion. Thorough reviewing is immediately punished: it takes longer, the author may push back, the PR is delayed, and sprint metrics suffer. The reward for thorough review is distant and uncertain (maybe a bug is caught, maybe the author learns something), while the reward for quick approval is immediate and certain. This is a classic reinforcement mismatch where the environment systematically trains the wrong behavior.

## Step 4: Map to intervention functions

Using [../com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md](../com-b-bcw-bct/com-b-to-bcw-intervention-function-mapping.md), the COM-B blockers map to intervention functions as follows:

| COM-B Blocker | Intervention Functions |
|---|---|
| PO (primary) | RE, ER, EN |
| SO (secondary) | RE, ER, MO, EN |
| AM (secondary) | PE, INC, COE, TR, ER, MO, EN |
| PC (secondary) | ED, TR, EN |

Consolidating by frequency and relevance to this scenario, the priority intervention functions are:

1. **ER (Environmental Restructuring)** -- appears across PO, SO, and AM. Restructure the review environment to reduce friction: smaller PRs, better tooling, guided review checklists, risk-surfacing automation. This is the highest-leverage function because the primary blockers are environmental.
2. **EN (Enablement)** -- appears across PO, SO, AM, and PC. Remove barriers that sit beyond education or training: protected review time, managed queues, load-balanced reviewer assignment. Enablement addresses the structural conditions that make good review impossible regardless of individual motivation.
3. **MO (Modelling)** -- appears for SO and AM. Show what good review looks like. Most engineers have never seen a thorough, well-structured review performed in real time. The descriptive norm is shallow review because that is all anyone observes.
4. **TR (Training)** -- appears for AM and PC. Build review skill through deliberate practice. Most engineers were never formally taught to review code. They learned by imitation in an environment where the dominant model was rubber-stamping. Training breaks the assumption that review skill is innate.
5. **PE (Persuasion)** -- appears for AM and PC. Make the value of good review visible through data and narrative. Connect review quality to outcomes (bugs caught, production incidents prevented) so that the abstract belief "reviews matter" becomes a concrete, felt conviction.

## Step 5: Select BCTs

Using [../com-b-bcw-bct/bct-taxonomy.md](../com-b-bcw-bct/bct-taxonomy.md), selecting specific techniques that implement the priority intervention functions:

### Via ER -> Grouping 12 (Antecedents) and 7 (Associations)

- **12.1 Restructuring the physical environment.** Enforce PR size limits: soft warning at 300 lines, hard block at 500 lines. This is the single highest-impact environmental change because it makes every downstream review behavior easier. A 200-line PR across 3 files is reviewable in working memory; a 600-line PR across 12 files is not. Additionally, restructure the diff view to surface risk indicators: files with high churn, functions with recent bug history, test-coverage delta.
- **12.5 Adding objects to the environment.** Add a structured review checklist template to every PR. The checklist includes sections: logic correctness, test coverage, architectural consistency, naming/readability, and security implications. The checklist is not a gate (reviewers are not forced to check every box) but a cognitive scaffold that directs attention beyond style nits.
- **7.1 Prompts/cues.** Automated prompt when a PR has been open for more than 4 hours without a reviewer assigned. A second prompt to the assigned reviewer if no activity after 4 hours. These cues break the "I'll get to it later" pattern by creating a timely, context-appropriate nudge.

### Via EN -> Grouping 1 (Goals and Planning) and 2 (Feedback and Monitoring)

- **1.1 Goal setting (behavior).** Set a team-level goal: average review turnaround under 4 hours, with a quality dimension measured by comment categories (style vs. logic vs. architecture vs. question). The goal is defined in terms of the behavior (review turnaround and depth), not just the outcome (bugs caught). This makes it actionable.
- **2.2 Feedback on behaviour.** Weekly team dashboard showing review turnaround time, comment type distribution (style/logic/architecture/question), coverage of reviews across team members, and PR size distribution. The dashboard makes review behavior visible without singling out individuals. It closes the feedback loop that is currently broken: engineers cannot see whether their review behavior is improving because no one measures it.

### Via MO -> Grouping 6 (Comparison of Behaviour)

- **6.1 Demonstration of the behavior.** A senior engineer performs a live "review walkthrough" in a team meeting: they share their screen, open a real PR, and narrate their thought process as they review it. They show how they identify the risky parts, how they check test coverage, how they assess architectural impact, and how they decide what is worth commenting on versus what is not. This makes the invisible skill of good review observable and imitable.

### Via TR -> Grouping 8 (Repetition and Substitution)

- **8.1 Behavioral practice/rehearsal.** Run a "review kata" session: the team reviews a deliberately buggy PR together in a group setting. The PR contains a mix of style issues, a logic bug, a test coverage gap, and an architectural concern. The team practices distinguishing high-value comments from low-value ones, and the facilitator names the patterns. This builds review skill through repetition in a low-stakes context.

### Via PE -> Grouping 5 (Natural Consequences)

- **5.3 Information about social and environmental consequences.** Present data connecting review quality to downstream outcomes: bugs caught during review versus bugs discovered in production, with estimated cost differential. Show specific examples: "This bug was caught in review and took 15 minutes to fix. This similar bug escaped review, caused a production incident, and took 3 days to resolve." Making consequences concrete and local shifts review from abstract obligation to felt necessity.

## Step 6: Tool levers

- **PO -> Automation, Streamlining:** CI integration that flags PRs exceeding 300 lines and suggests splitting strategies based on the file change graph. This removes the manual negotiation around PR size and makes the convention self-enforcing.
- **PO -> Integration:** Review dashboard showing real-time queue depth, average wait times, and reviewer load balance across the team. Integrates CI results, test coverage deltas, and file-risk scores directly into the review interface so reviewers do not need to context-switch.
- **PC -> Instruction, Cognitive Offloading:** Inline review guidance via collapsible checklist sections embedded in the PR template. Each section (logic, tests, architecture, security) includes 2-3 prompt questions that direct the reviewer's attention. This offloads the "what should I look for?" question from working memory to the interface.
- **SO -> Social Proof, Shared Visibility:** Team-level activity feed showing review depth metrics aggregated by team, not individual. Displays comment type distribution (what percentage of comments are substantive vs. style) and review turnaround trends. Team-level aggregation avoids surveillance dynamics while shifting the descriptive norm.
- **AM -> Defaults:** Auto-assignment of reviewers with rotation and load balancing. The default is "you have a reviewer assigned within 30 minutes" rather than "find someone to review your PR." Rotating assignment prevents bottlenecking on senior engineers and distributes review load.
- **RM -> Feedback Loops:** Monthly "review impact" summary that connects specific review comments to prevented production incidents, resolved design issues, or knowledge-sharing moments. This closes the long-horizon feedback loop: reviewers see that their effort mattered, which counteracts the learned helplessness dynamic.

## Step 7: Intervention design

### Phase 1: Reduce friction (weeks 1-3)

**Focus: ER, EN -- make review physically easier before asking for depth.**

The logic of starting here is that no amount of training or persuasion will produce better reviews while the environment punishes them. PO must be addressed first.

- **Enforce PR size convention** via CI warning at 300 lines and soft block at 500 lines. The CI message includes a link to a splitting guide with strategies for decomposing large changes. This is 12.1 (Restructuring the physical environment) targeting PO directly.
- **Add structured PR template** with required sections: "What changed," "Why it changed," "What to focus on in review," and "What I am least confident about." The last section is the most important -- it gives the reviewer an honest signal about where to direct attention. This is 12.5 (Adding objects to the environment) targeting both PO and PC.
- **Implement auto-reviewer assignment** with load balancing and domain-aware routing. The system assigns a reviewer within 30 minutes of PR creation, weighted by reviewer expertise in the changed files and current review load. This is 7.1 (Prompts/cues) combined with ER, targeting PO (workflow friction) and AM (reducing activation energy).
- **Designate 2 protected review blocks** per day in the team calendar (e.g., 10:00-10:30 and 14:00-14:30). During these blocks, the expectation is that engineers check their review queue before starting new feature work. This is EN targeting PO (time scarcity) by creating a structural time allocation.

### Phase 2: Build skill and norms (weeks 4-8)

**Focus: TR, MO, PE -- improve what happens during review now that the environment supports it.**

Phase 2 assumes that Phase 1 has made reviews physically tractable: PRs are smaller, reviewers are assigned, time is protected. Now the intervention can address quality.

- **Run 3 "review kata" sessions** over 6 weeks. Each session uses a different prepared PR containing realistic issues at different levels (style, logic, test coverage, architecture). The team reviews together, discusses what they found, and the facilitator names the patterns. This is 8.1 (Behavioral practice/rehearsal) targeting AM (building a new habit) and PC (building skill).
- **One senior engineer per team does a monthly live review narration.** They share their screen and review a real (or lightly anonymized) PR in real time, narrating their decision-making: what they look at first, how they assess risk, when they decide a comment is worth making, how they phrase architectural feedback constructively. This is 6.1 (Demonstration of the behavior) targeting SO (shifting the descriptive norm) and AM (providing a model to imitate).
- **Launch the review quality dashboard** showing team-level metrics: comment type distribution (style/logic/architecture/question), average turnaround time, PR size distribution, and review depth (comments per 100 lines). The dashboard is team-level, not individual, to avoid surveillance dynamics. This is 2.2 (Feedback on behaviour) targeting EN and SO.
- **Share "before/after" data** connecting review practice to outcomes: defects caught in review vs. defects escaped to production, with cost estimates. Use real examples from the team's own history where possible. This is 5.3 (Information about social and environmental consequences) targeting PE and RM.

### Phase 3: Sustain and reward (weeks 9+)

**Focus: INC, AM habit formation -- make good review self-reinforcing.**

Phase 3 assumes that the new review behaviors are emerging but not yet habitual. The intervention shifts to reinforcement and sustainability.

- **Integrate review contribution into performance conversations.** Managers explicitly discuss review quality alongside code output in 1:1s and performance reviews. Review volume and depth metrics are available (from the dashboard) as evidence. This targets SO -> INC by aligning the formal incentive structure with the desired behavior.
- **Team retrospectives include review practice quality** as a standing agenda item. Teams examine their review dashboard, discuss what improved, identify remaining friction, and adjust. This is 1.5 (Review behavior goals) targeting EN and RM.
- **Gradually tighten PR size limits** as teams internalize the pattern: move the soft limit from 300 to 200 lines over several months. This is an inversion of 8.7 (Graded tasks) -- starting with an achievable standard and raising the bar as competence grows, applied to the environmental constraint rather than the individual.
- **Celebrate "great catch" moments** in team channels. When a review comment prevents a real issue, the team lead highlights it publicly: "Great catch by [name] -- this would have caused [specific problem] in production." This is 10.4 (Social reward) targeting AM and SO by creating visible, immediate positive reinforcement for thorough review behavior.

## Framework observations

- **What worked: Correct identification of PO as the primary lever, and the capability lenses qualified this.** The framework correctly diagnosed this as an environmental problem first. But the capability lenses added an important qualification: engineers know how to *read code* but may not know how to *review code* — these are different skills. The PC lenses (**1.1** procedural fluency — **1.1.2**; **1.3** judgment — **1.3.4**, **1.3.6**; **1.5** metacognition — **1.5.1**) revealed that review skill is underdeveloped because it was never explicitly taught and there is no feedback mechanism. This means the intervention cannot be purely environmental — the TR and MO components (review katas, live narration) are not optional add-ons but necessary complements to the ER/EN core. Without the capability lenses, the intervention might have stopped at "make PRs smaller and add checklists," missing the skill-building layer that turns smaller PRs into better-reviewed PRs.

- **What worked: SO lenses added depth the behavior-state classification missed.** The State 2 classification focuses on PO blockers, which is correct but incomplete. The SO lenses -- particularly Norms (**SO 1.x**, e.g. **1.1**, **1.4**), Incentives (**SO 4.x**, e.g. **4.1**, **4.5**), and Power (**SO 6.x**, e.g. **6.1**, **6.6**) -- revealed that shallow review is not just a friction problem but a socially stabilized equilibrium. Rubber-stamping is a rational response to misaligned incentives and asymmetric deviance costs. The intervention must change the social reinforcement structure, not just the tooling.

- **What worked: BCT taxonomy forced breadth in intervention design.** Without the taxonomy, the intervention might have been "make PRs smaller and add a checklist." The BCT taxonomy pushed the design to include skill-building (8.1 review katas), social modelling (6.1 live review narration), feedback systems (2.2 team dashboard), and consequence salience (5.3 before/after data). Each of these addresses a different part of the COM-B system. The taxonomy acts as a checklist against narrow interventions.

- **Tension: AM may be harder to dislodge than the framework's secondary-blocker label suggests.** The diagnostic cycle classifies AM (learned helplessness) as a secondary blocker behind PO. That is structurally correct -- fix the environment and AM should begin to dissolve. But in practice, years of rubber-stamping have created a deeply ingrained habit loop (motivation **2.1**, e.g. **2.1.7** competing habit) and a learned-helplessness pattern (**2.4**, e.g. **2.4.1**) that may persist even after PO improves. An engineer whose last 500 reviews were rubber-stamps will not suddenly review deeply just because PRs are smaller and a checklist appears. The transition requires active habit disruption (review katas, live narration, protected time blocks) that the framework's "primary then secondary" sequencing somewhat undersells. The risk is that Phase 1 makes review easier but Phase 2 interventions are treated as optional.

- **Gap: The framework does not directly address metric misalignment as a distinct problem category.** Sprint velocity penalizing review time is partly SO (incentive architecture **4.x**, e.g. **4.1**, **4.2**) and partly an organizational design problem that sits above the level of individual behavior change. The BCW intervention functions do not cleanly map to "change what leadership measures." INC (Incentivisation) can add new rewards, but it cannot easily remove the existing metric that punishes the target behavior. The intervention design handles this pragmatically (Phase 3 integrates review into performance conversations), but the framework does not have a dedicated mechanism for diagnosing and intervening on metric systems that actively suppress the target behavior. This is a recurring blind spot for any behavior change framework applied to organizational contexts: the people designing the intervention are often not the people who control the measurement system.
