# TBTA Verse Generation Skill

Transform source Bible text (NIV/KJV) into TBTA CNL (Controlled Natural Language).

## Input
- Source verse text
- Book name (determines He1/He2 style)
- Character context (who has been introduced)

## Output
- CNL verse with explicit markers, brackets, and simplified vocabulary

---

## 7-Step Transformation Process

### Step 1: Resolve Coreference
Replace ambiguous pronouns:
- First/second person → `pronoun(referent)`: "I(Paul)", "you(Ruth)"
- Third person narrative → repeat proper name or use "that man/woman/person"
- Keep impersonal "it" (weather, conditions)

### Step 2: Segment Clauses
Split compound sentences at conjunctions:
- Move "and/but/then/so" to start of new sentence
- Target: one verb per sentence
- Keep subordinate clauses embedded in brackets

### Step 3: Add Explicit Brackets
Insert bracketed clarifications:
- `[which/who/that + info]` — relative clauses
- `[When/After/Before/While X]` — temporal context
- `[in order to X]` / `[because X]` — purpose/reason
- `[if X]` — conditionals (stay embedded)

### Step 4: Apply Named Formula
For new entities:
- First mention: "a [type] named [Name]"
- Known entity: "the [type] named [Name]"
- Subsequent: direct name reference
- God: always bare name (no article)

### Step 5: Simplify Vocabulary (LDV)
Replace archaic/complex terms:
- "begat" → "had a son named"
- "conceived" → "became pregnant"
- "knew his wife" → "sexed"
- "dwell/sojourn" → "live"
- Keep: Yahweh, tabernacle, Ark-of-the-Covenant

### Step 6: Add Discourse Markers
Front sentences with appropriate markers:
- "And" — continuation
- "Then" — sequence
- "But" — contrast
- "So" — result
- Omit for: first clause, section starts, speech intros

### Step 7: Apply Style (He1/He2)
**He1** (Genesis, Ruth, OT narrative): Natural flow, no underscore annotations
**He2** (Matthew, NT): Add `_implicit`, `_implicitActiveAgent`, dual renderings

---

## Quick Reference

```
Pronouns:     I(Name), you(Name), he(Name), that man
Brackets:     [relative], [temporal], [purpose], [conditional]
Annotations:  (title), (imp), (Name) for referent
Vocabulary:   LDV equivalents, keep religious terms
Connectives:  And/Then/But/So sentence-initial
```

---

## Example Transformation

**Source (KJV Ruth 1:1)**:
> Now it came to pass in the days when the judges ruled, that there was a famine in the land. And a certain man of Bethlehemjudah went to sojourn in the country of Moab, he, and his wife, and his two sons.

**CNL Output**:
> Elimelech (title) and Naomi move from Bethlehem to Moab. [When judges were ruling Israel] many people [who were living in Israel] did not have enough food. A certain man was from Bethlehem [which was in Judah]. That man, that man's wife, and that man's two sons moved from Bethlehem to a country named Moab [in order to live in Moab for a few years].

**Transformations applied**:
1. Added (title) section marker
2. Added [When judges...] temporal bracket
3. Added [who were living...] relative clause
4. Added [which was in Judah] geographic clarification
5. Used "a country named Moab" introduction formula
6. Added [in order to...] purpose clause
7. "sojourn" → "live"
