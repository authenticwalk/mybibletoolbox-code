# TBTA Blind Pattern Discovery V2

**Date**: 2024-12-02
**Method**: 14 parallel subagents analyzed 500-verse chunks WITHOUT seeing existing rules
**Total Verses**: 6,963

---

## Executive Summary

Blind analysis discovered **76+ distinct patterns** across 7 major categories. Key findings:

| Category | Patterns | Coverage |
|----------|----------|----------|
| Square Brackets | 5 types | 90%+ |
| Parenthetical Markers | 22+ types | 52% |
| Underscore Markers | 47+ types | 60-70% |
| Slash Alternatives | 30+ pairs | 20-25% |
| Hyphenated Compounds | 24+ types | 30-35% |
| Letter Suffixes | 6 types | 12-40% |
| Structural Markers | 10+ types | 15-25% |

---

## HIGH-FREQUENCY PATTERNS (50%+)

### 1. Square Bracket Clause Embedding (90%+)
Subordinate clauses nested in `[...]`, often 2-5 levels deep.
```
[who had a terrible disease] → relative
[in-order-to catch fish] → purpose
[when Jesus saw the crowds] → temporal
[if you obey] → conditional
[because God loved] → causal
[with-the-result-that people believed] → result
```

### 2. Parenthetical Pronoun Disambiguation (54%+)
Every pronoun clarified with referent: `pronoun(Name)`
```
I(Jesus), you(Pharisees), we(disciples) _excl
my(David's), your(Abraham's), his(Joseph's)
```

### 3. Possessive Chain Expansion (80%+)
Full possessive relationships spelled out:
```
"his wife" → "that man's wife"
"their father" → "Jacob's sons' father"
```

---

## MEDIUM-FREQUENCY PATTERNS (20-50%)

### 4. Underscore Semantic Markers (60-70%)
47+ distinct marker types discovered:

**Implicit Information (most common)**
- `_implicit` - General unstated information
- `_implicitNecessary` - Required for understanding
- `_implicitActiveAgent` - Agent in passive voice
- `_implicitType` - Category specification
- `_frameInferable` - Inferable from context

**Number/Quantity**
- `_dual` - Exactly two referents
- `_paucal` - Few (3-4)
- `_plural` - Multiple
- `_generic` - Non-specific reference

**Perspective/Reference**
- `_1stAs3rd` - First person as third (Son of Man)
- `_excl` - Exclusive we
- `_incl` - Inclusive we
- `_reflexive` - Self-reference
- `_emphasized` - Focus/emphasis

**Modification**
- `_descriptive` - Non-restrictive modifier
- `_restrictive` - Restrictive modifier
- `_morally` - Ethical qualification
- `_hyperbolic` - Exaggeration
- `_metonymy` - Figurative usage

**Discourse**
- `_paragraph` - Section break
- `_routinely` - Habitual action
- `_distantPast` - Past tense marker
- `_AdverbLDV` - Adverb from LDV

### 5. Slash Alternative Translations (20-25%)
Synonyms or translation options:
```
followers/disciples, Good-News/Gospel
family/clan, grain/barley, gather/harvest
teaches/preach, happy/joyful, cry/mourn-B
```

### 6. Imperative Marking (40-50%)
Commands marked with `(imp)`:
```
You(Abraham) (imp) go to the land
You(people) (imp) do not worry
```

### 7. Letter Suffix Disambiguation (12-40%)
Disambiguates senses: `-A`, `-B`, `-C`, `-D`
```
kingdom-A vs kingdom-B (different senses)
servants-A vs servants-B (different groups)
Lord-A vs Lord-C (divine vs human)
is-U (comparison) vs is-X (identity)
```

---

## LOW-FREQUENCY PATTERNS (5-20%)

### 8. Rhetorical Question System
Questions marked with expected answer:
```
(rhetorical) Question?
(statement) Assertion.

(yesrhetorical) - Expected "yes"
(norhetorical) - Expected "no"
```

### 9. Literal/Dynamic Dual Translations
Both formal and functional equivalents:
```
(literal) gates of hell will not defeat
(dynamic) power of Satan will not defeat

(complex) kingdom-B of heaven
(simple) God rules that person
```

### 10. Literal/Modern Units
Measurement conversions:
```
(literalunits) the 6th hour
(modernunits) 12PM
```

### 11. Structural Section Markers
```
(title) Jesus teaches about prayer
(paragraph) - Section break
(footnote) - Inline note
-Title - Dash prefix variant
(comment-begin)/(comment-end) - Editorial
```

### 12. Hyphenated Semantic Units
Multi-word concepts:
```
in-order-to, in-front-of, just-like
Son-of-Man, Good-News, mount-Olives
run-away, sit-down, stand-up, go-up
```

### 13. Named Entity Introduction
```
a man named Adam
a city named Jerusalem
a country named Moab
the tribe named Judah
```

### 14. Frame/Background Markers
```
(implicit-situational) - Context-recoverable
(implicit-info) - Background knowledge
(implicit-subaction) - Event subcomponent
(implicit-background) - Historical context
```

### 15. Reciprocal/Reflexive Marking
```
each-other(brothers) - Reciprocal
yourself(person) - Reflexive with referent
```

---

## RARE PATTERNS (<5%)

### 16. Iteration Marking
```
-iteration 7 times
walked around the city -iteration seven times
```

### 17. Composition Marking
```
pillar -composed-of salt
container _madeOf beautiful white stone
-quantity 225 grams
```

### 18. Name Etymology
```
-Footnote Benjamin means the son of my right hand
-footnote Bethel means the house of God
_ExplainName
```

### 19. Comparative Structures
```
[just-like a shepherd]
more-than _Adj 300 denarii
```

### 20. Realm of Authority
```
king of the Jews _RealmOfAuthority
```

### 21. Same-Thing List
```
a man's _sameThingList brother
```

### 22. Index Disambiguation
```
servants-A, servants-B (different groups)
things-A, things-B (different referent sets)
_genericDifferentNounIndex
```

---

## NOVEL PATTERNS NOT IN CURRENT RULES

### Discovered but undocumented:
1. `_adverbialFormOfHonestInLdv` - Adverb formation marker
2. `_imperfectiveNotBackgrounded` - Aspect marker
3. `_suggestiveLets` - Hortative marker
4. `_otherThingList` - List continuation
5. `_copiesInLDV` / `_copyinLDV` - Manuscript note
6. `_immediatePastAndShouldNotFeatures` - Modal+tense
7. `_RealmOfAuthority` - Title scope
8. `_foreignLanguage` - Non-English word
9. `-Begin-episode` - Narrative structure
10. `_trial` - Testing context

### Addressee specificity levels discovered:
- Generic: `you(people)`, `you(person)` (preferred)
- Role-based: `you(followers)`, `you(disciples)`
- Named: `you(Peter)`, `you(Abraham)`

### Bracket opener vocabulary (30+ types):
`[that`, `[who`, `[to`, `[when`, `[because`, `[if`, `[after`,
`[in-order-to`, `[just-like`, `[where`, `[while`, `[before`,
`[until`, `[which`, `[so-that`, `[with-the-result-that`

---

## PATTERN CO-OCCURRENCE

Most common combinations:
- Brackets + Parenthetical: 75% of verses
- Underscore + Slash: 35% of verses
- Possessive + Role markers: 60% of verses
- Title + Paragraph: 15% (section openings)

Average patterns per verse: 3-5

---

## COMPARISON TO CURRENT RULES.md

| Current Rule | Blind Discovery | Status |
|--------------|-----------------|--------|
| Coreference Resolution | Found (54%+) | ✓ Confirmed |
| Clause Segmentation | Found (90%+) | ✓ Confirmed |
| Subordinate Bracketing | Found (90%+) | ✓ Confirmed |
| Deixis Marking | Found (54%+) | ✓ Confirmed |
| Quote Framing | Found (30%+) | ✓ Confirmed |
| Imperative Marking | Found (40%+) | ✓ Confirmed |
| Yahweh Substitution | Not specifically flagged | - |
| LDV Substitution | Found (20-25%) | ✓ Confirmed |
| Hyphenated Verbs | Found (30%+) | ✓ Confirmed |
| Underscore Markers | Found 47+ types | ⚠️ EXPAND |
| Dual Representations | Found | ✓ Confirmed |
| Title Patterns | Found (15%+) | ✓ Confirmed |
| Letter Suffixes | Found (12-40%) | ⚠️ ADD |
| Frame Markers | Found | ⚠️ ADD |
| Iteration Markers | Found | ⚠️ ADD |
| Composition Markers | Found | ⚠️ ADD |

---

## RECOMMENDATIONS

1. **Expand underscore taxonomy** - 47+ types found vs ~15 documented
2. **Add letter suffix guide** - `-A`, `-B`, `-C` system underdocumented
3. **Document bracket openers** - 30+ opener types found
4. **Add frame/background markers** - `(implicit-situational)` etc.
5. **Document rare markers** - `_trial`, `_foreignLanguage`, etc.
6. **Clarify addressee preference** - Generic `(people)` over specific

---

## Files Generated

This analysis consolidates findings from 14 parallel subagents, each analyzing ~500 shuffled verses without access to existing rules.
