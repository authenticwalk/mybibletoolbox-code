# NIV → TBTA Quick Reference

## The Process

```
1. SEGMENT    → One verb per sentence
2. RESOLVE    → Replace pronouns with nouns
3. INTRODUCE  → Apply name/determiner patterns
4. RESTRUCTURE→ Apposition→relative, demonym→phrase, passive→active
5. SIMPLIFY   → L2 pairings, idiom→explicit
6. MARK       → Brackets, implicit markers, quotes
7. VERIFY     → Check rules, run linter
```

---

## Critical Rules (R1-R5)

| #   | Rule                 | Wrong → Right                |
| --- | -------------------- | ---------------------------- |
| R1  | No 3rd pronouns      | "he went" → "John went"      |
| R2  | One verb/sentence    | compound → split             |
| R3  | Bracket clauses      | `knew [Mary was there]`      |
| R4  | No "that" in patient | `knew [that X]` → `knew [X]` |
| R5  | Digits for numbers   | "two" → "2"                  |

---

## Patterns (R6-R10)

| Pattern    | Transform                                     |
| ---------- | --------------------------------------------- |
| Name intro | "a town named Bethlehem"                      |
| Apposition | "X, Y's husband" → "X, [who was Y's husband]" |
| Demonym    | "Moabite" → "[who was from Moab]"             |
| Passive    | "was left with" → "lived with"                |
| Membership | "was in X's clan" (not "from")                |

---

## L2 Pairings (R12)

```
serve/worship    promise/swear    gather/harvest
grain/barley     servants/workers kneel/bow
family/clan      friends/brothers-D
```

**Explications**:

- `daughter-in-law` → `son's wife`
- `mother-in-law` → `husband's mother`

---

## Quotes (R13)

```
Single:  X said, ["sentence"].
Multi:   X said, ["first]. Second. Third."
Nested:  X said, ["Y said, ["quote"]"]
Request: "Let me go" → You(X) (imp) let [me(Y) go...]
```

---

## Idioms → Explicit (R11)

| Idiom              | Replace With                         |
| ------------------ | ------------------------------------ |
| find favor in eyes | be kind to                           |
| come to the aid    | take care of                         |
| May the Lord bless | I pray [that Yahweh will bless...]   |
| man of standing    | People respected X + (implicit) rich |
| leftover grain     | grain [that people left]             |

---

## Special Cases (R19-R27)

| Rule | Issue               | Fix                          |
| ---- | ------------------- | ---------------------------- |
| R19  | Hyphenated verbs    | `pick-up` not `picked-up`    |
| R20  | "X had" with adverb | → "there was"                |
| R23  | Ambiguous words     | Add `_noun`, `_verb`, `_adj` |
| R24  | Wrong ontology verb | `birth` not `give birth`     |
| R25  | Clan membership     | "in X's clan" not "from"     |
| R26  | Scene start         | "One day..."                 |
| R27  | Missing destination | "gave X to Y" (need "to")    |

---

## Checklist

- [ ] No he/she/they/it (R1)
- [ ] One verb per sentence (R2)
- [ ] Subordinates bracketed (R3)
- [ ] No "that" in patient clauses (R4)
- [ ] Numbers as digits (R5)
- [ ] Names: "X named Y" (R6)
- [ ] Appositives → relatives (R7)
- [ ] Demonyms → descriptions (R8)
- [ ] L2 words paired (R12)
- [ ] Idioms explicit (R11)
- [ ] Hyphenated verbs correct (R19)
- [ ] Ambiguous words marked (R23)
- [ ] Ontology verbs correct (R24)
- [ ] Membership = "in" (R25)
- [ ] Destinations present (R27)
