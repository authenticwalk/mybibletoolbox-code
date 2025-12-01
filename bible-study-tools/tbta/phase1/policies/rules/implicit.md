# Implicit Information (Checklist §9)

## What is Implicit?
Information not in literal text but helpful for understanding.
- TND shows in light gray
- NASB shows in italics
- Translator can choose to include or exclude

## He1 Notation

| Type | Notation | Use |
|------|----------|-----|
| Regular implicit | `<<...>>` | Can be inferred, not literal |
| Necessary implicit | `<...>` | Grammatically required |

## Phase 2 Notation (for reference)

| Type | Notation |
|------|----------|
| Phrase implicit | `word _implicit` |
| Phrase necessary | `word _implicitNecessary` |
| Clause implicit | `(implicit-situational)` |

## Clause-Level Markers

| Marker | Use |
|--------|-----|
| `(implicit)` or `(implicit-info)` | Generic |
| `(implicit-situational)` | Inferred from situation (most common) |
| `(implicit-subaction)` | Event that must have happened |
| `(implicit-cultural)` | Ancient culture context |
| `(implicit-historical)` | Historical event |
| `(implicit-background)` | Background information |
| `(implicit-argument)` | Implicit patient clause |

## Critical Rule
**Don't make head implicit if modifiers are literal**:
- ❌ `the person _implicit [who was in that house]`
- Why? If "person" is removed, the whole phrase goes

## Passive Agents
When agent is implicit:
```
John was hit by a soldier _implicitActiveAgent
```
In He1:
```
John was hit <<by a soldier>>
```

## Placement
- Sentence implicit: marker at front
- Subordinate clause implicit: marker after some words in clause
  - `John talked to Mary [while John (implicit-situational) was in the town]`

## Examples

**Regular implicit** (can be omitted):
```
The family went to Moab <<in order to find food>>.
```

**Necessary implicit** (grammatically required):
```
<Naomi> <said>, "Go back to your mothers."
```

**Situational** (inferred from context):
```
(implicit-situational) Naomi's sons grew up.
```

**Subaction** (must have happened):
```
(implicit-subaction) The family arrived in Moab.
```

## Explain Name
Special construction for introducing names:
```
Cana named a town _explainName
```
Generates: `<<a town named>> Cana`

Why reversed? "Cana" is literal; "a town named" is implicit. If implicit removed, "Cana" stays.

## Common Mistakes

| Wrong | Right | Why |
|-------|-------|-----|
| Implicit head with literal modifier | Keep head literal | Whole phrase would be removed |
| Passive without agent | Add `<<by X>>` | Agent always required |
| Unmarked implicit | Use `<<...>>` or `<...>` | Must be marked |

