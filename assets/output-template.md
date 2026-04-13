# Output template

Use this as the **shape** of a COM-B diagnosis output. The **user does not fill this in**; the agent produces output that follows this structure.

**Purpose:** stable output shape, phased delivery, consistent formatting for downstream use (paste into docs, tickets, or tools).

---

## Conventions

- **Lens dimensions:** cite stable IDs from the lens files (e.g. `PO.1.2`, `PC.1.3.4`, `RM.1.3.5`). PO/SO use `PO.n.m` / `SO.n.m`; PC/PHC use `PC.1.x.y` / `PHC.2.x.y`; RM/AM use `RM.1.x.y` / `AM.2.x.y`. See [`references/lenses/lens-map.md`](references/lenses/lens-map.md).
- **BCW functions:** use abbreviations from the intervention mapping (e.g. `ED`, `ER`, `EN`).
- **BCTs:** cite **`BCT.n.m`** IDs and names (e.g. `BCT.12.1 Restructuring the physical environment`).

---

## Phase A: Summary and key insights (always delivered first)

### Behavior definition

Restate the structured behavior definition from Step 1:

- **Behavior:** ...
- **Who:** ...
- **Will do what:** ...
- **To what extent:** ...
- **In what context:** ...
- **For what outcome:** ...

### Summary

1–2 paragraphs in plain language. No taxonomy codes. Answers "what's going on and what should I do?" as a trusted advisor would. Covers:
- The core dynamic: what's preventing this behavior
- The highest-leverage area for intervention
- The recommended direction (not detailed steps — that's Phase B)

### Key insights

3–5 bullet points. Each is a specific finding — a tension, surprise, or highest-leverage point the diagnosis surfaced. Written so the user could repeat them to a colleague.

### Offer

After delivering Phase A, offer the user three paths:

> I can go deeper in three ways:
> - **In-depth report** — the full diagnostic with dimensional assessments, cross-lens analysis, and the BCW/BCT reasoning behind these recommendations
> - **Action plan** — a concrete, phased plan with specific changes, owners, and success signals
> - **Working analysis** — the practitioner worksheet showing how I got from lens findings to ranked interventions
>
> Which would be most useful? (You can also ask for more than one.)

---

## Phase B — Option 1: In-depth report

### Digest block

A fenced code block with compressed outputs — no prose. For quick scanning and diffing.

```text
dimensions = <top dimensional findings, e.g. PC.1.2.1 low, PO.2.7 high, SO.4.1 low>
tensions   = <cross-lens tensions, e.g. "C present but M absent">
leverage   = <highest-leverage dimensions>
functions  = <BCW function priority order>
bcts       = <FUNCTION→BCT.n.m,BCT.n.m | ...>
```

### Step 2: Lens analysis

One sub-section per active lens:

#### Capability findings
- Relevant dimensions with positions and evidence
- Sub-headings by sub-lens if multiple are active (e.g. `##### Mental models`, `##### Judgment`)

#### Opportunity findings
- Physical opportunity (PO) dimensions with positions and evidence
- Social opportunity (SO) dimensions with positions and evidence

#### Motivation findings
- Reflective motivation (RM) dimensions with positions and evidence
- Automatic motivation (AM) dimensions with positions and evidence

### Step 3: Cross-lens assessment

- Tensions between lenses (with dimension IDs)
- Reinforcements between lenses
- Prioritization: which findings are highest-leverage and why

### Step 4: BCW and BCT reasoning

- Table or list: dimensional findings → BCW functions (from practitioner worksheet ranking + base mapping)
- Consolidated priority order of functions with rationale
- Named BCTs per function with how each applies to this case

### Framework observations

Reflections after the diagnosis: what the framework surfaced, tensions, gaps, or risks — not a repeat of earlier sections.

---

## Phase B — Option 2: Action plan

### Phased rollout

One sub-section per phase (e.g. `### Phase 1: ... (weeks 1–3)`).

Each phase includes:
- **Focus:** which forces this phase addresses (in plain language, with dimension IDs parenthetical)
- **Concrete changes:** specific actions — tools, process changes, environment changes, social structures
- **Who owns it:** roles or teams responsible
- **Success signals:** what improves if this phase works; how to know it's time to advance

### Tool and AI recommendations

- Specific tools, AI capabilities, or framework mappings that support the plan
- How they connect to the intervention strategy

### Risks and watchpoints

- What could go wrong
- What signals would indicate the plan needs adjustment
- Regression risks (especially where the situational pattern could slide back)

---

## Phase B — Option 3: Working analysis

Reproduce the filled-out practitioner worksheet. This is the
intermediate reasoning that connects lens findings to the BCW
ranking and intervention design. Include all five sections:

1. COM-B priority ranking
2. Per-lens synthesis (tables + narrative)
3. Cross-lens interactions
4. BCW function ranking (with rationale and BCTs)
5. Intervention implications
