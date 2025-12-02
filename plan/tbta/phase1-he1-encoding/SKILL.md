# TBTA Verse Encoding Skill

> Transform NIV verses to Controlled Natural Language (CNL)

## Input
- NIV verse text
- Reference (Book Chapter:Verse)
- Format: He1 (natural/OT) or He2 (strict/NT)

## Output
- CNL verse with explicit markers, brackets, annotations

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
- Keep subordinate clauses [bracketed]

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
- God: always bare name

### Step 5: Mark Speech & Questions
- Direct speech: `["quoted text"]`
- Nested quotes: additional bracket levels
- Commands: `(imp)` before verb
- Rhetorical questions: `(rhetorical)` + `(statement)` equivalent
- Yes-expected: `(yesrhetorical)`, No-expected: `(norhetorical)`

### Step 6: Simplify Vocabulary (LDV)
- "begat" → "had a son named"
- "conceived" → "became pregnant"
- "knew his wife" → "sexed"
- "dwell/sojourn" → "live"
- Keep: Yahweh, tabernacle, Ark-of-the-Covenant

### Step 7: Add Discourse Markers
- "And" — continuation
- "Then" — sequence
- "But" — contrast
- "So" — result
- "Therefore" — logical conclusion
- Omit for: first clause, section starts, speech intros

### Step 8: Mark Implicit Information
- `_implicit` — general additions
- `_implicitActiveAgent` — passive voice agent
- `_implicitNecessary` — grammatically required
- `(implicit-situational)` — context obvious
- `(implicit-info)` — background knowledge

### Step 9: Add Semantic Annotations
- `_metonymy` — one thing for another
- `_hyperbolic` — non-literal "all"
- `_dual` — exactly two entities
- `_reflexive` — self-directed
- `_1stAs3rd` — Jesus as "Son of Man"
- `-iteration N` — repeated actions

### Step 10: Apply Style (He1/He2)
**He1** (OT): Natural flow, minimal annotations
**He2** (NT):
- Add `_implicit` markers extensively
- Provide `(literal)/(dynamic)` pairs
- Provide `(complex)/(simple)` for theology
- Add `(literalunits)/(modernunits)` for measurements

---

## Quick Reference

```
PRONOUNS:    I(Name), you(Name), _dual, _incl
BRACKETS:    [relative], [temporal], [purpose], [if], [just-like]
SPEECH:      ["quoted"], (imp), (rhetorical)/(statement)
IMPLICIT:    _implicit, _implicitActiveAgent, (implicit-info)
PAIRS:       (literal)/(dynamic), (complex)/(simple), (literalunits)/(modernunits)
SEMANTIC:    _metonymy, _hyperbolic, _reflexive, -iteration N
STRUCTURE:   (title), (paragraph), (footnote)
```

---

## Validation Checklist

- [ ] No bare pronouns (he/she/they) without antecedent nearby
- [ ] One main verb per sentence
- [ ] All subordinate clauses in `[brackets]`
- [ ] 1st/2nd person marked: `I(Name)`, `you(Name)`
- [ ] Imperatives marked: `(imp)`
- [ ] Quotes bracketed: `["..."]`
- [ ] "LORD" → "Yahweh" (OT)
- [ ] He2: underscore markers present
- [ ] He2: L2 pairings used

---

## Common Errors to Avoid

1. Converting "must/should" (keep as-is)
2. Converting passive to active (keep passive)
3. Missing brackets on subordinate clauses
4. Unmarked deixis (I/you without parenthetical)
5. Unmarked imperatives (missing `(imp)`)
6. Over-segmenting (lists can stay together)

---

## Example: Ruth 1:1

**NIV Input:**
> In the days when the judges ruled, there was a famine in the land. So a man from Bethlehem in Judah, together with his wife and two sons, went to live for a while in the country of Moab.

**He1 Output:**
> [When judges ruled] there was a famine in the land. So a man [who lived in a town named Bethlehem [which was in Judah]] went to live in a country named Moab. That man's wife and that man's 2 sons went with that man.

**Transforms applied:**
1. `In the days when` → `[When...]` (temporal bracket)
2. `a man from Bethlehem` → `a man [who lived in Bethlehem]` (relativization)
3. `Judah` → `[which was in Judah]` (location bracket)
4. `together with his wife and two sons` → segmented to separate sentence
5. `his wife` → `that man's wife` (coreference)
6. `two` → `2` (number as digit)
7. `the country of Moab` → `a country named Moab` (named entity)

---

## Sources

- **Evidence-based rules**: `plan/tbta/phase1-reverse-engineer/` (6,963 verses analyzed)
- **Analysis patterns**: `plan/tbta/.archive/phase1-reverse-engineer-claude-opus-4-5/`
- **Operational policies**: `bible-study-tools/tbta/phase1/policies/`
