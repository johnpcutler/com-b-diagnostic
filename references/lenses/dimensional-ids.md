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

## Source files

Definitions and scales live in:

- [capability-lenses.md](capability-lenses.md) — `PC.*`, `PHC.*`
- [motivation-lenses.md](motivation-lenses.md) — `RM.*`, `AM.*`
- [physical-opportunity-lenses.md](physical-opportunity-lenses.md) — `PO.*`
- [social-opportunity-lenses.md](social-opportunity-lenses.md) — `SO.*`

The working copy of all IDs for assessment is in [`../../assets/assessment-form-template.md`](../../assets/assessment-form-template.md). The **Situational Orientation** section at the top of that form lists seven named patterns (no IDs) as a triage aid before dimensional analysis.

BCT definitions and technique text: [`../com-b-bcw-bct/bct-taxonomy.md`](../com-b-bcw-bct/bct-taxonomy.md).
