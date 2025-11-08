# Experiments: Testing Lexicon Core Extraction

**Tool:** strongs-lexicon-core
**Phase:** Experimentation
**Created:** 2025-11-08

---

## Purpose

Test the extraction methodology on 5 diverse Strong's words to:
1. Validate extraction methods work correctly
2. Identify edge cases and failure modes
3. Refine convergence/divergence detection
4. Capture learnings for production phase

---

## Experiment Design

### Selection Criteria

**5 Word Types Chosen:**
1. **High-frequency** (5,000+ occurrences) - Maximum data available, test completeness
2. **Medium-frequency theological** (100-200 occurrences) - Test convergence detection, controversy handling
3. **Rare word** (<10 occurrences) - Test limited data handling, honest limitations
4. **Hebrew word** - Test Hebrew-specific extraction (BDB vs Thayer's)
5. **Word family** - Test convergence across related words, synonym distinctions

### Success Criteria

**Each experiment must produce:**
- ✅ Complete lexicon-core.yaml output (following schema)
- ✅ Learning document (what worked, what failed)
- ✅ Validation results (Level 1, 2, 3 scores)
- ✅ Edge cases discovered
- ✅ Refinements needed

---

## Experiment 1: High-Frequency Word

**Directory:** `exp1-high-freq-word/`

**Test Word:** G846 (αὐτός - he, she, it, himself)
- Occurrences: 5,597 (3rd person pronoun, highly frequent)
- Why chosen: Maximum data availability, comprehensive semantic range expected

**Research Questions:**
1. Can we extract complete semantic range for ultra-high-frequency word?
2. Do usage statistics match across sources?
3. How many semantic categories exist?
4. Are convergence patterns clear with abundant data?

**Expected Challenges:**
- Too much data (need to summarize effectively)
- Multiple distinct meanings (pronoun vs. intensive vs. reflexive)
- Potential for information overload

**Success Criteria:**
- [ ] 3+ semantic categories documented
- [ ] Usage statistics accurate (5,597 occurrences)
- [ ] Convergence patterns clear
- [ ] Etymology verified from multiple sources
- [ ] No fabricated examples

**Learning Goals:**
- How to handle ultra-frequent words?
- How to avoid duplication in base file check?
- What's the optimal semantic range depth?

---

## Experiment 2: Medium-Frequency Theological Word

**Directory:** `exp2-medium-freq/`

**Test Word:** G1411 (δύναμις - power, might, strength)
- Occurrences: 120
- Why chosen: Theologically significant, known controversy (dunamis ≠ dynamite)

**Research Questions:**
1. Can we detect and document the dunamis/dynamite controversy?
2. Do we find 7 usage categories (as documented in Thayer's)?
3. Is convergence clear across lexicons?
4. Can we identify diachronic shift (Classical → Koine)?

**Expected Challenges:**
- Controversy detection (dunamis/dynamite false etymology)
- Synonym distinctions (δύναμις vs. ἰσχύς vs. κράτος)
- Classical vs. NT usage differences

**Success Criteria:**
- [ ] Dunamis/dynamite error documented with scholarly refutation
- [ ] 7 semantic categories from Thayer's captured
- [ ] Synonym distinctions documented (5 related power words)
- [ ] Etymology verified (from δύναμαι "to be able")
- [ ] Diachronic analysis present

**Learning Goals:**
- How to detect controversies from web sources?
- How to document scholarly refutations?
- How to handle synonym analysis?

---

## Experiment 3: Rare Word

**Directory:** `exp3-rare-word/`

**Test Word:** TBD (select word with <10 NT occurrences)
- Occurrences: <10
- Why chosen: Test limited data handling, honest limitations

**Research Questions:**
1. How to handle words with minimal data?
2. What to do when semantic range is unclear?
3. How to avoid fabricating elaborate analysis for sparse data?
4. Should output explicitly note rarity?

**Expected Challenges:**
- Limited lexicon entries (basic definition only)
- Few usage examples
- Temptation to fabricate semantic range
- Unclear convergence patterns

**Success Criteria:**
- [ ] Explicitly notes rarity (e.g., "Appears only in ROM.16.14")
- [ ] Does NOT fabricate elaborate semantic range
- [ ] Extracts what's available (etymology, basic meaning)
- [ ] Marks confidence as LOW where appropriate
- [ ] Cross-references to related words (if available)

**Learning Goals:**
- How to be honest about limited data?
- What's minimum viable output?
- When to mark "insufficient data"?

---

## Experiment 4: Hebrew Word

**Directory:** `exp4-hebrew-word/`

**Test Word:** H430 (אֱלֹהִים - Elohim, God, gods)
- Occurrences: 2,606 (OT)
- Why chosen: Test Hebrew extraction (BDB instead of Thayer's), theologically central

**Research Questions:**
1. Does BDB extraction work correctly?
2. Are Hebrew-specific features handled (plural form for singular God)?
3. Can we document multiple usage categories (God, gods, judges, superlative)?
4. Do convergence patterns work for Hebrew?

**Expected Challenges:**
- Different lexicon structure (BDB vs. Thayer's)
- Plural form with singular meaning (grammatical number anomaly)
- Multiple distinct usages (true God, false gods, magistrates)
- Hebrew script handling

**Success Criteria:**
- [ ] BDB data extracted correctly
- [ ] Plural-singular usage documented
- [ ] Multiple usage categories identified (God, gods, judges, superlative)
- [ ] Etymology from base file used
- [ ] Theological significance noted

**Learning Goals:**
- How does Hebrew extraction differ from Greek?
- Are BDB categories structured differently?
- How to handle Hebrew morphology?

---

## Experiment 5: Word Family (Convergence Test)

**Directory:** `exp5-word-family/`

**Test Words:** Love word family
- G25 (ἀγαπάω - agapaō, to love - verb)
- G26 (ἀγάπη - agapē, love - noun)
- G5368 (φιλέω - phileō, to love - verb)

**Research Questions:**
1. Can we detect convergence patterns across related words?
2. Are synonym distinctions clear (agape vs. phileo)?
3. Do word families show consistent etymology?
4. How to document "family relationships"?

**Expected Challenges:**
- Distinguishing agape (divine love) from phileo (friendship love)
- Documenting nuances across 3 words
- Showing family relationships in schema

**Success Criteria:**
- [ ] Convergence patterns across word family documented
- [ ] Agape vs. phileo distinctions clear
- [ ] Etymology shows verb→noun relationship (G25→G26)
- [ ] Cross-references between family members
- [ ] Synonym analysis from Trench's (if available)

**Learning Goals:**
- How to document word families?
- Are convergence patterns stronger within families?
- How to show relationships in schema?

---

## Experiment Execution Order

1. **Experiment 1** (High-frequency) - Establish baseline methodology
2. **Experiment 2** (Medium-frequency) - Test controversy detection
3. **Experiment 4** (Hebrew) - Test language-specific extraction
4. **Experiment 3** (Rare) - Test edge case handling
5. **Experiment 5** (Word family) - Test relationship detection

**Rationale for Order:**
- Start with data-rich word (easier debugging)
- Test known controversy case second (dunamis)
- Hebrew third (different lexicon structure)
- Rare word fourth (known to be challenging)
- Word family last (builds on all prior learnings)

---

## Execution Process

### For Each Experiment

**Step 1: Setup**
- Create experiment subdirectory
- Write experiment-specific README
- Document research questions and success criteria

**Step 2: Execute Extraction**
- Run extraction methods (base file → BibleHub → StudyLight → BLB)
- Capture raw data from each source
- Apply convergence/divergence detection

**Step 3: Generate Output**
- Create lexicon-core.yaml following schema
- Ensure fair use compliance (convergence grouping)
- Add inline citations

**Step 4: Validate**
- Run Level 1 validation (CRITICAL - must pass 100%)
- Run Level 2 validation (HIGH - 80%+ pass)
- Run Level 3 validation (MEDIUM - 60%+ pass)
- Document validation scores

**Step 5: Capture Learnings**
- What worked well?
- What failed?
- What edge cases discovered?
- What refinements needed?
- Update LEARNINGS.md

---

## Learnings Capture

**Location:** `LEARNINGS.md`

**Template:**
```markdown
# Learnings from Lexicon Core Experiments

## Experiment 1: High-Frequency Word (G846)
**What Worked:**
- [List successes]

**What Failed:**
- [List failures]

**Edge Cases Discovered:**
- [List edge cases]

**Refinements Needed:**
- [List improvements]

## Experiment 2: Medium-Frequency (G1411)
[Same structure...]

## Overall Patterns
- [Cross-experiment insights]

## Schema Refinements
- [Changes needed to schema]

## Methodology Updates
- [Changes to extraction methods]
```

---

## Validation Criteria

### Level 1: CRITICAL (100% pass required)
- No fabricated data
- Inline citations present
- No percentages
- Base file read first
- Sources in ATTRIBUTION.md

### Level 2: HIGH PRIORITY (80%+ pass required)
- Etymology from multiple sources
- Semantic categories appropriate for frequency
- Usage statistics accurate
- Convergence documented
- Divergence noted when exists

### Level 3: MEDIUM PRIORITY (60%+ pass required)
- Cross-reference codes extracted
- Diachronic analysis when relevant
- Fair use compliance verified

---

## Next Steps

1. Execute Experiment 1 (high-frequency)
2. Capture detailed learnings
3. Refine methodology based on Exp 1
4. Execute remaining experiments sequentially
5. Aggregate learnings across all experiments
6. Update schema based on learnings
7. Refine extraction methods
8. Prepare for production phase

---

**See Also:**
- `../research/extraction-methods.md` - How to extract
- `../research/convergence-patterns.md` - How to detect convergence
- `../schema.yaml` - Output format
- `../validation/quality-checklist.md` - Validation criteria
