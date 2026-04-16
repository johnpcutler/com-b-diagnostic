# Behavior Canvas

A structured template for defining the target behavior before diagnosis. Fill this out (or have the agent fill it from your description) before proceeding to dimensional analysis.

## Fields

| Field | Question it answers | If unclear, ask about... |
|-------|--------------------|--------------------------| 
| **Behavior** | What is the behavior? (summary statement) | Can you state in one sentence what people should be doing? |
| **Who** | Who are the actors? | Is this one role or multiple? Do different actors face different conditions? |
| **Will do what** | What specific action should they perform? | What does "doing it" look like concretely? What are the observable steps? |
| **To what extent** | How often, how deeply, to what observable standard? | What frequency, quality bar, or completeness threshold counts as "doing it"? |
| **In what context** | What environment, tools, constraints? | Where does this happen? What tools are involved? What time/resource constraints exist? |
| **For what outcome** | What result should this produce? | What changes if this behavior happens consistently? How would you know? |
| **Current state** | Where does the behavior sit right now? (optional) | See pattern vocabulary below. |
| **Prior attempts** | What has been tried that didn't work? (optional) | What interventions, fixes, or workarounds have been attempted? Why did they fail or fall short? |
| **Relevant context** | Which optional static context should inform diagnosis? (optional) | Which files in `user-context/` matter here (for example, `user-context/team-context-platform.md`)? Which level matters most: org, team, role? |

## Pattern vocabulary for Current state

These are optional labels for describing where the behavior sits. They are orientation, not diagnostic findings.

| Pattern | Signal |
|---------|--------|
| Fully Realized & Stable | Ritualized, reliable, trusted — but may hide cost or block improvement |
| Realized but Friction-Filled | Mandatory but painful; the environment fights it |
| Partially Realized / Inconsistent | Exists in pockets; lacks alignment or consistency |
| Weakly Realized | Agreed and valued, but continually displaced by competing priorities |
| Aspirational Only | Identity-level desire without practice, infrastructure, or defined skill |
| Actively Suppressed | Systemic forces (political, structural, incentive-based) prevent the behavior |
| Contested / Undefined | No shared definition; conceptual ambiguity about what the behavior even is |

## Example

> **Behavior:** Regularly review and analyze key performance metrics
> **Who:** Product teams
> **Will do what:** Conduct regular, in-depth reviews and analyses of key performance metrics
> **To what extent:** In a weekly meeting, dedicating time to discuss trend patterns and metric shifts and identify both routine and special variations in the data
> **In what context:** Using a centralized data dashboard that includes tools like Process Behavior Charts (PBCs) and Statistical Process Control (SPC), accessible to all team members
> **For what outcome:** To pinpoint areas for improvement, ensure data-driven insights inform product decisions and align actions with business objectives
> **Current state:** Weakly Realized — everyone agrees metrics matter, but sprint pressure displaces the review every time
> **Prior attempts:** Tried a "metrics Monday" standing meeting — attendance dropped after 3 weeks. Also added a dashboard link to Slack — people click it but don't discuss what they see. The team lead thinks the issue is motivation, but the dashboard is hard to read and nobody was trained on SPC.
> **Relevant context:** See `user-context/team-context-platform.md` and `user-context/org-context-enterprise.md` (org and team context are most relevant because cross-team handoffs shape who can act on metric insights).
