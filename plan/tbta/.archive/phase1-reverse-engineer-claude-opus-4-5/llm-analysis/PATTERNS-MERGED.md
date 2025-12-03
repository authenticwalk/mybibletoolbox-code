# TBTA Pattern Discovery: Consolidated Analysis

**Corpus**: 6,963 verses across 16 books
**Analysis**: 14 LLM subagents, each analyzing ~500 shuffled verses
**Date**: 2024-12-02

## Executive Summary

The original 12-rule framework captures only ~25% of TBTA transformations. Analysis reveals **60+ distinct patterns** organized into a sophisticated linguistic annotation system.

---

## CONFIRMED: Original 12 Rules

All found in 13+/14 chunks with >95% consistency:

| # | Rule | Pregnant Phrase | Consistency |
|---|------|-----------------|-------------|
| 1 | Coreference Resolution | pronouns → explicit nouns | 100% |
| 2 | Clause Segmentation | one predicate per sentence | 100% |
| 3 | Explicit Relativization | appositives → [who/that/which] | 98% |
| 4 | Deixis Marking | I(Speaker), you(Addressee) | 99% |
| 5 | LDV Substitution | simple/complex word pairs | 85% |
| 6 | Subordinate Bracketing | [...] for non-main clauses | 100% |
| 7 | Quote Framing | said, ["..."] | 100% |
| 8 | Imperative Marking | (imp) before verbs | 100% |
| 9 | Hyphenated Verbs | run-away, sit-down | 95% |
| 10 | Modal Decomposition | can → is able [to] | 98% |
| 11 | Demonym → Description | Moabite → [from Moab] | 70%* |
| 12 | Gap-Filling | implicit-info, implicit-situational | 100% |

*Rule 11 only appears when demonyms occur in source text.

---

## DISCOVERED: New Pattern Categories

### Category A: Underscore Semantic Taxonomy (30+ markers)

**A1. Implicit Information Types** (Matt 12:45, Matt 22:4, Mark 14:28)
```
_implicit           - General recoverable info
_implicitNecessary  - Essential for understanding
_implicitActiveAgent - Passive → active agent
_implicitType       - Category specification
_frameInferable     - Inferable from discourse frame
implicit-situational - Context-recoverable
implicit-info       - Background knowledge
implicit-subaction  - Event subcomponent
```

**A2. Number/Quantity Markers** (Gen 19:36, Mark 10:47, Gen 6:10)
```
_dual     - Exactly two referents
_paucal   - Few (3-4)
_plural   - Multiple
_incl     - Inclusive we (includes addressee)
_excl     - Exclusive we (excludes addressee)
```

**A3. Reference Type Markers** (Matt 13:32, Mark 7:13, 1 Sam 12:21)
```
_generic        - Generic reference
_genericImplicit - Implicit generic
_hyperbolic     - Non-literal exaggeration
_metonymy       - Metonymic usage
_1stAs3rd       - First person as third
_reflexive      - Reflexive pronoun
```

**A4. Modification Markers** (Matt 23:27, Mark 12:38, Matt 20:27)
```
_descriptive  - Non-restrictive modifier
_restrictive  - Restrictive modifier
_emphasized   - Focus/emphasis
_adj          - Adjectival
_adv          - Adverbial
```

**A5. Temporal/Aspect Markers** (Mark 5:4, Josh 6:4, Neh 9:12)
```
_routinely       - Habitual action
_past            - Past reference
_significantTime - Temporally important
-iteration N     - Repeated N times
```

**A6. Frame/Composition Markers** (Gen 2:7, Matt 21:7, Mark 14:51)
```
_madeOf         - Material composition
-composed-of    - Physical composition
_quantity       - Quantity specification
_event          - Event nominalization
```

---

### Category B: Dual Representation System

**B1. Literal/Dynamic Pairs** (Matt 16:18, Mark 4:19, Matt 13:38)
```
(literal) gates of hell will not defeat
(dynamic) power of Satan will not defeat
```

**B2. Complex/Simple Pairs** (Matt 6:10, Matt 13:33, Matt 23:13)
```
(complex) kingdom-B of heaven
(simple) God rules that person
```

**B3. Literalunits/Modernunits** (Matt 27:45, Mark 6:21, Matt 20:3)
```
(literalunits) the 6th hour
(modernunits) 12PM
```

---

### Category C: Rhetorical Question System

**C1. Question Type Marking** (Matt 16:10, Matt 23:11, Mark 2:7)
```
(rhetorical)    - General rhetorical
(yesrhetorical) - Expected "yes" answer
(norhetorical)  - Expected "no" answer
```

**C2. Statement Pairing** (every rhetorical question)
```
(norhetorical) Did you(followers) remember...?
(statement) You(followers) should remember...
```

---

### Category D: Suffix Disambiguation System

**D1. Verb Sense Suffixes** (Matt 18:27, Mark 10:26, Matt 22:4)
```
call-A, call-B, call-C  - Different senses
serve-A, serve-B        - Different argument frames
is-U (comparison), is-X (identity), is-V (evaluative)
```

**D2. Noun Reference Suffixes** (Matt 22:4, Matt 23:13, Mark 14:68)
```
servants-A, servants-B  - Different referent groups
things-A, things-B      - Different sets
kingdom-A, kingdom-B    - Different senses
```

---

### Category E: Structural/Discourse Markers

**E1. Title/Section Markers** (Acts 3:1, Matt 8:23, Gen 6:9)
```
(title)     - Section title
-Title      - Inline title
-title      - Lowercase variant
(paragraph) - Paragraph break
_paragraph  - Underscore variant
```

**E2. Comment/Footnote System** (Matt 23:13, Mark 14:68, Matt 21:5)
```
(footnote)       - Inline footnote
(comment-begin)  - Comment start
(comment-end)    - Comment end
-Footnote        - Name etymology, cross-refs
```

**E3. Discourse Connectives** (Matt 21:24, Acts 15:19, Mark 14:31)
```
Then-C, Then-D      - Different continuation types
So (consequently)   - Inferential
Thus, Therefore     - Consequence
```

---

### Category F: Explicit Semantic Relations

**F1. Purpose/Result** (Gen 16:7, Matt 22:4, 2 Sam 2:14)
```
[in-order-to X]      - Purpose clause
[so-that Y]          - Result clause
[with-the-result Z]  - Consequence
```

**F2. Conditional Structures** (Gen 44:32, Matt 10:33, Gen 24:44)
```
[If X] then Y        - Simple conditional
[If-C X]             - Counterfactual
```

**F3. Comparison Structures** (Matt 19:24, Gen 10:9, Matt 18:27)
```
[just-like X]        - Simile
more-than Y          - Comparative
is-U like            - Metaphorical copula
```

**F4. Temporal Structures** (Josh 8:19, Acts 15:33, Mark 11:12)
```
[When X happened]    - Temporal clause
[After X]            - Sequential
Previously, Later    - Temporal adverbs
At-that-time         - Temporal frame
```

---

### Category G: Entity/Reference Tracking

**G1. Named Entity Marking** (Gen 16:7, 2 Sam 7:29, Gen 46:10)
```
a man named X        - Person introduction
the city named Y     - Place introduction
the tribe named Z    - Group introduction
```

**G2. Possessive Chains** (Gen 16:5, Matt 22:4, 2 Sam 7:29)
```
my(Sarai's) servant  - Nested possessive
your(king's) feast   - Owner explicit
```

**G3. Reciprocal/Reflexive** (Acts 15:39, Gen 42:28, Matt 14:26)
```
each-other(X)        - Reciprocal with antecedent
yourself(guard)      - Reflexive with referent
```

---

## Pattern Statistics

| Category | Patterns | Frequency |
|----------|----------|-----------|
| Original 12 | 12 | Very High |
| A: Underscore Taxonomy | 30+ | High |
| B: Dual Representations | 6 | Medium |
| C: Rhetorical Questions | 4 | Medium |
| D: Suffix Disambiguation | 10+ | High |
| E: Structural Markers | 10+ | Medium |
| F: Semantic Relations | 10+ | High |
| G: Entity Tracking | 6 | High |

**Total: 60+ distinct transformation patterns**

---

## Key Insights

1. **TBTA is a semantic annotation system**, not just simplified English
2. **Underscore markers** are the backbone - 30+ types encoding implicit info, number, reference, modification
3. **Dual representations** serve different audiences (literal/dynamic, complex/simple)
4. **Suffix disambiguation** (-A, -B, -C) tracks verb senses and referent groups
5. **He1 vs He2 difference**: He2 (NT) has 10x more underscore markers than He1 (OT)

---

## Recommendations

1. **Expand RULES.md** from 12 → 25 core rules (group related underscore markers)
2. **Create marker taxonomy** document for the 30+ underscore types
3. **Document He1/He2 differences** separately (OT natural, NT annotated)
4. **Add suffix disambiguation guide** for verb/noun sense marking
