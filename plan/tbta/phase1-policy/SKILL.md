# TBTA Verse Generation Skill

> Convert NIV verse → TBTA intermediary language (language-neutral semantic representation).

## Input
- NIV verse text
- Book/chapter/verse reference

## Process

### Step 1: SEGMENT
Split into simple sentences. **One verb per sentence.**
```
NIV: "The man's name was Elimelech, his wife's name was Naomi"
→ "That man's name was Elimelech. That man's wife's name was Naomi."
```

### Step 2: RESOLVE PRONOUNS
- **3rd person** (he/she/they/it) → explicit nouns
- **1st/2nd person** → mark referent: `I(Naomi)`, `you(Ruth)`, `my(Boaz's)`
- **we/us** → add `_incl` or `_excl`
```
"he went" → "John went"
"I said" → "I(Naomi) said"
```

### Step 3: INTRODUCE NOUNS
| Context | Pattern |
|---------|---------|
| First mention | `a man`, `some people` |
| After mention | `that man`, `those people` |
| Named entity | `a country named Moab` |

### Step 4: RESTRUCTURE
| Pattern | Transform |
|---------|-----------|
| Apposition | `X, Y's husband` → `X, [who was Y's husband]` |
| Demonym | `Moabite` → `[who was from Moab]` |
| Passive | `was left with` → `lived with` |
| "can" | → `is able [to...]` |

### Step 5: SIMPLIFY VOCABULARY
- L2 words: use pairings (`family/clan`, `grain/barley`, `gathering/harvesting`)
- Complex terms: explicate (`daughter-in-law` → describe as `son's wife` if needed)

### Step 6: ADD STRUCTURE
- **Brackets**: All subordinate clauses in `[...]`
- **Patient clauses**: NO "that" - write `knew [Mary was there]`
- **Purpose**: `[in order to...]` not bare infinitive
- **Quotes**: `X said, ["First sentence]. Second sentence."`
- **Commands**: `You(X) (imp) verb...`
- **Implicit**: `(implicit-info)` for added context

### Step 7: VERIFY
Apply checklist:
- [ ] No 3rd person pronouns
- [ ] One verb per sentence
- [ ] All subordinates bracketed
- [ ] No "that" starting patient clauses
- [ ] Numbers as digits (2, 10, not two, ten)
- [ ] Names introduced: "X named Y"
- [ ] Hyphenated verbs base form: `run-away` not `ran-away`

---

## Examples

### Narrative
```
NIV: "Now Elimelech, Naomi's husband, died, and she was left with her two sons."

TBTA: "Elimelech [who was Naomi's husband] died later. So Naomi lived with only Naomi's 2 sons."
```

### Dialogue
```
NIV: "Go back, my daughters. Why would you come with me?"

TBTA: "My(Naomi's) daughters, you(daughters in law) (imp) return to your(daughters in law's) houses. You(daughters) (imp) do not come with me(Naomi)."
```

### Introduction
```
NIV: "Now there was a famine in the land. So a man from Bethlehem in Judah..."

TBTA: "[When judges were ruling Israel] many people [who were living in Israel] did not have enough food. A certain man was from Bethlehem [which was in Judah]."
```

---

## Critical Rules Summary

| Rule | Wrong | Right |
|------|-------|-------|
| Pronouns | "he went" | "John went" |
| Patient | `knew [that X]` | `knew [X]` |
| Numbers | "two sons" | "2 sons" |
| Hyphenated | "ran-away" | "run-away" |
| Purpose | "went to see" | "went [in order to see]" |
| Apposition | "X, the king" | "X, [who was the king]" |
| Demonym | "Moabite women" | "women [who were from Moab]" |
| Can | "can go" | "is able [to go]" |

## L2 Pairings (memorize)
```
family/clan          grain/barley        gathering/harvesting
workers/harvesters   buy/redeem          master/lord
serve/worship        promise/swear       wine/vinegar
```

## Output Format
Plain text with:
- Simple sentences (one verb each)
- Bracketed subordinate clauses
- Marked pronouns: `I(X)`, `you(Y)`, `my(Z's)`
- Commands: `You(X) (imp) verb`
- Quotes: `X said, ["first]. rest."`
