# TBTA Verse Transformation Rules

> **Corpus**: 6,963 verses | **Format**: He1 (natural) / He2 (strict)
> **Format**: Rule (supporting refs; NOT contradicting refs)

---

## Strategy

**Copy NIV EXCEPT**:
- Pronouns → explicit nouns (coreference resolution)
- Compound sentences → segmented clauses
- Complex vocabulary → LDV pairs (He2)

---

## Section A: Coreference Resolution 🟢 HIGH

**Pronoun-referent annotation** (1 Sam 1:8, 1 Sam 3:9, 1 Sam 17:34, 2 John 1:3; NOT 1 Sam 1:1)
```
he/she/it/they → [Name] or "that man/woman/person"
his/her/their → [Name's] or "that person's"
I(Paul), you(Hannah), we(disciples)
```
Exception: Bare "he/she" in narrative introductions

**Proper name repetition** (1 Sam 17:40, 1 Sam 3:6, 1 Sam 1:4)
Pattern: Repeat character name instead of pronoun — "David...David...David's"
Consistency: ⭐⭐⭐⭐⭐

**Demonstrative anaphora** (1 Sam 9:7, 1 Sam 2:35, 1 Sam 4:16)
Pattern: "that man", "this person", "those people" replacing pronouns
Consistency: ⭐⭐⭐⭐⭐

---

## Section B: Clause Structure 🟢 HIGH

**Clause segmentation** (1 Sam 1:5, 1 Sam 2:10, 1 Sam 19:22)
Pattern: Split compound sentences; move conjunction to sentence start
Consistency: ⭐⭐⭐⭐⭐

**Subordinate Bracketing** (Gen 1:6, Gen 1:9, Gen 1:11; NOT Gen 1:1)
All non-main clauses in `[...]`:
- Relative: `[that/who/which...]`
- Purpose: `[in-order-to...]`, `[so-that...]`
- Temporal: `[when...]`, `[after...]`, `[before...]`
- Conditional: `[if...]`
- Causal: `[because...]`
- Result: `[with-the-result-that...]`

**Temporal bracketing** (1 Sam 1:4, 1 Sam 13:10; NOT 1 Sam 25:36, Acts 1:5)
Pattern: `[When/After/Before/While/until X]`
Exception: Some temporal markers NOT bracketed

**Purpose/reason marking** (1 Sam 9:11, 1 Sam 13:8; NOT Acts 17:25, Dan 2:1)
Pattern: `[in order to X]`, `[because X]`, `[so that X]`
Exception: Inconsistent bracketing of "because"

---

## Section C: Speech & Questions 🟢 HIGH

**Direct speech bracketing** (Matt 21:5, 2 Sam 15:10, 1 Sam 19:17)
Pattern: `["quoted text"]` with nested brackets (up to 4 levels)
Consistency: ⭐⭐⭐⭐⭐ (100%)

**Quote Framing** (Gen 1:3, Gen 1:6, Gen 1:9)
```
Speaker said, ["Quote text."]
Nested: ["X said, ['inner quote']"]
```

**Imperative marking** (1 Sam 3:6, 1 Sam 23:2, Mark 13:2; NOT 1 Sam 17:32, 1 Sam 1:17)
Pattern: `(imp)` before all command verbs
Exception: Modals, wishes, and blessings not marked

**Rhetorical question transformation** 🟡 MEDIUM (Mark 8:4, Mark 14:37; NOT 1 Sam 1:8, Gen 3:11)
Pattern: `(rhetorical)` / `(yesrhetorical)` / `(norhetorical)` + `(statement)` equivalent
Exception: OT ~20% vs NT ~85%

---

## Section D: Deixis Marking 🟢 HIGH

**Deixis Marking** (Gen 1:26, Gen 1:28, Gen 3:9; NOT Gen 1:1)
Mark 1st/2nd person referents in parentheses:
```
I(Speaker), you(Addressee), my(Possessor's), we(Group)
```

**Prefer generic labels over specific groups**:
- ✓ `you(people)`, `you(person)` - generic
- ✗ `you(Disciples)`, `you(followers)` - too specific

He2 additions: `_incl` (inclusive we), `_excl` (exclusive we)

---

## Section E: Implicit Information 🟢 HIGH (NT)

**General implicit** (Mark 10:1, Mark 8:4)
Pattern: `_implicit` — inferable objects, purposes, content

**Grammatically required** (Mark 13:16, Mark 13:6)
Pattern: `_implicitNecessary` — required for sentence completeness

**Passive agent marking** (Mark 13:13, Mark 9:2)
Pattern: `by X _implicitActiveAgent` — converts passive to active with agent
Consistency: ⭐⭐⭐⭐⭐

**Situational context** (Mark 8:1, Mark 13:1)
Pattern: `(implicit-situational)` — scene/context details

**Background knowledge** (1 Sam 23:6, 1 Sam 2:30)
Pattern: `(implicit-info)` — prior narrative or cultural knowledge

---

## Section F: Translation Pairs (NT Only) 🟢 HIGH

**Literal/dynamic equivalence** (Mark 7:6, Mark 14:36, Mark 1:3)
Pattern: `(literal) X. (dynamic) Y.`
Usage: Idioms, metaphors, cultural references (174 examples)
Consistency: ⭐⭐⭐⭐⭐

**Complex/simple theological** (Mark 9:1, Mark 4:11, Mark 11:22)
Pattern: `(complex) kingdom of God (simple) God ruling people`
Usage: Abstract theological terms (94 examples)

**Ancient/modern units** (Mark 14:5, Matt 18:24, Mark 15:33)
Pattern: `(literalunits) denarii (modernunits) year's wages`
Usage: Currency, time, measurements (23 examples, 100% paired)

---

## Section G: Grammatical Markers 🟢 HIGH

**Dual number** (Mark 14:16, Mark 1:17, Matt 20:30)
Pattern: `_dual` — marks exactly two entities
Consistency: ⭐⭐⭐⭐⭐

**Iteration counting** (1 Sam 18:11, 1 Sam 20:41, Gen 31:7)
Pattern: `-iteration N` — "bowed -iteration 7 times"
Consistency: ⭐⭐⭐⭐⭐

**Clusivity** (Mark 14:15, Matt 22:17; NOT 1 Sam throughout)
Pattern: `_incl` (inclusive we) / `_excl` (exclusive we)
Exception: OT rarely marked - NT-only

---

## Section H: LDV Substitution 🟡 MEDIUM

**LDV Substitution** (Matt 4:10, Matt 6:10, Mark 4:10, Ruth 1:2)
L2 level words paired: `simple/complex`
```
people/disciples, stories/parables, spirits/demons
family/clan, grain/barley, gather/harvest
teaches/preach, happy/joyful, cry/mourn-B
```
Stats: He1 9.2% | He2 47.6%

**Hyphenated Verbs** (Gen 2:21, Gen 3:8, Mark 1:17)
Phrasal verbs hyphenated, **ALWAYS BASE FORM**:
```
go-up (not went-up), sit-down (not sat-down)
run-away, stand-up, come-out, throw-away
```

---

## Section I: Semantic Annotations 🟡 MEDIUM

**Metonymy** (Mark 6:14, Matt 11:20; NOT 1 Sam 7:16, 1 Sam 18:6)
Pattern: `X of Y _metonymy` — Herod=soldiers, towns=people
Exception: OT rarely marks metonymy

**Hyperbolic quantifiers** (Mark 1:5, Mark 5:5; NOT Acts 1:8, 1 Sam 2:10)
Pattern: `all _hyperbolic` — non-literal universal quantifiers
Exception: Many "all" unmarked; "every" never marked

**Verb sense disambiguation** (Mark 13:14, Mark 9:1, Matt 21:32)
Pattern: `-A/-B/-C/-D` suffixes — see-A (physical) vs see-B (perceive)
Usage: Selective - only high-ambiguity polysemous verbs

---

## Section J: Low Confidence Rules 🔴 LOW

**Demonym → Description** (Ruth 1:2, Ruth 1:4; NOT Ruth 1:1)
**55% applied** - Inconsistent:
```
"Moabite" → "[who was from Moab]" (sometimes)
```

**Modal Decomposition** (Gen 1:25, Esther 4:11)
**14% applied** - Only "can" converted:
```
"can X" → "is able [to X]" ✓
"must X" → kept as "must" ✗
```

**Number Formatting** (Gen 1:28, Gen 5:5)
**~50% applied** - Inconsistent:
- Large numbers → digits: 127, 180, 10000
- Small numbers (1-12) → sometimes words

**Passive Voice**
**0% converted** - Passives remain passive
He2 marks agent with `_implicitActiveAgent`

---

## Quick Reference

| Pattern | Transform | Confidence |
|---------|-----------|------------|
| pronouns | → explicit nouns | 🟢 HIGH |
| compound sentence | → multiple sentences | 🟢 HIGH |
| subordinate clause | → `[bracketed]` | 🟢 HIGH |
| I/you/we | → `I(Name)`, `you(Name)` | 🟢 HIGH |
| direct speech | → `said, ["..."]` | 🟢 HIGH |
| command | → `(imp) verb` | 🟢 HIGH |
| LORD | → Yahweh | 🟢 HIGH |
| complex word (He2) | → `simple/complex` | 🟡 MEDIUM |
| phrasal verb | → `run-away` | 🟡 MEDIUM |
| demonym | → `[from X]` | 🔴 LOW |
| "can" | → `is able [to]` | 🔴 LOW |
| passive | → keep passive | N/A |

---

## He1 vs He2 Format

| Feature | He1 (OT style) | He2 (NT style) |
|---------|----------------|----------------|
| Underscore markers | Rare (0.6%) | Common (64%) |
| L2 word pairings | 9.2% | 47.6% |
| Sense suffixes | No | Yes (-A, -B, -C) |
| Dual translations | No | Yes |
| Use case | Natural reading | NLP/MT input |

---

## Validation Summary

- **6,963 verses** analyzed across 15 books
- **33 rules** documented with evidence
- **High consistency** (⭐⭐⭐⭐+): Coreference, speech, implicit, structure
- **NT-specific** patterns: Translation pairs, semantic annotations
- **Known exceptions** documented with verse references
