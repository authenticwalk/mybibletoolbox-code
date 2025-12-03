# TBTA Reverse Engineering: Three-Agent Comparison

**Task**: Reverse engineer TBTA's Verse column transformation rules (NIV → CNL)  
**Agents**: Claude Opus 4.5, Gemini 3 Pro Preview, GPT-5.1  
**Date**: 2024-12-02

---

## 1. Ranking: Best to Worst

### 🥇 1st Place: Claude Opus 4.5

**Score: 95/100**

**Pros**:
- ✅ **Empirical methodology**: Downloaded all 16 CSV files (6,963 verses), wrote Python analysis scripts
- ✅ **Quantitative evidence**: Provided exact counts (e.g., "915 supporting, 6 contradicting")
- ✅ **Discovered He1/He2 dichotomy**: Identified OT (natural) vs NT (strict) format differences with statistics
- ✅ **Reliability classification**: Correctly identified which rules are actually applied (>95%) vs aspirational
- ✅ **Critical insight on passives**: Found passive→active is NOT applied (0% in corpus)
- ✅ **Critical insight on modals**: Only "can"→"is able" is applied; "must/should" kept as-is
- ✅ **Bracket analysis**: Counted actual bracket openers (`[that`: 4,537, `[who`: 2,562)
- ✅ **Actionable SKILL.md**: 7-step process with validation checklist

**Cons**:
- ❌ Could have provided more worked examples in SKILL.md
- ❌ Deep analysis script could have examined more edge cases

---

### 🥈 2nd Place: PR Branch (claude/reverse-engineer-verse-column)

**Score: 88/100**

**Pros**:
- ✅ **12 well-structured rules** with verse references
- ✅ **Good He1/He2 comparison** table
- ✅ **Bracket type summary** table
- ✅ **Worked example** for Ruth 1:1 transformation
- ✅ **Comprehensive coverage** of all major patterns
- ✅ **Multiple supporting analysis files** (discourse markers, bracketing, vocabulary)

**Cons**:
- ❌ **Less rigorous quantification** than Opus 4.5 analysis
- ❌ **Claims passive→active is applied** (contradicts corpus evidence)
- ❌ **Claims modal decomposition applies to "must"** (contradicts corpus evidence)
- ❌ **Missing reliability classification** - treats all rules as equally reliable

---

### 🥉 3rd Place: GPT-5.1 (No-CSV Variant)

**Score: 75/100**

**Pros**:
- ✅ **Honest about methodology**: Explicitly states "hypotheses to be verified"
- ✅ **Good He1/He2 style analysis** with nuanced continuum view
- ✅ **Mental validation scenarios** for edge cases
- ✅ **Identified risks**: Over-application of segmentation in poetic material
- ✅ **Genre-specific patterns**: Genealogies, beatitudes, parables

**Cons**:
- ❌ **No empirical data**: Relies entirely on "internal knowledge" and existing examples
- ❌ **No quantification**: Cannot distinguish reliable from aspirational rules
- ❌ **Speculative claims**: Some rules based on what "would" happen, not what does
- ❌ **Modal decomposition claim wrong**: Says "must"→"has to" is applied (it's not)

---

### 4th Place: Gemini 3 Pro Preview

**Score: 65/100**

**Pros**:
- ✅ **Concise format**: Compressed rules into readable format
- ✅ **Good source strategy** section
- ✅ **Terminology index** helpful

**Cons**:
- ❌ **Minimal evidence**: Only 2-3 verse references per rule
- ❌ **No He1/He2 analysis**: Missed this critical distinction
- ❌ **Wrong on passives**: Claims "Passives (convert to active where possible)"
- ❌ **Wrong on modals**: Claims "must X" → "has to [X]"
- ❌ **No reliability classification**: All rules presented as equally valid
- ❌ **Conflict markers in file**: Output contains git merge conflict markers (incomplete work)

---

## 2. Key Disagreements & Validation

### Disagreement 1: Passive Voice Conversion

| Agent | Claim | 
|-------|-------|
| Claude Opus 4.5 | ❌ NOT converted (0% in corpus) |
| PR Branch | ✅ Convert to active where possible |
| GPT-5.1 | (Not explicitly addressed) |
| Gemini | ✅ Convert to active where possible |

**VALIDATION**: Claude Opus 4.5 is **CORRECT**.

Evidence from `deep_analysis.py`:
```
Total passive 'X by Y' constructions: 76 (all remain passive)
Examples:
- "was controlled by an unclean spirit" ✓ (kept)
- "was carried by 4 men" ✓ (kept)
- "was mixed by those soldiers" ✓ (kept)
```

**Verdict**: Passive→active is an aspirational rule from TBTA documentation, but NOT actually applied in the corpus.

---

### Disagreement 2: Modal Decomposition

| Agent | Claim |
|-------|-------|
| Claude Opus 4.5 | Only "can"→"is able"; "must/should" kept |
| PR Branch | "must X" → "has to [X]" |
| GPT-5.1 | "must X" → "has to [X]" |
| Gemini | "must X" → "has to [X]" |

**VALIDATION**: Claude Opus 4.5 is **CORRECT**.

Evidence from `deep_analysis.py`:
```
'is/was able to' usage: 133
Bare modal (must/should/can) usage: 787

Words following 'must':
  must not: 57
  must be: 21
  must do: 15
```

**Verdict**: "must" indicates obligation and is kept as-is. Only "can" (ability) is decomposed to "is able [to...]".

---

### Disagreement 3: He1 vs He2 Format Distinction

| Agent | Recognition |
|-------|-------------|
| Claude Opus 4.5 | ✅ Full quantitative analysis |
| PR Branch | ✅ Recognized with table |
| GPT-5.1 | ✅ Recognized with style continuum |
| Gemini | ❌ Not mentioned |

**VALIDATION**: He1/He2 distinction is **REAL and SIGNIFICANT**.

Evidence:
```
Underscore markers:
  He1 (OT): 0.6% of verses
  He2 (NT): 64.3% of verses

L2 pairings (word/word):
  He1: 9.2% of verses
  He2: 47.6% of verses
```

---

### Disagreement 4: Demonym Conversion Rate

| Agent | Claim |
|-------|-------|
| Claude Opus 4.5 | 55% applied (157 supporting, 126 contradicting) |
| PR Branch | Applied selectively |
| GPT-5.1 | Applied for narrative identity |
| Gemini | "Moabite" → "[who was from Moab]" (implied always) |

**VALIDATION**: Claude Opus 4.5 is **CORRECT**.

Demonym conversion is selective - proper nouns like "Jew", "Greek" often remain as-is.

---

### Disagreement 5: Number Formatting

| Agent | Claim |
|-------|-------|
| Claude Opus 4.5 | ~50% applied, large numbers as digits |
| PR Branch | Not addressed |
| GPT-5.1 | Not addressed |
| Gemini | Not addressed |

**VALIDATION**: Claude Opus 4.5 provides unique insight.

Evidence:
```
Digit usage: 2 (288), 3 (153), 7 (134), 1 (113), 12 (89)
Word numbers retained: one (338), two (128), three (83)
```

Pattern: Large numbers as digits, small numbers (1-12) may be words.

---

## 3. Summary: What Each Agent Got Right/Wrong

### Claude Opus 4.5
- ✅ Passive not converted
- ✅ Only "can" decomposed
- ✅ He1/He2 distinction quantified
- ✅ Demonym 55% selective
- ✅ Reliability classification

### PR Branch
- ✅ Good rule structure
- ✅ He1/He2 recognized
- ❌ Passive conversion claimed
- ❌ Modal decomposition for "must" claimed

### GPT-5.1
- ✅ Honest about speculative nature
- ✅ Good style analysis
- ❌ Modal decomposition for "must" claimed
- ❌ No quantitative validation

### Gemini
- ✅ Concise format
- ❌ Passive conversion claimed
- ❌ Modal decomposition for "must" claimed
- ❌ No He1/He2 analysis
- ❌ Incomplete (merge conflicts)

---

## 4. Recommendations

1. **Use Claude Opus 4.5's RULES.md** as the authoritative reference
2. **Merge the reliability classification** into the official policy
3. **Remove aspirational rules** (passive→active) or mark as "not applied"
4. **Clarify modal decomposition**: Only "can"→"is able", not "must"→"has to"
5. **Add He1/He2 format selector** to SKILL.md for book-appropriate output

---

## 5. Files to Review

| Agent | Key Files |
|-------|-----------|
| Claude Opus 4.5 | `RULES.md`, `SKILL.md`, `analyze_rules.py`, `deep_analysis.py` |
| PR Branch | `RULES.md`, `SKILL.md`, `TEST-RESULTS.md` |
| GPT-5.1 | `rules-evidence.md`, `style-and-edge-cases.md` |
| Gemini | `RULES.md` (has merge conflicts), `REPORT.md` |

