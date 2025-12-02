# TBTA Phase 1 (He1) — Subagent Encoding V3

> **Mission**: Convert NIV verse into simplified English (He1) for TBTA.
> **Approach**: Policy + Reverse-Engineering (blended rules with evidence)

## Files to Read First

| File | Purpose |
|------|---------|
| `plan/tbta/phase1-he1-encoding/RULES.md` | Blended rules: policy (📘) + evidence (🟢🟡🔴) |
| `bible-study-tools/tbta/phase1/policies/learnings.md` | Accumulated patterns from prior encodings |

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

## Key Rules (Blended)

### Confidence Levels

| Symbol | Meaning | Source |
|--------|---------|--------|
| 🟢 HIGH | 95%+ consistent in corpus | Reverse-engineering |
| 🟡 MEDIUM | Context-dependent | Reverse-engineering |
| 🔴 LOW | <50% consistent | Reverse-engineering |
| 📘 POLICY | Official TBTA docs | Policy |

### Passive Voice 🟢 HIGH
**Keep passive, mark agent**:
```
✓ "was hit by a soldier"
✓ "was circumcised by a person"
✗ Converting passive to active
```

### Numbers 🟢 HIGH
- Semantic layer uses digits (`2`, `3`, `10`)
- Text rendering may show words — this is OK

### Forbidden Words 📘 POLICY
| Word | Alternative |
|------|-------------|
| can | "is able [to...]" |
| even | omit or rephrase |
| any | "a" in negative context |
| own | omit or `_emphasized` |
| going to | "will" |

### Aspect Verbs 📘 POLICY
"begin/start/stop/finish/continue" modify the verb, not create clause:
```
✓ John started talking to Mary
✗ John started [talking to Mary]
```

### Common L2 Pairings 🟡 MEDIUM
```
serve/worship, promise/swear, gather/harvest
grain/barley, family/clan, workers/servants
daughter-in-law → son's wife
```

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
