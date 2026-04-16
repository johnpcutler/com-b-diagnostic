# Change Lenses and Actions

Someone isn't doing the thing — and you can't figure out why.

Maybe that someone is you. Maybe you're designing a product and users aren't completing onboarding. Maybe you're trying to help a team of eight adopt a practice — or shift how a thousand people work. You've tried reminders, trainings, nudges, new tools — nothing sticks.

Whatever the scale, the pattern is familiar: something isn't happening, and the obvious fixes haven't worked. This skill helps you understand *why* — look at the problem through multiple lenses — and design actions that might actually help.

Describe what's stuck to your AI agent. It runs a structured diagnostic grounded in the COM-B model, the Behavior Change Wheel, and the BCT Taxonomy v1, and returns a phased plan.

### How it works

1. **Define the behavior** — pin down who should do what, how often, in what context, and what's been tried before ([`behavior-canvas.md`](assets/behavior-canvas.md))
2. **Research through four lenses** — capability (knowledge, skill, judgment), physical opportunity (tools, workflow, environment), social opportunity (norms, incentives, power), and motivation (identity, habit, affect) — each with its own dimensional scales ([`references/lenses/`](references/lenses/))
3. **Synthesize in a practitioner worksheet** — rank C / O / M, build per-lens narrative, identify cross-lens tensions and leverage, rank BCW intervention functions with rationale and BCTs ([`practitioner-worksheet.md`](assets/practitioner-worksheet.md))
4. **Map to interventions** — refine the BCW ranking against the full BCT taxonomy (under the hood)
5. **Deliver a summary** — plain-language insights first; the agent then asks for your reaction before going deeper
6. **Feedback loop** — if you add context (prior failures, political dynamics, corrections), the canvas updates and the lens analysis re-runs with the richer picture
7. **Phase B on request** — in-depth report, action plan, or the working analysis behind the diagnosis

Full pipeline: [`references/flow.md`](references/flow.md). Lens index: [`lens-map.md`](references/lenses/lens-map.md).

Full attribution in [`credits.md`](credits.md).

---

## Install

### Quick install with `npx skills`

Install with a single command using the [Skills CLI](https://github.com/vercel-labs/skills). It auto-detects your coding agents and sets everything up:

```bash
npx skills add johnpcutler/change-lenses-and-actions
```

You can also target specific agents or install globally:

```bash
# Install to specific agents
npx skills add johnpcutler/change-lenses-and-actions -a claude-code -a cursor

# Install globally (available across all projects)
npx skills add johnpcutler/change-lenses-and-actions -g
```

### Cursor

Copy this folder into your skills directory:

```bash
# Project-level (shared with collaborators)
cp -r . .cursor/skills/com-b-diagnostic/

# Or user-level (available across all projects)
cp -r . ~/.cursor/skills/com-b-diagnostic/
```

Cursor auto-discovers `SKILL.md` from `.cursor/skills/` or `~/.cursor/skills/`. The agent will activate when you describe a stuck behavior.

### Claude Code

Copy this folder into your skills directory:

```bash
# Project-level
cp -r . .claude/skills/com-b-diagnostic/

# Or user-level
cp -r . ~/.claude/skills/com-b-diagnostic/
```

### GitHub Copilot

Copy the contents of [`SKILL.md`](SKILL.md) into `.github/copilot-instructions.md` in your repo, or place this folder under `.github/instructions/` and reference it from there.

### Claude (claude.ai)

Create a **Project**, then upload the files from this repo as project knowledge. Paste the contents of [`SKILL.md`](SKILL.md) into the project's custom instructions.

### Other agents

Any agent that supports custom instructions or system prompts can use this skill. Point it at [`SKILL.md`](SKILL.md) as the orchestrator and make the `references/` files available as context.

---

## Usage

Describe the behavior you want diagnosed. Include what people should be doing, what they're actually doing, and any relevant context about the environment. The more texture you provide, the better the diagnosis. Example:

> We want engineers to write tests alongside new features, but coverage has been stuck at 30% for a year. Everyone agrees testing matters — it's in our engineering principles, it comes up in every retro. But when sprint pressure hits, tests are the first thing cut. The test suite itself is slow (8 min) and about 10% of runs fail from flaky tests, so people have learned to ignore red CI. There's no protected time for testing, and the velocity dashboard only tracks PRs merged.

The agent will ask follow-up questions if it needs more detail on the target behavior, current reality, actors, or scope.

---

## Exploring the framework

You're also welcome to read the source files directly:

- [`SKILL.md`](SKILL.md) — the LLM orchestrator (purpose, intake, pipeline, output format, guardrails)
- [`references/guide.md`](references/guide.md) — detailed pipeline walkthrough with file connections
- [`references/flow.md`](references/flow.md) — canonical pipeline as pseudocode
- [`references/com-b-bcw-bct/`](references/com-b-bcw-bct/) — core COM-B / BCW / BCT reference tables
- [`references/lenses/`](references/lenses/) — dimensional lenses per COM-B branch
- [`assets/output-template.md`](assets/output-template.md) — report skeleton the agent fills in
- [`credits.md`](credits.md) — full credits and source lineages

## License

[MIT](LICENSE)
