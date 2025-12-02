# TBTA Phase 1 (He1) — Subagent Encoding V2

> **Mission**: Convert NIV verse into simplified English (He1) for TBTA.
> **Approach**: Reverse-engineering (rules derived from 6,963 encoded verses)

## Also Read

| File | Purpose |
|------|---------|
| `learnings-v2.md` | V2-specific patterns from prior encodings |

## Input/Output

**Input**: Verse reference + NIV text
**Output**: Encoded He1 text + linter results + issues for orchestrator

---

## 10-Step Transformation Process

### Step 1: Resolve Coreference
- First/second person: `pronoun(referent)` — "I(Paul)", "you(Ruth)"
- Third person: repeat name or "that man/woman/person"
- Keep impersonal "it" for weather/conditions

### Step 2: Segment Clauses
- Split at conjunctions (and/but/then/so)
- Move conjunction to new sentence start
- Target: one verb per sentence

### Step 3: Add Explicit Brackets
- `[which/who/that + info]` — relative clauses
- `[When/After/Before/While X]` — temporal
- `[in order to X]` / `[because X]` — purpose/reason
- `[if X]` — conditionals (stay embedded)
- `[just-like X]` — similes

### Step 4: Apply Named Formula
- First mention: "a [type] named [Name]"
- Known entity: "the [type] named [Name]"
- Subsequent: direct name

### Step 5: Mark Speech & Questions
- Direct speech: `["quoted text"]`
- Commands: `(imp)` before verb
- Nested quotes: additional bracket levels

### Step 6: Simplify Vocabulary
- L0-1: use directly
- L2: pair as `simple/complex`
- L3+: alternate or explicate

### Step 7: Add Discourse Markers
- "And" — continuation, "Then" — sequence, "But" — contrast, "So" — result
- Omit for: first clause, section starts

### Step 8: Mark Implicit Information (He2 mainly)
- `_implicit`, `_implicitActiveAgent`, `(implicit-info)`

### Step 9: Apply Learnings
- Read `learnings.md`, apply matching patterns, note issues

### Step 10: Validate with Linter
- Run linter until clean (max 12 iterations)

---

# RULES (Reverse-Engineered from 6,963 Verses)

## Strategy

**Copy NIV EXCEPT**:
- Pronouns → explicit nouns (coreference resolution)
- Compound sentences → segmented clauses
- Complex vocabulary → LDV pairs (He2)

---

## 🟢 HIGH Confidence Rules (>95% consistent)

### 1. Coreference Resolution
(Gen 1:22, Gen 1:26, Gen 1:28, Gen 3:6, Gen 4:8; NOT Gen 1:2)

Replace 3rd-person pronouns with explicit referents:
```
he/she/it/they → [Name] or "that man/woman/person"
his/her/their → [Name's] or "that person's"
```

### 2. Clause Segmentation
(Gen 1:4, Gen 1:5, Gen 1:10, Gen 1:16, Gen 1:27)

One predicate per sentence. Split at conjunctions:
```
"X and Y did Z" → "X did A. Y did B."
```

### 3. Subordinate Bracketing
(Gen 1:6, Gen 1:9, Gen 1:11, Gen 1:17, Gen 1:18; NOT Gen 1:1)

All non-main clauses in `[...]`:
- Relative: `[that/who/which...]`
- Purpose: `[in-order-to...]`, `[so-that...]`
- Temporal: `[when...]`, `[after...]`, `[before...]`
- Conditional: `[if...]`
- Causal: `[because...]`
- Result: `[with-the-result-that...]`

### 4. Deixis Marking
(Gen 1:26, Gen 1:28, Gen 1:29, Gen 3:9, Gen 3:11; NOT Gen 1:1)

```
I(Speaker), you(Addressee), my(Possessor's), we(Group)
```

**Prefer generic labels**: `you(people)` not `you(Disciples)`

He2 additions: `_incl` (inclusive we), `_excl` (exclusive we)

### 5. Quote Framing
(Gen 1:3, Gen 1:6, Gen 1:9, Gen 1:11, Gen 1:26; NOT Gen 1:1)

```
Speaker said, ["Quote text."]
Nested: ["X said, ['inner quote']"]
```

### 6. Imperative Marking
(Gen 1:22, Gen 1:28, Gen 3:3, Gen 3:14, Gen 4:7)

```
You(Addressee) (imp) verb...
```

### 7. Yahweh Substitution
(Gen 2:4, Gen 2:5, Gen 2:7, Gen 2:8, Gen 2:9; NOT Daniel references)

```
LORD (NIV) → Yahweh (CNL)
```
OT only.

### 8. Explicit Relativization
(Gen 1:11, Gen 1:12, Gen 1:21, Gen 1:24, Gen 2:8; NOT Gen 1:1)

```
"X, the king" → "X, [who was the king]"
"city in Y" → "city [which was in Y]"
```

---

## 🟡 MEDIUM Confidence Rules (Context-dependent)

### 9. LDV Substitution
(Matt 4:10, Matt 6:10, Mark 4:10, Ruth 1:2; NOT Ruth 1:1)

L2 level words paired: `simple/complex`
```
people/disciples, stories/parables, spirits/demons
family/clan, grain/barley, gather/harvest
```

He1: 9.2% | He2: 47.6%

### 10. Hyphenated Verbs
(Gen 2:21, Gen 3:8, Gen 4:8, Mark 1:17, Mark 2:14; NOT Gen 1:1)

**ALWAYS BASE FORM** (never inflected):
```
go-up (not went-up), sit-down (not sat-down)
```

### 11. Underscore Implicit Markers (He2)
(Matt 12:45, Matt 22:4, Mark 14:28, Mark 6:7, Acts 15:33)

```
_implicit, _implicitNecessary, _implicitActiveAgent
_paragraph, _descriptive, _frameInferable
_dual, _generic, _hyperbolic, _metonymy
```

### 12. Dual Representations (He2)
(Matt 6:10, Matt 16:18, Matt 27:45, Mark 4:19, Acts 2:1)

```
(literal)/(dynamic) - Translation style
(complex)/(simple) - Accessibility
(literalunits)/(modernunits) - Time/measurement
```

### 13. Rhetorical Question Handling (He2)
(Matt 16:10, Matt 23:11, Mark 2:7, Mark 7:18, Matt 5:47)

```
(norhetorical) Did you remember...?
(statement) You should remember...
```

### 14. Named Entity Introduction
(Gen 2:8, Gen 2:11, Gen 2:13, Gen 4:17, Gen 4:25; NOT Gen 1:1)

```
a man named Adam
a city named Enoch
a country named Moab
```

### 15. Structural Markers
(Ruth 1:1, Matt 5:1, Matt 5:13, Matt 5:17, Acts 3:1)

```
(title), -Title - Section headers
(paragraph), _paragraph - Breaks
```

**Titles describe ACTION**: "(title) Jesus teaches about God's laws"

---

## 🔴 LOW Confidence Rules (<50% consistent)

### 16. Demonym → Description
(Ruth 1:2, Ruth 1:4; NOT Ruth 1:1)
**55% applied**: `"Moabite" → "[who was from Moab]"` (sometimes)

### 17. Modal Decomposition
(Gen 1:25, Esther 4:11; NOT Gen 3:3)
**14% applied**: `"can X" → "is able [to X]"` ✓, keep "must/should"

### 18. Number Formatting
(Gen 1:28, Gen 5:5; NOT Gen 1:5)
**~50% applied**: Large → digits, small → varies

### 19. Passive Voice
(N/A; NOT Mark 2:3, Mark 5:2)
**0% converted** - Passives remain passive. He2 marks agent: `_implicitActiveAgent`

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
| passive | → keep passive | 🔴 N/A |

---

## He1 vs He2 Format

| Feature | He1 (OT style) | He2 (NT style) |
|---------|----------------|----------------|
| Underscore markers | Rare (0.6%) | Common (64%) |
| L2 word pairings | 9.2% | 47.6% |
| Sense suffixes | No | Yes (-A, -B, -C) |
| Dual translations | No | Yes |

---

## Linter & Output

**Linter**: `https://editor.tabitha.bible/check?text={urlencoded_he1}`
**Ontology**: `https://ontology.tabitha.bible/?q={word}`

### Output Format

```markdown
# {BOOK} {ch}:{vs} — He1 Encoding (V2)

## NIV Input
"..."

## Transformations Applied
1. [Step X]: {what changed}

## Final He1
"..."

## Linter Results
Errors: {list or "None"}

## Issues for Orchestrator
- {Pattern not covered / ambiguity}
```
