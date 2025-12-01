# TBTA Phase 1 (He1) — V2: Rules-First

> **Mission**: Convert NIV verses into simplified English (He1) for TBTA.

## Process

For each verse in `./TODO.md`:

1. **Get NIV** → `quote_verse {Book} {ch}:{vs} NIV`
2. **Draft He1** → Apply 5 transforms, log each step to `./output/{BOOK}-{ch}-{vs}.md`
3. **Check** → `editor.tabitha.bible/check?text={urlencoded}`
4. **Compare** → `sources.tabitha.bible/Bible/{Book}/{ch}/{vs}` (only after drafting!)
5. **Learn** → Update `./learnings.md` if new pattern

---

## Output Format

**Create file**: `./output/{BOOK}-{ch:03d}-{vs:03d}.md`

```markdown
# {BOOK} {ch}:{vs} — He1 Encoding (V2)

## Step 1: Download NIV
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

## Final He1
text = "..."

## Check Results
Errors: {list or "None"}

## Comparison
Reference: {from sources.tabitha.bible}
Differences: {list or "Matches"}
```

---

## The 5 Transforms

| Step | Goal | Rule |
|------|------|------|
| 1 | Copy NIV | Raw input |
| 2 | Fix pronouns | Resolve 3rd person, split sentences |
| 3 | Simplify vocabulary | L0-1 direct, L2 pair, L3 alternate |
| 4 | Group participants | Collapse repeated noun phrases |
| 5 | Fix clauses | Add brackets, relative clauses |

---

## Rules by Category

### Pronouns (§3)
- ❌ Third person pronouns (he/she/they) — resolve to nouns
- ✅ First/second person: `I(Paul)`, `you(people)`, `we(Peter) _excl`
- ✅ After first occurrence: can use natural pronouns

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
- ✅ One verb per clause
- ✅ Subordinate clauses in brackets: `[who was in the house]`
- ✅ Max 4 levels of nesting
- ❌ "that" starting patient clauses: `knew [X...]` not `knew [that X...]`
- ✅ Relative clauses need relativizer: `who`, `whom`, `that`

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

| Pattern | ❌ Wrong | ✅ Right |
|---------|----------|----------|
| Existence | "did not have food" | "there was not enough food" |
| Numbers | "two sons" | "2 sons" |
| Ambiguity | "judges ruled" | "judges _noun ruled" |
| Apposition | "X, Y's husband" | "X [who was Y's husband]" |
| Nationality | "X the Moabite" | "X [who was from Moab]" |
| Ability | "can go" | "is able [to go]" |
| Purpose | "went to see" | "went [in order to see]" |
| Passive | "was hit" | "was hit by X" |

### Idioms (from learnings)
- "find favor in eyes" → `be kind to me`
- "The Lord be with you" → `I pray [that Yahweh will be with you]`
- "was left with" → `lived with only`
- "leftover grain" → `grain [that people left]`

---

## APIs

| Tool | URL |
|------|-----|
| Check | `editor.tabitha.bible/check?text={urlencoded}` |
| Sources | `sources.tabitha.bible/Bible/{Book}/{ch}/{vs}` (JSON) |
| Ontology | `ontology.tabitha.bible/?q={word}` |

---

## Success Criteria

- [ ] Check Tool: no blocking errors
- [ ] L2+ words: pairings or alternates
- [ ] Pronouns: resolved
- [ ] Patient clauses: no leading "that"
- [ ] Compared with reference

---

## Files

- `./checklist.md` — Full rules (344 lines)
- `./notation.md` — Bracket syntax
- `./learnings.md` — Patterns from practice
- `./output/` — Your step-by-step work logs

