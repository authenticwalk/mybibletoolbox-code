# TBTA Phase 1 (He1) — Subagent V1 (Policy-First)

> **Mission**: Convert NIV verse into simplified English (He1) for TBTA.
> **Approach**: Policy-based rules from official TBTA documentation.

## Also Read

| File | Purpose |
|------|---------|
| `learnings-v1.md` | V1-specific patterns from prior encodings |

## Your Task

You will receive: verse reference + NIV text
You must return: encoded He1 text that passes the linter

## Process

1. **Apply 5 transforms** to the NIV text
2. **Run checklist pass** (Step 6)
3. **Validate** with linter until clean (max 12 iterations)
4. **Return** your final He1 encoding

---

## The 5 Transforms + Checklist Pass

| Step | Goal | Rule |
|------|------|------|
| 1 | Copy NIV | Raw input |
| 2 | Fix pronouns | Resolve 3rd person to nouns, split sentences |
| 3 | Simplify vocabulary | L0-1 direct, L2 pair, L3 alternate |
| 4 | Group participants | Collapse repeated noun phrases |
| 5 | Fix clauses | Add brackets, relative clauses |
| **6** | **Checklist pass** | **Verify remaining rules** |

### Step 6: Checklist Pass

| Check | Rule | Reference |
|-------|------|-----------|
| Quotes | Speaker + verb intro? First sentence bracketed? | §10 |
| Implicit | `<<regular>>` or `<necessary>` marked? | §9 |
| Passives | Agent with "by"? | §13, §24 |
| Commands | `(imp)` or natural English? | §15 |
| Causality | "to" → "in order to"? | §8 |
| Tense | Perfect only if "recently/previously" works? | §18 |
| Connectors | And/But/Then/So flow? | §32 |
| Special | No "can", "even", "any", "own"? | §17, §24 |

---

## Rules by Category

### Pronouns (§3)
- **Third person (he/she/they/it)** → ALWAYS resolve to nouns, even after first mention
- **First/second person**: `I(Paul)`, `you(people)`, `we(Peter) _excl`
- "Natural pronouns" = 1st/2nd person keeps pronoun form after initial marking

### Words (§1-2)
| Level | Color | Action |
|-------|-------|--------|
| 0-1 | Blue/Cream | Use directly |
| 2 | Magenta | Pair: `simple/complex` |
| 3 | Green | Alternate: `(complex)...(simple)...` |
| 4 | Brown | Proper nouns, use directly |

**Common pairings**: `serve/worship`, `promise/swear`, `gather/harvest`, `grain/barley`, `family/clan`

**Explications**: `daughter-in-law` → `son's wife`, `mother-in-law` → `husband's mother`

### Clauses (§4-7)
- One verb per clause
- Subordinate clauses in brackets: `[who was in the house]`
- Max 4 levels of nesting
- NO "that" starting patient clauses: `knew [X...]` not `knew [that X...]`
- Relative clauses need relativizer: `who`, `whom`, `that`
- Hyphenated verbs NEVER inflect: `pick-up` not `picked-up`
- But "sit down", "stand up" are TWO WORDS and DO inflect: `sat down`, `stood up`

### Determiners (§3.1)
| Situation | Use |
|-----------|-----|
| First mention | `a man`, `some men` |
| Already mentioned | `that man` |
| Newly contrasted | `this man` |
| Frame inferable | `the king` |
| Generic | No article |

### Quotes (§10)
```
X said, ["First sentence]. Second sentence..."
```
Bracket only first sentence (patient clause of "say").

### Commands (§15)
```
You(John) (imp) go to the town.
```

### Special Constructions

| Pattern | Wrong | Right |
|---------|-------|-------|
| Existence | "did not have food" | "there was not enough food" |
| Numbers | "two sons" | "2 sons" |
| Ambiguity | "judges ruled" | "judges _noun ruled" |
| Apposition | "X, Y's husband" | "X [who was Y's husband]" |
| Nationality | "X the Moabite" | "X [who was from Moab]" |
| Ability | "can go" | "is able [to go]" |
| Purpose | "went to see" | "went [in order to see]" |
| Passive | "was hit" | "was hit by X" |

### Idioms
- "find favor in eyes" → `be kind to me`
- "The Lord be with you" → `I pray [that Yahweh will be with you]`
- "was left with" → `lived with only`
- "leftover grain" → `grain [that people left]`

### Verb-Specific
- Use `gave birth to` (NOT "birth" or "birthed")
- Use `sexed` not "slept with" or "had sex with"
- Use `came to X` instead of `arrived at X`
- Use `lived` instead of `living`

---

## Linter API

**URL**: `https://editor.tabitha.bible/check?text={urlencoded_he1}`

Run this after each iteration. Fix all errors before returning.

**Ontology lookup**: `https://ontology.tabitha.bible/?q={word}` — check word levels

---

## Output Format

Return your work in this format:

```markdown
# {BOOK} {ch}:{vs} — He1 Encoding

## Step 1: Copy NIV
text = "..."

## Step 2: Fix Pronouns
Changes: {list each pronoun → noun replacement}
text = "..."

## Step 3: Simplify Vocabulary
Changes: {list each word → replacement with reason}
text = "..."

## Step 4: Group Participants
Changes: {list groupings or "none needed"}
text = "..."

## Step 5: Fix Clauses
Changes: {list clause fixes}
text = "..."

## Step 6: Checklist Pass
Quotes: {ok or changes}
Implicit: {ok or changes}
Passives: {ok or changes}
Commands: {ok or changes}
Causality: {ok or changes}
Connectors: {ok or changes}
text = "..."

## Final He1
text = "..."

## Linter Results
Errors: {list or "None"}
Iterations: {number}
```

---

## Success Criteria

Your encoding is complete when:
- [ ] Linter passes (no blocking errors)
- [ ] L2+ words have pairings or alternates
- [ ] All 3rd person pronouns resolved to nouns
- [ ] Patient clauses have no leading "that"
- [ ] All `learnings-v1.md` patterns applied

## Issues for Orchestrator

If you encounter patterns not covered in this skill or learnings-v1.md, report them:
```
Issues: {list patterns/ambiguities encountered}
```
