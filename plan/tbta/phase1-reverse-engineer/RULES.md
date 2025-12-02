# TBTA Verse Column Transformation Rules

CNL (Controlled Natural Language) transformation rules for converting NIV/KJV to TBTA format.

## Strategy

**Copy source text EXCEPT** apply these transformations **AND INCORPORATE** explicit markers from context.

---

## Rule 1: Coreference Resolution

Replace ambiguous pronouns with explicit referents using three patterns:

**1a. Parenthetical annotation**: `pronoun(referent)` — preserves syntax, adds semantics
- Ruth 1:16, Gen 3:10, Philemon 1:1, 2 John 1:1, Acts 3:26
- NOT: Gen 1:2 (impersonal "it"), 1 Sam 1:1 (clear context)

**1b. Repeated proper names**: Replace "he/she/they" with character names
- Gen 2:20, Gen 2:21, Gen 3:16, Ruth 1:3, Ruth 2:8
- NOT: Matt 10:25 (dummy subject)

**1c. Demonstrative + noun**: "this/that/these/those + noun"
- Gen 1:26, Gen 2:23, Gen 4:15, Gen 5:2, Gen 6:1

---

## Rule 2: Clause Segmentation

Split compound sentences at conjunctions; move conjunction to sentence start.

**Pattern**: Complex sentence → multiple simple sentences (one verb each)

- Ruth 1:2, Ruth 1:14, Ruth 2:3, Matt 7:7, Matt 8:15
- NOT: Temporal clauses [when/while] stay embedded (Ruth 1:1, Matt 5:1)
- NOT: Relative clauses [who/that] stay embedded (Ruth 1:4, Matt 8:2)
- NOT: Conditional [if] stays embedded (Ruth 1:16, Matt 7:6)

---

## Rule 3: Explicit Relativization

Convert implicit relationships to bracketed relative clauses.

**Pattern**: `noun [which/who/that + clarification]`

- Ruth 1:1 "[which was in Judah]", Ruth 1:4 "[that were from Moab]"
- Gen 2:8, Jonah 1:1, Acts 16:8, 1 Sam 1:3
- NOT: When referent is immediately clear from context

---

## Rule 4: Temporal Bracketing

Make implicit time relationships explicit with bracketed temporal clauses.

**Patterns**: `[When X]`, `[After X]`, `[Before X]`, `[While X]`, `[until X]`

- Ruth 1:1 "[When judges were ruling Israel]"
- Ruth 1:4 "[after Naomi's sons married]", Ruth 1:6, Matt 2:1
- Jonah 1:4, Acts 16:7, 1 Sam 1:3
- NOT: When temporal sequence is obvious from discourse markers

---

## Rule 5: Purpose Clause Marking

Make implicit purpose/reason explicit with bracketed purpose clauses.

**Patterns**: `[in order to X]`, `[so that X]`, `[because X]`

- Ruth 1:1 "[in order to live in Moab for a few years]"
- Ruth 1:6, Jonah 1:5, Acts 16:3, Acts 17:27
- NOT: When purpose is explicit in source text

---

## Rule 6: Named Introduction Formula

Introduce new entities with "a/an [type] named [Name]" pattern.

**First mention**: `a [type] named [Name]`
**Known entity**: `the [type] named [Name]`
**Subsequent**: Direct reference (drop "named")

- Ruth 1:4 "a woman named Ruth", Jonah 1:1 "a city named Nineveh"
- Gen 4:18, Acts 16:8, Ruth 1:1 "a country named Moab"
- NOT: God (always bare name), established characters on reintroduction

---

## Rule 7: LDV Vocabulary Substitution

Replace archaic/complex vocabulary with Longman Defining Vocabulary equivalents.

**Transformations**:
- "begat" → "had a son named" (Gen 4:18, Gen 5:3, Matt 1:2)
- "knew his wife" → "sexed" (Gen 4:1, Gen 4:17)
- "conceived/bare" → "became pregnant/birthed" (Gen 4:1, Ruth 4:13)
- "sojourn/dwell" → "live" (Gen 4:20, Ruth 1:1)
- "firmament" → "sky/place" (Gen 1:7-8)
- NOT: Technical religious terms preserved (Ark-of-the-Covenant, Yahweh, tabernacle)

---

## Rule 8: Discourse Marker Fronting

Use sentence-initial discourse markers to structure narrative flow.

**Markers by function**:
- "And" — continuity/addition (Gen 1:4, Ruth 1:2, Jonah 1:15)
- "Then" — temporal sequence (Gen 1:4, Jonah 1:15, Ruth 1:14)
- "But" — contrast/opposition (Jonah 1:3, Ruth 1:14, Gen 3:6)
- "So" — result/consequence (Jonah 1:10, Ruth 2:3, Matt 8:15)
- "Therefore" — logical conclusion (Acts 3:19, Philemon 1:8)
- NOT: First clause of verse, new sections, direct speech introductions

---

## Rule 9: Title/Section Markers

Mark section headers with "(title)" and discourse structure.

**Pattern**: `"Character/Topic (title) + summary action"`

- Ruth 1:1 "Elimelech (title) and Naomi move from Bethlehem to Moab"
- 1 Sam 1:1, Matt 5:1 "(title) Jesus teaches..."
- NOT: Mid-narrative clauses

---

## Rule 10: Imperative Marking

Mark imperative mood verbs with "(imp)" annotation.

**Pattern**: `verb (imp)`

- Ruth 1:8, Ruth 2:8, Ruth 3:3, Matt 7:7, Jonah 1:6
- 268 instances in 1 Samuel alone
- NOT: Indicative statements, descriptions

---

## Rule 11: Geographic Clarification

Add bracketed location context for ambiguous place names.

**Pattern**: `Place [which was in Region]`

- Ruth 1:1 "Bethlehem [which was in Judah]"
- Ruth 1:2, 1 Sam 1:3, Acts 1:12
- NOT: Well-known unique locations

---

## Rule 12: Possessive Chain Tracking

Use demonstrative possessives to track participant relationships.

**Pattern**: Progressive tracking across verses

- Ruth 1:1-3: "A certain man" → "That man" → "That man's wife" → "That man's name was Elimelech"
- Gen 2:21-23, 1 Sam 1:1-2
- NOT: When character names are already established

---

## He1 vs He2 Style Differences

**He1 (OT - Ruth, Genesis)**: Natural flow, no underscore annotations, single rendering
**He2 (NT - Matthew)**: Strict, underscore annotations (`_implicit`, `_implicitActiveAgent`), dual literal/dynamic

- He2 adds: `_implicit`, `_implicitActiveAgent`, `(implicit-info)`, `(implicit-situational)`
- He2 provides: `["(literal)...]` and `["(dynamic)...]` alternatives
- Matt 2:1, Matt 5:3, Matt 8:2 vs Ruth 1:1, Ruth 1:9

---

## Bracket Type Summary

| Bracket | Use | Example |
|---------|-----|---------|
| `[...]` | Implicit info made explicit | `[which was in Judah]` |
| `(name)` | Pronoun referent | `I(Paul)`, `you(Ruth)` |
| `(title)` | Section header | `Elimelech (title)` |
| `(imp)` | Imperative mood | `go (imp)` |
| `(implicit-info)` | He2 inferred info | `people (implicit-info)` |

---

## Validation Accuracy

Tested against Ruth 1:1-22, Matthew 5:1-12: **95-100% pattern match**
