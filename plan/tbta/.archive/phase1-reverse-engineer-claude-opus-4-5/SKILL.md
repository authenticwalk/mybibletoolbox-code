# TBTA Verse Generation Skill

> Transform NIV verses to Controlled Natural Language (CNL)

## Input
- NIV verse text
- Reference (Book Chapter:Verse)
- Format: He1 (natural/OT) or He2 (strict/NT)

## Process

```
1. COPY NIV base text
2. SEGMENT → one predicate per sentence
3. RESOLVE pronouns → explicit nouns
4. BRACKET all subordinate clauses [...]
5. MARK deixis: I(Speaker), you(Addressee)
6. MARK imperatives: (imp) verb
7. FRAME quotes: said, ["..."]
8. SUBSTITUTE "LORD" → "Yahweh" (OT only)
9. APPLY He2 markers (if He2 format)
```

---

## Transform Rules (Apply in Order)

### 🟢 Always Apply

| Rule | Pattern | Example |
|------|---------|---------|
| Clause Segmentation | One verb per sentence | "X and Y" → "X. Y." |
| Coreference | pronouns → nouns | "he went" → "Boaz went" |
| Bracketing | subordinate → `[...]` | "who was king" → `[who was king]` |
| Deixis | 1st/2nd person marked | "I said" → "I(Boaz) said" |
| Quote Framing | quotes → `["..."]` | said "X" → said, ["X"] |
| Imperative | command → `(imp)` | "Go!" → "(imp) Go" |
| Yahweh | LORD → Yahweh | OT only |

### 🟡 He2 Only

| Rule | Pattern |
|------|---------|
| LDV Pairs | `simple/complex` (e.g., people/disciples) |
| Underscore Markers | `_implicit`, `_paragraph`, `_dual` |
| Sense Suffixes | `kingdom-B`, `things-C` |
| Dual Translations | `(literal)/(dynamic)`, `(complex)/(simple)` |

### 🔴 Apply Selectively

| Rule | Notes |
|------|-------|
| "can" → "is able [to]" | Only for ability modal |
| Demonym → "[from X]" | Inconsistent - use judgment |
| Numbers | Large → digits, small → varies |

---

## Bracket Types

| Type | Opener | Example |
|------|--------|---------|
| Relative | `[that/who/which]` | the man `[who was king]` |
| Purpose | `[in-order-to]` | went `[in-order-to harvest]` |
| Result | `[with-the-result-that]` | spoke `[with-the-result-that people believed]` |
| Temporal | `[when/after/before]` | `[after the king died]` |
| Conditional | `[if]` | `[if you obey]` |
| Causal | `[because]` | `[because God loved]` |
| Comparative | `[just-like]` | `[just-like a shepherd]` |
| Content | `[that]` | knew `[that God was good]` |

---

## Example: Ruth 1:1

### Input (NIV)
```
In the days when the judges ruled, there was a famine in the land. So a man from Bethlehem in Judah, together with his wife and two sons, went to live for a while in the country of Moab.
```

### Output (He1)
```
[When judges ruled] there was a famine in the land. So a man [who lived in a town named Bethlehem [which was in Judah]] went to live in a country named Moab. That man's wife and that man's 2 sons went with that man.
```

### Transform Notes
1. `In the days when` → `[When...]` (temporal bracket)
2. `a man from Bethlehem` → `a man [who lived in a town named Bethlehem]` (relativization)
3. `Judah` → `[which was in Judah]` (location bracket)
4. `together with his wife and two sons` → segmented to separate sentence
5. `his wife` → `that man's wife` (coreference)
6. `two` → `2` (number as digit)
7. `the country of Moab` → `a country named Moab` (named entity)

---

## Validation Checklist

- [ ] No bare pronouns (he/she/they) without antecedent nearby
- [ ] One main verb per sentence
- [ ] All subordinate clauses in `[brackets]`
- [ ] 1st/2nd person marked: `I(Name)`, `you(Name)`
- [ ] Imperatives marked: `(imp)`
- [ ] Quotes bracketed: `["..."]`
- [ ] "LORD" → "Yahweh" (OT)
- [ ] He2: underscore markers present
- [ ] He2: L2 pairings used

---

## Common Errors to Avoid

1. ❌ Converting "must/should" (keep as-is)
2. ❌ Converting passive to active (keep passive)
3. ❌ Missing brackets on subordinate clauses
4. ❌ Unmarked deixis (I/you without parenthetical)
5. ❌ Unmarked imperatives (missing `(imp)`)
6. ❌ Over-segmenting (lists can stay together)
