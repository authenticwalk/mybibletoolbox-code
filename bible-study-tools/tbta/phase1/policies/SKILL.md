# TBTA Phase 1 (He1) Skill

> **Mission**: Convert NIV verses into simplified English (He1) that TBTA can encode for any target language.

## Process

```
1. GET    ──► quote_verse {Book} {ch}:{vs} NIV
2. DRAFT  ──► 5 transforms, log to ./output/{BOOK}-{ch:03d}-{vs:03d}.md
3. CHECK  ──► editor.tabitha.bible/check
4. FIX    ──► rules/ folder, repeat until clean
5. COMPARE──► sources.tabitha.bible (only now!)
6. LEARN  ──► Update learnings.md
```

---

## Output Format

**Create file**: `./output/{BOOK}-{ch:03d}-{vs:03d}.md`

Show each step with the current text state:

```markdown
# {BOOK} {ch}:{vs} — He1 Encoding

## Step 1: Download NIV
text = "..."

## Step 2: Fix Pronouns
Changes: {list each pronoun → noun}
text = "..."

## Step 3: Simplify Vocabulary  
Changes: {list each word → replacement}
text = "..."

## Step 4: Group Participants
Changes: {list or "none needed"}
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

1. **Copy NIV** — raw input
2. **Fix pronouns** — resolve he/she/they to nouns, split sentences
3. **Simplify vocabulary** — ontology-friendly words, pairings for L2
4. **Group participants** — collapse repeated noun phrases
5. **Fix clauses** — add brackets, relative clauses

[See worked examples →](./examples.md)

---

## Rules Quick Reference

### Critical (memorize these)

| Rule | Wrong | Right |
|------|-------|-------|
| No 3rd person pronouns | "he went" | "John went" |
| Numbers as digits | "two sons" | "2 sons" |
| No "that" in patient clauses | "knew [that X]" | "knew [X]" |
| One verb per clause | compound verbs | split sentences |
| L2 words need pairing | "worship" | "serve/worship" |

### By Category

| Category | Key Rules | Details |
|----------|-----------|---------|
| Pronouns | Resolve 3rd person, mark 1st/2nd with referent | [→ pronouns.md](./rules/pronouns.md) |
| Words | Levels 0-1 direct, L2 pair, L3 alternate | [→ vocabulary.md](./rules/vocabulary.md) |
| Clauses | Brackets, relativizers, max 4 nesting | [→ clauses.md](./rules/clauses.md) |
| Determiners | a/that/this/the/∅ by context | [→ determiners.md](./rules/determiners.md) |
| Quotes | Bracket first sentence only | [→ quotes.md](./rules/quotes.md) |
| Implicit | `<<regular>>`, `<necessary>` | [→ implicit.md](./rules/implicit.md) |
| Special | Passives, commands, causality | [→ special.md](./rules/special.md) |

### Common Patterns (from practice)

| Pattern | Transform |
|---------|-----------|
| Apposition: "X, Y's husband" | "X [who was Y's husband]" |
| Nationality: "X the Moabite" | "X [who was from Moab]" |
| Existence: "had no food" | "there was no food" |
| Idiom: "find favor" | "be kind to" |
| Purpose: "went to see" | "went [in order to see]" |

[Full pattern list →](./learnings.md)

---

## APIs

| Tool | URL |
|------|-----|
| Check | `editor.tabitha.bible/check?text={urlencoded}` |
| Sources | `sources.tabitha.bible/Bible/{Book}/{ch}/{vs}` |
| Ontology | `ontology.tabitha.bible/?q={word}` |

---

## Success Criteria

- [ ] Check Tool clean
- [ ] L2+ words paired/alternated  
- [ ] Pronouns resolved
- [ ] No "that" in patient clauses
- [ ] Compared with reference

---

## File Structure

```
policies/
├── SKILL.md          ← You are here (overview)
├── TODO.md           ← Verses to complete
├── output/           ← Your step-by-step work logs
├── examples.md       ← Worked examples (any book)
├── learnings.md      ← Discovered patterns
├── rules/
│   ├── pronouns.md   ← Checklist §3
│   ├── vocabulary.md ← Checklist §1-2
│   ├── clauses.md    ← Checklist §4-7
│   ├── determiners.md← Checklist §3.1
│   ├── quotes.md     ← Checklist §10
│   ├── implicit.md   ← Checklist §9
│   └── special.md    ← Checklist §13-24
├── checklist.md      ← Original (reference only)
└── notation.md       ← Syntax reference
```

**Philosophy**: 
- SKILL.md = what you need 80% of the time
- rules/*.md = extracted from checklist.md, organized by topic
- learnings.md = patterns discovered from practice
- checklist.md = authoritative source (but rarely read directly)

