# TBTA Verse Column Rules

> **Goal**: Transform NIV → language-neutral semantic representation any language can generate from.

## CRITICAL (Must Apply)

### R1: No 3rd Person Pronouns
Replace he/she/it/they/him/her/them with explicit nouns.
```
"he went" → "John went"
"she said" → "Naomi said"
"they" → "those people" / "Naomi and Ruth"
```

### R2: One Verb Per Sentence
Split compound sentences. Auxiliaries (do/will/can/may) don't count as separate verbs.
```
"went and bought food" → "went to town. That man bought food."
```

### R3: Bracket Subordinate Clauses
All non-main clauses in `[...]`:
- Relative: `man [who was in house]`
- Patient: `knew [Mary was there]`
- Purpose: `went [in order to see Mary]`
- Adverbial: `[When John arrived] Mary left`

### R4: No "that" in Patient Clauses
TBTA interprets "that" as demonstrative.
```
Wrong: knew [that Mary was there]
Right: knew [Mary was there]
```

### R5: Numbers as Digits
```
Wrong: "two sons", "ten years"
Right: "2 sons", "10 years"
```

---

## HIGH PRIORITY

### R6: Name Introduction
`[article] [category] named [Name]`
```
"Moab" → "a country named Moab"
"Ruth" → "a woman named Ruth"
After mention: "that country named Moab" or just "Moab"
```

### R7: Apposition → Relative Clause
```
"Elimelech, Naomi's husband" → "Elimelech, [who was Naomi's husband]"
"Bethlehem in Judah" → "Bethlehem, [which was in Judah]"
```

### R8: Demonyms → Descriptions
```
"Moabite women" → "women [who were from Moab]"
"Ephrathites" → "people [who were in Ephrah's family/clan]"
```

### R9: Determiner System
| Determiner | When |
|------------|------|
| a/some | First mention |
| that/those | Already mentioned |
| this/these | Newly contrasted / physically present |
| the | Frame inferable (the king = of this country) |
| ∅ | Generic ("People like food") |

### R10: Passive → Active
```
"was left with" → "lived with"
"was given" → "received"
```
If passive needed, include agent: `was hit by X` or `by X _implicitActiveAgent`

---

## STANDARD

### R11: Pronoun Marking
1st/2nd person: Mark referent in parentheses.
```
"I(Naomi) said"
"you(Ruth) should go"
"my(Boaz's) workers"
"we(Peter) _excl" / "we(Peter) _incl"
```

### R12: L2 Vocabulary Pairings
```
family/clan       grain/barley      gathering/harvesting
workers/harvesters  buy/redeem      master/lord
wine/vinegar      serve/worship     promise/swear
```
**Explications**: `daughter-in-law` → `son's wife`

### R13: Quote Structure
Single: `X said, ["sentence"].`
Multi: `X said, ["first]. Second. Third."`
Nested: `X said, ["Y said, ["quote"]"]`

### R14: Command (Imperative) Pattern
```
You(John) (imp) go to the town.
```
In quotes after addressee: `["My daughter, (imp) go."]`

### R15: Purpose Clauses
Use `[in order to...]` not bare "to".
```
Wrong: "went to see Mary"
Right: "went [in order to see Mary]"
```

### R16: Implicit Information
- Regular: `(implicit-info)` or `<<...>>`
- Necessary: `_implicitNecessary` or `<...>`
- Types: `(implicit-situational)`, `(implicit-background)`, `(implicit-subaction)`

### R17: Titles/Sections
```
(title) Section heading here.
(paragraph) for paragraph breaks.
```

---

## SPECIAL CASES

### R18: Hyphenated Verbs
NEVER inflect. Use base form.
```
Wrong: "ran-away", "sat-down"
Right: "run-away", "sit-down"
```
Mark tense if needed: `stand-up _present`

### R19: No "can"
```
Wrong: "can go"
Right: "is able [to go]"
```

### R20: No "when/where" as Relativizers
```
Wrong: "time [when John left]"
Right: "time [that John left at]"
```

### R21: Reflexives
```
"yourself(Boaz) (imp) buy the land"
"each-other(people)"
```

### R22: Divine Names
- Standard: "Yahweh"
- Formal: "the LORD"
- Prayer pattern: `I(X) pray [that Yahweh will...]`

### R23: "all of" vs "all"
```
Generic: "God loves all people"
Specific: "all of those people"
```

### R24: Membership = "in" not "from"
```
Wrong: "Boaz was from Elimelech's family"
Right: "Boaz was in Elimelech's family/clan"
```

---

## QUICK CHECKLIST

- [ ] No he/she/it/they (R1)
- [ ] One verb per sentence (R2)
- [ ] Subordinates bracketed (R3)
- [ ] No "that" in patient clauses (R4)
- [ ] Numbers as digits (R5)
- [ ] Names: "X named Y" (R6)
- [ ] Appositives → relatives (R7)
- [ ] Demonyms → descriptions (R8)
- [ ] 1st/2nd pronouns marked (R11)
- [ ] L2 words paired (R12)
- [ ] Hyphenated verbs not inflected (R18)
- [ ] "can" → "is able [to]" (R19)
