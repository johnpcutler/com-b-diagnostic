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
| `S` | Behavior-state lens | `S.{state}` or `S.{state}.{dim}` | `S.3`, `S.3.4` |
| `BCT` | Behaviour Change Technique (taxonomy v1) | `BCT.{n}.{m}` | `BCT.12.1`, `BCT.7.1` |

After the prefix, every segment is separated by a **dot**. Do not glue digits to the letter (`S1` is wrong; use `S.1`).

**Note:** COM-B uses “B” for the *behavior* construct. IDs starting with **`S`** refer to the **behavior-state lens** (lifecycle / maturity position), not the generic COM-B behavior term.

## Source files

Definitions and scales live in:

- [behavior-lenses.md](behavior-lenses.md) — `S.*`
- [capability-lenses.md](capability-lenses.md) — `PC.*`, `PHC.*`
- [motivation-lenses.md](motivation-lenses.md) — `RM.*`, `AM.*`
- [physical-opportunity-lenses.md](physical-opportunity-lenses.md) — `PO.*`
- [social-opportunity-lenses.md](social-opportunity-lenses.md) — `SO.*`

The working copy of all IDs for assessment is in [`../../assets/assessment-form-template.md`](../../assets/assessment-form-template.md).

BCT definitions and technique text: [`../com-b-bcw-bct/bct-taxonomy.md`](../com-b-bcw-bct/bct-taxonomy.md).
