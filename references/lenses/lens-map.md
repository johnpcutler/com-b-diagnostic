# Lens map

This file is the entry point for all 35 sub-lenses in the COM-B diagnostic framework. Read it before opening any lens file to orient on which sub-lenses exist, what each one asks, and where to find details.

## Dimensional ID convention

Lens dimensions are cited with **dotted prefixes** so numeric segments never collide across files (e.g. PC `1.2.1` vs RM `1.2.1`).

## Prefixes

| Prefix | Lens | Pattern | Example |
|--------|------|---------|---------|
| `PC` | Psychological capability | `PC.1.{sub}.{dim}` | `PC.1.2.1` |
| `PHC` | Physical capability | `PHC.2.{sub}.{dim}` | `PHC.2.3.4` |
| `RM` | Reflective motivation | `RM.1.{sub}.{dim}` | `RM.1.3.5` |
| `AM` | Automatic motivation | `AM.2.{sub}.{dim}` | `AM.2.4.1` |
| `PO` | Physical opportunity | `PO.{section}.{dim}` | `PO.3.7` |
| `SO` | Social opportunity | `SO.{section}.{dim}` | `SO.4.1` |
| `BCT` | Behaviour Change Technique (taxonomy v1) | `BCT.{n}.{m}` | `BCT.12.1`, `BCT.7.1` |

After the prefix, every segment is separated by a **dot**. Do not glue digits to the letter (e.g. `PO1` is wrong; use `PO.1`).

## Sub-lens shortcodes

Each sub-lens has a hybrid shortcode for cross-referencing: `{prefix}-{section number}-{Name}`. The section number preserves the link to dimension IDs (e.g. `PC-1.1-Knowledge` contains `PC.1.1.*`). These appear in sub-lens headings and intervention notes. They are **not** part of dimension IDs.

| Shortcode | Sub-lens | File | Diagnostic question |
|-----------|----------|------|---------------------|
| PC-1.1-Knowledge | Declarative and Procedural Knowledge / Skill Acquisition | capability-lenses.md | Is the issue facts, concepts, procedures, or fluency? |
| PC-1.2-Models | Mental Models / Situation Models | capability-lenses.md | Are people reasoning from the right model of the system or situation? |
| PC-1.3-Judgment | Judgment and Decision Competence | capability-lenses.md | Can they make workable judgments under the real conditions of the task? |
| PC-1.4-Signal | Signal Detection and Pattern Recognition | capability-lenses.md | Can they perceive and recognize the right signals in time? |
| PC-1.5-Meta | Metacognition and Calibration | capability-lenses.md | Do they know when they do not know, and can they regulate accordingly? |
| PC-1.6-Shared | Shared Representations and Conceptual Alignment | capability-lenses.md | Are people working from compatible concepts and definitions? |
| PC-1.7-Scaffold | Supported Performance and Scaffolding | capability-lenses.md | Can they perform only with support, or independently? |
| PHC-2.1-MotorLearn | Motor Learning and Psychomotor Skill Acquisition | capability-lenses.md | How practiced and fluent is the bodily skill? |
| PHC-2.2-Coordination | Motor Control and Coordination | capability-lenses.md | How well organized and stable is the movement? |
| PHC-2.3-Fatigue | Work Physiology, Fatigue, and Recovery | capability-lenses.md | Can the behavior be sustained over time? |
| PHC-2.4-Function | Functional Motor Performance | capability-lenses.md | Can the person perform the required bodily actions at all? |
| PHC-2.5-Ergo | Physical Ergonomics as Demand Analysis | capability-lenses.md | Do the bodily demands of the task exceed the actor's sustainable capacity? |
| RM-1.1-SDT | Self-Determination Theory (SDT) | motivation-lenses.md | Is the motivation self-endorsed or mainly controlled? |
| RM-1.2-Efficacy | Self-Efficacy | motivation-lenses.md | Do people believe they can execute the behavior? |
| RM-1.3-EVC | Expectancy-Value-Cost | motivation-lenses.md | Does the behavior seem worth doing? |
| RM-1.4-Identity | Identity-Based Motivation | motivation-lenses.md | Does the behavior fit who the person is or wants to be? |
| RM-1.5-Intentions | Goal Intentions and Implementation Intentions | motivation-lenses.md | Has intention been translated into actionable plans? |
| AM-2.1-Habit | Habit Formation | motivation-lenses.md | What does the person do on autopilot? |
| AM-2.2-Reward | Reinforcement, Reward, and Wanting | motivation-lenses.md | What is being rewarded or made attractive in the moment? |
| AM-2.3-Affect | Affect and Emotion | motivation-lenses.md | What feelings pull the person toward or away from the behavior? |
| AM-2.4-Helplessness | Learned Helplessness and Perceived Uncontrollability | motivation-lenses.md | Has the person learned that trying does not matter? |
| PO-1-WorkSys | Work-System Configuration and Constraints | physical-opportunity-lenses.md | Where is the local work system misaligned for this behavior? |
| PO-2-Resource | Resource and Capacity Conditions | physical-opportunity-lenses.md | Is capacity/scheduling scarcity displacing the behavior? |
| PO-3-Workflow | Workflow and Process Architecture | physical-opportunity-lenses.md | Where do handoffs, dependencies, and queues suppress execution? |
| PO-4-Visibility | Information and State Visibility in the Environment | physical-opportunity-lenses.md | Are relevant states and consequences visible at point of action? |
| PO-5-Tooling | Tooling and Interface Affordances | physical-opportunity-lenses.md | Do tools make the behavior easy and recoverable in context? |
| PO-6-PhysEnv | Physical Environment and Ergonomic Conditions | physical-opportunity-lenses.md | Does the physical setting support sustainable execution? |
| PO-7-Control | Control Loops and Adaptive Regulation (Cybernetics) | physical-opportunity-lenses.md | Can the system sense, decide, and correct fast enough to stay stable? |
| SO-1-Norms | Norms and Normative Climate | social-opportunity-lenses.md | What does the local social reality reward or discourage? |
| SO-2-Roles | Roles, Authority, and Boundary Clarity | social-opportunity-lenses.md | Who is socially authorized to do what? |
| SO-3-Network | Network Position and Social Capital | social-opportunity-lenses.md | Who can access trust, information, and sponsorship pathways? |
| SO-4-Incentives | Incentives, Accountability, and Reinforcement Architecture | social-opportunity-lenses.md | What behavior do reward/accountability systems actually produce? |
| SO-5-Legitimacy | Legitimacy, Meaning, and Identity Safety | social-opportunity-lenses.md | Is the behavior socially legitimate and identity-safe? |
| SO-6-Power | Power, Politics, and Psychological Safety | social-opportunity-lenses.md | Is it politically safe to attempt, discuss, and improve the behavior? |
| SO-7-Governance | Governance Viability and Recursion (Viable System Lens) | social-opportunity-lenses.md | Is autonomy/coordination/governance structured to keep the behavior viable at scale? |

## Source files

Definitions and scales live in:

- [capability-lenses.md](capability-lenses.md) — `PC.*`, `PHC.*`
- [motivation-lenses.md](motivation-lenses.md) — `RM.*`, `AM.*`
- [physical-opportunity-lenses.md](physical-opportunity-lenses.md) — `PO.*`
- [social-opportunity-lenses.md](social-opportunity-lenses.md) — `SO.*`

The working copy of all IDs for assessment is in [`../../assets/assessment-form-template.md`](../../assets/assessment-form-template.md). The **Situational Orientation** section at the top of that form lists seven named patterns (no IDs) as a triage aid before dimensional analysis.

BCT definitions and technique text: [`../com-b-bcw-bct/bct-taxonomy.md`](../com-b-bcw-bct/bct-taxonomy.md).
