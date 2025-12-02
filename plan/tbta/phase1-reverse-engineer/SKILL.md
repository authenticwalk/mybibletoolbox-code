# TBTA Verse Generation Skill

Transform source Bible text into TBTA CNL (Controlled Natural Language).

## Input
- Source verse text (NIV/KJV)
- Book name (He1=OT natural, He2=NT strict)
- Character context (who has been introduced)

## Output
- CNL verse with explicit markers, brackets, annotations

---

## 10-Step Transformation Process

### Step 1: Resolve Coreference
- First/second person → `pronoun(referent)`: "I(Paul)", "you(Ruth)"
- Third person → repeat name or "that man/woman/person"
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

## Example Transformation

**Source (KJV Ruth 1:1)**:
> Now it came to pass in the days when the judges ruled, that there was a famine in the land. And a certain man of Bethlehemjudah went to sojourn in the country of Moab, he, and his wife, and his two sons.

**CNL Output (He1 style)**:
> Elimelech (title) and Naomi move from Bethlehem to Moab. [When judges were ruling Israel] many people [who were living in Israel] did not have enough food. A certain man was from Bethlehem [which was in Judah]. That man, that man's wife, and that man's two sons moved from Bethlehem to a country named Moab [in order to live in Moab for a few years].

**Transformations applied**:
1. (title) section marker
2. [When judges...] temporal bracket
3. [who were living...] relative clause
4. [which was in Judah] geographic clarification
5. "a country named Moab" introduction formula
6. [in order to...] purpose clause
7. "sojourn" → "live" (LDV)
8. "That man" demonstrative for coreference

---

## He2 Example (Matthew 5:3)

**Source**: Blessed are the poor in spirit, for theirs is the kingdom of heaven.

**CNL Output (He2 style)**:
> ["(literal) People [who have a poor spirit] are blessed by God _implicitActiveAgent]. ["(dynamic) People [who know [those people need God]] are blessed by God _implicitActiveAgent]. (literal) For the kingdom-B of heaven belongs to those people. (dynamic) For God will be those people's king.

**He2 markers applied**:
1. `_implicitActiveAgent` for passive
2. `(literal)/(dynamic)` dual rendering
3. Kingdom theology simplified
