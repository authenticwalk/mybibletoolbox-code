# Blind Test Results: Ruth 1 (He1) & Matthew 5 (He2)

**Date**: 2024-12-02
**Test Method**: Subagents given TEST-SKILL.md rules only, no reference to actual TBTA

---

## Summary

| Format | Verses | Structural Match | Critical Failures |
|--------|--------|------------------|-------------------|
| He1 (Ruth 1) | 22 | ~60% | 6 rule gaps |
| He2 (Matt 5:1-24) | 24 | ~70% | 5 rule gaps |

---

## He1 (Ruth 1) Analysis

### What Worked ✓
- Basic coreference resolution (he → that man)
- Quote framing with `said, ["..."]`
- Deixis marking: `I(Naomi)`, `you(Ruth)`
- Imperative marking: `(imp)`
- Yahweh substitution: LORD → Yahweh
- Basic subordinate bracketing

### Critical Failures ✗

#### 1. Missing Title Markers
```
Subagent: [no title]
Actual:   Elimelech (title) and Naomi move from Bethlehem to Moab.
```
**Rule Gap**: He1 DOES use `(title)` markers - not documented

#### 2. Vocabulary Simplification
```
Subagent: "there was a famine in the land"
Actual:   "many people [who were living in Israel] did not have enough food"
```
**Rule Gap**: Abstract nouns → concrete descriptions (famine → no food)

#### 3. Named Entity Pattern Not Applied
```
Subagent: "the country of Moab"
Actual:   "a country named Moab"
```
**Rule Gap**: "X of Y" → "X named Y" pattern inconsistently applied

#### 4. Nested Relativization Missing
```
Subagent: "from Bethlehem in Judah"
Actual:   "from Bethlehem [which was in Judah]"
```
**Rule Gap**: Location appositives → bracketed relatives

#### 5. L2 Pairings in He1
```
Subagent: "Ephrathites"
Actual:   "Ephrah's family/clan"
```
**Rule Gap**: He1 DOES use some L2 pairs - documented as He2-only

#### 6. Purpose Clauses Expanded
```
Subagent: "went to live for a while"
Actual:   "moved... [in order to live in Moab for a few years]"
```
**Rule Gap**: Implicit purpose → explicit `[in-order-to]`

---

## He2 (Matthew 5:1-24) Analysis

### What Worked ✓
- `(literal)/(dynamic)` dual translations
- `_implicitActiveAgent` markers
- `kingdom-B` sense suffixes
- Quote framing
- Deixis marking
- Basic subordinate bracketing

### Critical Failures ✗

#### 1. Hyphenated Verbs Not Applied
```
Subagent: "Jesus went up on a mountainside. Jesus sat down."
Actual:   "Jesus go-up the side of a mountain. And Jesus sit-down."
```
**Rule Gap**: Hyphenated verbs use BASE FORM (go-up, not went-up)

#### 2. Addressee Consistency
```
Subagent: "You(Disciples)"
Actual:   "You(people)" or "You(followers)"
```
**Rule Gap**: Generic `(people)` preferred over specific groups

#### 3. L2 Verb Pairings Missing
```
Subagent: "Jesus began to teach"
Actual:   "Jesus teaches/preach"
```
**Rule Gap**: Common verbs need L2 pairs: teaches/preach, cry/mourn-B

#### 4. Marker Types Missing
```
Subagent: [no _AdverbLDV]
Actual:   "similarly _AdverbLDV"
```
**Rule Gap**: `_AdverbLDV`, `_Dimplicit`, `_distantPast` not documented

#### 5. Descriptive Titles vs Generic
```
Subagent: "(title) The Sermon on the Mount"
Actual:   "(title) Jesus teaches/preach about God's laws to people on a mountain"
```
**Rule Gap**: Titles describe ACTION, not traditional names

---

## Rules to Add/Fix

### HIGH Priority (affects many verses)

| Issue | Current Rule | Fix |
|-------|--------------|-----|
| Hyphenated verb form | "run-away, sit-down" | Add: "Always BASE form, never inflected" |
| Title content | Not specified | Add: "Titles describe the action, not traditional names" |
| L2 in He1 | "He2 mainly" | Fix: "Common pairs appear in He1 too: family/clan" |
| Named entity pattern | "a man named X" | Add: "a country named X", "a town named X" |

### MEDIUM Priority (affects some verses)

| Issue | Current Rule | Fix |
|-------|--------------|-----|
| Addressee generics | "you(Addressee)" | Add: "Prefer (people), (person) over specific groups" |
| Abstract → concrete | Not documented | Add: "famine → people did not have food" |
| New underscore types | Only `_implicit` | Add: `_AdverbLDV`, `_Dimplicit`, `_distantPast` |

### LOW Priority (edge cases)

| Issue | Notes |
|-------|-------|
| `_1stAs3rd` | Son of Man references |
| `(footnote)` placement | Cross-reference format |
| Nested possessives | "that man's wife's name" |

---

## Test Verdict

**He1 Rules**: Need significant expansion for:
- Title markers
- Named entity patterns
- Vocabulary simplification principles

**He2 Rules**: Core structure solid, needs:
- Expanded underscore taxonomy
- Verb form clarification (base form only)
- L2 pairing examples

**Recommendation**: Update RULES.md with HIGH priority fixes, then re-test.
