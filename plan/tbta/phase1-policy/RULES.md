# TBTA Verse Rules (Compressed)

> **Goal**: NIV → Controlled Natural Language for universal translation

## Source Strategy

**Base**: Copy NIV text, **except**:
- Pronouns (resolve to nouns)
- Compound sentences (segment)
- Idioms (decompose to meaning)
- Passives (convert to active where possible)
- Complex vocabulary (apply LDV substitution)

**Incorporate from**:
- **Hebrew**: "Yahweh" for יהוה (not NIV's "LORD")
- **Greek/Hebrew**: Implicit cultural context `(implicit-info)`
- **Scholarly sources**: Historical footnotes `(footnote)`
- **Semantic analysis**: Clause boundaries, participant tracking

---

## Core Transforms (5 rules)

### 1. Coreference Resolution
Replace 3rd-person pronouns with explicit referents.
```
he/she/it/they → [Name] or [that + noun]
```

### 2. Clause Segmentation
One predicate per sentence. Split at conjunctions.
```
"X and Y did Z" → "X did A. Y did B."
```

### 3. Explicit Relativization
Appositive → bracketed relative clause.
```
"X, the king" → "X, [who was the king]"
"city in Y" → "city [which was in Y]"
```

### 4. Deixis Marking
Mark 1st/2nd person referents in parentheses.
```
I(Speaker), you(Addressee), my(Possessor's), we(Group) _incl/_excl
```

### 5. LDV Substitution (Longman Defining Vocabulary)
| Level | Color | Action |
|-------|-------|--------|
| L0-L1 | Blue/Cream | Use directly |
| L2 | Magenta | Pair: `simple/complex` |
| L3 | Green | Alternate: `(complex)...(simple)...` |
| L4 | Brown | Proper nouns, use directly |

**Common L2 pairings**: `family/clan`, `grain/barley`, `gather/harvest`, `buy/redeem`

---

## Notation Patterns (3 rules)

### 6. Subordinate Bracketing
All non-main clauses in `[...]`:
- Relative: `[who/that/which...]`
- Patient: `knew [X happened]`
- Purpose: `[in order to...]`
- Conditional: `[if X then...]`

### 7. Quote Framing
```
Speaker said, ["First sentence]. Continuation."
```
Nested: `["X said, ["inner quote"]"]`

### 8. Imperative Marking
```
You(Addressee) (imp) verb...
```

---

## Lexical Rules (3 rules)

### 9. Hyphenated Verbs
Never inflect. Base form only.
```
run-away, sit-down, stand-up (not ran-away, sat-down)
```

### 10. Modal Decomposition
```
"can X" → "is able [to X]"
"must X" → "has to [X]" / obligation marker
```

### 11. Demonym → Description
```
"Moabite" → "[who was from Moab]"
"Ephrathite" → "[who was in Ephrah's family/clan]"
```

---

## Implicit Information

### 12. Gap-filling
Add missing subactions, cultural context:
```
(implicit-info) Boaz walked to Ruth.
(footnote) At that time, judges ruled Israel.
```

Types: `(implicit-situational)`, `(implicit-background)`, `(implicit-subaction)`

---

## Underscore Semantic Markers (NEW - from LLM analysis)

### 13. Implicit Type Taxonomy
```
_implicit           - General recoverable info
_implicitNecessary  - Essential for understanding
_implicitActiveAgent - Agent in passive: "by God _implicitActiveAgent"
_frameInferable     - Inferable from discourse frame
```

### 14. Number Distinctions
```
_dual     - Exactly two: "those disciples _dual"
_paucal   - Few (3-4): "fish _paucal"
_incl     - Inclusive we (includes addressee)
_excl     - Exclusive we (excludes addressee)
```

### 15. Reference Type Markers
```
_generic     - Generic reference: "people _generic"
_hyperbolic  - Exaggeration: "all _hyperbolic the people"
_metonymy    - Metonymic: "Herod of soldiers _metonymy"
_1stAs3rd    - Self in 3rd person: "Son-of-Man _1stAs3rd"
```

---

## Dual Representation System (NEW)

### 16. Literal/Dynamic Pairs
```
(literal) gates of hell will not defeat
(dynamic) power of Satan will not defeat
```

### 17. Complex/Simple Pairs
```
(complex) kingdom-B of heaven
(simple) God rules that person
```

### 18. Literalunits/Modernunits
```
(literalunits) the 6th hour
(modernunits) 12PM
```

---

## Rhetorical Questions (NEW)

### 19. Question Type + Statement Pairing
```
(norhetorical) Did you(followers) remember...?
(statement) You(followers) should remember...

(yesrhetorical) - Expected "yes" answer
(rhetorical) - General rhetorical question
```

---

## Disambiguation System (NEW)

### 20. Verb Sense Suffixes
```
call-A, call-B  - Different verb senses
is-U (comparison), is-X (identity)
```

### 21. Noun Reference Suffixes
```
servants-A, servants-B  - Different groups
things-A, things-B      - Different referent sets
```

---

## Structural Markers (NEW)

### 22. Title/Section
```
(title), -Title, -title  - Section headers
(paragraph), _paragraph  - Paragraph breaks
```

### 23. Footnote/Comment
```
(footnote) - Inline footnote
(comment-begin)/(comment-end) - Editorial notes
```

### 24. Discourse Connectives
```
Then-C, Then-D  - Different continuation types
So (consequently) - Inferential connective
```

---

## Quick Reference

| NIV Pattern | TBTA Transform |
|-------------|----------------|
| "he went" | Coreference → "John went" |
| "X, the king" | Relativization → "X, [who was king]" |
| "harvest" | LDV L2 → "gather/harvest" |
| "Moabite" | Demonym → "[from Moab]" |
| "can do" | Modal → "is able [to do]" |
| "LORD" | Hebrew → "Yahweh" |
| Passive | Active voice where possible |

---

## Terminology Index

| Term | Meaning |
|------|---------|
| **CNL** | Controlled Natural Language |
| **LDV** | Longman Defining Vocabulary (2000 core words) |
| **Coreference** | Pronoun → explicit noun |
| **Deixis** | Speaker/hearer reference marking |
| **Relativization** | Appositive → relative clause |
| **L2 pairing** | simple/complex word pair |
| **He1/He2** | Phase 1 (natural) / Phase 2 (strict) |
| **_implicit** | Underscore marker for recoverable info |
| **_dual/_paucal** | Number distinctions beyond singular/plural |
| **(literal)/(dynamic)** | Translation style pair |
| **(complex)/(simple)** | Accessibility pair |
| **-A/-B suffix** | Verb/noun sense disambiguation |

---

## Pattern Count Summary

| Category | Rules | Patterns |
|----------|-------|----------|
| Core Transforms | 1-5 | 5 |
| Notation Patterns | 6-8 | 3 |
| Lexical Rules | 9-11 | 3 |
| Implicit Information | 12 | 1 |
| **Underscore Taxonomy** | 13-15 | 30+ markers |
| **Dual Representation** | 16-18 | 3 |
| **Rhetorical Questions** | 19 | 1 |
| **Disambiguation** | 20-21 | 2 |
| **Structural Markers** | 22-24 | 3 |
| **Total** | | **60+ patterns** |
