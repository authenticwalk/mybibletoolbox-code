# TBTA Phase 1 (He1) — V2: Rules-First

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

## Step 6: Checklist Pass (read `./checklist.md`)
Quotes: {ok or changes}
Implicit: {ok or changes}
Passives: {ok or changes}
Commands: {ok or changes}
Causality: {ok or changes}
Connectors: {ok or changes}
(other...): {ok or changes}
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

## The 5 Transforms + Checklist Pass

| Step | Goal | Rule |
|------|------|------|
| 1 | Copy NIV | Raw input |
| 2 | Fix pronouns | Resolve 3rd person, split sentences |
| 3 | Simplify vocabulary | L0-1 direct, L2 pair, L3 alternate |
| 4 | Group participants | Collapse repeated noun phrases |
| 5 | Fix clauses | Add brackets, relative clauses |
| **6** | **Checklist pass** | **Verify remaining rules (see below)** |

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
- ❌ Third person (he/she/they/it) — ALWAYS resolve to nouns, even after first mention
- ✅ First/second person: `I(Paul)`, `you(people)`, `we(Peter) _excl`
- ⚠️ "Natural pronouns" = 1st/2nd person keeps pronoun form after initial marking

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
- ⚠️ Hyphenated verbs: NEVER inflect — `sit-down` not `sat-down` (see learnings.md)

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
| Targets | `targets.tabitha.bible/English/{Book}/{ch}/{vs}` (sanity-check output) |
| Ontology | `ontology.tabitha.bible/?q={word}` |

---

## Success Criteria

A verse is **NOT DONE** until:

- [ ] ⚠️ **Linter passes** — `check` returns no blocking errors
- [ ] L2+ words: pairings or alternates
- [ ] Pronouns: resolved
- [ ] Patient clauses: no leading "that"
- [ ] Compared with `sources.tabitha.bible` reference
- [ ] ⚠️ **Learnings updated** — new patterns added to `./learnings.md`

---

## Files

- `./checklist.md` — Full rules (344 lines)
- `./notation.md` — Bracket syntax
- `./learnings.md` — Patterns from practice
- `./output/` — Your step-by-step work logs

