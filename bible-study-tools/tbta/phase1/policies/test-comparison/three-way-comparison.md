# Three-Way SKILL.md Comparison

## The Versions

| Version | Approach | Lines | Philosophy |
|---------|----------|-------|------------|
| **v1-current** | Examples-first | 212 | Detailed Ruth examples + quick reference table |
| **v2-integrated** | Rules-first | 148 | Checklist rules reorganized into SKILL, compact |
| **v3-progressive** | Index + subfiles | 98 | Minimal SKILL, rules extracted to `rules/*.md` |

---

## What Each Version Does

### v1-current (Examples-First)
```
SKILL.md (212 lines)
├── Quick Reference table (12 patterns)
├── Process flowchart
├── 5 Transforms with FULL Ruth 1:2 example (50+ lines)
├── Second example: Ruth 1:3
├── 3 Decision trees
├── APIs table
├── Success criteria
├── Common mistakes table
└── Training docs table
```

**Pros:**
- ✅ Concrete examples show exact transformations
- ✅ Decision trees for tricky cases
- ✅ Self-contained (don't need to read other files)

**Cons:**
- ❌ Ruth-specific examples
- ❌ Only 12 patterns in quick ref (checklist has 50+)
- ❌ Must read checklist.md for edge cases
- ❌ Learnings.md patterns not integrated

---

### v2-integrated (Rules-First)
```
SKILL.md (148 lines)
├── Process (compact)
├── 5 Transforms table (compact)
├── Rules by Category:
│   ├── Pronouns (checklist §3)
│   ├── Words (checklist §1-2) with pairings from learnings
│   ├── Clauses (checklist §4-7)
│   ├── Determiners (checklist §3.1)
│   ├── Implicit (checklist §9)
│   ├── Quotes (checklist §10)
│   ├── Special Constructions table
│   ├── Idiom Simplification (from learnings)
│   └── Verb Issues (from learnings)
├── APIs table
├── Success criteria
└── Files table
```

**Pros:**
- ✅ All major checklist rules in one place
- ✅ Learnings integrated (pairings, idioms, verbs)
- ✅ Book-agnostic (no Ruth examples)
- ✅ Compact (148 lines)

**Cons:**
- ❌ No worked examples (harder to learn)
- ❌ Still can't capture ALL 344 lines of checklist
- ❌ Some rules summarized, might miss nuance

---

### v3-progressive (Index + Subfiles)
```
SKILL.md (98 lines) ← Minimal overview
├── Process
├── 5 Transforms (one-liners)
├── Rules Quick Reference (critical 5)
├── Category table with links to rules/*.md
├── Common Patterns table
├── APIs
├── Success criteria
└── File structure diagram

rules/
├── pronouns.md   ← Full checklist §3
├── vocabulary.md ← Full checklist §1-2
├── clauses.md    ← Full checklist §4-7
├── determiners.md← Full checklist §3.1
├── quotes.md     ← Full checklist §10
├── implicit.md   ← Full checklist §9
└── special.md    ← Full checklist §13-24

examples.md       ← Worked examples (any book)
learnings.md      ← Discovered patterns
```

**Pros:**
- ✅ SKILL.md is short (98 lines)
- ✅ ALL checklist rules preserved in rules/*.md
- ✅ Progressive disclosure (overview → details)
- ✅ Book-agnostic
- ✅ Learnings separate, can grow indefinitely
- ✅ Examples separate, can add from any book

**Cons:**
- ❌ Requires creating 7+ new files
- ❌ Must click through to find rules
- ❌ More files to maintain
- ❌ rules/*.md files don't exist yet

---

## Coverage Analysis

### Does each version capture checklist.md?

| Checklist Section | v1 | v2 | v3 |
|-------------------|----|----|-----|
| §1-2 Words/Senses | Partial (table) | Yes (summary) | Full (vocabulary.md) |
| §3 Pronouns | Partial | Yes (summary) | Full (pronouns.md) |
| §3.1 Determiners | No | Yes (table) | Full (determiners.md) |
| §4-7 Clauses | Partial | Yes (summary) | Full (clauses.md) |
| §8 Causality | No | Partial | Full (special.md) |
| §9 Implicit | No | Yes | Full (implicit.md) |
| §10 Quotes | No | Yes | Full (quotes.md) |
| §11-24 Special | No | Partial | Full (special.md) |

### Does each version capture learnings.md?

| Learnings Category | v1 | v2 | v3 |
|--------------------|----|----|-----|
| Verb Structure | Yes (decision tree) | Yes | Link |
| Numbers | Yes (table) | Yes | Link |
| Ambiguous Words | Yes (table) | Yes | Link |
| Patient Clauses | Yes (table) | Yes | Link |
| L2 Pairings | No | Yes (list) | Link |
| Verb Issues | No | Yes (list) | Link |
| Idioms | Partial | Yes (list) | Link |
| Quote Structure | No | Yes | Link |

---

## Recommendation

**For immediate use: v2-integrated**
- Best balance of completeness and usability
- All major rules in one file
- Learnings integrated
- No new files needed

**For long-term: v3-progressive**
- Scales as checklist grows
- Preserves ALL rules
- Clear separation of concerns
- But requires creating rules/*.md files first

**v1-current is good for:**
- Training (examples help learning)
- But should add more book-agnostic examples

---

## Proposed Hybrid

Take best of each:

```
SKILL.md (≤150 lines)
├── Process (from v1: flowchart)
├── 5 Transforms (from v2: compact table)
├── Critical Rules (from v2: top 15 patterns)
├── Decision Trees (from v1: 3 trees)
├── APIs (from v1)
├── Success Criteria (from v1)
└── Links to:
    ├── examples.md (from v3: book-agnostic)
    ├── rules/*.md (from v3: full checklist)
    └── learnings.md (existing)
```

This gives:
- ✅ Self-contained for 80% of cases
- ✅ Full checklist preserved in subfiles
- ✅ Book-agnostic examples
- ✅ Progressive disclosure
- ✅ Learnings can grow

