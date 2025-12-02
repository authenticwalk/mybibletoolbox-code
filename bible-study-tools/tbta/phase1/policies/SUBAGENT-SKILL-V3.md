# TBTA Phase 1 (He1) — Subagent Encoding V3

> **Mission**: Convert NIV verse into simplified English (He1) for TBTA.
> **Approach**: Policy + Reverse-Engineering (blended rules with evidence)

## Also Read

| File | Purpose |
|------|---------|
| `bible-study-tools/tbta/phase1/policies/learnings.md` | Accumulated patterns from prior encodings |

**Note**: Rules are embedded below (Section A-K). No external RULES.md needed.

## Input

You receive from orchestrator:
- Verse reference + NIV text

## Output

Return to orchestrator:
- Encoded He1 text (linter-validated)
- Issues encountered (patterns not in rules/learnings)

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
- **Exception**: "start/stop/finish/continue" + verb = NO bracket (aspect, not clause)

### Step 3: Add Explicit Brackets
- `[which/who/that + info]` — relative clauses
- `[When/After/Before/While X]` — temporal
- `[in order to X]` / `[because X]` — purpose/reason
- `[if X]` — conditionals (stay embedded)
- `[just-like X]` — similes
- **Use "after" not "when"** if action clearly follows

### Step 4: Apply Named Formula
- First mention: "a [type] named [Name]"
- Known entity: "the [type] named [Name]"
- Subsequent: direct name

### Step 5: Mark Speech & Questions
- Direct speech: `["quoted text"]`
- Commands: `(imp)` before verb
- Nested quotes: additional bracket levels
- Rhetorical: `(rhetorical)` + `(statement)` (NT ~85%, OT ~20%)

### Step 6: Simplify Vocabulary
- Check ontology for word levels
- L0-1: use directly
- L2: pair as `simple/complex`
- L3+: alternate or explicate
- **Forbidden**: can, even, any, own, "going to"

### Step 7: Add Discourse Markers
- "And" — continuation
- "Then" — sequence
- "But" — contrast
- "So" — result
- Omit for: first clause, section starts

### Step 8: Mark Implicit Information

**He1 format** (angle brackets):
- `<<implicit info>>` — general additions
- `<necessary implicit>` — grammatically required

**He2 format** (underscore):
- `_implicit`, `_implicitActiveAgent`, `_implicitNecessary`

### Step 9: Apply Grammatical Constraints (📘 POLICY)
- No "going to" → use "will"
- No double negatives → use positive "all"
- One direct object per verb → "give X to Y" not "give Y X"
- "all of" for specific nouns → "all of those people"
- No participles/gerunds → rewrite as clauses
- Same noun same way within sentence

### Step 10: Validate with Linter
- Run linter until clean (max 12 iterations)
- Fix all blocking errors

---

## Blended Rules (Policy 📘 + Evidence 🟢🟡🔴)

> **Corpus**: 6,963 verses | **Format**: He1 (natural) / He2 (strict)
> **Books**: Genesis, Joshua, Ruth, 1-2 Samuel, Nehemiah, Esther, Daniel, Jonah, Nahum, Matthew, Mark, Acts, Titus, Philemon, 2 John

### Confidence Levels

| Symbol | Meaning | Source |
|--------|---------|--------|
| 🟢 HIGH | 95%+ consistent in corpus | Reverse-engineering |
| 🟡 MEDIUM | Context-dependent | Reverse-engineering |
| 🔴 LOW | <50% consistent | Reverse-engineering |
| 📘 POLICY | Official TBTA docs | Policy |

---

### Section A: Coreference Resolution 🟢 HIGH

**Pronoun-referent annotation** (1 Sam 1:8, 1 Sam 3:9, 1 Sam 17:34, 2 John 1:3)
```
he/she/it/they → [Name] or "that man/woman/person"
his/her/their → [Name's] or "that person's"
I(Paul), you(Hannah), we(disciples)
```
Exception: Bare "he/she" in narrative introductions

**Proper name repetition** (1 Sam 17:40, 1 Sam 3:6, 1 Sam 1:4)
Pattern: Repeat character name instead of pronoun — "David...David...David's"

**Demonstrative anaphora** (1 Sam 9:7, 1 Sam 2:35, 1 Sam 4:16)
Pattern: "that man", "this person", "those people" replacing pronouns

---

### Section B: Clause Structure 🟢 HIGH

**Clause segmentation** (1 Sam 1:5, 1 Sam 2:10, 1 Sam 19:22)
Pattern: Split compound sentences; move conjunction to sentence start

**Subordinate Bracketing** (Gen 1:6, Gen 1:9, Gen 1:11)
All non-main clauses in `[...]`:
- Relative: `[that/who/which...]`
- Purpose: `[in-order-to...]`, `[so-that...]`
- Temporal: `[when...]`, `[after...]`, `[before...]`
- Conditional: `[if...]`
- Causal: `[because...]`
- Result: `[with-the-result-that...]`

**Temporal bracketing** (1 Sam 1:4, 1 Sam 13:10)
Pattern: `[When/After/Before/While/until X]`
Exception: Some temporal markers NOT bracketed

**Purpose/reason marking** (1 Sam 9:11, 1 Sam 13:8)
Pattern: `[in order to X]`, `[because X]`, `[so that X]`

---

### Section C: Speech & Questions 🟢 HIGH

**Direct speech bracketing** (Matt 21:5, 2 Sam 15:10, 1 Sam 19:17)
Pattern: `["quoted text"]` with nested brackets (up to 4 levels)

**Quote Framing** (Gen 1:3, Gen 1:6, Gen 1:9)
```
Speaker said, ["Quote text."]
Nested: ["X said, ['inner quote']"]
```

**Imperative marking** (1 Sam 3:6, 1 Sam 23:2, Mark 13:2)
Pattern: `(imp)` before all command verbs
Exception: Modals, wishes, and blessings not marked

**Rhetorical question transformation** 🟡 MEDIUM (Mark 8:4, Mark 14:37)
Pattern: `(rhetorical)` / `(yesrhetorical)` / `(norhetorical)` + `(statement)` equivalent
Exception: OT ~20% vs NT ~85%

---

### Section D: Deixis Marking 🟢 HIGH

**Deixis Marking** (Gen 1:26, Gen 1:28, Gen 3:9)
Mark 1st/2nd person referents in parentheses:
```
I(Speaker), you(Addressee), my(Possessor's), we(Group)
```

**Prefer generic labels over specific groups**:
- ✓ `you(people)`, `you(person)` - generic
- ✗ `you(Disciples)`, `you(followers)` - too specific

He2 additions: `_incl` (inclusive we), `_excl` (exclusive we)

---

### Section E: Implicit Information 🟢 HIGH (NT)

**General implicit** (Mark 10:1, Mark 8:4)
Pattern: `_implicit` — inferable objects, purposes, content

**Grammatically required** (Mark 13:16, Mark 13:6)
Pattern: `_implicitNecessary` — required for sentence completeness

**Passive agent marking** (Mark 13:13, Mark 9:2)
Pattern: `by X _implicitActiveAgent` — converts passive to active with agent

**Background knowledge** (1 Sam 23:6, 1 Sam 2:30)
Pattern: `(implicit-info)` — prior narrative or cultural knowledge

**He1 Implicit Notation**:
- `<<implicit info>>` — regular implicit information
- `<necessary implicit>` — grammatically required implicit
- Example: `John was hit <<by a soldier>>` (agent implicit)

---

### Section F: Translation Pairs (NT Only) 🟢 HIGH

**Literal/dynamic equivalence** (Mark 7:6, Mark 14:36, Mark 1:3)
Pattern: `(literal) X. (dynamic) Y.`
Usage: Idioms, metaphors, cultural references

**Complex/simple theological** (Mark 9:1, Mark 4:11, Mark 11:22)
Pattern: `(complex) kingdom of God (simple) God ruling people`

**Ancient/modern units** (Mark 14:5, Matt 18:24, Mark 15:33)
Pattern: `(literalunits) denarii (modernunits) year's wages`

---

### Section G: Grammatical Markers 🟢 HIGH

**Dual number** (Mark 14:16, Mark 1:17, Matt 20:30)
Pattern: `_dual` — marks exactly two entities

**Iteration counting** (1 Sam 18:11, 1 Sam 20:41, Gen 31:7)
Pattern: `-iteration N` — "bowed -iteration 7 times"

**Clusivity** (Mark 14:15, Matt 22:17)
Pattern: `_incl` (inclusive we) / `_excl` (exclusive we)
Exception: OT rarely marked - NT-only

---

### Section H: LDV Substitution 🟡 MEDIUM

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

### Section I: Semantic Annotations 🟡 MEDIUM

**Metonymy** (Mark 6:14, Matt 11:20)
Pattern: `X of Y _metonymy` — Herod=soldiers, towns=people

**Hyperbolic quantifiers** (Mark 1:5, Mark 5:5)
Pattern: `all _hyperbolic` — non-literal universal quantifiers
Exception: Many "all" unmarked; "every" never marked

**Verb sense disambiguation** (Mark 13:14, Mark 9:1, Matt 21:32)
Pattern: `-A/-B/-C/-D` suffixes — see-A (physical) vs see-B (perceive)

---

### Section J: Low Confidence Rules 🔴 LOW

**Demonym → Description** (Ruth 1:2, Ruth 1:4)
**55% applied** - Inconsistent:
```
"Moabite" → "[who was from Moab]" (sometimes)
```

**Number Formatting** (Gen 1:28, Gen 5:5)
**semantic_encoding: 100% correct**
- `semantic_encoding`: Always uses digits
- `phase_1_encoding`: Inconsistently renders as words
- Large numbers → digits: 127, 180, 10000
- Small numbers (1-12) → sometimes words

**Passive Voice** 🟢 HIGH (Gen 14:13, Gen 17:24)
**Correctly followed** — Policy says KEEP passive, mark agent:
- Passives remain passive (correct per policy §0.13)
- Agent included with "by": `"was circumcised by a person"`
- He2 marks implicit agents with `_implicitActiveAgent`

---

### Section K: Grammatical Constraints 📘 POLICY

**Aspect Verbs Are Not Separate Verbs** (§0.19)
"begin", "start", "stop", "finish", "continue" modify the following verb:
```
✓ John started talking to Mary
✗ John started [talking to Mary]  (no bracket!)
```

**No "going to" for Future** (§0.28)
```
✓ John will see Mary
✗ John is going to see Mary
```

**No Double Negatives** (§0.29)
```
✓ All people love their mothers
✗ No person does not love his mother
```

**One Direct Object Per Verb** (§0.27)
```
✓ John gave the present to Mary
✗ John gave Mary the present
```

**"all of" vs "all"** (§0.17)
Use "all of" unless noun is generic:
```
✓ All of those people went   (specific)
✓ God loves all people       (generic)
✗ All those people went
```

**Same Noun Same Way** (§0.36)
Within same sentence, repeat noun identically:
```
✓ Paul gave letters... those men would read letters
✗ Paul gave letters... those men would read THOSE letters
```

**No Participles/Gerunds** (§0.31)
Rewrite as clauses:
```
✓ It is fun [that a person teaches]
✗ Teaching is fun
```

**"when" vs "after"** (§0.39)
If action clearly follows, use "after":
```
✓ [After John saw Jesus] John was happy
✗ [When John saw Jesus] John was happy (if caused by seeing)
```

**Forbidden Words** (§0.16-17):
| Word | Why | Alternative |
|------|-----|-------------|
| even | emphasis not encodable | omit or rephrase |
| any | use "a" in negative | "not eat an apple" |
| own | emphasis not encodable | omit or `_emphasized` |
| can | modal | "is able [to...]" |
| going to | future | "will" |

---

### Quick Reference

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
| "can" | → `is able [to]` | 🟢 HIGH |
| passive | → keep passive + "by agent" | 🟢 HIGH |
| numbers | → digits (semantic layer) | 🟢 HIGH* |
| start/stop/finish | → NO bracket on following verb | 📘 POLICY |
| "going to" | → "will" | 📘 POLICY |
| double negative | → positive "all" | 📘 POLICY |
| two direct objects | → "give X to Y" | 📘 POLICY |

---

### He1 vs He2 Format

| Feature | He1 (OT style) | He2 (NT style) |
|---------|----------------|----------------|
| Implicit markers | `<<...>>` / `<...>` | `_implicit` / `_implicitNecessary` |
| Underscore markers | Rare (0.6%) | Common (64%) |
| L2 word pairings | 9.2% (optional) | 47.6% (required) |
| Sense suffixes | Rare | Yes (-A, -B, -C) |
| Brackets | No (for He1 draft) | Yes (full subordinate) |
| Dual translations | No | Yes |
| Use case | Natural reading | NLP/MT input |

---

## Linter API

**URL**: `https://editor.tabitha.bible/check?text={urlencoded_he1}`

**Ontology lookup**: `https://ontology.tabitha.bible/?q={word}`

**Verify rules**: [sources.tabitha.bible](https://sources.tabitha.bible)

---

## Output Format

```markdown
# {BOOK} {ch}:{vs} — He1 Encoding (V3)

## NIV Input
"..."

## Transformations Applied
1. [Step X]: {what changed}
2. ...

## Final He1
"..."

## Linter Results
Errors: {list or "None"}
Iterations: {count}

## Issues for Orchestrator
- {Pattern not in rules / unexpected behavior / ambiguity}
```

---

## Self-Learning Protocol

**Your role**: READ-ONLY

1. Apply all rules from `RULES.md` (blended policy + evidence)
2. Apply all patterns from `learnings.md`
3. If you encounter something NOT covered:
   - Complete the encoding as best you can
   - Report the issue in "Issues for Orchestrator" section
4. Do NOT modify learnings.md - orchestrator handles that

**Orchestrator's role**: WRITE

1. Analyzes your reported issues
2. Writes detailed diagnostic to `learnings/{slug}.md`
3. Updates `learnings.md` with new policy
