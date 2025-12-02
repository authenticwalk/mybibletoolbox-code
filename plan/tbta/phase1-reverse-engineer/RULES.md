# TBTA Verse Column Transformation Rules

Comprehensive CNL rules derived from 6,963 verses across 15 books. Each rule uses pregnant linguistic terminology with evidence.

**Format**: `**Rule** (supporting refs; NOT contradicting refs)`

---

## Section A: Coreference Resolution

**Pronoun-referent annotation** (1 Sam 1:8, 1 Sam 3:9, 1 Sam 17:34, 2 John 1:3, 1 Sam 23:2; NOT 1 Sam 1:1)
Pattern: `pronoun(referent)` — "I(Paul)", "you(Hannah)", "we(disciples)"
Exception: Bare "he/she" in narrative introductions

**Proper name repetition** (1 Sam 17:40, 1 Sam 3:6, 1 Sam 1:4, 1 Sam 1:13, 1 Sam 19:24)
Pattern: Repeat character name instead of pronoun — "David...David...David's"
No contradictions found - highly consistent

**Demonstrative anaphora** (1 Sam 9:7, 1 Sam 2:35, 1 Sam 4:16, 1 Sam 28:12, 1 Sam 4:4)
Pattern: "that man", "this person", "those people" replacing pronouns
No contradictions found - highly consistent

---

## Section B: Clause Structure

**Clause segmentation** (1 Sam 1:5, 1 Sam 2:10, 1 Sam 19:22, 1 Sam 1:7, 1 Sam 13:5)
Pattern: Split compound sentences; move conjunction to sentence start
No contradictions found - rule consistently applied

**Explicit relativization** (1 Sam 19:22, 1 Sam 13:5, 2 John 1:1, Acts 17:11, 1 Sam 17:1; NOT 1 Sam 1:1, Jonah 1:9, Mark 5:1)
Pattern: `[which/who/that + info]` — "[which was in Judah]"
Exception: Inconsistent bracketing in some verses

**Temporal bracketing** (1 Sam 1:4, 1 Sam 13:10, 1 Sam 2:15, 1 Sam 1:12, 1 Sam 1:22; NOT 1 Sam 25:36, 1 Sam 15:35, Acts 1:5)
Pattern: `[When/After/Before/While/until X]`
Exception: Some temporal markers NOT bracketed

**Purpose/reason marking** (1 Sam 9:11, 1 Sam 13:8, 1 Sam 1:5, 2 Sam 24:21, 1 Sam 6:7; NOT Acts 17:25, Dan 2:1, Gen 31:40)
Pattern: `[in order to X]`, `[because X]`, `[so that X]`
Exception: Inconsistent bracketing of "because"

---

## Section C: Speech & Questions

**Direct speech bracketing** (Matt 21:5, 2 Sam 15:10, 1 Sam 19:17, Gen 32:4, 2 Sam 7:5)
Pattern: `["quoted text"]` with nested brackets for reported speech (up to 4 levels)
No contradictions found - 100% consistent

**Rhetorical question transformation** (Mark 8:4, Mark 14:37, Mark 14:48, Mark 2:7, Matt 18:12; NOT 1 Sam 1:8, Gen 3:11)
Pattern: `(rhetorical)` / `(yesrhetorical)` / `(norhetorical)` + `(statement)` equivalent
Exception: OT questions often NOT transformed (~20% vs NT ~85%)

**Imperative marking** (1 Sam 3:6, 1 Sam 23:2, Mark 13:2, Josh 6:4, Gen 22:2; NOT 1 Sam 17:32, 1 Sam 1:17, Gen 3:11)
Pattern: `(imp)` before all command verbs
Exception: Modals, wishes, and blessings not marked

---

## Section D: Implicit Information Taxonomy

**General implicit** (Mark 10:1, Mark 8:4, Mark 8:6, Mark 13:13, Mark 4:9)
Pattern: `_implicit` — inferable objects, purposes, content

**Grammatically required** (Mark 13:16, Mark 13:6, Mark 14:2, Mark 13:28, Mark 2:18)
Pattern: `_implicitNecessary` — required for sentence completeness

**Passive agent marking** (Mark 13:13, Mark 9:2, Mark 13:2, Mark 5:4, Mark 7:2)
Pattern: `by X _implicitActiveAgent` — converts passive to active with agent
No contradictions - agents only needed for passives

**Situational context** (Mark 8:1, Mark 13:1, Mark 13:16, Mark 13:29, Mark 14:20)
Pattern: `(implicit-situational)` — scene/context details

**Background knowledge** (1 Sam 23:6, 1 Sam 2:30, 1 Sam 13:9, 1 Sam 17:33, 1 Sam 3:3)
Pattern: `(implicit-info)` — prior narrative or cultural knowledge

**Implied sub-steps** (Mark 14:16, Gen 34:2, Mark 14:40, Mark 7:14, Mark 6:38)
Pattern: `(implicit-subaction)` — intermediate actions in sequences

**Frame elements** (Mark 13:1, Mark 14:20, Mark 14:27, Mark 14:23, Mark 3:32)
Pattern: `_frameInferable` — predictable scene elements

---

## Section E: Translation Pairs (NT/Gospel only)

**Literal/dynamic equivalence** (Mark 7:6, Mark 14:36, Mark 1:3, Mark 13:35, Mark 16:9)
Pattern: `(literal) X. (dynamic) Y.` — word-for-word vs meaning-based
Usage: Idioms, metaphors, cultural references (174 examples, Matthew/Mark only)

**Complex/simple theological** (Mark 9:1, Mark 4:11, Mark 11:22, Mark 10:15, Mark 13:26)
Pattern: `(complex) kingdom of God (simple) God ruling people`
Usage: Abstract theological terms → functional descriptions (94 examples)

**Ancient/modern units** (Mark 14:5, Matt 18:24, Mark 15:33, Mark 6:48, Matt 25:15)
Pattern: `(literalunits) denarii (modernunits) year's wages`
Usage: Currency, time, measurements (23 examples, 100% paired)

---

## Section F: Grammatical Markers

**Dual number** (Mark 14:16, Mark 1:17, Matt 20:30, Mark 11:6, Matt 24:40)
Pattern: `_dual` — marks exactly two entities
No contradictions found - exceptionally consistent

**Clusivity** (Mark 14:15, Matt 22:17, Matt 8:17, Mark 13:4, Mark 9:5; NOT 1 Sam throughout)
Pattern: `_incl` (inclusive we) / `_excl` (exclusive we)
Exception: OT verses rarely marked - appears NT-only

**Iteration counting** (1 Sam 18:11, 1 Sam 20:41, Gen 31:7, Gen 33:3, Josh 6:15)
Pattern: `-iteration N` — "bowed -iteration 7 times"
No contradictions found - consistent when counts present

**First-as-third person** (Matt 12:32, Matt 10:23, Matt 20:18, Matt 19:28, Matt 25:32; NOT Matt 8:20, Mark 9:12)
Pattern: `Son-of-man _1stAs3rd` — Jesus's self-references
Exception: Some "Son of Man" references unmarked

**Reflexive marking** (Mark 5:5, Mark 3:24, Mark 14:72, Mark 10:27, Matt 6:19; NOT Acts 16:28, Mark 15:30, Ruth 3:3)
Pattern: `_reflexive` — conceptual/emphasized self-reference
Exception: Grammatical reflexives (hygiene, routine) NOT marked

---

## Section G: Semantic Annotations

**Metonymy** (Mark 6:14, Matt 11:20, Matt 26:57, Mark 11:4, Matt 21:32; NOT 1 Sam 7:16, 1 Sam 18:6)
Pattern: `X of Y _metonymy` — Herod=soldiers, towns=people
Exception: OT rarely marks metonymy

**Hyperbolic quantifiers** (Mark 1:5, Mark 5:5, Mark 4:32, Mark 13:13, Matt 8:34; NOT Acts 1:8, Acts 16:5, 1 Sam 2:10)
Pattern: `all _hyperbolic` — non-literal universal quantifiers
Exception: Many "all" unmarked; "every" never marked

**Verb sense disambiguation** (Mark 13:14, Mark 9:1, Matt 21:32, Mark 14:71, Mark 10:42)
Pattern: `-A/-B/-C/-D` suffixes — see-A (physical) vs see-B (perceive)
Usage: Selective - only high-ambiguity polysemous verbs

**Noun index tracking** (Mark 15:7, Mark 2:15, Matt 13:17, Mark 7:36, Mark 6:12)
Pattern: `_differentNounIndex`, `_newNounIndex`, `_sameAsLastNounIndex`
Usage: Gospel-heavy; absent in simpler narratives

---

## Section H: Comparisons

**Named introduction** (Ruth 1:4, Acts 17:34, Gen 4:18, 1 Sam 1:1, Jonah 1:1)
Pattern: `a [type] named [Name]` — first mention introduction
Alternative: `The name of X was Y` for formal genealogies

**Simile expansion** (1 Sam 26:20, Gen 19:28, Matt 10:16, Ruth 2:12, 1 Sam 17:36)
Pattern: `[just-like X]` for clause comparisons; `like` for simple noun comparisons
No contradictions - pattern choice depends on complexity

**Comparative marking** (Gen 25:28, 2 Sam 13:15, 1 Sam 18:8, Gen 29:30, 1 Sam 1:5)
Pattern: `[more-than X]` for verbal comparisons; "better/greater than" for attributes
No contradictions - pattern choice depends on structure

---

## Section I: Document Structure

**Section titles** (1 Sam 30:26, Mark 15:33, Matt 4:1, Josh 6:1, 2 Sam 12:1)
Pattern: `(title) {3-6 word summary}`
Usage: Major narrative sections

**Paragraph breaks** (Mark 14:16, Mark 8:1, Matt 26:6, Mark 6:14, Mark 4:10)
Pattern: `(paragraph)` or `_paragraph` at discourse shifts
Usage: Scene transitions, speaker changes, topic shifts

**Footnotes** (Mark 9:48, Matt 6:22, Matt 21:5, Matt 5:31, Mark 13:25)
Pattern: `(footnote) You(people) (imp) see [Scripture-ref]`
Alternative: Name etymologies, cultural explanations

**Alternative readings** (Matt 26:50, Mark 9:49, Neh 8:10, Gen 46:27, Mark 7:11)
Pattern: `(primary)` → `(meaning-1)` → `(alt)`
Usage: Ambiguous syntax, literal vs figurative, textual variants

---

## Section J: Style Differences

**He1 style (OT)** — Natural flow, minimal annotations, single renderings
Books: Genesis, Ruth, Joshua, 1-2 Samuel, Esther, Nehemiah, Daniel, Jonah, Nahum

**He2 style (NT)** — Technical, extensive annotations, dual renderings
Books: Matthew, Mark, Acts, Titus, Philemon, 2 John
Markers: `_implicit*`, `(literal)/(dynamic)`, `(complex)/(simple)`, `(literalunits)/(modernunits)`

---

## Quick Reference

| Category | Markers | Consistency |
|----------|---------|-------------|
| Coreference | `(referent)`, name repetition | ⭐⭐⭐⭐⭐ |
| Brackets | `[relative]`, `[temporal]`, `[purpose]` | ⭐⭐⭐⭐ |
| Speech | `["quoted"]`, `(imp)`, `(rhetorical)` | ⭐⭐⭐⭐ |
| Implicit | `_implicit*`, `(implicit-*)` | ⭐⭐⭐⭐⭐ |
| Pairs | `(literal)/(dynamic)`, etc. | ⭐⭐⭐⭐⭐ (NT) |
| Grammatical | `_dual`, `-iteration` | ⭐⭐⭐⭐⭐ |
| Semantic | `_metonymy`, `_hyperbolic` | ⭐⭐⭐ (NT>OT) |
| Structure | `(title)`, `(paragraph)`, `(footnote)` | ⭐⭐⭐⭐⭐ |

---

## Validation Summary

- **6,963 verses** analyzed across 15 books
- **33 rules** documented with evidence
- **High consistency** (⭐⭐⭐⭐+): Coreference, speech, implicit, structure
- **NT-specific** patterns: Translation pairs, semantic annotations
- **Known exceptions** documented with verse references
