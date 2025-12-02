# TBTA Phase 1 (He1) — V3: Progressive

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
# {BOOK} {ch}:{vs} — He1 Encoding (V3)

## Step 1: Download NIV
text = "..."

## Step 2: Fix Pronouns
Rules used: (from rules/pronouns.md)
Changes: {list each change}
text = "..."

## Step 3: Simplify Vocabulary  
Rules used: (from rules/vocabulary.md)
Changes: {list each change with reason}
text = "..."

## Step 4: Group Participants
Changes: {list or "none needed"}
text = "..."

## Step 5: Fix Clauses
Rules used: (from rules/clauses.md)
Changes: {list each change}
text = "..."

## Step 6: Checklist Pass
Rules used: (from checklist.md §8-10, §13, §15, §17-18, §24, §32)
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
Errors: {list or "None"}

## Comparison
Reference: {from sources.tabitha.bible}
Differences: {list or "Matches"}

## Learnings
{any new patterns to add to learnings.md}
```

---

## The 5 Transforms + Checklist Pass

1. **Copy NIV** — raw input
2. **Fix pronouns** — resolve he/she/they to nouns, split sentences → [rules/pronouns.md](./rules/pronouns.md)
3. **Simplify vocabulary** — ontology-friendly words, pairings for L2 → [rules/vocabulary.md](./rules/vocabulary.md)
4. **Group participants** — collapse repeated noun phrases
5. **Fix clauses** — add brackets, relative clauses → [rules/clauses.md](./rules/clauses.md)
6. **Checklist pass** — verify rules not covered by transforms 2-5:

| Check | Rule | Reference |
|-------|------|-----------|
| Quotes | Speaker + verb? First sentence bracketed? | [→ quotes.md](./rules/quotes.md) |
| Implicit | `<<regular>>` or `<necessary>`? | [→ implicit.md](./rules/implicit.md) |
| Passives | Agent with "by"? | [→ special.md](./rules/special.md) |
| Commands | `(imp)` or natural English? | [→ special.md](./rules/special.md) |
| Causality | "to" → "in order to"? | [→ special.md](./rules/special.md) |
| Tense | Perfect only if "recently/previously" works? | checklist.md §18 |
| Connectors | And/But/Then/So flow? | checklist.md §32 |
| Forbidden | No "can", "even", "any", "own"? | checklist.md §17, §24 |

---

## Quick Reference (80% of cases)

| Rule | Wrong | Right |
|------|-------|-------|
| No 3rd person pronouns | "he went" | "John went" |
| Numbers as digits | "two sons" | "2 sons" |
| No "that" in patient clauses | "knew [that X]" | "knew [X]" |
| One verb per clause | compound verbs | split sentences |
| L2 words need pairing | "worship" | "serve/worship" |

---

## Rules by Category

| Category | Key Rules | Details |
|----------|-----------|---------|
| Pronouns | Resolve 3rd person, mark 1st/2nd | [→ pronouns.md](./rules/pronouns.md) |
| Words | L0-1 direct, L2 pair, L3 alternate | [→ vocabulary.md](./rules/vocabulary.md) |
| Clauses | Brackets, relativizers, max 4 nesting | [→ clauses.md](./rules/clauses.md) |
| Determiners | a/that/this/the/∅ by context | [→ determiners.md](./rules/determiners.md) |
| Quotes | Bracket first sentence only | [→ quotes.md](./rules/quotes.md) |
| Implicit | `<<regular>>`, `<necessary>` | [→ implicit.md](./rules/implicit.md) |
| Special | Passives, commands, causality | [→ special.md](./rules/special.md) |

---

## Common Patterns

| Pattern | Transform |
|---------|-----------|
| Apposition: "X, Y's husband" | "X [who was Y's husband]" |
| Nationality: "X the Moabite" | "X [who was from Moab]" |
| Existence: "had no food" | "there was no food" |
| Idiom: "find favor" | "be kind to" |
| Purpose: "went to see" | "went [in order to see]" |

[Full pattern list →](./learnings.md)

[Worked examples →](./examples.md)

---

## APIs

| Tool | URL |
|------|-----|
| Check | `editor.tabitha.bible/check?text={urlencoded}` |
| Sources | `sources.tabitha.bible/Bible/{Book}/{ch}/{vs}` |
| Ontology | `ontology.tabitha.bible/?q={word}` |

---

## File Structure

```
policies/
├── SKILL-v3-progressive.md  ← You are here
├── TODO.md                  ← Verses to complete
├── output/                  ← Your step-by-step work logs
├── examples.md              ← Worked examples
├── learnings.md             ← Discovered patterns
├── rules/
│   ├── pronouns.md
│   ├── vocabulary.md
│   ├── clauses.md
│   ├── determiners.md
│   ├── quotes.md
│   ├── implicit.md
│   └── special.md
├── checklist.md             ← Original (reference only)
└── notation.md              ← Syntax reference
```
