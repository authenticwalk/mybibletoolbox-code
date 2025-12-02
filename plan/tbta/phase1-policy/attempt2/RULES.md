# TBTA Verse Rules (Evidence-Based)

> **Goal**: NIV → Controlled Natural Language for universal translation
> **Data Source**: 6,963 verses from 15 books analyzed via 14 parallel subagents

## Source Strategy

**Base**: Copy NIV text, **except**:
- Pronouns (resolve to explicit nouns)
- Compound sentences (segment to one predicate each)
- Idioms/figurative language (decompose or mark)
- Passives (convert to active with agent marking)
- Complex vocabulary (L2 pairing)

**Incorporate from Hebrew/Greek/scholarship**:
- "Yahweh" for יהוה (not "LORD")
- Implicit cultural context `(implicit-info)`
- Historical footnotes `(footnote)`
- Semantic participant tracking

---

## Core Transforms (Phase: Both)

### 1. Coreference Resolution
Replace all pronouns with explicit referents in parentheses.

**Pattern**: `pronoun(referent)` or full noun replacement

| NIV | CNL |
|-----|-----|
| "he said to him" | "Boaz said to Ruth" |
| "his wife" | "Abraham's wife" / "my(Sarai's) wife" |
| "they returned" | "David and those men returned" |

**Supporting refs**: Gen 16:5, 2 Sam 7:29, Ruth 2:8, Matt 22:4, Philemon 1:13
**Exceptions**: None found - universally applied

### 2. Clause Segmentation
One predicate per sentence. Split compound sentences.

**Pattern**: Period + "And/Then/So" for sequential actions

| NIV | CNL |
|-----|-----|
| "He came and saw and conquered" | "He came. And he saw. And he conquered." |
| "while sitting...holding" | "Saul was sitting. And Saul was holding." |

**Supporting refs**: 1 Sam 19:9, 2 Sam 21:20, Ruth 2:10, Gen 11:30, Acts 18:22
**Exceptions**: None found

### 3. Bracket-Enclosed Subordination
All subordinate clauses in `[brackets]`. Supports 2-5 nesting levels.

**Types**:
- Temporal: `[When X happened]`, `[After X]`, `[Before Y]`
- Conditional: `[if X]`, `[unless Y]`
- Purpose: `[in order to X]`, `[so that Y]`
- Relative: `[who X]`, `[that Y]`, `[which Z]`
- Reason: `[because X]`

**Supporting refs**: Gen 16:5, Matt 12:45, Acts 15:33, 1 Sam 17:4, Dan 11:41
**Exceptions**: Very short relative clauses sometimes unbracketed in He1

### 4. Deixis Marking
Mark 1st/2nd person pronouns with speaker/addressee identity.

**Pattern**: `I(Speaker)`, `you(Addressee)`, `my(Possessor's)`, `we(Group)_incl/_excl`

| NIV | CNL |
|-----|-----|
| "I will bless you" | "I(Yahweh) will bless you(Abraham)" |
| "You must obey me" | "you(Jacob) (imp) obey me(Rebekah)" |

**Supporting refs**: Gen 16:9, 2 Sam 2:14, Ruth 2:9, Matt 6:10, Gen 27:8
**Exceptions**: None found

### 5. LDV Substitution (Longman Defining Vocabulary)
Pair complex words with simpler alternatives.

**Patterns**:
- Slash pairing: `gifts/sacrifices`, `meal/feast`, `family/clan`
- Underscore simpler: `servant_slave`, `asked_begged`

| Level | Example |
|-------|---------|
| L2 pairing | `gather/harvest`, `grain/barley` |
| Proper nouns | Use directly (Bethlehem, Yahweh) |

**Supporting refs**: 1 Sam 1:4, Ruth 2:1, Matt 22:4, Gen 23:19, Esther 2:19
**Exceptions**: Technical terms sometimes kept without pairing

---

## Notation Patterns (Phase: Both)

### 6. Quote Framing
Direct speech in `["..."]` with explicit speech verbs.

**Pattern**: `Speaker said to Addressee, ["quote content"]`
**Nested**: `["outer ['inner'] outer"]`

**Supporting refs**: Gen 16:9, 2 Sam 2:14, Ruth 1:8, Matt 22:4, Gen 27:7
**Exceptions**: None found

### 7. Imperative Marking
Commands marked with `(imp)` before verb.

**Pattern**: `You(Addressee) (imp) verb...`

| NIV | CNL |
|-----|-----|
| "Go home" | "You(Ruth) (imp) go home" |
| "Listen to me" | "You(servants) (imp) listen to me(king)" |

**Supporting refs**: Gen 16:9, 2 Sam 7:29, Ruth 2:9, Matt 22:4, Gen 27:8
**Exceptions**: Suggestive uses `_suggestiveLets` for "Let us..."

### 8. Name Introduction Formula
Introduce named entities with explicit pattern.

**Pattern**: `a [role] named [Name]` or `[Name] [who was...]`

| NIV | CNL |
|-----|-----|
| "Elimelech's wife Naomi" | "Elimelech's wife named Naomi" |
| "the prophet Isaiah" | "a prophet named Isaiah [who told God's messages]" |

**Supporting refs**: Ruth 1:2, Dan 1:1, 1 Sam 1:4, Gen 23:19, Nahum 1:1
**Exceptions**: Well-established names (God, Yahweh) not reintroduced

---

## Implicit Information Markers (Phase: Both)

### 9. Implicit Information Tags
Surface hidden information with explicit markers.

**Tag Types**:
- `(implicit-info)` - General background
- `(implicit-situational)` - Context-dependent
- `(implicit-subaction)` - Implied actions
- `(implicit-background)` - Historical context
- `_implicit` - Inline marker
- `_implicitNecessary` - Required for sense
- `_frameInferable` - Culturally expected

**Supporting refs**: Ruth 2:1, Matt 2:1, Gen 1:1, Acts 21:15, 1 Sam 17:4
**Exceptions**: None found

### 10. Passive Agent Recovery
Convert passive to active with explicit agent marking.

**Pattern**: Passive → Active + `_implicitActiveAgent`

| NIV | CNL |
|-----|-----|
| "was killed" | "was killed by soldiers _implicitActiveAgent" |
| "were sent" | "were sent by the king _implicitActiveAgent" |

**Supporting refs**: Matt 22:4, Matt 6:10, Acts 15:33, 2 Sam 21:20
**Exceptions**: Some passives retained with agent tag

---

## Discourse Structure (Phase: Both)

### 11. Title/Paragraph Markers
Section structure made explicit.

**Markers**:
- `(title)` or `-Title` - Section headings
- `_paragraph` or `(paragraph)` - Paragraph breaks
- `(footnote)` - Historical/textual notes
- `(comment-begin)...(comment-end)` - Annotations

**Supporting refs**: Ruth 1:1, Matt 2:1, Jonah 1:1, Gen 1:1, Acts 1:1
**He1 preference**: `-Title`, `-Begin-episode`
**He2 preference**: `(title)`, `_paragraph`

### 12. Temporal/Sequential Markers
Time and sequence made explicit.

**Patterns**:
- `Then`, `At that time`, `One day`, `Later`
- `[When X was Y years old]` - Age formulas
- `-D` suffix for discourse continuity (Then-D)

**Supporting refs**: Gen 11:20, 1 Sam 19:9, Dan 1:1, Ruth 1:1
**Exceptions**: None found

---

## He2-Only Patterns (NT Books)

### 13. Rhetorical Question Marking
Tag rhetorical questions with statement equivalents.

**Pattern**: `(rhetorical) Question? (statement) Answer.`
**Variants**: `(yesrhetorical)`, `(norhetorical)`

**Supporting refs**: Matt 16:10, Matt 23:13, Mark 4:7, Acts 15:33
**NOT in**: Ruth, Genesis, Daniel (He1 books)

### 14. Complex/Simple Alternation
Difficult concepts presented in parallel forms.

**Pattern**: `(complex) Abstract version. (simple) Concrete version.`
**Also**: `(literal) Figurative meaning. (dynamic) Plain meaning.`

**Supporting refs**: Matt 6:10, Matt 23:13, Matt 22:4, Mark 4:7
**NOT in**: OT books (use single form)

### 15. 1st-as-3rd Person Reference
Jesus's self-references as "Son of Man" marked.

**Pattern**: `_1stAs3rd` or `_1stas3rd`

**Supporting refs**: Matt 12:45, Matt 16:10 (Jesus referring to self)
**NOT in**: OT books

### 16. Modern Unit Conversion
Ancient measures with modern equivalents.

**Pattern**: `(literalunits) ancient. (modernunits) modern.`

**Supporting refs**: Matt 22:4, Mark 4:7 (time/distance)
**NOT in**: OT books (ancient units only)

---

## He1-Only Patterns (OT Books)

### 17. Genealogical Formulas
Structured age/descendant patterns.

**Pattern**: `[When X was Y years old] X had a son named Z`

**Supporting refs**: Gen 11:20, Gen 23:19
**NOT in**: NT books (different genealogy format)

### 18. Narrative Episode Markers
Scene boundaries with episode tags.

**Pattern**: `-Begin-episode`, `-Title` (vs. He2's `(title)`)

**Supporting refs**: Ruth 1:1, Jonah 1:1, Gen 1:1
**NOT in**: NT books (use parenthetical markers)

---

## Lexical Rules (Phase: Both)

### 19. Hyphenated Compound Verbs
Base form only, never inflected.

**Pattern**: `run-away`, `sit-down`, `stand-up` (not `ran-away`)

**Supporting refs**: Jonah 1:1, Ruth 2:9, 2 Sam 7:29
**Exceptions**: None found

### 20. Modal Decomposition
Modals expanded to explicit constructions.

| NIV | CNL |
|-----|-----|
| "can X" | "is able [to X]" |
| "must X" | "has to [X]" |
| "should X" | "ought [to X]" |

**Supporting refs**: Gen 11:30, Ruth 2:9, Matt 6:10
**Exceptions**: None found

### 21. Demonym → Description
Nationality/origin as relative clause.

| NIV | CNL |
|-----|-----|
| "Moabite" | "[who was from Moab]" |
| "Ephrathite" | "[who was from Ephrath's family/clan]" |

**Supporting refs**: Ruth 1:1, 1 Sam 1:4, Nahum 1:1
**Exceptions**: Well-known groups (Israelites, Philistines) sometimes kept

---

## Special Markers

### 22. Number/Grammatical Markers
Explicit grammatical features.

**Markers**:
- `_dual` - Exactly two entities
- `_paucal` - Few entities
- `_generic` - General reference
- `_reflexive` - Self-reference
- `_metonymy` - Figure of speech
- `_hyperbolic` - Exaggeration

**Supporting refs**: Gen 1:26, Matt 22:4, 2 John 1:1
**Exceptions**: None found

### 23. Verb Sense Suffixes
Disambiguate polysemous verbs.

**Pattern**: `verb-A`, `verb-B`, `verb-C` for different senses
**Also**: `is-U` (identity), `is-B` (attribute), `be-E` (existence)

**Supporting refs**: Matt 6:10, Acts 15:33, Gen 16:9
**Exceptions**: None found

---

## Quick Reference Table

| NIV Pattern | TBTA Transform | Phase |
|-------------|----------------|-------|
| "he went" | "John went" / "he(John) went" | Both |
| "his wife" | "David's wife" / "his(David's) wife" | Both |
| "X, the king" | "X, [who was king]" | Both |
| "harvest the grain" | "gather/harvest the grain/barley" | Both |
| "Moabite woman" | "woman [who was from Moab]" | Both |
| "can do" | "is able [to do]" | Both |
| "LORD" | "Yahweh" | Both |
| Passive voice | Active + `_implicitActiveAgent` | Both |
| Rhetorical Q | `(rhetorical) Q? (statement) A.` | He2 |
| Complex concept | `(complex) X. (simple) Y.` | He2 |
| Ancient units | `(literalunits) X. (modernunits) Y.` | He2 |

---

## Terminology Index

| Term | Meaning |
|------|---------|
| **CNL** | Controlled Natural Language |
| **LDV** | Longman Defining Vocabulary (2000 core words) |
| **Coreference** | Pronoun → explicit noun resolution |
| **Deixis** | Speaker/hearer/location reference marking |
| **Relativization** | Appositive → relative clause |
| **He1** | Phase 1 - OT books (natural flow) |
| **He2** | Phase 2 - NT books (strict notation) |
| **L2 pairing** | Simple/complex vocabulary pair |

---

## Validation Notes

- **6,963 verses analyzed** from 15 books
- **~25 core patterns** consistently applied across both phases
- **~5 He2-only patterns** for Greek NT features
- **~3 He1-only patterns** for Hebrew narrative
- **Subagent consensus**: 14/14 agents identified coreference, bracketing, deixis as universal
