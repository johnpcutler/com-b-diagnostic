# COM-B Diagnostic Skill

A structured LLM skill for diagnosing stuck behaviors and choosing evidence-based interventions. Given a description of what people do (or fail to do), the skill traces a seven-step pipeline from behavior state → COM-B blockers → dimensional lens analysis → BCW intervention functions → named BCTs → tool/design levers → phased rollout.

Built on the COM-B model, the Behavior Change Wheel, and the BCT Taxonomy v1, with dimensional lenses drawn from SDT, NDM, SEIPS, social-norms theory, and other research traditions. Full attribution in [`credits.md`](credits.md).

## Quick start

1. Read [`SKILL.md`](SKILL.md) — the LLM orchestrator: purpose, intake, pipeline routing, output format, and guardrails.
2. Browse [`references/guide.md`](references/guide.md) — the detailed pipeline walkthrough with file connections.
3. See [`references/scenarios/`](references/scenarios/) for worked examples.

## Structure

```
SKILL.md                          # LLM instructions: intake → pipeline → output → guardrails
credits.md                        # Full credits and source lineages
references/
    guide.md                      # Pipeline walkthrough and file connections
    flow.md                       # Canonical pipeline pseudocode + field spec
    com-b-bcw-bct/                # Core COM-B / BCW / BCT reference tables
    lenses/                       # Dimensional lenses per COM-B branch
    scenarios/                    # Worked end-to-end examples
assets/
    output-template.md            # Report skeleton for diagnosis output (agent-filled)
```

## License

See [`LICENSE`](LICENSE).
