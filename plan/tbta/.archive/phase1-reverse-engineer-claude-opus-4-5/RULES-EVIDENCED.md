# TBTA Verse Rules (Evidence-Based)

> **Goal**: NIV → Controlled Natural Language for universal translation
> **Model**: Claude Opus 4.5
> **Date**: 2024-12-02

## Source Strategy

**Base**: Copy NIV text, **except**:
- Pronouns (resolve to nouns)
- Compound sentences (segment)
- Idioms (decompose to meaning)
- Passives (convert to active where possible)
- Complex vocabulary (apply LDV substitution)

**Incorporate from**:
- **Hebrew**: "Yahweh" for יהוה (not NIV's "LORD")
- **Greek/Hebrew**: Implicit cultural context `(implicit-info)`
- **Scholarly sources**: Historical footnotes `(footnote)`
- **Semantic analysis**: Clause boundaries, participant tracking

---

### Coreference Resolution
**Evidence**: (Genesis 4:15, Genesis 9:5, Genesis 9:6, Genesis 11:8, Genesis 11:9; NOT Genesis 1:2, Matthew 22:17, Matthew 12:23)
**Pattern**: `that man|that woman|that person|that family|that group`
**Stats**: 915 supporting, 6 contradicting

### Clause Segmentation
**Evidence**: (Genesis 1:5, Genesis 1:10, Genesis 1:11, Genesis 1:12, Genesis 1:14)
**Pattern**: `Multiple sentences per verse`
**Stats**: 3014 supporting, 0 contradicting

### Explicit Relativization
**Evidence**: (Genesis 1:4, Genesis 1:6, Genesis 1:9, Genesis 1:10, Genesis 1:11; NOT Genesis 27:18, Genesis 27:32, Genesis 48:8)
**Pattern**: `[who/which/that...]`
**Stats**: 4073 supporting, 67 contradicting

### Deixis Marking
**Evidence**: (Genesis 1:22, Genesis 1:26, Genesis 1:28, Genesis 1:29, Genesis 1:30; NOT Acts 20:16, Acts 20:17, Acts 21:13)
**Pattern**: `I(Speaker), you(Addressee), we(Group)`
**Stats**: 3248 supporting, 3 contradicting

### LDV Substitution
**Evidence**: (Genesis 34:10, Genesis 50:17, Genesis 34:27, Joshua 2:1, Joshua 2:2)
**Pattern**: `simple/complex pairings`
**Stats**: 1466 supporting, 0 contradicting

### Subordinate Bracketing
**Evidence**: (Genesis 1:2, Genesis 2:2, Genesis 2:3, Genesis 2:7, Genesis 2:8; NOT 1 Samuel 30:12, Matthew 8:15, Mark 10:7)
**Pattern**: `[in order to...], [if...], [when...]`
**Stats**: 2362 supporting, 4 contradicting

### Quote Framing
**Evidence**: (Genesis 1:6, Genesis 3:1, Genesis 3:9, Genesis 3:13, Genesis 4:1)
**Pattern**: `X said, ["quote"]`
**Stats**: 1016 supporting, 0 contradicting

### Imperative Marking
**Evidence**: (Genesis 1:22, Genesis 1:28, Genesis 3:3, Genesis 4:8, Genesis 4:23)
**Pattern**: `You(Addressee) (imp) verb`
**Stats**: 1189 supporting, 0 contradicting

### Hyphenated Verbs
**Evidence**: (Genesis 1:17, Genesis 1:18, Genesis 2:7, Genesis 2:24, Genesis 3:17; NOT Matthew 7:25, Matthew 7:27, Matthew 28:4)
**Pattern**: `run-away, sit-down, stand-up`
**Stats**: 1076 supporting, 4 contradicting

### Modal Decomposition
**Evidence**: (Genesis 1:25, Genesis 2:20, Genesis 8:5, Genesis 13:15, Genesis 13:16; NOT Genesis 2:5, Genesis 2:15, Genesis 2:17)
**Pattern**: `can → is able, must → has to`
**Stats**: 133 supporting, 787 contradicting

### Demonym → Description
**Evidence**: (Genesis 19:10, Genesis 21:17, Genesis 22:11, Genesis 28:8, Genesis 34:19; NOT Genesis 10:16, Genesis 10:17, Genesis 10:18)
**Pattern**: `Moabite → [who was from Moab]`
**Stats**: 157 supporting, 126 contradicting

### Gap-filling (Implicit Info)
**Evidence**: (Genesis 5:1, Genesis 6:2, Genesis 34:2, Genesis 34:29, Genesis 34:30)
**Pattern**: `(implicit-info), (footnote), (implicit-subaction)`
**Stats**: 1526 supporting, 0 contradicting

### Yahweh Substitution
**Evidence**: (Genesis 8:21, Genesis 11:5, Genesis 11:6, Genesis 11:7, Genesis 11:8; NOT Daniel 8:13)
**Pattern**: `LORD → Yahweh`
**Stats**: 914 supporting, 1 contradicting

### Number Formatting
**Evidence**: (Genesis 1:28, Genesis 1:29, Genesis 2:9, Genesis 2:10, Genesis 2:25; NOT Genesis 1:16, Genesis 2:9, Genesis 2:16)
**Pattern**: `word numbers → digits (two → 2)`
**Stats**: 535 supporting, 507 contradicting

### Passive → Active Voice
**Evidence**: (N/A; NOT Genesis 14:13, Genesis 14:21, Genesis 17:24)
**Pattern**: `was done by X → X did`
**Stats**: 0 supporting, 76 contradicting

### Title Patterns
**Evidence**: (Genesis 45:1, Genesis 50:15, Joshua 1:1, Joshua 1:10, Joshua 2:1)
**Pattern**: `(title) Descriptive action statement`
**Stats**: 378 supporting, 0 contradicting

### Addressee Patterns
**Evidence**: (Genesis 1:28, Genesis 1:29, Genesis 2:17, Genesis 24:14, Genesis 24:43; NOT Matthew 8:26, Matthew 9:13, Matthew 9:38)
**Pattern**: `you(people) vs you(Disciples)`
**Stats**: 484 supporting, 229 contradicting

### Hyphenated Verb Base Form
**Evidence**: (Genesis 13:17, Genesis 19:1, Genesis 19:26, Genesis 21:16, Genesis 21:18; NOT Matthew 7:25, Matthew 7:27, Matthew 28:4)
**Pattern**: `go-up (not went-up)`
**Stats**: 216 supporting, 5 contradicting

### Underscore Markers
**Evidence**: (Nehemiah 9:3, Nehemiah 9:2, Nehemiah 10:33, Nehemiah 11:3, Nehemiah 11:19)
**Pattern**: `_implicit, _implicitActiveAgent, etc.`
**Stats**: 1416 supporting, 0 contradicting
