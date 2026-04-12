# Scenario: "Everyone agrees we should write tests, but we keep skipping them"

```
state      = S4: Weakly Realized
blockers   = PO* AM* | RM PC SO                           (* = primary)
lenses.RM  = [1.3.5-1.3.8 present-cost,hidden-benefit, 1.5.3-1.5.4 no-if-then,
              1.1.6 internalization (SDT)]
lenses.AM  = [2.1.7 competing-habit, 2.2.1-2.2.6 inverted-reinforcement,
              2.3.1-2.3.3 aversive-affect, 2.4.1 helplessness]
lenses.PO  = [2.3 no-slack, 3.7 testing-not-in-workflow, 5.1-5.7 hostile-tooling,
              7.4 no-loop-closure]
lenses.PC  = [1.1.2 local-procedure, 1.2.1 mental-model, 1.5.1 calibration,
              1.7.6 transfer-under-support]
lenses.SO  = [1.1-1.2 descriptive≠injunctive, 4.1 shipping>testing,
              5.1-5.3 legitimacy, 6.6 power-gradient]
functions  = ER >> EN > TR > PE > MO                      COE↓
bcts       = ER→12.1,7.1,12.5 | EN→1.4,1.1 | TR→8.3,8.7 | PE→5.2,5.5 | MO→6.1
tools      = PO:scaffold-gen,parallel-suite | AM:pr-checkbox,coverage-delta |
             RM:impact-dashboard | SO:test-hero
phases     = [wk1-4] ER+EN → [wk5-10] TR+MO+AM → [wk11+] PE+INC+sustain
```

## The situation

An engineering team of roughly 25 engineers builds and maintains a mid-size SaaS platform. Test coverage hovers around 30%, concentrated in a few legacy modules where one diligent engineer wrote tests years ago. Every retrospective mentions "we should write more tests." Every post-incident review concludes with an action item about improving test coverage. Engineers genuinely believe in testing — many come from organizations with strong testing cultures, several have given internal talks about TDD, and the team's engineering principles document explicitly lists "automated testing" as a core value. Nobody disagrees that testing matters.

But when sprint pressure hits, tests are the first thing cut. The pattern is remarkably consistent: start the sprint intending to write tests alongside new features, get behind on delivery commitments by mid-sprint, drop tests to hit the deadline, feel guilty at the retrospective, add "improve test coverage" to the backlog, repeat. The testing backlog grows every quarter. Some tests exist, but the existing suite is brittle — roughly 10% of CI runs produce false failures from flaky tests — and the full suite takes 8 minutes to complete. Engineers have learned to ignore red CI signals because they are unreliable. New code is almost never test-driven; the rare test is written after the fact as a box-checking exercise.

The testing gap is not a knowledge problem. Engineers know how to write tests. It is not a values problem. Engineers believe tests are important. It is not a commitment problem in the usual sense — they genuinely intend to test. It is an execution problem under pressure: the behavior is endorsed, understood, and repeatedly intended, but it loses every time it competes with delivery urgency. The result is a growing gap between stated practice and actual practice, a slow accumulation of production incidents in untested code, and an increasingly demoralized team that feels like it cannot live up to its own standards.

## Step 1: Classify the behavior state

Using the diagnostic cycle in [../behavior-jtbd-maturity-diagnostic-cycle.md](../behavior-jtbd-maturity-diagnostic-cycle.md), this team sits squarely in **State 4: Weakly Realized**.

The state signal for Weakly Realized is "agreed and valued, but continually displaced," and the characteristics match precisely:

- **Not a knowledge problem.** Engineers know how to write tests. They have the technical skill. Many have done it in previous jobs. This distinguishes the situation from Aspirational Only (State 5), where the behavior has never been practiced and the skill is undefined.
- **Not a commitment problem.** The team genuinely values testing. There is no contested definition of what testing means, no political resistance to it, no one arguing that tests are unnecessary. This distinguishes it from Contested/Undefined (State 7) and Actively Suppressed (State 6).
- **Loses to urgency, fire drills, scarcity.** Testing consistently loses the competition for time against feature delivery, bug fixes, and sprint commitments. The displacement is not occasional — it is the dominant pattern. Every sprint, testing is the adjustment variable that absorbs schedule pressure.
- **Creates guilt and a backlog of "shoulds."** The team feels bad about not testing. They add test coverage improvements to the backlog. They talk about it at retros. The intention persists even as the behavior fails to materialize. This affective signature — guilt without action — is the hallmark of Weakly Realized.

This is not Partially Realized/Inconsistent (State 3), because the failure is not about process variation or competing interpretations of what testing means. Everyone agrees on what good testing looks like. The problem is that almost no one does it. And it is not Realized but Friction-Filled (State 2), because the behavior is not consistently happening in a painful way — it is not consistently happening at all.

## Step 2: Identify COM-B blockers

Referencing [../com-b-behavior-states-primary-secondary-blockers.md](../com-b-behavior-states-primary-secondary-blockers.md) for the quick lookup and grounding in the Weakly Realized state from [../behavior-jtbd-maturity-diagnostic-cycle.md](../behavior-jtbd-maturity-diagnostic-cycle.md):

### Primary blockers

- **PO: Time scarcity — sprint commitments do not account for testing time.** Feature work fills all available engineering capacity. Story point estimates cover implementation and code review but not test writing. Sprint planning treats testing as something that "should" happen but does not allocate concrete time for it. When the sprint gets tight — and it always gets tight — testing is the only discretionary item. Everything else has a stakeholder waiting for it.

- **AM: Habit competition — the established workflow does not include testing.** The dominant habit loop is: ticket assigned → write code → manually verify in staging → push PR → get review → merge. Testing is not a step in this sequence. It is an add-on that requires a separate decision each time. Other automatic behaviors (checking Slack, jumping on urgent bugs, responding to review comments) crowd out the proactive, effortful behavior of writing a test. The automaticity of the competing workflow is high; the automaticity of testing is near zero.

- **PO: High activation energy — the test infrastructure is hostile.** The existing test suite takes 8 minutes to run in CI. Roughly 10% of runs produce false failures from flaky tests. Test files are poorly organized — finding the right test file for a module requires navigating an inconsistent directory structure. There are no test generators or scaffolding tools. Writing the first test for a new module means setting up imports, mocking dependencies, and configuring test utilities from scratch. The activation energy to write one test is disproportionate to the value of one test.

### Secondary blockers

- **RM: Short-term bias — the cost of testing is immediate and the benefit is diffuse.** Writing a test costs 30 minutes now, concretely. The benefit — fewer bugs, faster debugging, safer refactoring — is probabilistic and arrives weeks or months later. The reinforcement environment sharply favors skipping: close the ticket now, avoid the bug maybe never. This is a textbook temporal discounting problem.

- **PC: Limited self-regulation structures — no triggers, no cues, no environmental prompts.** There is nothing in the development environment that initiates "write the test now." No PR template asks about tests. No CI check reports coverage changes. No linter warns about untested new functions. The decision to test must be generated entirely from internal motivation, which is unreliable under cognitive load and time pressure.

- **SO: Fire-drill culture — heroic firefighting is rewarded over preventive work.** The team culture visibly celebrates the engineer who fixes a production incident at midnight. It does not celebrate the engineer who wrote the test that prevented the incident from happening. The social reward structure is misaligned: reactive work gets public praise, preventive work is invisible. This makes testing feel like unrewarded effort in the social context.

## Step 3: Deepen with lenses

*Dimensional IDs: [../motivation-lenses.md](../motivation-lenses.md) `x.y.z` (RM/AM); [../physical-opportunity-lenses.md](../physical-opportunity-lenses.md) `n.m` (PO); [../capability-lenses.md](../capability-lenses.md) `x.y.z` (PC); [../social-opportunity-lenses.md](../social-opportunity-lenses.md) `n.m` (SO).*

### Motivation lenses ([../motivation-lenses.md](../motivation-lenses.md))

This is where the real diagnostic lives. The motivation picture is complex: high RM endorsement at the value level, but weak RM translation into action, combined with multiple AM forces that actively work against the behavior.

#### Reflective Motivation

**1.3 Expectancy-Value-Cost** — *RM **1.3.2**, **1.3.4**, **1.3.5**, **1.3.8** (value / utility / effort / present weighting):* Engineers recognize the value of testing — it has high attainment value ("I want to be the kind of engineer who writes tests") and high utility value ("tests catch bugs, enable refactoring, document behavior"). But the effort cost is high and front-loaded: writing a test takes real time right now, time that competes with closing the next ticket. The present-vs-future weighting is sharply skewed. The cost is borne in this sprint; the benefit accrues probabilistically across future sprints. When the sprint is tight — and it is always tight — the reflective calculus resolves in favor of skipping. The behavior fails not because engineers do not value it but because the cost-benefit ratio in the moment is unfavorable. This is compounded by the fact that the benefit is invisible: you never see the bug that a test prevented.

**1.5 Goal/Implementation Intentions** — *RM **1.5.3**, **1.5.4** (plan specificity / cue linkage):* The intention exists at a high level — "we should write more tests" — but it has not been converted into implementation intentions. There are no if-then plans. No one has specified: "when I finish writing a function, I create the test file before moving to the next ticket." The goal is a floating aspiration disconnected from any specific context, time, or trigger. The intention-action gap is wide precisely because the intention is abstract. It is a goal without an action plan, and research consistently shows that goal intentions without implementation intentions have weak effects on behavior.

**1.1 Self-Determination Theory** — *RM **1.1.6**, **1.1.7** (internalization / self-concordance):* Testing motivation in this team is partly controlled rather than fully autonomous. The team hears "we should test" in retros, in post-incident reviews, in engineering principles documents — but this is experienced as an external expectation rather than a self-generated choice. For most engineers, testing has been endorsed at the value level ("I believe testing is important") but not internalized at the regulation level ("I test because it is part of how I work"). The few engineers who do test-drive by choice have genuinely internalized the behavior — they test because it feels wrong not to, not because they are supposed to. Most have not reached that level of internalization. The behavior sits in the "identified regulation" zone: valued but not yet integrated into the self.

#### Automatic Motivation

**2.1 Habit Formation** — *AM **2.1.1**, **2.1.7** (automaticity / competing habits):* The dominant habit loop is: trigger (ticket assigned) → routine (write code, manual test, push) → reward (PR merged, ticket closed, sprint progress). Testing is not part of this loop. There is no context-response association between "finished a function" and "write a test." The automaticity of the competing behavior (code-review-merge) is high — engineers can do it without thinking. The automaticity of testing is near zero — every instance requires a fresh decision, effort, and activation. The habit formation lens predicts that the behavior will fail unless it can be embedded into an existing routine with a stable cue and a rewarding outcome. Currently, testing has none of these.

**2.2 Reinforcement, Reward, and Wanting** — *AM **2.2.1**, **2.2.2**, **2.2.4** (immediacy / magnitude / relief vs aversive test runs):* The reinforcement schedule strongly favors the competing behavior. Skipping tests produces immediate reward: the ticket closes faster, the sprint board looks better, the PM is satisfied. Writing tests produces no immediate reward and a possible future reward (fewer bugs) that is both delayed and probabilistic. Worse, the existing test suite actually punishes testing effort — flaky tests mean that writing a test can create a false failure that blocks your own PR, making the experience of testing aversive rather than rewarding. The reinforcement contingencies are precisely backwards: the behavior you want is punished, and the behavior you do not want is rewarded.

**2.3 Affect and Emotion** — *AM **2.3.1**, **2.3.3**, **2.3.6** (valence / anticipation / regulation):* Tests are associated with frustration. The 8-minute CI wait is boring. The flaky test investigation is infuriating ("my test passes locally but fails in CI because of some shared state issue"). The test infrastructure itself — poorly documented, inconsistently organized, requiring arcane mocking patterns — produces dread. Compare this with the feeling of shipping a feature: satisfying, visible, celebrated. The emotional valence of testing is aversive; the emotional valence of shipping is attractive. Until the affect associated with testing shifts from frustration to competence and flow, the automatic motivation system will resist the behavior.

**2.4 Learned Helplessness** — *AM **2.4.1**, **2.4.3** (controllability / generalization):* The team has a history of failed testing initiatives. Two years ago, someone added 200 tests to the payment module. Within six months, 40 of them were flaky and the rest were ignored because the suite was too slow to run locally. The experience taught engineers that effort (writing tests) is disconnected from outcomes (a reliable test suite). This is the core mechanism of learned helplessness: perceived uncontrollability. Engineers have learned — through direct experience — that writing tests does not reliably produce a better testing outcome. The environment needs to change before the motivation can recover.

### Physical opportunity lenses ([../physical-opportunity-lenses.md](../physical-opportunity-lenses.md))

**2. Resource and Capacity** — *PO **2.3** (slack margin), **2.7** (activation overhead):* Zero slack. Sprint commitments fill 100% of engineering capacity with feature delivery. Story point estimates do not include testing time — or if they nominally do, the buffer is the first thing consumed when scope creeps or unexpected issues arise. There is no protected time for testing, no "test day," no percentage of sprint capacity reserved for engineering quality. Testing competes for the same scarce resource as feature work, and feature work always wins because it has a stakeholder attached to it. The activation overhead compounds the problem: even if an engineer had 30 minutes of unexpected free time, the startup cost of navigating the test infrastructure makes it unlikely they would choose to spend it writing a test.

**3. Workflow and Process Architecture** — *PO **3.7** (activation energy — testing not a workflow step):* Testing is not a step in the development workflow. It is an optional add-on that happens if and only if the engineer makes a separate decision to do it. The PR template does not ask about test coverage. Code review does not systematically check for tests. CI does not gate on coverage thresholds. The definition of "done" for a ticket does not include "tests pass for new logic." The process architecture treats testing as discretionary — and discretionary behaviors under time pressure are the first to be dropped. The activation energy is high because testing must be self-initiated, and the workflow provides no structural cue, no checkpoint, and no gate that triggers or enforces it.

**5. Tooling and Interface Affordances** — *PO **5.1**, **5.3**, **5.4**, **5.7** (affordance / path / error tolerance / automation fit):* The test infrastructure is actively hostile to the desired behavior. Slow suite (8 minutes full run), high false-failure rate (10% flaky), poor organization (no consistent test file naming or directory structure), no scaffolding (no CLI tool to generate a test file with correct imports and describe blocks), and no local fast-feedback loop (running the full suite locally is impractical). The tooling creates friction at every step: finding where to put the test, setting up the test file, writing the test, running the test, and interpreting the result. Each friction point provides an off-ramp for the engineer to say "I'll write the test later" — and "later" never comes.

**7. Control Loops** — *PO **7.4** (loop closure — no coverage→outcome feedback):* There is no feedback loop connecting test coverage to outcomes. Engineers do not see which production bugs would have been caught by tests. There is no dashboard showing coverage trends, no report connecting untested code to incidents, no signal that testing effort produces better outcomes. The absence of a control loop means the behavior is open-loop: engineers act (or do not act) without receiving information about the consequences of their choice. Without feedback, the system cannot self-correct. The team cannot learn from its own behavior because the signal is buried.

### Capability lenses ([../capability-lenses.md](../capability-lenses.md))

PC is not a primary blocker — engineers know how to write tests. But the capability lenses reveal subtler gaps that compound the environmental and motivational problems.

**1.1 Declarative and Procedural Knowledge** — *PC **1.1.2** (contextual procedural fluency in this codebase):* Engineers have generic testing knowledge: they understand assertions, mocking, test structure, and the difference between unit and integration tests. What they lack is *contextual* procedural knowledge: how to write effective tests in *this* codebase with *these* patterns. The codebase has complex dependency injection, several custom mocking utilities that are undocumented, and inconsistent test patterns across modules (some use one test runner, others use a different one). The gap is not "how to test" but "how to test here." A new team member who knows testing well would still need 2-3 hours to figure out the local conventions before writing their first test.

**1.2 Mental Models** — *PC **1.2.1** (model of what "good test" means):* Some engineers hold a flawed mental model of what "good testing" means in this context. The dominant model is "tests verify that the code works," which leads to tests that duplicate implementation logic — testing that a function returns what the code says it should return, rather than testing behavior against requirements. A more effective mental model would frame testing as "tests document expected behavior and catch regressions," which leads to tests that are resilient to refactoring. This mental model gap means that even when engineers do write tests, some of those tests are low-value (they break on every refactor without catching any bugs).

**1.5 Metacognition and Calibration** — *PC **1.5.1** (calibration of test quality):* Engineers who have not tested consistently in this codebase may overestimate the difficulty. The test infrastructure's hostility (flaky tests, slow suite) has created a reputation that makes testing seem harder than it would be if the infrastructure were fixed. Conversely, engineers who do write occasional tests may overestimate their quality — without peer review of test code and without data on which tests actually catch regressions, there is no calibration mechanism. The team cannot distinguish between "good test" and "test that exists."

**1.7 Supported Performance** — *PC **1.7.6** (transfer under support — scaffolding unlocks latent skill):* With the right scaffolding — test generators, templates, documented mocking patterns, and a fast feedback loop — most engineers on this team could test competently. The capability gap is more about infrastructure and scaffolding than about fundamental skill. This is the optimistic capability finding: the PC investment required is not "teach people to test" but "make the local testing environment navigable," which is actually a PO intervention that unlocks latent PC.

### Social opportunity lenses ([../social-opportunity-lenses.md](../social-opportunity-lenses.md))

**1. Norms and Normative Climate** — *SO **1.1**, **1.2** (descriptive vs injunctive):* The descriptive norm is "we don't test." The injunctive norm is "we should test." This contradiction is the social signature of Weakly Realized behaviors. Engineers look around and see that nobody is testing consistently. They hear that testing matters in retros and post-incident reviews. The descriptive norm wins because it carries more behavioral weight: what people actually do is a stronger signal than what people say they should do. Deviance from the descriptive norm (actually writing tests) is not punished, but it is not rewarded either — it is invisible. A testing norm cannot establish itself when the behavior is invisible to peers.

**4. Incentives, Accountability, and Reinforcement Architecture** — *SO **4.1**, **4.5** (reward / recognition for shipping vs prevention):* The reinforcement structure strongly favors shipping over testing. Sprint velocity counts tickets closed, not tests written. Performance reviews track feature delivery, not codebase reliability. There is no formal or informal accountability for test coverage — no one asks "did you test this?" in code review, and the CI pipeline does not report coverage deltas. The fire-drill culture compounds this: the engineer who fixes a production incident at 2am gets public praise in Slack; the engineer who wrote the test that would have prevented the incident gets nothing, because the prevented incident is invisible. Preventive work is systematically undervalued because it produces non-events.

**5. Legitimacy, Meaning, and Identity Safety** — *SO **5.1**, **5.3** (legitimacy / identity safety for "testing as work"):* Testing occupies an ambiguous legitimacy position. It is endorsed in principle but deprioritized in practice, which sends a mixed signal about whether it is "real work." An engineer who spends 30 minutes writing tests when the sprint is behind may face implicit (or explicit) pushback: "why are you testing when we have tickets to close?" The act of testing can feel identity-threatening in a delivery-focused culture — it signals that you are "not focused on shipping." Until the organizational culture genuinely treats testing as part of shipping rather than an alternative to it, the legitimacy problem will persist.

**6. Power, Politics, and Psychological Safety** — *SO **6.6** (status — who can challenge sprint norms):* Raising the testing issue at a systemic level — "our sprint planning doesn't account for testing time," "our incentives punish testing" — requires challenging leadership's resource allocation decisions. This is politically risky. The engineers who feel the problem most acutely (those who have tried to test and been burned) may lack the organizational standing to push for infrastructure investment. Junior engineers may not feel safe raising the issue at all. The testing problem is sustained partly by a power asymmetry: the people who set sprint commitments are not the people who experience the downstream consequences of untested code.

## Step 4: Map to intervention functions

Referencing [../com-b-to-bcw-intervention-function-mapping.md](../com-b-to-bcw-intervention-function-mapping.md) Table 1:

From COM-B blockers to intervention functions:

- **PO** → RE (Restriction), ER (Environmental Restructuring), EN (Enablement)
- **AM** → PE (Persuasion), INC (Incentivisation), COE (Coercion), TR (Training), ER (Environmental Restructuring), MO (Modelling), EN (Enablement)
- **RM** → ED (Education), PE (Persuasion), INC (Incentivisation), COE (Coercion)
- **PC** → ED (Education), TR (Training), EN (Enablement)
- **SO** → RE (Restriction), ER (Environmental Restructuring), MO (Modelling), EN (Enablement)

Priority functions for this scenario, ranked by leverage:

1. **ER (Environmental Restructuring)** — the single highest-leverage function. Restructure the development environment so that testing is the path of least resistance rather than a discretionary add-on. This addresses PO (hostile test infrastructure, no workflow integration) and AM (no cues, no habit support). If the environment does not change, no amount of persuasion or education will produce sustained behavior. The infrastructure must be fixed before the habit can form.

2. **EN (Enablement)** — remove barriers that make the behavior structurally impossible. Fix the test suite speed, eliminate flaky tests, provide time in sprint planning for testing. This is the prerequisite layer: without EN, the behavior is physically blocked regardless of motivation or capability.

3. **TR (Training)** — build the habit through practice, not just knowledge. Engineers know how to write tests in the abstract, but they do not have an established practice of writing tests in this codebase with this infrastructure. Training here means rehearsal and repetition (8.1, 8.3) to build the context-response association, not classroom instruction.

4. **PE (Persuasion)** — make the cost of not testing visible and emotionally salient. Connect untested code to production incidents. Show the time cost of debugging versus the time cost of testing. Shift the emotional valence from "testing is a chore" to "untested code is a risk I chose to take."

5. **MO (Modelling)** — show what a good testing practice looks like in this specific codebase. Demonstrate TDD on a real ticket, narrate the decision process, make the behavior observable and imitable. This addresses the gap between abstract knowledge ("I know TDD") and contextualized practice ("I can TDD effectively in our codebase").

COE (Coercion) is deprioritized. Coverage mandates imposed punitively would generate resentment and low-quality tests written to hit a number. INC (Incentivisation) has a supporting role (Phase 3) but should not lead — the goal is intrinsic habit formation, not extrinsic reward dependence.

## Step 5: Select BCTs

Referencing [../com-b-to-bcw-intervention-function-mapping.md](../com-b-to-bcw-intervention-function-mapping.md) Table 3 to navigate into [../bct-taxonomy.md](../bct-taxonomy.md):

### Via ER → Grouping 12 (Antecedents) and Grouping 7 (Associations)

- **12.1 Restructuring the physical environment** — Fix the test infrastructure: parallelize the test suite (8 min → 2 min), quarantine flaky tests into a separate non-blocking suite, add test scaffolding generators to the CLI, reorganize test directories to mirror source directories. The physical environment of testing is currently hostile; restructure it so that writing a test is low-friction and running a test is fast and trustworthy.

- **7.1 Prompts/cues** — Add a CI check that reports the coverage delta on every PR. Not a gate (yet), but a visible prompt at the point of decision: "this PR adds 120 lines of code and reduces test coverage by 3%." The prompt makes the consequence of the choice legible in the moment, creating a cue that is hard to ignore without consciously deciding to ignore it.

- **12.5 Adding objects to the environment** — Add test file templates and generators to the CLI tools engineers already use. `make test ModuleName` creates a test file with correct imports, a describe block, and a placeholder assertion. The object is added to the environment to lower activation energy from "navigate the test infrastructure and set everything up" to "run one command."

### Via EN → Grouping 1 (Goals and Planning)

- **1.4 Action planning** — Create implementation intentions: "When I create a new module, I generate the test file first, before writing production code." "When I finish a function, I write at least one assertion before marking the ticket as in-review." These convert the vague goal ("write more tests") into specific if-then plans anchored to existing workflow moments.

- **1.1 Goal setting (behavior)** — Set a team behavior goal: "Every PR that adds new logic includes at least one test for that logic." The goal is defined in terms of behavior (include a test), not outcome (achieve X% coverage). Behavior goals are more actionable because the engineer controls whether to write a test; they do not control the coverage percentage, which depends on the entire codebase.

### Via TR → Grouping 8 (Repetition and Substitution)

- **8.3 Habit formation** — Pair testing with an existing habit by creating a context-response link: "When I move a ticket to in-review, the last step is running the test I wrote." Attach the new behavior to a stable context (the transition point between coding and review) so that repetition in that context builds automaticity over time.

- **8.7 Graded tasks** — Start small: in weeks 5-6, the expectation is one assertion per PR. In weeks 7-8, a happy-path test. In weeks 9-10, edge-case tests. Graduated difficulty prevents the overwhelm of "we need 80% coverage" and gives early wins that build confidence and momentum. The first task should be achievable in under 5 minutes with the new scaffolding tools.

### Via PE → Grouping 5 (Natural Consequences)

- **5.2 Salience of consequences** — Monthly "bug autopsy" showing which production incidents occurred in untested code, with a comparison: "this incident took 4 hours to debug and affected 200 users; a test covering this code path would have taken 20 minutes to write." The method makes the consequences of the omission vivid, specific, and local rather than abstract and hypothetical.

- **5.5 Anticipated regret** — Before skipping tests on a PR, prompt: "If this code breaks in production at 2am, will you wish you had written the test?" This is not a gate — it does not block the merge. It raises awareness of the anticipated emotional consequence of the choice, which research shows shifts behavior even when the person is free to proceed.

### Via MO → Grouping 6 (Comparison of Behaviour)

- **6.1 Demonstration of the behavior** — A senior engineer live-streams a TDD session on a real ticket from the current sprint, narrating the decisions: why this test first, how to mock this dependency, when to use a unit test versus an integration test, how to handle the edge case. The demonstration makes the behavior observable, concrete, and imitable in context. It addresses the gap between "I know how to test in theory" and "I can see how testing works in our codebase, with our patterns, on our tickets."

## Step 6: Tool levers

Referencing [../com-b-tool-influence-mechanisms-and-levers.md](../com-b-tool-influence-mechanisms-and-levers.md):

- **PO: Test scaffold generator in the CLI.** `make test ModuleName` creates a test file with imports, a describe block, and a placeholder assertion. Mechanism: Reduction of Resource Cost, Streamlining. Targets the high activation energy that prevents engineers from starting. When starting a test takes 5 seconds instead of 5 minutes, the decision calculus changes.

- **PO: Parallelized test suite and flaky test quarantine.** Split the suite into fast unit tests (target: under 90 seconds) and slower integration tests. Quarantine flaky tests into a non-blocking suite that runs nightly, not on every PR. Mechanism: Automation, removing friction. Targets the hostile tooling environment that makes testing aversive.

- **AM: PR template with checkbox for test inclusion.** "Tests included: [ ] yes [ ] no — if no, explain why." The default framing assumes tests will be included; opting out requires a conscious, documented decision. Mechanism: Defaults. Targets the absent cue in the current workflow by embedding a decision point at the moment of PR creation.

- **AM: Coverage delta shown in PR diff.** A CI bot comments on every PR with the coverage change: lines added, lines tested, net coverage delta. Visible at the point of decision, before merge. Mechanism: Cues & Reminders. Targets the absent feedback by making the consequence of the choice legible in real time.

- **RM: "Testing impact" dashboard.** A lightweight dashboard showing: bugs caught by tests this month, production incidents in untested code paths, estimated debugging time saved by test coverage. Mechanism: Feedback Loops, Persuasion. Targets the invisible benefit of testing by making the value concrete and trackable.

- **SO: Weekly "test hero" highlight.** In the team standup or Slack channel, highlight the person who wrote the test that caught a real bug before production. Mechanism: Social Proof. Targets the social reward gap by making preventive work visible and celebrated rather than invisible.

## Step 7: Intervention design

### Phase 1: Fix the infrastructure (weeks 1-4)

**Focus:** ER, EN — make testing physically possible before asking for behavior change. Do not ask engineers to change their behavior in a hostile environment; change the environment first.

- **Parallelize the test suite.** Split into fast unit tests and slower integration tests. Target: unit suite completes in under 90 seconds in CI, integration suite runs on a separate schedule. (12.1 Restructuring the physical environment)
- **Quarantine flaky tests.** Identify the 10% of tests producing false failures. Move them to a quarantine suite that runs nightly and does not block PRs. Fix or delete them over the next 4 weeks. Reduce false-failure rate from 10% to under 1%. (12.1)
- **Add test scaffold generator to CLI tooling.** `make test ModuleName` creates a correctly structured test file. (12.5 Adding objects to the environment)
- **Adjust sprint planning.** Include testing time in story point estimates explicitly. If a story is estimated at 5 points for implementation, the estimate should include testing effort. Alternatively, reserve 15% of sprint capacity as a "quality budget" that includes testing. (EN, PO capacity)
- **Set team behavior goal.** "Every PR for new logic includes at least one test." (1.1 Goal setting (behavior)). The goal is intentionally modest — it is about the behavior (include a test), not about a coverage number.

### Phase 2: Build the habit (weeks 5-10)

**Focus:** TR, MO, AM — create the context-response association between coding and testing.

- **Add coverage delta check to CI.** A bot comments on every PR with the coverage change. Not a gate, but a visible signal. (7.1 Prompts/cues)
- **Add PR template checkbox for test inclusion.** "Tests included: [ ] yes [ ] no — if no, explain." The default framing nudges toward testing. (AM default)
- **Run biweekly TDD pairing sessions.** A senior engineer who tests well pairs with a different team member each session for 1 hour on a real ticket from the sprint. The pair writes tests together on production code. (8.1 Behavioral practice/rehearsal, 6.1 Demonstration of the behavior)
- **Create implementation intention cards.** Posted in Slack, in the PR template, near monitors: "When I create a new file → I generate the test file first." "When I finish a function → I write at least one assertion before moving to the next ticket." (1.4 Action planning, 8.3 Habit formation)
- **Start with graded tasks.** Weeks 5-6: one assertion per PR — it can be as simple as "this function exists and returns something." Weeks 7-8: test the happy path for new logic. Weeks 9-10: test at least one edge case or error path. The difficulty increases only after the easier level has become routine. (8.7 Graded tasks)

### Phase 3: Make it self-reinforcing (weeks 11+)

**Focus:** PE, INC — connect testing to outcomes and reward it so the behavior sustains without external scaffolding.

- **Monthly "bug autopsy" presentation.** Trace production incidents to untested code. Show the comparison: "this incident took 4 hours; a test would have taken 20 minutes." Make the consequence vivid and specific. (5.2 Salience of consequences)
- **Add coverage threshold gate to CI (graduated).** Week 11: warn when a PR reduces coverage by more than 2%. Week 15: block merge when a PR reduces coverage by more than 5% without a documented exception. Increase strictness gradually so the gate is accepted rather than resented. (COE graduated, RE)
- **Integrate test contribution into performance conversations.** Alongside feature delivery, discuss: "How did this engineer contribute to codebase reliability this quarter?" Make preventive work legible in the systems that matter for career advancement. (SO incentive alignment)
- **Celebrate "great catch" moments.** When a test catches a real bug before production, celebrate it in standup. Name the engineer. Describe what would have happened without the test. Make preventive work socially visible and rewarded. (10.4 Social reward)
- **Quarterly review.** Compare defect rates, deployment confidence (willingness to deploy on Friday), and on-call incident load before and after the testing practice change. Use the data to reinforce the value of the investment. (9.2 Pros and cons)
- **Anticipated regret prompt.** When a PR has no tests and the coverage delta is negative, the CI bot adds a non-blocking comment: "No tests for new logic. If this code causes a production incident, will you wish you had tested it?" (5.5 Anticipated regret)

## Framework observations

- **What worked: The framework correctly identified this as NOT a knowledge or values problem — and the additional lenses confirmed rather than contradicted this.** The "Weakly Realized" classification nailed it — the behavior is endorsed and understood but continually displaced. The primary blocker identification (PO + AM, not PC or RM) directed the intervention toward infrastructure and habit-building. The capability lenses (added as a completeness check) confirmed the diagnosis: engineers have generic testing knowledge but lack local procedural fluency (**1.1.2**) and hold an incomplete mental model of what "good testing" means in this codebase (**1.2.1**). Crucially, the PC finding (**1.7.6** transfer under support) confirmed that the capability gap is actually a PO gap in disguise — with proper scaffolding, the skill is already there. The social opportunity lenses surfaced a reinforcement architecture (SO **4.x**, e.g. **4.1**, **4.5**) that systematically rewards firefighting over prevention and a legitimacy problem (SO **5.x**, e.g. **5.1**, **5.3**) that makes testing feel like "not real work" under sprint pressure. These SO findings explain why the PO and AM problems were never fixed: the social system actively sustains them.

- **What worked: The motivation lenses distinguished the specific AM mechanisms at play.** It is not just "habit" — it is a combination of habit competition (**2.1**, e.g. **2.1.7**), reinforcement misalignment (**2.2**, e.g. **2.2.1**–**2.2.4**), aversive affect (**2.3**, e.g. **2.3.1**), and learned helplessness (**2.4**, e.g. **2.4.1**). Each requires a different intervention. Fixing the test infrastructure addresses **2.3** (reducing the aversive association) and **2.4** (making effort feel consequential again). Habit formation techniques (8.3) address **2.1** (building the missing context-response link). Making consequences salient (5.2) addresses **2.2** (connecting the behavior to a visible reward). Without the lens decomposition, the AM blocker would have been treated as a single problem requiring a single intervention, which would have been insufficient.

- **What worked: The BCT taxonomy added the critical insight of "graded tasks" (8.7).** Starting with "write one assertion per PR" rather than "achieve 80% coverage" is the difference between a behavior change that sticks and one that gets abandoned in week 2. The 80% target is a goal-setting problem (outcome goal) that overwhelms with its distance from current state. One assertion per PR is a behavior goal (1.1) combined with graduated difficulty (8.7) that produces early success, builds self-efficacy, and creates the repetition needed for habit formation. The taxonomy pushed the intervention design toward gradualism, which is where behavior change science consistently finds the strongest effects.

- **Tension: The framework sequences intervention functions (ER before TR before PE), but in practice the infrastructure fix (Phase 1) requires organizational investment that depends on RM at the leadership level.** An engineering manager has to prioritize "fix the test suite" over feature work — which is the same temporal discounting problem the individual engineers face, just one level up. Leadership must absorb an immediate cost (4 weeks of reduced feature velocity) for a future benefit (better testing practice). The framework handles the individual engineer's behavior change well, but it does not explicitly represent this recursive structure: the precondition for the individual intervention (a working test suite) is itself a behavior change problem at the organizational level that requires its own COM-B analysis, its own blocker identification, and its own intervention design.

- **Gap: The "Weakly Realized" state is extremely common in engineering organizations, and the framework handles it well at the diagnostic level. But the BCT taxonomy was designed for health behavior change, and some of the most powerful software-engineering interventions do not map cleanly to any single BCT.** CI gates, linters, auto-generated test scaffolds, coverage bots — these are best described as combinations of 12.1 (restructuring the physical environment) + 7.1 (prompts/cues) + RE (restriction), but the taxonomy was not designed to describe automated toolchain interventions that simultaneously restructure the environment, provide cues, and restrict competing behaviors in a single configuration change. This is a productive gap rather than a failure — it suggests the framework would benefit from a "toolchain intervention" extension for software engineering contexts, where a single tool change can implement multiple BCTs simultaneously in a way that health interventions rarely can.
