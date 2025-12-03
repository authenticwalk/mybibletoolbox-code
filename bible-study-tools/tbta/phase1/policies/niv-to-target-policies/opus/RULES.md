# NIV → TBTA Target Conversion

## Core Principle

Create **language-neutral semantic representation** that any language can generate from. Remove English idioms, implicit assumptions, and ambiguous references.

---

# THE PROCESS

## Step 1: SEGMENT

Break into simple sentences. **One main verb per sentence.**

```
NIV: "The man's name was Elimelech, his wife's name was Naomi, and they had two sons."

→ That man's name was Elimelech. Elimelech's wife's name was Naomi. They had 2 sons.
```

## Step 2: RESOLVE REFERENCES

Replace all 3rd person pronouns with explicit nouns.

```
"He went" → "John went"
"They said to him" → "The Pharisees said to Jesus"
```

## Step 3: INTRODUCE NOUNS

Apply correct determiners and introduction patterns.

```
First mention: "a man", "some men"
After mention: "that man", "those men"
Names: "a town named Bethlehem"
```

## Step 4: RESTRUCTURE

Convert English-specific constructions to universal patterns.

```
Apposition → Relative clause: "X, Y's husband" → "X, [who was Y's husband]"
Demonyms → Description: "Moabite women" → "women [who were from Moab]"
Passive → Active: "was left with" → "lived with"
```

## Step 5: SIMPLIFY VOCABULARY

Use ontology-friendly words. Pair L2 words.

```
"worship" → "serve/worship"
"harvest" → "gather/harvest"
"urge" → "tell"
```

## Step 6: MARK STRUCTURE

Add brackets, mark implicit info, format quotes.

```
Patient clauses: "knew [Mary was there]"
Implicit info: "<<Naomi's sons grew up.>>"
Quotes: Speaker said, ["First sentence]. Second sentence."
```

## Step 7: VERIFY

Check against rules. Run linter.

---

# RULES BY IMPORTANCE

## CRITICAL (Must Always Apply)

### R1: No Third Person Pronouns

Never use: he, she, it, they, him, her, them

Replace with:

- Proper name: "Jesus", "Paul"
- Demonstrative + noun: "that man", "those people"
- Repeated noun: "Naomi" (not "she")

**Exception**: `each-other(people)` allowed for reciprocal.

### R2: One Verb Per Sentence

Each sentence has exactly one main verb. Auxiliaries (do, will, can) don't count.

```
Wrong: "The man went to town and bought food and returned home."
Right: "The man went to town. That man bought food. That man returned home."
```

### R3: Bracket Subordinate Clauses

All subordinate clauses in square brackets `[...]`.

| Type      | Example                          |
| --------- | -------------------------------- |
| Relative  | `the man [who was in the house]` |
| Patient   | `John knew [Mary was there]`     |
| Purpose   | `went [in order to see Mary]`    |
| Adverbial | `[When John arrived] Mary left`  |

Main clause is NEVER bracketed (except first sentence of quote).

### R4: No "That" in Patient Clauses

TBTA interprets "that" as demonstrative determiner.

```
Wrong: knew [that Mary was there]
Right: knew [Mary was there]
```

### R5: Numbers as Digits

Word numbers not recognized as adjectives.

```
Wrong: "two sons", "ten years"
Right: "2 sons", "10 years"
```

---

## HIGH PRIORITY (Apply in Most Cases)

### R6: Name Introduction Pattern

`[article] [category] named [Name]`

```
"Moab" → "a country named Moab"
"Ruth" → "a woman named Ruth"
"Bethlehem" → "a town named Bethlehem"
```

After first mention: "that country named Moab" or just "Moab".

### R7: Apposition → Relative Clause

English apposition is ambiguous. Convert to explicit relative clause.

```
"Elimelech, Naomi's husband" → "Elimelech, [who was Naomi's husband]"
"Bethlehem in Judah" → "Bethlehem, [which was in Judah]"
"Jesus, the son of God" → "Jesus, [who was God's son]"
```

### R8: Demonyms → Descriptive Phrases

Nationality adjectives don't translate universally.

```
"Moabite women" → "women [who were from Moab]"
"Ephrathites" → "people [who were in Ephrah's family/clan]"
"Israelites" → "people of Israel"
"Hebrew slaves" → "slaves [who were Hebrews]"
```

### R9: Determiner System

| Determiner       | When to Use                                  |
| ---------------- | -------------------------------------------- |
| `a` / `some`     | First mention                                |
| `that` / `those` | Already mentioned                            |
| `this` / `these` | New contrast or physically present           |
| `the`            | Frame inferable (the king = of this country) |
| ∅ (none)         | Generic ("People like food")                 |

**Key**: Prefer `that` over `the` after first mention.

### R10: Passive → Active Voice

Many languages lack passive. Convert when possible.

```
"she was left with her sons" → "she lived with her sons"
"was left without" → "didn't have"
"was given" → "received"
"is called" → "people call X"
```

When passive needed, include agent: `was hit by a soldier`.

---

## STANDARD (Apply as Needed)

### R11: Idiom → Explicit Meaning

English idioms don't translate.

| Idiom                          | Replacement                                |
| ------------------------------ | ------------------------------------------ |
| come to the aid of             | take care of                               |
| the LORD's hand turned against | the LORD treated X badly                   |
| find favor in eyes             | be kind to                                 |
| set out on the road            | started walking on the road                |
| urge me to leave               | tell me to leave                           |
| leftover grain                 | grain [that people left]                   |
| May the Lord bless you         | I pray [that Yahweh will bless you]        |
| The Lord be with you           | I pray [that Yahweh will be with you]      |
| man of standing                | People respected X + (implicit) X was rich |

### R12: Vocabulary Levels

| Level        | Action                                     |
| ------------ | ------------------------------------------ |
| 0-1 (simple) | Use directly                               |
| 2 (complex)  | Pair: `simple/complex`                     |
| 3 (abstract) | Use alternates: `(complex)... (simple)...` |
| 4 (names)    | Use directly                               |

**Common L2 pairings**:

- `serve/worship`
- `promise/swear`
- `gather/harvest`
- `grain/barley`
- `servants/workers`
- `kneel/bow`
- `family/clan`
- `friends/brothers-D`

**Explications** (when pairing won't work):

- `daughter-in-law` → `son's wife`
- `mother-in-law` → `husband's mother`

### R13: Quote Structure

**Single sentence**: Bracket entire quote

```
Naomi said, ["Return to your houses"].
```

**Multi-sentence**: Bracket FIRST sentence only

```
Naomi said, ["Return to your houses]. May the LORD bless you."
```

**Speaker + verb required**: Always `X said/asked/shouted, [...]`

**Addressee**: Use vocative in quote: `"My daughters, return..."`

**Nested quotes**:

```
Naomi said, ["Boaz said, ["Stay with my(Boaz's) workers"]"]
```

**Request patterns**: "Let me go" → imperative to listener

```
"Let me go" → You(Naomi) (imp) let [me(Ruth) go to...]
```

### R14: Implicit Information

| Notation  | Use                                         |
| --------- | ------------------------------------------- |
| `<<...>>` | Regular implicit (can be omitted)           |
| `<...>`   | Necessary implicit (grammatically required) |

**Types**:

- Gap-filling subactions: `<<Naomi's sons grew up.>>`
- Implied consequences: `<<If you come, you will become sad.>>`
- Passive agents: `was hit <<by a soldier>>`

### R15: Purpose Clauses

Use `[in order to...]` not bare infinitive.

```
Wrong: "went to see Mary"
Right: "went [in order to see Mary]"
```

Same agent required. Different agent? Use `[so that X could...]`.

### R16: Relative Clause Rules

**Must have relativizer**: who, whom, that

```
Wrong: "the man in the house"
Right: "the man [who was in the house]"
```

**No "when/where" as relativizers**:

```
Wrong: "the time [when John left]"
Right: "the time [that John left at]"
```

**No "that" with proper nouns** (use "who"):

```
"Jesus, [who was in Galilee]" (not "that")
```

### R17: 1st/2nd Person Pronouns

Mark referent in parentheses:

```
"I(Paul) went to the town"
"you(people) should listen"
```

Mark inclusive/exclusive for "we":

```
"We(Paul) _excl" — excluding hearer
"We(Paul) _incl" — including hearer
```

### R18: Titles and Footnotes

**Titles** at section start:

```
(title) Elimelech and Naomi move from Bethlehem to Moab.
```

**Footnotes** for cultural context:

```
(footnote) Before the Israelites had kings, judges were leaders.
```

---

## SPECIAL CASES

### R19: Hyphenated Verbs

Never inflect. Use as written in ontology.

```
Wrong: "picked-up", "stood-up"
Right: "pick-up", "stand-up"
```

Mark tense if needed: `pick-up _present`

Common hyphenated verbs: `sit-down`, `stand-up`, `pick-up`, `pull-out`

### R20: Existence vs Having

Use existential "there was" not "X had" (especially with adverbial clauses):

```
Wrong: "They had no food" (with adverbial clause before)
Right: "There was no food"
```

### R21: Divine Names

- Adults: "the LORD"
- Children: "Yahweh"
- "the LORD Almighty" for שְׁדַּי forms

### R22: Rhetorical Questions

Adults: Keep as questions
Children: Convert to statements

```
Adult: "Won't you marry other men?"
Child: "You should marry other men."
```

Mark type: `(yesrhetorical)`, `(norhetorical)`, `(rhetorical)`
Always provide `(statement)` alternate.

### R23: Ambiguous Words

Add `_noun`, `_verb`, `_adj` to clarify words that could be multiple parts of speech:

```
"judges _noun" — people who judged (not the verb "judges")
"judge _verb" — the action of judging
```

### R24: Ontology-Specific Verbs

Use exact ontology forms:

| Wrong      | Right   | Why                             |
| ---------- | ------- | ------------------------------- |
| give birth | birth   | "give birth" not in ontology    |
| arrived at | came to | "arrived" has case frame issues |
| living     | lived   | "living" not recognized         |

### R25: Membership vs Origin

For clan/family membership, use "in" not "from":

```
Wrong: "Boaz was from Elimelech's family"
Right: "Boaz was in Elimelech's family/clan"
```

"from" = origin/departure; "in" = membership/belonging

### R26: Scene Markers

Use "One day" to mark beginning of new scene (Begin Scene relation):

```
One day Ruth said to Naomi...
```

### R27: Destination Markers

Verbs like "give" require explicit destination:

```
Wrong: "gave the food Naomi"
Right: "gave the food to Naomi"
```

---

# VALIDATION CHECKLIST

Before submission:

- [ ] No 3rd person pronouns (R1)
- [ ] One verb per sentence (R2)
- [ ] All subordinate clauses bracketed (R3)
- [ ] No "that" in patient clauses (R4)
- [ ] Numbers as digits (R5)
- [ ] Names: "X named Y" pattern (R6)
- [ ] Appositives → relative clauses (R7)
- [ ] Demonyms → descriptions (R8)
- [ ] L2+ words paired/alternated (R12)
- [ ] Idioms simplified (R11)
- [ ] Quotes properly structured (R13)
- [ ] Implicit info marked (R14)
- [ ] Hyphenated verbs not inflected (R19)
- [ ] Ambiguous words marked (R23)
- [ ] Ontology verbs correct (R24)
- [ ] Membership uses "in" not "from" (R25)
- [ ] Destination markers present (R27)
- [ ] Linter passes

---

# AUDIENCE VARIATIONS

| Feature             | Churched Adult | Unchurched Adult | Children       |
| ------------------- | -------------- | ---------------- | -------------- |
| Implicit subactions | Omit           | `<<mark>>`       | Include inline |
| Divine name         | the LORD       | the LORD         | Yahweh         |
| Rhetorical Q        | Keep           | Keep             | → Statement    |
| Vocabulary          | Standard       | Standard         | Simplified     |
| Footnotes           | Minimal        | Full             | Full           |
| "bitter"            | bitter         | bitter           | sad            |
| "wept"              | wept           | wept             | cried          |
