# Diagnostic report skeleton

Use this as the **shape** of a COM-B diagnosis output. It mirrors the pattern in [`references/scenarios/`](../references/scenarios/). The **user does not fill this in**; the agent produces a report that follows this structure.

**Purpose:** stable report shape, consistent long outputs, preserved sections, predictable formatting for any downstream use (paste into docs, tickets, or tools).

---

## Conventions

- **Lens dimensions:** cite stable IDs from the lens files (e.g. `PO 1.2`, `PC 1.3.4`, `RM 1.3.5`). PO/SO use `section.dimension`; PC/PHC/RM/AM use `sub-lens.dimension`.
- **BCW functions:** use abbreviations from the intervention mapping (e.g. `ED`, `ER`, `EN`).
- **BCTs:** cite taxonomy numbers and names (e.g. `12.1 Restructuring the physical environment`).
- **Primary blockers:** mark with `*` in digest `blockers` line where helpful.

---

## Title

```markdown
# Scenario: "<short label for the situation>"
```

One line that names the behavior-in-context (not a generic title).

---

## Intro (one sentence)

Point to the canonical pipeline, e.g. that the report follows [`references/flow.md`](../references/flow.md) and that the fenced block below is the **digest**.

---

## Digest block (required)

Immediately after the intro, a **fenced code block** with **outputs only** — no prose. Same field names as scenarios so skims and diffs stay predictable.

Use only `lenses.{branch}` keys for branches in play (omit empty branches).

```text
state      = S?: <full state name>
blockers   = <codes>; * = primary, e.g. PO* AM SO | ...
lenses.PC  = [id short-tag, ...]   # if PC in play
lenses.PHC = [...]                 # if PHC in play
lenses.PO  = [...]                 # if PO in play
lenses.SO  = [...]                 # if SO in play
lenses.RM  = [...]                 # if RM in play
lenses.AM  = [...]                 # if AM in play
functions  = <BCW order, use >> or > for emphasis if needed>
bcts       = <FUNCTION→n.n,n.n | ...>
tools      = <COM-B:token pairs or short tokens>
phases     = <e.g. [wk1-3] A+B → [wk4-8] C>
```

---

## The situation

Context-only prose: what people do or fail to do, actors, environment, recent changes. **Not** a numbered pipeline step.

---

## Step 1: Classify the behavior state

- State ID and full name (S1–S7).
- Signals from the diagnostic cycle that matched.
- Why this state and not an adjacent one (brief).

---

## Step 2: Identify COM-B blockers

- Primary blockers (with evidence tied to the situation).
- Secondary blockers (with evidence).
- Use sub-headings like **Primary blockers** / **Secondary blockers** when it helps readability.

---

## Step 3: Deepen with lenses

- Opening line listing which lens files apply and ID format reminder (optional but matches scenarios).
- One **sub-section per active COM-B branch** (e.g. `### Physical opportunity lenses`), with narrative paragraphs keyed to dimensional IDs.

---

## Step 4: Map to intervention functions

- Table or list: COM-B blockers → applicable BCW functions (from intervention mapping).
- **Consolidated priority order** of functions for this case, with rationale tied to lens dimensions.

---

## Step 5: Select BCTs

- Group by BCW function (sub-headings like `### Via ER -> Grouping 12 …`).
- For each: technique number, name, and how it applies to this case.

---

## Step 6: Tool levers

- Bulleted list of concrete tool/process/design changes.
- Key each item by COM-B branch; note mechanism where useful (still traceable to BCTs / functions).

---

## Step 7: Intervention design

- One sub-heading **per phase** (e.g. `### Phase 1: … (weeks …)`).
- Each phase: **Focus** (which functions / dimensions), concrete actions with BCT numbers, owners if known, **advance signal** (what improves if the phase works).

---

## Framework observations

Reflections **after** the diagnosis: what the framework surfaced, tensions (e.g. primary vs secondary blockers), gaps, or risks — not a repeat of Steps 1–7.
