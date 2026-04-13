# Dimensional ID convention

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

| Shortcode | Sub-lens | File |
|-----------|----------|------|
| PC-1.1-Knowledge | Declarative and Procedural Knowledge / Skill Acquisition | capability-lenses.md |
| PC-1.2-Models | Mental Models / Situation Models | capability-lenses.md |
| PC-1.3-Judgment | Judgment and Decision Competence | capability-lenses.md |
| PC-1.4-Signal | Signal Detection and Pattern Recognition | capability-lenses.md |
| PC-1.5-Meta | Metacognition and Calibration | capability-lenses.md |
| PC-1.6-Shared | Shared Representations and Conceptual Alignment | capability-lenses.md |
| PC-1.7-Scaffold | Supported Performance and Scaffolding | capability-lenses.md |
| PHC-2.1-MotorLearn | Motor Learning and Psychomotor Skill Acquisition | capability-lenses.md |
| PHC-2.2-Coordination | Motor Control and Coordination | capability-lenses.md |
| PHC-2.3-Fatigue | Work Physiology, Fatigue, and Recovery | capability-lenses.md |
| PHC-2.4-Function | Functional Motor Performance | capability-lenses.md |
| PHC-2.5-Ergo | Physical Ergonomics as Demand Analysis | capability-lenses.md |
| RM-1.1-SDT | Self-Determination Theory (SDT) | motivation-lenses.md |
| RM-1.2-Efficacy | Self-Efficacy | motivation-lenses.md |
| RM-1.3-EVC | Expectancy-Value-Cost | motivation-lenses.md |
| RM-1.4-Identity | Identity-Based Motivation | motivation-lenses.md |
| RM-1.5-Intentions | Goal Intentions and Implementation Intentions | motivation-lenses.md |
| AM-2.1-Habit | Habit Formation | motivation-lenses.md |
| AM-2.2-Reward | Reinforcement, Reward, and Wanting | motivation-lenses.md |
| AM-2.3-Affect | Affect and Emotion | motivation-lenses.md |
| AM-2.4-Helplessness | Learned Helplessness and Perceived Uncontrollability | motivation-lenses.md |
| PO-1-WorkSys | Work-System Configuration and Constraints | physical-opportunity-lenses.md |
| PO-2-Resource | Resource and Capacity Conditions | physical-opportunity-lenses.md |
| PO-3-Workflow | Workflow and Process Architecture | physical-opportunity-lenses.md |
| PO-4-Visibility | Information and State Visibility in the Environment | physical-opportunity-lenses.md |
| PO-5-Tooling | Tooling and Interface Affordances | physical-opportunity-lenses.md |
| PO-6-PhysEnv | Physical Environment and Ergonomic Conditions | physical-opportunity-lenses.md |
| PO-7-Control | Control Loops and Adaptive Regulation (Cybernetics) | physical-opportunity-lenses.md |
| SO-1-Norms | Norms and Normative Climate | social-opportunity-lenses.md |
| SO-2-Roles | Roles, Authority, and Boundary Clarity | social-opportunity-lenses.md |
| SO-3-Network | Network Position and Social Capital | social-opportunity-lenses.md |
| SO-4-Incentives | Incentives, Accountability, and Reinforcement Architecture | social-opportunity-lenses.md |
| SO-5-Legitimacy | Legitimacy, Meaning, and Identity Safety | social-opportunity-lenses.md |
| SO-6-Power | Power, Politics, and Psychological Safety | social-opportunity-lenses.md |
| SO-7-Governance | Governance Viability and Recursion (Viable System Lens) | social-opportunity-lenses.md |

## Source files

Definitions and scales live in:

- [capability-lenses.md](capability-lenses.md) — `PC.*`, `PHC.*`
- [motivation-lenses.md](motivation-lenses.md) — `RM.*`, `AM.*`
- [physical-opportunity-lenses.md](physical-opportunity-lenses.md) — `PO.*`
- [social-opportunity-lenses.md](social-opportunity-lenses.md) — `SO.*`

The working copy of all IDs for assessment is in [`../../assets/assessment-form-template.md`](../../assets/assessment-form-template.md). The **Situational Orientation** section at the top of that form lists seven named patterns (no IDs) as a triage aid before dimensional analysis.

BCT definitions and technique text: [`../com-b-bcw-bct/bct-taxonomy.md`](../com-b-bcw-bct/bct-taxonomy.md).
