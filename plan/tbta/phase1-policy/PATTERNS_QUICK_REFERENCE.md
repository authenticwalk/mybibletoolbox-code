# TBTA Linguistic Patterns - Quick Reference

## Underscore Markers (Semantic & Grammatical)

| Pattern | Frequency | Purpose |
|---------|-----------|---------|
| `_implicit` | 23.6% | Mark unstated but inferable information |
| `_implicitActiveAgent` | 5.6% | Mark implied agent in passive voice |
| `_implicitNecessary` | 5.0% | Mark context-required inferences |
| `_implicitType` | 2.2% | Mark implicit type/category reference |
| `_frameInferable` | 2.4% | Mark frame-based inference |
| `_generic` | 2.0% | Mark generic/non-specific plurals |
| `_descriptive` | 2.0% | Mark descriptive vs. identifying appositives |
| `_paragraph` | 7.2% | Mark paragraph structure |
| `_dual` | 3.0% | Mark exactly two entities |
| `_metonymy` | 1.2% | Mark figurative language (part for whole) |
| `_routinely` | 1.2% | Mark habitual/characteristic actions |
| `_morally` | 0.6% | Mark ethically evaluated actions |
| `_newSense` | 0.6% | Mark semantic shift/metaphorical use |

---

## Parenthetical Markers (Clarification & Commentary)

| Pattern | Frequency | Purpose |
|---------|-----------|---------|
| `(role)` | 42.8% | Clarify pronoun referent by role: (priests), (man), (Jesus) |
| `(imp)` | 15.8% | Mark imperative mood commands |
| `(literal)` / `(dynamic)` | 5.2% | Mark translation approach |
| `(rhetorical)` / `(yesrhetorical)` | 5.2% | Mark rhetorical questions |
| `(implicit-situational)` | 4.4% | Mark situation-dependent context |
| `(title)`, `(footnote)`, `(paragraph)` | Variable | Mark structural elements |

---

## Bracketing & Delimiter Patterns

| Pattern | Frequency | Purpose |
|---------|-----------|---------|
| `[relative clause]` | 90.8% | Delimit relative clauses & embedded structures |
| `[that...]` | Very high | Mark relative clauses |
| `[so that...]` | Very high | Mark purpose clauses |
| `[because...]` | Very high | Mark causal clauses |
| `[when/while...]` | High | Mark temporal clauses |
| `[if/unless...]` | High | Mark conditional clauses |

---

## Word & Concept Modification Patterns

| Pattern | Frequency | Purpose |
|---------|-----------|---------|
| `word/alternative` | 23.0% | Present translation options: followers/disciples, spirits/demons |
| `hyphenated-compound` | 21.8% | Unify multi-word concepts: in-front-of, get-up, each-other |
| `-A, -B, -C, -D` suffixes | 12.2% | Disambiguate repeated concepts in same verse |
| `possessive(referent)'s` | 27.6% | Expand possessive pronouns: your(Abraham's), I(Jesus)'s |

---

## Discourse Structure Markers

| Pattern | Frequency | Purpose |
|---------|-----------|---------|
| `Thus`, `So`, `Then`, `But`, `Because` | 39.0% | Explicit discourse connectives marking logical/temporal relationships |

---

## Most Common Marker Combinations (Interactions)

```
[clause _implicit]                          # Bracket + implicit marker
us(role)                                    # Slash + role marker
[relative clause [nested clause]]           # Nested brackets
(imp) You(role)                             # Imperative + role marker
word-A... word-A                            # Letter suffix for disambiguation
followers/disciples... (followers)          # Slash + role marker
```

---

## Quick Lookup by Use Case

### For Pronoun Resolution
- Role markers: `(priests)`, `(man)`, `(Jesus)` (42.8%)
- Possessive expansion: `your(Abraham's)`, `I(Jesus)'s` (27.6%)

### For Complex Syntax
- Square brackets: `[embedded structures]` (90.8%)
- Nested brackets: `[[multiple levels]]` (common)

### For Implicit Information
- `_implicit` marker (23.6%)
- `_implicitActiveAgent` for passive voice (5.6%)
- `_implicitNecessary` for required context (5.0%)

### For Translation Variation
- Slash alternatives: `followers/disciples` (23.0%)
- Translation type: `(literal)` vs `(dynamic)` (5.2%)

### For Ambiguity Resolution
- Letter suffixes: `covered-A`, `covered-B` (12.2%)
- Role clarification: `(priests)`, `(officials)` (42.8%)

### For Semantics
- `_generic` for non-specific plurals (2.0%)
- `_descriptive` for appositive type (2.0%)
- `_metonymy` for figurative language (1.2%)
- `_newSense` for semantic shift (0.6%)

---

## Processing Priority (Highest to Lowest Impact)

1. **Square brackets** (90.8%) - Parse embedded structures first
2. **Role markers** (42.8%) - Resolve pronouns second
3. **Discourse markers** (39.0%) - Establish logical flow
4. **Possessive expansion** (27.6%) - Clarify possessive relations
5. **Slash alternatives** (23.0%) - Handle lexical variation
6. **_implicit markers** (23.6%) - Flag inference requirements
7. **Hyphenated compounds** (21.8%) - Treat as semantic units
8. **Imperative (imp)** (15.8%) - Mark command structures
9. **Letter suffixes** (12.2%) - Track repeated concepts
10. **_paragraph markers** (7.2%) - Track structure
11. **All other patterns** - Handle as needed

---

## Field Application Examples

### Example 1: Complex Role Resolution
```
"[us(followers) _excl prepare-B the Passover of the meal _metonymy
[so that you(Jesus) and we(followers) _implicit could eat that meal _implicit]]"
```
Patterns used: brackets, role markers, exclusive marker, letter suffix, metonymy, implicit markers

### Example 2: Passive Voice with Implicit Agent
```
"The servant of the Lord-A was treated badly _implicitActiveAgent by [people _implicitActiveAgent]"
```
Patterns used: letter suffix, implicit agent markers

### Example 3: Rhetorical Structure
```
"(yesrhetorical) Is this man the person [who builds things with wood]?
(statement) This man is only-C _implicit the person [who builds things with wood]"
```
Patterns used: parenthetical commentary, brackets, letter suffix, implicit marker

### Example 4: Conditional with Nested Clauses
```
"[Because Pilate wanted [to satisfy that crowd],] Pilate freed Barabbas for-C that crowd.
Then Pilate ordered [soldiers _implicitNecessary to whip Jesus]"
```
Patterns used: nested brackets, letter suffix, implicit marker, conjunction

---

## Pattern Statistics Summary

- **Total patterns identified:** 23
- **Patterns in 3+ verses (threshold):** 23
- **Most common pattern:** Square brackets (90.8%)
- **Most important for AI:** Role markers (42.8%) & Square brackets (90.8%)
- **Most fine-grained:** Underscore markers (13 subtypes)
- **Most frequent class:** Parenthetical markers (42.8-7.2%)
- **Average verse complexity:** 3-5 distinct patterns per verse
- **Cumulative coverage:** Covers ~95% of annotation needs in dataset
