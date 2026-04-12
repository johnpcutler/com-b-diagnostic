# COM-B Diagnostic Skill

Diagnose stuck behaviors and design evidence-based interventions. Give your AI agent a description of what people do (or fail to do), and it runs a six-step pipeline: behavior state → COM-B blockers → dimensional lens analysis → BCW intervention functions → named BCTs → phased intervention design.

Built on the COM-B model, the Behavior Change Wheel, and the BCT Taxonomy v1. Full attribution in [`credits.md`](credits.md).

---

## Install

Clone or download this repo, then point your tool at the skill directory.

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

### ChatGPT

Create a **GPT** or use **Custom Instructions**. Paste the contents of [`SKILL.md`](SKILL.md) as the system prompt, and upload the `references/` folder contents as knowledge files.

### Other agents

Any agent that supports custom instructions or system prompts can use this skill. Point it at [`SKILL.md`](SKILL.md) as the orchestrator and make the `references/` files available as context.

---

## Usage

Describe a behavior that is stuck, inconsistent, or contested. The agent runs the pipeline and produces a structured diagnostic report. Example prompts:

- "Why aren't engineers writing tests even though everyone agrees they should?"
- "Diagnose why our teams aren't doing continuous discovery"
- "What's blocking adoption of code review best practices?"

---

## Exploring the framework

You're also welcome to read the source files directly:

- [`SKILL.md`](SKILL.md) — the LLM orchestrator (purpose, intake, pipeline, output format, guardrails)
- [`references/guide.md`](references/guide.md) — detailed pipeline walkthrough with file connections
- [`references/flow.md`](references/flow.md) — canonical pipeline as pseudocode
- [`references/scenarios/`](references/scenarios/) — four worked end-to-end examples
- [`references/com-b-bcw-bct/`](references/com-b-bcw-bct/) — core COM-B / BCW / BCT reference tables
- [`references/lenses/`](references/lenses/) — dimensional lenses per COM-B branch
- [`assets/output-template.md`](assets/output-template.md) — report skeleton the agent fills in
- [`credits.md`](credits.md) — full credits and source lineages

## License

[MIT](LICENSE)
