# TBTA Blind Test Skill

> Transform NIV verses to CNL WITHOUT reference materials

## Instructions

You will transform Bible verses from NIV to Controlled Natural Language (CNL).

**IMPORTANT**:
- Use ONLY your internal Bible knowledge for NIV text
- Apply ONLY the rules provided below
- DO NOT access any external files or reference the actual TBTA output

## Input Format
```
Reference: [Book Chapter:Verse-Verse]
Format: He1 or He2
```

## Output Format
```
[Reference]: [Your CNL transformation]
```

---

## Rules to Apply

### Step 1: Copy NIV from Memory
Recall the NIV text for each verse from your training data.

### Step 2: Segment Clauses
Split into one main verb per sentence:
```
"X did A and Y did B" → "X did A. Y did B."
```

### Step 3: Resolve Pronouns
Replace 3rd-person pronouns with explicit nouns:
```
he/she/they → Name or "that man/woman/person"
```

### Step 4: Bracket Subordinate Clauses
All non-main clauses in `[...]`:
```
Relative: [who...], [that...], [which...]
Purpose: [in-order-to...]
Temporal: [when...], [after...], [before...]
Conditional: [if...]
Causal: [because...]
```

### Step 5: Mark Deixis
1st/2nd person pronouns get speaker identity:
```
I(Speaker), you(Addressee), my(Possessor's), we(Group)
```

### Step 6: Mark Imperatives
Commands prefixed with `(imp)`:
```
You(Name) (imp) go...
```

### Step 7: Frame Quotes
Direct speech in brackets:
```
X said, ["Quote text."]
```

### Step 8: Yahweh Substitution (OT)
```
LORD → Yahweh
```

### Step 9: He2 Additions (if He2 format)
- Add `_implicit` markers where information is implied
- Use `simple/complex` word pairs for technical terms
- Add `_paragraph` at section breaks

---

## Example

**Input**:
```
Reference: Genesis 1:3
Format: He1
```

**Your Process**:
1. Recall NIV: "And God said, 'Let there be light,' and there was light."
2. Frame quote: said, ["..."]
3. No pronouns to resolve
4. Simple structure, minimal bracketing needed

**Output**:
```
Genesis 1:3: Then God said, ["Let light be!"] And light was.
```

---

## Validation

After each verse, verify:
- [ ] No bare pronouns without clear antecedent
- [ ] One main verb per sentence
- [ ] All subordinate clauses bracketed
- [ ] 1st/2nd person marked with identity
- [ ] Imperatives have `(imp)`
- [ ] Quotes have `["..."]`

---

## Begin Test

Transform all verses in the given chapter using these rules.
Output each verse on its own line in format:
```
[Reference]: [CNL output]
```
