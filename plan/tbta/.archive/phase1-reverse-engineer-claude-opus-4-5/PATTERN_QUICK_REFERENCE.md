# TBTA Pattern Quick Reference

## All 13 Discovered Patterns - At a Glance

| # | Pattern Name | Frequency | Usage |
|---|---|---|---|
| 1 | Nested Square Brackets | 70.0% | Mark clausal groupings & logical relationships |
| 2 | Parentheses Person Clarifications | 54.4% | Disambiguate pronouns: `you(Pharisees)` |
| 3 | Parenthetical Grammatical Tags | 39.6% | Translation mood: `(imp)`, `(literal)`, `(complex)` |
| 4 | Bracketed Logical Clauses | 35.0% | Mark why/when/purpose: `[because...]`, `[so that...]` |
| 5 | Hyphenated Semantic Units | 34.6% | Compound meanings: `just-like`, `in-order-to` |
| 6 | Grammatical Function Tags | 31.8% | Translation choices & mood (overlaps #3) |
| 7 | Verb Alternative Forms | 19.2% | Meaning variants: `teaching/preach`, `save/rescue` |
| 8 | Underscore Semantic Markers | 18.4% | Flag linguistic features: `_implicit`, `_paragraph` |
| 9 | Capital Letter Suffixed Compounds | 18.0% | Semantic variants: `Good-News`, `kingdom-B` |
| 10 | Subject Reference Chains | 12.0% | Repeat subjects to avoid pronoun ambiguity |
| 11 | Dash Prefixed Explanations | 0.8% | Etymology notes: `-Footnote Levi means near` |
| 12 | Double Quote Closures | 0.6% | Mark speech end: `"text here""` |
| 13 | Means Definition Statements | 0.6% | Define names: `Name means [definition]` |

---

## Pattern Categories by Function

### STRUCTURAL MARKERS (70%)
- **Nested Square Brackets**: `[main [subordinate]]`
- **Bracketed Logical Clauses**: `[because/when/so that...]`

### DISAMBIGUATION (54%)
- **Parentheses Person Clarifications**: `pronoun(PersonName)`
- **Subject Reference Chains**: Repeat subjects instead of pronouns

### TRANSLATION GUIDANCE (40%)
- **Parenthetical Grammatical Tags**: `(imp)`, `(title)`, `(literal)`, `(dynamic)`, `(complex)`, `(simple)`
- **Grammatical Function Tags**: Same as above
- **Verb Alternative Forms**: `verb1/verb2`

### SEMANTIC PRECISION (35%)
- **Hyphenated Semantic Units**: `concept-phrase-unit`
- **Capital Letter Suffixed Compounds**: `word-X` where X is letter variant
- **Underscore Semantic Markers**: `_implicit`, `_paragraph`, `_hyperbolic`, etc.

### SPECIALIZED NOTATION (<1%)
- **Dash Prefixed Explanations**: `-Footnote text`
- **Double Quote Closures**: `text""`
- **Means Definition Statements**: `X means [Y]`

---

## Common Underscore Markers

| Marker | Meaning | Usage |
|---|---|---|
| `_implicit` | Content reader must infer | Unstated but contextually clear |
| `_paragraph` | Structural division | Beginning of new section |
| `_hyperbolic` | Rhetorical device | Not to be interpreted literally |
| `_implicitNecessary` | Grammatically required but unstated | Required by target language grammar |
| `_implicitActiveAgent` | Subject of action not named | "was done [by X]" pattern |
| `_plural` | Grammatical number | Group interpretation |
| `_dual` | Exactly two | Specific to dual-number languages |
| `_generic` | Generic/non-specific | "A person did..." vs "John did..." |
| `_singular` | Single item | Specific to singular reference |
| `_incl` | Inclusive language | Speaker included in group |
| `_instrument` | Means of action | "with X" or "by means of X" |
| `_descriptive` | Descriptive not restrictive | Which clause vs that clause |
| `_1stAs3rd` | First person described as third | Special perspective shift |
| `_metonymy` | Figure of speech | Container for content, etc. |
| `_excl` | Exclusive language | Speaker excluded from group |
| `_frameInferable` | Context makes meaning clear | Can be inferred from surrounding frame |
| `_implicitExplainName` | Etymology implicit in name | Name meaning derivable from content |

---

## Parenthetical Tag Categories

### Grammatical Mood
- `(imp)`: Imperative
- `(title)`: Section heading/title

### Translation Approach
- `(literal)`: Word-for-word translation
- `(dynamic)`: Meaning-for-meaning translation

### Sentence Structure
- `(complex)`: Multi-clause construction
- `(simple)`: Single clause or simplified
- `(paragraph)`: Paragraph-level structural marker

### Specialized Discourse
- `(footnote)`: Annotation or note
- `(implicit-situational)`: Situation makes meaning clear
- `(implicit-info)`: Information context makes clear

---

## Pattern Nesting Examples

```
Simple bracketing:
[When X happens] Y occurs

Nested bracketing (showing hierarchy):
[When X [that shows Z]] Y occurs

Person clarification + bracketing:
The king(Saul) wanted [to help David]

Full complexity:
_paragraph You(David) [must not [cross the river(Jordan)]]

Verb alternatives with semantic markers:
Jesus was _hyperbolic teaching/preaching [so that people(crowds) would believe]

Capital suffix with underscore:
Jesus proclaimed the _implicit Good-News [about God [ruling (imp) people]]
```

---

## Frequency Impact for Implementation

**Must implement** (70%): Nested square brackets
**Should implement** (50%+): Person clarifications, grammatical tags
**Recommend** (30%+): Logical clause marking, hyphenated units
**Consider** (10-20%): Underscore markers, verb alternatives
**Specialized use** (<1%): Etymology, definitions, quote closures

---

## Pattern Combinations

Most verses use **multiple patterns together**:

- Brackets (70%) + Person clarifications (54%) = ~40-50% combined
- Tags (40%) + Brackets (70%) = ~30-40% combined
- Hyphenated units (35%) + Brackets (70%) = ~25-30% combined

This suggests TBTA encoding layers patterns for maximum semantic precision.

---

## Quick Lookup by Marker

| Symbol | Pattern | Purpose |
|---|---|---|
| `[...]` | Square brackets | Clausal grouping, logical relationships |
| `(...)` | Parentheses | Person/subject clarification, grammatical tags |
| `_word` | Underscore prefix | Linguistic feature markers |
| `word-X` | Capital suffix | Semantic variants |
| `verb/verb` | Slash notation | Alternative forms |
| `-word` | Dash prefix | Explanatory notes/footnotes |
| `""` | Double quotes | Speech/quote closure |
| `means` | Literal word | Definition/etymology |
