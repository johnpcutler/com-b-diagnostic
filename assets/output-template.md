# Diagnostic Output

Structured output format for a COM-B behavioral diagnosis.

---

## 1. Behavior state classification

| Field | Value |
|-------|-------|
| **State** | _S? — State Name_ |
| **Matched signals** | _List the signals from the diagnostic cycle that matched_ |
| **Rationale** | _Why this state and not an adjacent one_ |

## 2. COM-B blockers

| Priority | Code | Branch | Evidence |
|----------|------|--------|----------|
| Primary | _e.g. PC_ | _Psychological Capability_ | _What was observed_ |
| Secondary | _e.g. SO_ | _Social Opportunity_ | _What was observed_ |

## 3. Lens analysis

| COM-B code | Lens dimension | Short tag | Evidence |
|-----------|---------------|-----------|----------|
| _PC_ | _PC 1.2.3_ | _Mental-model gap in cue interpretation_ | _Observed pattern_ |
| _SO_ | _SO 4.5_ | _Norm misalignment_ | _Observed pattern_ |

## 4. Intervention functions

_Ordered by lens-driven priority._

| Priority | Function | Rationale (linked to lens dimension) |
|----------|----------|--------------------------------------|
| 1 | _e.g. Education (ED)_ | _Addresses PC 1.2.3 — actors lack mental model for..._ |
| 2 | _e.g. Environmental Restructuring (ER)_ | _Addresses SO 4.5 — current environment signals..._ |

## 5. BCTs

| Function | BCT # | Technique name | How it applies |
|----------|-------|---------------|----------------|
| _ED_ | _4.1_ | _Instruction on how to perform the behavior_ | _..._ |
| _ER_ | _12.1_ | _Restructuring the physical environment_ | _..._ |

## 6. Tool levers

| COM-B branch | Lever | Mechanism | Source |
|-------------|-------|-----------|--------|
| _PC_ | _e.g. Inline guidance at decision point_ | _ED → 4.1_ | _diagnostic cycle S?_ |
| _SO_ | _e.g. Make peer behavior visible_ | _ER → 12.5_ | _diagnostic cycle S?_ |

## 7. Phased rollout

### Phase 1 — _Name_ (weeks 1–?)

- **Focus:** _Which COM-B branches / lens dimensions_
- **Functions active:** _ED, ER_
- **BCTs:** _4.1, 12.1_
- **Levers:** _What changes_
- **Owner:** _Who_
- **Advance signal:** _What you'd observe if this phase is working_

### Phase 2 — _Name_ (weeks ?–?)

_..._

## 8. Actor profiles (if multi-actor)

_Include only if scope involves multiple actor groups._

| Actor | Target behavior | Primary COM-B blocker | Key lens dimension |
|-------|----------------|----------------------|-------------------|
| _Role A_ | _..._ | _PC_ | _PC 1.2.3_ |
| _Role B_ | _..._ | _SO_ | _SO 4.5_ |

**Interface failures:**

- _Where does Actor A's output become Actor B's input?_
- _What breaks at that handoff?_
