# TBTA Phase 1 (He1) Skill

> **Mission**: Convert NIV verses into simplified English (He1) that TBTA can encode for any target language.

## Quick Reference

| Pattern | ❌ Avoid | ✅ Use Instead |
|---------|----------|----------------|
| Existence | "people did not have food" | "there was not enough food" |
| Numbers | "two sons" | "2 sons" |
| Ambiguity | "judges ruled" | "judges _noun ruled" |
| Patient clause | "knew [that X...]" | "knew [X...]" |
| Complex L2 word | "worship" alone | "serve/worship" (pairing) |
| Nationality | "Ruth the Moabite" | "Ruth [who was from Moab]" |
| Name intro | "The man's name was X" | "a man named X" (first mention) |
| Idioms | "find favor in eyes" | "be kind to me" |
| Apposition | "X, Y's husband, died" | "X [who was Y's husband] died" |
| Passive state | "was left with X" | "lived with only X" |
| Consequence | "X died, and Y..." | "X died. So Y..." |
| Temporal | (implicit timing) | Add "later", "then", "after" |

See `./learnings.md` for the full list with examples.

---

## Process

```
┌─────────────────────────────────────────────────────────────┐
│  1. GET VERSE (quote_verse) ──► NIV text                    │
│                                                             │
│  2. DRAFT HE1 (no peeking!) ──► step-by-step transforms    │
│       └─► Log work in ./output/{book}-{ch:03d}-{vs:03d}.md  │
│                                                             │
│  3. CHECK ──► editor.tabitha.bible/check?text=...           │
│       └─► Fix errors using checklist.md, notation.md        │
│       └─► Repeat until clean (max 12 iterations)            │
│                                                             │
│  4. COMPARE (only now!) ──► sources.tabitha.bible           │
│       └─► Diff your He1 vs phase_1_encoding                 │
│                                                             │
│  5. LEARN ──► Record patterns in ./learnings.md             │
│       └─► Update SKILL.md only if instructions were unclear │
│                                                             │
│  6. NEXT VERSE ──► Mark done in ./TODO.md                   │
└─────────────────────────────────────────────────────────────┘
```

---

## The 5 Transforms (easiest → hardest)

Apply these in order. Show your text after each step.

### 1️⃣ Copy NIV
```text
The man's name was Elimelek, his wife's name was Naomi, and the names 
of his two sons were Mahlon and Kilion. They were Ephrathites from 
Bethlehem, Judah. And they went to Moab and lived there.
```

### 2️⃣ Fix pronouns & split sentences
Resolve "they/there" → explicit subjects. One clause per sentence.
```text
The man's name was Elimelek. His wife's name was Naomi. 
The names of his 2 sons were Mahlon and Kilion.
The man, his wife, and his 2 sons were Ephrathites from Bethlehem, Judah.
And the man, his wife, and his 2 sons went to the country of Moab 
and lived in the country of Moab.
```

### 3️⃣ Simplify vocabulary
Use ontology-friendly words. Replace culture-specific terms.
```text
That man's name was Elimelech. That man's wife's name was Naomi.
One son's name was Mahlon. The other son's name was Kilion.
Elimelech and Naomi were people in Ephrah's family in the town 
named Bethlehem in the region named Judah.
That family went to a country named Moab and lived in Moab.
```

### 4️⃣ Generalize & group participants
Collapse repeated participants. Add pairings for L2 words.
```text
That man's name was Elimelech. That man's wife's name was Naomi.
One son's name was Mahlon. The other son's name was Kilion.
Elimelech and Naomi were in Ephrah's family/clan.
That family was living in a town named Bethlehem in the region named Judah.
That family went to a country named Moab. And that family lived in Moab.
```

### 5️⃣ Fix subordinate clauses
Turn prepositional phrases into relative clauses where needed.
```text
That man's name was Elimelech. And that man's wife's name was Naomi.
One son's name was Mahlon. And the other son's name was Kilion.
Elimelech and Naomi were in Ephrah's family/clan.
That family was living in a town named Bethlehem [which was in Judah].
But that family went to a country named Moab. And that family lived in Moab.
```

✅ **This matches the reference `phase_1_encoding` from sources.tabitha.bible**

---

## Second Example: Ruth 1:3 (shorter verse)

### NIV
```text
Now Elimelek, Naomi's husband, died, and she was left with her two sons.
```

### Step-by-step
| Step | Text |
|------|------|
| 1️⃣ Copy | Now Elimelek, Naomi's husband, died, and she was left with her two sons. |
| 2️⃣ Pronouns | Elimelek, Naomi's husband, died. Naomi was left with Naomi's 2 sons. |
| 3️⃣ Vocabulary | Elimelech, Naomi's husband, died. Naomi lived with only Naomi's 2 sons. |
| 4️⃣ Group | (no grouping needed) |
| 5️⃣ Clauses | Elimelech [who was Naomi's husband] died later. So Naomi lived with only Naomi's 2 sons. |

**Key transforms applied:**
- Apposition → relative clause (`[who was Naomi's husband]`)
- "was left with" → "lived with only" (idiom simplification)
- "she" → "Naomi" (pronoun resolution)
- Added "later" (temporal marker)
- "and" → "So" (consequence conjunction)

---

## Decision Trees

### When is a word too complex?

```
Is it in the ontology at Level 0-1 (blue/cream)?
  ├─ YES → Use it directly
  └─ NO → Is it Level 2 (magenta)?
           ├─ YES → Pair it: simple/complex (e.g., "serve/worship")
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
  e.g., "Elimelek, Naomi's husband, died"
  ├─ YES → Convert to relative clause
  │         ✅ "Elimelech [who was Naomi's husband] died"
  └─ NO → Leave as-is
```

---

## APIs

| Tool | URL | Use |
|------|-----|-----|
| **Check** | `editor.tabitha.bible/check?text={urlencoded}` | Lint your He1 |
| **Sources** | `sources.tabitha.bible/Bible/{Book}/{ch}/{vs}` | Reference He1 (`Accept: application/json`) |
| **Targets** | `targets.tabitha.bible/English/{Book}/{ch}/{vs}` | Generated English for audiences |
| **Ontology** | `ontology.tabitha.bible/?q={word}&category=all&scope=stems` | Check word level/senses |

---

## Success Criteria

A verse is **done** when:

- [ ] Check Tool returns no blocking errors
- [ ] All L2+ words have pairings or alternates
- [ ] Pronouns are resolved (first occurrence per verse at minimum)
- [ ] No "that" starting patient clauses
- [ ] Clause count matches verb count
- [ ] You've compared with `phase_1_encoding` and logged any learnings

---

## Common Mistakes & Fixes

| Symptom | Cause | Fix |
|---------|-------|-----|
| "have cannot be used with different-participant patient clause" | Adverbial clause before "have" | Use existential "be" |
| "word not found" | Number written as word | Use numerals: 2, 3, 10 |
| "ambiguous word" | Noun/verb confusion | Add `_noun` or `_verb` |
| Checker loops on same error | Wrong sense of word | Check ontology, specify `-A`, `-B`, etc. |
| Generated English sounds wrong | Missing pairing | Add `simple/complex` for L2 words |

---

## Training Docs

| Doc | Purpose |
|-----|---------|
| `./checklist.md` | Full rules (344 lines) — the authoritative reference |
| `./notation.md` | Syntax for brackets, implicit markers, quotes, etc. |
| `./learnings.md` | Patterns discovered from errors — check before drafting |
| `./TODO.md` | Verses to complete |
| `./output/` | Your work logs per verse |
