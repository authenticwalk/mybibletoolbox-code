# TBTA Phase 1 (He1) — V1: Examples-First

> **Mission**: Convert NIV verses into simplified English (He1) for TBTA.

## Process

For each verse in `./TODO.md`:

1. **Get NIV** → `quote_verse {Book} {ch}:{vs} NIV`
2. **Read learnings** → Check `./learnings.md` for known patterns ⚠️ REQUIRED
3. **Draft He1** → Apply 5 transforms + checklist pass, log to `./output/{BOOK}-{ch}-{vs}.md`
4. **Check** → `editor.tabitha.bible/check?text={urlencoded}` ⚠️ MUST PASS
5. **Fix** → Repeat steps 3-4 until linter clean (max 12 iterations)
6. **Compare** → `sources.tabitha.bible/Bible/{Book}/{ch}/{vs}` (only after drafting!)
7. **Learn** → Add new patterns to `./learnings.md` ⚠️ REQUIRED

**Hard Requirements:**
- ⚠️ Linter MUST pass — verse not done until `check` returns no blocking errors
- ⚠️ Check learnings FIRST — avoid repeating known mistakes
- ⚠️ Update learnings — add any new patterns discovered

---

## Output Format

**Create file**: `./output/{BOOK}-{ch:03d}-{vs:03d}.md`

Write each step showing the text state:

```markdown
# {BOOK} {ch}:{vs} — He1 Encoding (V1)

## Step 1: Download NIV
text = "..."

## Step 2: Fix Pronouns
Changes: he→John, they→the family
text = "..."

## Step 3: Simplify Vocabulary  
Changes: worship→serve/worship, two→2
text = "..."

## Step 4: Group Participants
Changes: "John, Mary, and the children"→"that family"
text = "..."

## Step 5: Fix Clauses
Changes: "in the house"→"[who was in the house]"
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

## Check Results
Errors: (list or "None")

## Comparison
Reference: (from sources.tabitha.bible)
Differences: (list or "Matches")
```

---

## The 5 Transforms + Checklist Pass

After the 5 transforms, run a checklist pass for rules not covered:

| Check | Rule |
|-------|------|
| Quotes | Speaker + verb intro? First sentence bracketed? (§10) |
| Implicit | `<<regular>>` or `<necessary>` marked? (§9) |
| Passives | Agent included with "by"? (§13) |
| Commands | `(imp)` notation or natural English? (§15) |
| Causality | "to" → "in order to" where needed? (§8) |
| Connectors | And/But/Then/So flow? (§32) |
| Special | No "can", "even", "any"? (§17, §24) |

---

## Learn from Examples

### Example A: Ruth 1:2

**Step 1: Download NIV**
```
text = "The man's name was Elimelek, his wife's name was Naomi, and the names of his two sons were Mahlon and Kilion. They were Ephrathites from Bethlehem, Judah. And they went to Moab and lived there."
```

**Step 2: Fix Pronouns**
- "They" (first) → "The man, his wife, and his 2 sons"
- "they" (second) → "the man, his wife, and his 2 sons"
- "there" → "in the country of Moab"
- Split into separate sentences
```
text = "The man's name was Elimelek. His wife's name was Naomi. The names of his 2 sons were Mahlon and Kilion. The man, his wife, and his 2 sons were Ephrathites from Bethlehem, Judah. And the man, his wife, and his 2 sons went to the country of Moab and lived in the country of Moab."
```

**Step 3: Simplify Vocabulary**
- "Ephrathites" → "people in Ephrah's family"
- "Bethlehem, Judah" → "town named Bethlehem in region named Judah"
```
text = "That man's name was Elimelech. That man's wife's name was Naomi. One son's name was Mahlon. The other son's name was Kilion. Elimelech and Naomi were people in Ephrah's family in the town named Bethlehem in the region named Judah. That family went to a country named Moab and lived in Moab."
```

**Step 4: Group Participants**
- "Elimelech and Naomi" stays (needed for context)
- Add "family/clan" pairing
```
text = "That man's name was Elimelech. That man's wife's name was Naomi. One son's name was Mahlon. The other son's name was Kilion. Elimelech and Naomi were in Ephrah's family/clan. That family was living in a town named Bethlehem in the region named Judah. That family went to a country named Moab. And that family lived in Moab."
```

**Step 5: Fix Clauses**
- "in the region named Judah" → relative clause
- Add connectors: "And", "But"
```
text = "That man's name was Elimelech. And that man's wife's name was Naomi. One son's name was Mahlon. And the other son's name was Kilion. Elimelech and Naomi were in Ephrah's family/clan. That family was living in a town named Bethlehem [which was in Judah]. But that family went to a country named Moab. And that family lived in Moab."
```

---

### Example B: Ruth 1:3

**Step 1: Download NIV**
```
text = "Now Elimelek, Naomi's husband, died, and she was left with her two sons."
```

**Step 2: Fix Pronouns**
- "she" → "Naomi"
- "her" → "Naomi's"
```
text = "Elimelek, Naomi's husband, died. Naomi was left with Naomi's 2 sons."
```

**Step 3: Simplify Vocabulary**
- "was left with" → "lived with only" (idiom)
```
text = "Elimelech, Naomi's husband, died. Naomi lived with only Naomi's 2 sons."
```

**Step 4: Group Participants**
- (no grouping needed)
```
text = "Elimelech, Naomi's husband, died. Naomi lived with only Naomi's 2 sons."
```

**Step 5: Fix Clauses**
- Apposition "Naomi's husband" → relative clause
- "and" → "So" (consequence)
- Add "later" (temporal)
```
text = "Elimelech [who was Naomi's husband] died later. So Naomi lived with only Naomi's 2 sons."
```

---

## Quick Reference

| Pattern | ❌ Wrong | ✅ Right |
|---------|----------|----------|
| Pronouns | "he went" | "John went" |
| Numbers | "two sons" | "2 sons" |
| Apposition | "X, Y's husband" | "X [who was Y's husband]" |
| Nationality | "X the Moabite" | "X [who was from Moab]" |
| Existence | "had no food" | "there was no food" |
| Patient clause | "knew [that X]" | "knew [X]" |
| L2 words | "worship" | "serve/worship" |

---

## Decision Trees

### Word too complex?
```
Level 0-1 (blue/cream)? → Use directly
Level 2 (magenta)? → Pair: simple/complex
Level 3 (green)? → Alternate: (complex)...(simple)...
Level 4 (brown)? → Proper noun, use directly
```

### Apposition?
```
"X, Y's Z, verb" → "X [who was Y's Z] verb"
```

---

## APIs

| Tool | URL |
|------|-----|
| Check | `editor.tabitha.bible/check?text={urlencoded}` |
| Sources | `sources.tabitha.bible/Bible/{Book}/{ch}/{vs}` (JSON) |
| Ontology | `ontology.tabitha.bible/?q={word}` |

---

## Files

- `./checklist.md` — Full rules (reference)
- `./learnings.md` — Patterns from practice
- `./output/` — Your step-by-step work logs

