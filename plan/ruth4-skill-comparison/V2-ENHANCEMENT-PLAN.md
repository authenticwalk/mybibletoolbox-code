# V2 Enhancement Plan: What to Merge from Other Files

## Summary

| Source | Valuable Content | Priority |
|--------|------------------|----------|
| **SKILL.md** | Step 6 Checklist Pass, Hard Requirements | HIGH |
| **SKILL-old.md** | Decision Trees, Common Mistakes table | HIGH |
| **learnings.md** | Hyphenated verbs, L2 pairings | CRITICAL |
| **examples.md** | (imp) examples, rhetorical questions | MEDIUM |

---

## CRITICAL: Missing from V2 (causes test failures)

### 1. Hyphenated Verbs Rule (from learnings.md)
**V2 agents made this error repeatedly.**

```markdown
### Hyphenated Verbs (§NEW)
- ❌ NEVER inflect hyphenated verbs
- ✅ Use base form always: `sit-down`, `pick-up`, `stand-up`
- ❌ Wrong: "picked-up", "sat-down"
- ✅ Right: "Boaz pick-up the grain", "Ruth sit-down"
```

### 2. Nested Quotes (from learnings.md)
**V2 doesn't cover this at all.**

```markdown
### Nested Quotes (§NEW)
- Structure: `["outer quote ["inner quote"]"]`
- Example: `said, ["Boaz said, ["Stay with my workers"]"]`
```

### 3. Request Patterns (from learnings.md)
**"Let me go" pattern confused all agents.**

```markdown
### Request Patterns (§NEW)
- "Let me go" → `You(X) (imp) let [me(Y) go to...]`
- The request is an imperative to the listener
```

---

## HIGH: Add to V2 (improves accuracy significantly)

### From SKILL.md: Step 6 Checklist Pass

**Why**: V2 has 5 transforms but no verification pass. Agents stopped too early.

```markdown
## Step 6: Checklist Pass

After the 5 transforms, verify these additional rules:

| Category | Check | Reference |
|----------|-------|-----------|
| **Quotes** | Speaker + verb intro? First sentence bracketed? | §10 |
| **Implicit** | `<<regular>>` or `<necessary>` marked? | §9 |
| **Passives** | Agent included with "by"? | §13, §24 |
| **Commands** | `(imp)` notation with explicit `you(addressee)`? | §15 |
| **Causality** | "to" → "in order to" where needed? | §8 |
| **Tense** | Perfect only if "recently/previously" works? | §18 |
| **Connectors** | And/But/Then/So flow naturally? | §32 |
| **Determiners** | a/that/this/the correct? | §3.1 |
| **Special** | No "can", "even", "any", "own"? | §17, §24 |
```

### From SKILL.md: Hard Requirements

**Why**: Agents didn't prioritize linter or learnings file.

```markdown
## Hard Requirements

⚠️ **Linter MUST pass** — verse is not done until `check` returns no blocking errors
⚠️ **Check learnings FIRST** — read `./learnings.md` before drafting
⚠️ **Update learnings** — if you discover a new pattern, add it
```

### From SKILL-old.md: Decision Trees

**Why**: Algorithmic approach helps agents make consistent decisions.

```markdown
## Decision Trees

### When is a word too complex?
```
Is it in the ontology at Level 0-1 (blue/cream)?
  ├─ YES → Use it directly
  └─ NO → Is it Level 2 (magenta)?
           ├─ YES → Pair it: simple/complex
           └─ NO → Is it Level 3 (green)?
                    ├─ YES → Use (complex)/(simple) alternates
                    └─ NO (Level 4, brown) → Proper noun, use directly
```

### How to handle "have" + clause?
```
Does "have" appear with an adverbial clause before it?
  ├─ YES → Rewrite using existential "be"
  │         ❌ "[When X happened] people did not have food"
  │         ✅ "[When X happened] there was not enough food"
  └─ NO → "have" is probably fine
```

### How to handle apposition (X, Y's Z, ...)?
```
Is there a noun followed by a clarifying phrase?
  ├─ YES → Convert to relative clause
  │         ✅ "Elimelech [who was Naomi's husband] died"
  └─ NO → Leave as-is
```
```

### From SKILL-old.md: Common Mistakes & Fixes

**Why**: Agents kept making these same mistakes.

```markdown
## Common Mistakes & Fixes

| Symptom | Cause | Fix |
|---------|-------|-----|
| "have cannot be used with different-participant patient clause" | Adverbial clause before "have" | Use existential "be" |
| "word not found" | Number written as word | Use numerals: 2, 3, 10 |
| "ambiguous word" | Noun/verb confusion | Add `_noun` or `_verb` |
| Checker loops on same error | Wrong sense of word | Check ontology, specify `-A`, `-B`, etc. |
| Generated English sounds wrong | Missing pairing | Add `simple/complex` for L2 words |
| Hyphenated verb error | Verb was inflected | Use base form: `sit-down` not `sat-down` |
```

### From SKILL-old.md: Targets API

**Why**: V2 is missing this useful API.

```markdown
| **Targets** | `targets.tabitha.bible/English/{Book}/{ch}/{vs}` | Generated English for audiences |
```

---

## MEDIUM: Add to V2 (improves completeness)

### From learnings.md: Expanded L2 Pairings

V2 has some, but learnings.md has more:

```markdown
### L2 Word Pairings (§1-2)

| L2 Word | Pairing |
|---------|---------|
| worship | serve/worship |
| swear | promise/swear |
| harvest | gather/harvest |
| barley | grain/barley |
| workers | servants/workers |
| bow | kneel/bow |
| daughter-in-law | son's wife (explicate) |
| mother-in-law | husband's mother (explicate) |
```

### From learnings.md: Idiom Simplifications

```markdown
### Idiom Simplifications (§NEW)

| Idiom | Transform |
|-------|-----------|
| "find favor in eyes" | "be kind to me" |
| "leftover grain" | "grain/barley [that people left]" |
| "The Lord be with you" | "I pray [that Yahweh will be with you]" |
| "The Lord bless you" | "I pray [that Yahweh will do good things for you]" |
| "May the Lord..." | "I pray [that Yahweh will...]" |
```

### From examples.md: Pattern Summary Table

Great quick reference at the end:

```markdown
## Pattern Summary

| NIV Pattern | He1 Transform |
|-------------|---------------|
| Third person pronoun | Resolve to noun |
| Apposition (X, Y's Z) | Relative clause [who was Y's Z] |
| Nationality (X the Y-ite) | Relative clause [who was from Y] |
| "was left with" | "lived with only" |
| "The Lord be with you" | "I pray [that Yahweh will be with you]" |
| "bless" | "do good things for" |
| "can" | "is able [to...]" |
| Rhetorical question | Add (statement) version |
| Number words | Digits |
```

### From examples.md: Rhetorical Questions

V2 doesn't mention this at all:

```markdown
### Rhetorical Questions (§NEW)

When encoding rhetorical questions:
1. Provide the question with `(yesrhetorical)` marker
2. Provide the `(statement)` version immediately after

Example:
```
(yesrhetorical) Which person is able [to fight against us]?
(statement) No person is able [to fight against us].
```
```

### From examples.md: Commands with (imp)

V2 mentions (imp) but no example. Genesis 22:2 shows it perfectly:

```markdown
### Commands Example (§15)

NIV: "Take your son... and go to the region of Moriah."

He1: `["You(Abraham) (imp) take your(Abraham's) son [who is your(Abraham's) only son] [whom you(Abraham) love]. That son is named Isaac. And you(Abraham) (imp) go to a region named Moriah."]`

Key points:
- Explicit `you(addressee)` before each imperative
- `(imp)` marker on command verbs
- Possessives clarified: `your(Abraham's)`
```

---

## What NOT to Bring

| Content | Why Skip |
|---------|----------|
| V1's sparse structure | V2's categorical structure is better |
| V3's linked files approach | Causes sync issues, keep in single file |
| SKILL.md's linked rules/ | Same reason - keep consolidated |
| Redundant examples | Only add examples that show NEW patterns |

---

## Proposed V2 Structure After Enhancement

```markdown
# TBTA Phase 1 (He1) — V2 Enhanced

## Hard Requirements (⚠️)
## Process
## The 5 Transforms + Checklist Pass
## Rules by Category (with § references)
## Decision Trees
## Common Mistakes & Fixes
## L2 Pairings Table
## Idiom Transformations
## Pattern Summary
## APIs
## Success Criteria
## Files
```

**Estimated size**: ~250 lines (up from ~160)
**Expected accuracy improvement**: 55% → 75%+ based on errors fixed
