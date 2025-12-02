# TBTA Verse Generation Skill

> NIV → Controlled Natural Language (CNL)  
> Based on reverse-engineering 6,963 TBTA verses

## Input
- NIV verse text
- Bible reference (Book Chapter:Verse)
- Format: He1 (natural) or He2 (strict)

## Process

```
1. COPY NIV base text
2. SEGMENT into one-predicate sentences
3. RESOLVE coreference (pronouns → nouns)
4. BRACKET subordinate clauses [...]
5. MARK deixis: I(Speaker), you(Addressee)
6. MARK imperatives: (imp) verb
7. SUBSTITUTE vocabulary (He2: use L2 pairings)
8. ADD implicit context markers (He2 only)
9. REPLACE "LORD" → "Yahweh" (OT)
```

## Transform Rules (Priority Order)

### Always Apply (🟢 >95% reliable)

1. **Clause Segmentation**: One verb per sentence
2. **Coreference Resolution**: `he/she/they` → `[Name]` or `that man/woman`
3. **Subordinate Bracketing**: `[who...]`, `[that...]`, `[when...]`, `[because...]`
4. **Deixis Marking**: `I(Speaker)`, `you(Addressee)`, `we(Group)`
5. **Quote Framing**: `said, ["Quote text"]`
6. **Imperative Marking**: `You(Name) (imp) verb`
7. **Yahweh Substitution**: `LORD` → `Yahweh` (OT only)

### Apply in He2 Format

8. **LDV L2 Pairings**: `simple/complex` (e.g., `people/disciples`)
9. **Underscore Markers**: `_implicit`, `_paragraph`, `_descriptive`
10. **Hyphenated Verbs**: `come-out`, `sit-down` with suffix `-B`, `-C`

### Apply Selectively

11. **Demonym → Description**: Only for geographic origin `[who was from X]`
12. **Modal "can"**: `can X` → `is able [to X]` (NOT must/should)
13. **Numbers**: Large numbers as digits, small numbers (1-12) may be words

### Do NOT Apply

14. ~~Passive → Active~~: Keep passive constructions as-is

---

## Example Transformation

### Input
**Reference**: Ruth 1:2  
**NIV**: "The man's name was Elimelek, his wife's name was Naomi, and the names of his two sons were Mahlon and Kilion. They were Ephrathites from Bethlehem, Judah. And they went to Moab and lived there."

### Transform Steps

| Step | Output |
|------|--------|
| 1. Copy | The man's name was Elimelek, his wife's name was Naomi, and the names of his two sons were Mahlon and Kilion. They were Ephrathites from Bethlehem, Judah. And they went to Moab and lived there. |
| 2. Segment | The man's name was Elimelek. His wife's name was Naomi. The names of his two sons were Mahlon and Kilion. They were Ephrathites from Bethlehem, Judah. They went to Moab. They lived there. |
| 3. Coreference | That man's name was Elimelech. That man's wife's name was Naomi. One son's name was Mahlon. The other son's name was Kilion. Elimelech and Naomi were Ephrathites from Bethlehem, Judah. That family went to Moab. That family lived in Moab. |
| 4. Bracket | That man's name was Elimelech. That man's wife's name was Naomi. One son's name was Mahlon. The other son's name was Kilion. Elimelech and Naomi were [in Ephrah's family/clan]. That family was living in a town named Bethlehem [which was in Judah]. That family went to a country named Moab. That family lived in Moab. |

### Final Output (He1)
```
That man's name was Elimelech. And that man's wife's name was Naomi. One son's name was Mahlon. And the other son's name was Kilion. Elimelech and Naomi were in Ephrah's family/clan. That family was living in a town named Bethlehem [which was in Judah]. But that family went to a country named Moab. And that family lived in Moab.
```

---

## He1 vs He2 Output Comparison

### He1 (Natural - OT Style)
```
That man's name was Elimelech. And that man's wife's name was Naomi.
```

### He2 (Strict - NT Style)
```
That man's name was Elimelech. And that man's wife's name was Naomi. _paragraph
```

---

## Bracketing Quick Reference

| Clause Type | Pattern | Example |
|-------------|---------|---------|
| Relative | `[who/that/which...]` | `the man [who was king]` |
| Content | `[that...]` | `knew [that Ruth was good]` |
| Purpose | `[in order to...]` | `went [in order to harvest]` |
| Temporal | `[when/after/before...]` | `[when judges ruled]` |
| Conditional | `[if...]` | `[if you go]` |
| Causal | `[because...]` | `[because the king was generous]` |
| Comparative | `[just-like...]` | `[just-like a shepherd]` |

---

## Common L2 Pairings

| Simple | Complex |
|--------|---------|
| people | disciples |
| stories | parables |
| spirits | demons |
| family | clan |
| grain | barley |
| gather | harvest |
| buy | redeem |
| dirty | unclean |
| surprised | amazed |
| holes | caves |
| followers | disciples |

---

## Validation Checklist

- [ ] No bare pronouns (he/she/they) without clear antecedent
- [ ] One main verb per sentence
- [ ] All subordinate clauses in `[brackets]`
- [ ] First/second person marked: `I(Name)`, `you(Name)`
- [ ] Imperatives marked: `(imp)`
- [ ] Quotes bracketed: `["..."]`
- [ ] "LORD" → "Yahweh" (OT)
- [ ] He2: underscore markers present
- [ ] He2: L2 pairings used

---

## Error Patterns to Avoid

1. ❌ Converting "must/should" to "has to" (keep as-is)
2. ❌ Converting passive to active (keep passive)
3. ❌ Missing brackets on subordinate clauses
4. ❌ Unmarked deixis (I/you without parenthetical)
5. ❌ Unmarked imperatives (missing `(imp)`)
6. ❌ Over-converting demonyms (some stay as proper nouns)

