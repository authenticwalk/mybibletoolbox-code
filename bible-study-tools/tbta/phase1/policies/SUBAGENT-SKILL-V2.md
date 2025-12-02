# TBTA Phase 1 (He1) — Subagent Encoding V2

> **Mission**: Convert NIV verse into simplified English (He1) for TBTA.
> **Role**: Read-only access to rules/learnings. Report issues for orchestrator to analyze.

## Files to Read First

Before encoding, read these files:

| File | Purpose |
|------|---------|
| `plan/tbta/phase1-he1-encoding/RULES.md` | Full transformation rules with evidence |
| `bible-study-tools/tbta/phase1/policies/learnings.md` | Accumulated patterns from prior encodings |

## Input

You receive from orchestrator:
- Verse reference + NIV text

## Output

Return to orchestrator:
- Encoded He1 text (linter-validated)
- Issues encountered (patterns not in learnings)

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
- Check ontology for word levels
- L0-1: use directly
- L2: pair as `simple/complex`
- L3+: alternate or explicate

### Step 7: Add Discourse Markers
- "And" — continuation
- "Then" — sequence
- "But" — contrast
- "So" — result
- Omit for: first clause, section starts

### Step 8: Mark Implicit Information (He2 mainly)
- `_implicit` — general additions
- `_implicitActiveAgent` — passive voice agent
- `(implicit-info)` — background knowledge

### Step 9: Apply Rules & Learnings
- Read `RULES.md` for evidence-based transformation rules
- Read `learnings.md` for accumulated patterns from prior encodings
- Apply matching patterns to your encoding
- Note any patterns you cannot apply (report to orchestrator)

### Step 10: Validate with Linter
- Run linter until clean (max 12 iterations)
- Fix all blocking errors

---

## Key Rules (Summary)

> Full rules with evidence in `plan/tbta/phase1-he1-encoding/RULES.md`

### Pronouns
- **Third person**: ALWAYS resolve to nouns, even after first mention
- **First/second person**: `I(Paul)`, `you(people)`, `we(Peter) _excl`

### Clauses
- One verb per clause
- Subordinate clauses in brackets: `[who was in the house]`
- Max 4 levels of nesting
- NO "that" starting patient clauses: `knew [X...]` not `knew [that X...]`
- Hyphenated verbs NEVER inflect: `pick-up` not `picked-up`

### Common L2 Pairings
```
serve/worship, promise/swear, gather/harvest
grain/barley, family/clan, workers/servants
daughter-in-law → son's wife
mother-in-law → husband's mother
```

### Quotes
```
X said, ["First sentence]. Second sentence..."
```
Bracket only first sentence.

### Commands
```
You(John) (imp) go to the town.
```

### Idioms
- "find favor in eyes" → `be kind to me`
- "The Lord be with you" → `I pray [that Yahweh will be with you]`

### Verb-Specific
- Use `gave birth to` (NOT "birth" or "birthed")
- Use `sexed` not "slept with"
- Use `came to X` instead of `arrived at X`
- Use `lived` instead of `living`

---

## Linter API

**URL**: `https://editor.tabitha.bible/check?text={urlencoded_he1}`

**Ontology lookup**: `https://ontology.tabitha.bible/?q={word}`

---

## Output Format

```markdown
# {BOOK} {ch}:{vs} — He1 Encoding

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
- {Pattern not in learnings / unexpected behavior / ambiguity}
```

---

## Self-Learning Protocol

**Your role**: READ-ONLY

1. Apply all patterns from `learnings.md`
2. If you encounter something NOT covered by learnings:
   - Complete the encoding as best you can
   - Report the issue in "Issues for Orchestrator" section
3. Do NOT modify learnings.md - orchestrator handles that

**Orchestrator's role**: WRITE

1. Analyzes your reported issues
2. Writes detailed diagnostic to `learnings/{slug}.md`
3. Updates `learnings.md` with new policy
