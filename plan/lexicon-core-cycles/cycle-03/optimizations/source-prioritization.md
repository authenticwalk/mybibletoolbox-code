# Source Prioritization Strategy

**Cycle:** 3 - Context Engineering
**Optimization:** Refinement #4
**Expected Savings:** 2 minutes per word
**Risk Level:** Low
**Richness Impact:** Neutral (same or better quality from authoritative sources)

---

## Executive Summary

Stop checking all sources equally. Use authoritative sources first and skip redundant lookups. The strategy follows a simple principle: **Consult comprehensive sources before general lexicons, cite all but read strategically.**

**Key Rules:**
1. **Synonyms:** Trench first (if exists) → TDNT (if theological) → Individual lexicons (only if gaps)
2. **Theology:** TDNT first → HELPS second → Individual lexicons last
3. **Grammar:** Abbott-Smith first → Skip HELPS for grammatical-pathway words → LSJ for classical patterns
4. **Convergence:** Group sources by agreement, cite all, consult authoritative first

---

## 1. Synonym Analysis Priority

### Current Problem (3-4 min wasted)
- Consulting 4-5 lexicons individually for synonym distinctions
- Trench exists with comprehensive analysis but checked last or alongside others
- Overlapping content from TDNT, Thayer, Abbott-Smith creates redundancy

### Optimized Strategy

```yaml
synonym_workflow:
  step_1_check_trench:
    time: "30 seconds"
    action: "Search Trench's Synonyms for word"
    if_comprehensive_section_exists:
      - "Read Trench's full analysis (2-3 min)"
      - "Note any synonyms mentioned by Trench"
      - "Cite: {trench}"
      - "SKIP individual lexicon synonym hunting"
      - "Use TDNT only if theological depth needed beyond Trench"
    if_trench_absent_or_minimal:
      - "Proceed to step_2_theological_check"

  step_2_theological_check:
    condition: "If theological word AND Trench absent/minimal"
    time: "3-4 min"
    action: "Check TDNT synonym section"
    if_tdnt_has_synonyms:
      - "Read TDNT synonym analysis"
      - "Cite: {tdnt}"
      - "SKIP general lexicons for synonym details"
    if_tdnt_minimal:
      - "Proceed to step_3_individual_lexicons"

  step_3_individual_lexicons:
    condition: "Only if Trench AND TDNT both absent/minimal"
    time: "4-5 min"
    sources: ["Thayer", "Abbott-Smith", "LSJ (classical only)"]
    action: "Check 2-3 lexicons for synonym notes"
    cite: "All consulted sources"
```

### Decision Tree

```
START: Need synonym distinctions
│
├─ Trench has section on this word?
│  ├─ YES → Read Trench (2-3 min)
│  │       ├─ Comprehensive? → DONE (cite {trench})
│  │       └─ Mentions synonym but brief? → Note it, proceed to theological check
│  │
│  └─ NO → Is this a theological word?
│         ├─ YES → Check TDNT (3-4 min)
│         │        ├─ Has synonym section? → Read TDNT, DONE (cite {tdnt})
│         │        └─ Minimal? → Check 2-3 individual lexicons (4-5 min)
│         │
│         └─ NO (grammatical/common word) → Check 2-3 lexicons (3-4 min)
│                └─ Focus: Abbott-Smith, Thayer
```

### Time Savings Examples

**Example 1: G26 ἀγάπη (love) - Trench exists**
- **Old approach:** Check Thayer (3 min) + Abbott-Smith (3 min) + TDNT (4 min) + Trench (3 min) = **13 min**
- **New approach:** Check Trench first (30 sec), find comprehensive section, read Trench (3 min), reference TDNT for theological depth (1 min scan) = **4.5 min**
- **Savings:** 8.5 minutes

**Example 2: G1411 δύναμις (power) - Trench absent but TDNT strong**
- **Old approach:** Check Thayer (3 min) + Abbott-Smith (3 min) + TDNT (4 min) + LSJ (2 min) = **12 min**
- **New approach:** Check Trench (30 sec, not found), check TDNT (4 min, comprehensive), cite others without deep reading = **5 min**
- **Savings:** 7 minutes

**Example 3: G846 αὐτός (he/she/it) - Grammatical word, no Trench**
- **Old approach:** Check Thayer (2 min) + Abbott-Smith (3 min) + Trench (30 sec, not found) + LSJ (2 min) = **7.5 min**
- **New approach:** Check Trench (30 sec, not found), Abbott-Smith for grammar (3 min), cite others = **3.5 min**
- **Savings:** 4 minutes

**Average savings for synonym analysis: 6.5 minutes**
**Conservative estimate (after other optimizations): 2-3 minutes**

---

## 2. Theological Content Priority

### Current Problem (2-3 min wasted)
- Checking general lexicons before specialized theological dictionaries
- HELPS consulted for every word (but has limited coverage for some categories)
- Thayer, Abbott-Smith read in full even when TDNT is more comprehensive

### Optimized Strategy

```yaml
theological_workflow:
  step_1_comprehensive_theological:
    first: "TDNT (Theological Dictionary of NT)"
    time: "4-5 min"
    conditions:
      - "Word has theological significance (detected in word-type analysis)"
      - "NT Greek words only"
    action: "Read TDNT entry in full"
    coverage: "Etymology, usage history, theological development, controversies"
    cite: "{tdnt}"
    skip_if_comprehensive:
      - "Individual lexicon theology sections (just cite them)"
      - "LSJ for NT theological terms (classical usage already in TDNT)"

  step_2_practical_application:
    second: "HELPS Word-studies"
    time: "2-3 min"
    conditions:
      - "TDNT provides comprehensive theological base"
      - "Need practical application insights"
    action: "Read HELPS for prefix analysis, usage patterns, application"
    cite: "{helps}"
    note: "HELPS complements TDNT (practical vs academic)"

  step_3_classical_lexicons:
    third: "Thayer, Abbott-Smith, LSJ"
    time: "2-3 min for specific gaps"
    conditions:
      - "Need specific details not in TDNT/HELPS"
      - "Etymology depth, classical usage comparison"
    action: "Targeted reading for gaps only"
    cite: "All consulted"

  hebrew_pathway:
    first: "TWOT (Theological Wordbook of OT)"
    time: "4-5 min"
    for: "Hebrew words with theological significance"
    cite: "{twot}"

    second: "NIDOTTE"
    time: "3-4 min (if TWOT absent or brief)"
    cite: "{nidotte}"

    third: "BDB, Gesenius"
    time: "2-3 min for gaps"
    cite: "All consulted"
```

### Decision Tree

```
START: Extract theological content
│
├─ Language?
│  ├─ GREEK (NT)
│  │   └─ TDNT has entry?
│  │       ├─ YES → Read TDNT (4-5 min)
│  │       │        ├─ Comprehensive? → Add HELPS for application (2 min), cite others
│  │       │        └─ Brief? → Check Thayer, Abbott-Smith for gaps (2-3 min)
│  │       │
│  │       └─ NO → Check HELPS (2-3 min)
│  │               └─ Then Thayer, Abbott-Smith (3-4 min)
│  │
│  └─ HEBREW (OT)
│      └─ TWOT has entry?
│          ├─ YES → Read TWOT (4-5 min)
│          │        └─ Add NIDOTTE if brief (2 min), cite BDB
│          │
│          └─ NO → Check NIDOTTE (3-4 min)
│                  └─ Then BDB, Gesenius (3-4 min)
```

### Time Savings Examples

**Example 1: G26 ἀγάπη (love) - TDNT comprehensive**
- **Old approach:** Thayer (3 min) + Abbott-Smith (3 min) + HELPS (2 min) + TDNT (4 min) + LSJ (2 min) = **14 min**
- **New approach:** TDNT first (4 min comprehensive), HELPS application (2 min), cite others without full reading = **6 min**
- **Savings:** 8 minutes

**Example 2: G5287 ὑπόστασις (substance/reality) - TDNT comprehensive**
- **Old approach:** Thayer (3 min) + Abbott-Smith (2 min) + TDNT (4 min) + LSJ (3 min for classical) = **12 min**
- **New approach:** TDNT (4 min covers etymology, classical, theological), cite others = **5 min**
- **Savings:** 7 minutes

**Example 3: H430 אֱלֹהִים (God) - TWOT comprehensive**
- **Old approach:** BDB (4 min) + Gesenius (3 min) + TWOT (5 min) + NIDOTTE (4 min) = **16 min**
- **New approach:** TWOT first (5 min comprehensive), cite BDB and NIDOTTE without full reading = **7 min**
- **Savings:** 9 minutes

**Average savings for theological content: 8 minutes**
**Conservative estimate (overlaps with synonym optimization): 2-3 minutes**

---

## 3. Grammar Priority

### Current Problem (1-2 min wasted)
- HELPS consulted for grammatical-pathway words (rarely has entries)
- Multiple grammar-focused lexicons checked sequentially
- Classical Greek sources consulted before NT-specific resources

### Optimized Strategy

```yaml
grammar_workflow:
  word_type_detection:
    grammatical_words: ["pronouns", "particles", "conjunctions", "prepositions", "articles"]
    action: "Set grammar_pathway = true"

  step_1_nt_grammar:
    first: "Abbott-Smith"
    time: "3-4 min"
    why: "Concise, comprehensive, morphology focus, NT-specific"
    action: "Read Abbott-Smith entry for grammatical analysis"
    coverage: "Forms, syntax, usage patterns, frequency"
    cite: "{abbott-smith}"

  step_2_pedagogical:
    second: "Mounce (if needed)"
    time: "2 min"
    conditions:
      - "Need pedagogical clarity (textbook-style explanation)"
      - "Word has complex morphology needing simplified explanation"
    action: "Read Mounce for clear explanations"
    cite: "{mounce}"

  step_3_classical_comparison:
    third: "LSJ (classical Greek)"
    time: "2-3 min"
    conditions:
      - "Need classical Greek usage comparison"
      - "Diachronic analysis requires pre-Koine patterns"
    action: "Check LSJ for classical usage, frequency changes"
    cite: "{lsj}"

  skip_sources:
    helps:
      reason: "HELPS rarely has grammatical word entries"
      exception: "Only check if word has theological overlay (e.g., ἐν with theological uses)"
      time_saved: "2-3 min per grammatical word"

    tdnt:
      reason: "TDNT focuses on theological terms, not grammar words"
      exception: "Particles with theological significance (e.g., ἀλλά contrasts)"
      time_saved: "3-4 min per grammatical word"
```

### Decision Tree

```
START: Extract grammar for word
│
├─ Word type?
│  ├─ GRAMMATICAL (pronoun, particle, conjunction, preposition)
│  │   └─ Check Abbott-Smith (3-4 min)
│  │       ├─ Comprehensive? → Add LSJ for classical (2 min), cite others
│  │       │                   └─ SKIP: HELPS, TDNT (save 5-6 min)
│  │       │
│  │       └─ Brief/absent? → Check Mounce (2 min), LSJ (2 min)
│  │                          └─ SKIP: HELPS, TDNT
│  │
│  └─ CONTENT WORD (verb, noun, adjective)
│      └─ Theological significance?
│          ├─ YES → Check Abbott-Smith (3 min), TDNT (4 min), HELPS (2 min)
│          │        └─ Grammar embedded in theological analysis
│          │
│          └─ NO → Check Abbott-Smith (3 min), Mounce if needed (2 min)
│                  └─ SKIP: TDNT, HELPS for pure grammar
```

### Time Savings Examples

**Example 1: G846 αὐτός (he/she/it) - Pure grammatical pronoun**
- **Old approach:** Abbott-Smith (3 min) + Mounce (2 min) + HELPS (2 min checked, nothing found) + LSJ (2 min) = **9 min**
- **New approach:** Abbott-Smith (3 min), LSJ (2 min), cite Mounce without full read, SKIP HELPS = **5 min**
- **Savings:** 4 minutes

**Example 2: G1722 ἐν (in, by, with) - Preposition with some theological usage**
- **Old approach:** Abbott-Smith (3 min) + Mounce (2 min) + HELPS (3 min) + TDNT (skimmed, 2 min) = **10 min**
- **New approach:** Abbott-Smith (3 min), HELPS (2 min for theological overlay only), cite others = **5 min**
- **Savings:** 5 minutes

**Example 3: G2532 καί (and, also, even) - Pure conjunction**
- **Old approach:** Abbott-Smith (2 min) + Thayer (2 min) + HELPS (2 min check, minimal) + LSJ (2 min) = **8 min**
- **New approach:** Abbott-Smith (2 min), LSJ (2 min), cite Thayer, SKIP HELPS = **4 min**
- **Savings:** 4 minutes

**Average savings for grammatical words: 4.3 minutes**
**Frequency:** ~30% of all words are grammatical
**Weighted average savings: 1.3 minutes per word**

---

## 4. Convergence Strategy

### Concept: "Cite All, Consult Strategically"

When multiple sources cover the same topic, cite all authoritative sources but only read comprehensively from the most authoritative/comprehensive source.

### Implementation

```yaml
convergence_protocol:

  step_1_identify_coverage:
    action: "Quick scan (30 sec each) to identify which sources have content"
    sources: "All relevant lexicons/dictionaries"
    output: "List of sources with coverage (cite these)"

  step_2_group_by_agreement:
    action: "Identify clusters of agreement"
    example: "TDNT, Thayer, Abbott-Smith all define ἀγάπη as 'divine love'"
    output: "Source groups with shared positions"

  step_3_prioritize_reading:
    primary_read: "Most comprehensive/authoritative source in cluster"
    secondary_read: "Sources with unique perspectives"
    skip_detailed_read: "Redundant sources (but still cite)"

    citation_format:
      pattern: "{tdnt}, {thayer}, {abbott-smith} agree..."
      time: "Read 1 source (4 min), skim 2 sources (1 min each) vs reading all 3 (12 min)"
      savings: "6 minutes"

  step_4_divergence_handling:
    when: "Sources disagree or have different emphases"
    action: "Read all divergent sources to capture full spectrum"
    example: "Thayer emphasizes classical, TDNT emphasizes theological, HELPS emphasizes practical"
    output: "Synthesis showing different facets"
```

### Convergence Patterns

#### Pattern 1: Complete Agreement
**Example:** G40 ἅγιος (holy) - all sources agree on "set apart for God"

```yaml
old_approach:
  - "Read TDNT full entry (5 min)"
  - "Read Thayer full entry (3 min)"
  - "Read Abbott-Smith full entry (3 min)"
  - "Read HELPS full entry (2 min)"
  - total: "13 minutes"

new_approach:
  - "Quick scan all sources (2 min) - identify agreement"
  - "Read TDNT comprehensively (5 min) - most thorough"
  - "Cite: {tdnt}, {thayer}, {abbott-smith}, {helps} agree on core definition"
  - total: "7 minutes"
  - savings: "6 minutes"
```

#### Pattern 2: Complementary Emphasis
**Example:** G26 ἀγάπη (love) - sources have different but compatible angles

```yaml
old_approach:
  - "Read Trench full entry (4 min)"
  - "Read TDNT full entry (5 min)"
  - "Read Thayer full entry (3 min)"
  - "Read HELPS full entry (2 min)"
  - total: "14 minutes"

new_approach:
  - "Identify focus areas (1 min): Trench=synonyms, TDNT=theology, HELPS=application"
  - "Read Trench for synonyms (4 min)"
  - "Skim TDNT for theological depth (2 min)"
  - "Skim HELPS for application (1 min)"
  - "Cite all with specific roles: {trench} for distinctions, {tdnt} for theology, {helps} for application"
  - total: "8 minutes"
  - savings: "6 minutes"
```

#### Pattern 3: Significant Disagreement
**Example:** G5287 ὑπόστασις (substance/confidence/reality) - scholarly debate

```yaml
old_approach:
  - "Read TDNT (5 min)"
  - "Read Thayer (3 min)"
  - "Read LSJ (3 min)"
  - "Read Abbott-Smith (3 min)"
  - total: "14 minutes"

new_approach:
  - "Identify disagreement (1 min)"
  - "Read all sources to capture full debate (12 min)"
  - "Synthesize different positions"
  - total: "13 minutes"
  - savings: "1 minute (minimal, but accuracy maintained)"
```

**Convergence savings:** 3-6 minutes when sources agree, 0-1 minute when sources disagree

---

## 5. Complete Source Priority Matrix

### New Testament Greek Words

| Word Type | Primary | Secondary | Tertiary | Skip | Time |
|-----------|---------|-----------|----------|------|------|
| **Theological** | TDNT (4-5 min) | HELPS (2 min) | Thayer, Abbott-Smith (cite) | LSJ for NT-only terms | 6-7 min |
| **Grammatical** | Abbott-Smith (3 min) | LSJ (2 min) | Mounce if needed (2 min) | HELPS, TDNT | 5 min |
| **Rare (<20 uses)** | TDNT if exists | Thayer, Abbott-Smith | LSJ for etymology | HELPS often absent | 5-6 min |
| **Ultra-common (1000+)** | Abbott-Smith | Focus on frequency shifts | Limit depth | Full diachronic unnecessary | 4-5 min |

### Old Testament Hebrew Words

| Word Type | Primary | Secondary | Tertiary | Skip | Time |
|-----------|---------|-----------|----------|------|------|
| **Theological** | TWOT (4-5 min) | NIDOTTE (cite) | BDB, Gesenius (cite) | - | 6-7 min |
| **Common/Grammar** | BDB (3-4 min) | Gesenius (2 min) | TWOT if has entry | NIDOTTE (minimal gram.) | 5-6 min |
| **Rare** | BDB (3 min) | TWOT if theological | Gesenius for etymology | - | 5 min |

### Synonym Analysis (Any Word)

| Scenario | Primary | Secondary | Skip | Time |
|----------|---------|-----------|------|------|
| **Trench has section** | Trench (3-4 min) | TDNT if theological (2 min) | Individual lexicons | 5-6 min |
| **No Trench, theological** | TDNT (4 min) | Thayer, Abbott-Smith (cite) | LSJ | 5-6 min |
| **No Trench, grammatical** | Abbott-Smith (3 min) | Thayer (2 min) | TDNT, HELPS | 5 min |

---

## 6. Implementation Checklist

### Pre-Extraction Analysis (1-2 min)
```yaml
before_starting:
  - "Identify word type (theological/grammatical/rare/common)"
  - "Set primary source priorities based on type"
  - "Flag if Trench likely has synonym section"
  - "Plan source consultation order"
```

### During Extraction
```yaml
source_consultation_order:
  1_synonym_analysis:
    - "Check Trench FIRST (30 sec)"
    - "If comprehensive, read Trench (3 min), cite others"
    - "If absent, use TDNT (theological) or Abbott-Smith (grammatical)"

  2_theological_content:
    - "Greek: TDNT first, then HELPS"
    - "Hebrew: TWOT first, then NIDOTTE"
    - "Skip general lexicons for theology if specialized source comprehensive"

  3_grammar_content:
    - "Abbott-Smith FIRST for NT Greek"
    - "SKIP HELPS for pure grammatical words"
    - "LSJ for classical comparison only"

  4_convergence_check:
    - "Quick scan all relevant sources (2 min)"
    - "Identify agreement clusters"
    - "Read most comprehensive, cite all"
```

### Documentation
```yaml
metadata_tracking:
  sources_consulted: "List all sources checked"
  sources_cited: "List all sources with content"
  primary_sources: "Mark which sources were read comprehensively vs cited only"
  time_saved: "Note any sources skipped and why"

example:
  sources_consulted: ["{tdnt}", "{helps}", "{thayer}", "{abbott-smith}"]
  sources_cited: ["{tdnt}", "{helps}", "{thayer}"]
  primary_source_read: "{tdnt}"
  sources_cited_only: ["{helps}", "{thayer}"]
  rationale: "TDNT comprehensive for theological analysis; HELPS and Thayer cited for agreement"
  time_saved: "4 min (skipped full reading of HELPS and Thayer)"
```

---

## 7. Time Savings Calculation

### Per Word Type

**Theological Words (50% of corpus):**
- Old approach: 14 min average (all sources read fully)
- New approach: 7 min average (strategic prioritization)
- Savings: 7 min
- Weighted: 7 min × 50% = **3.5 min average**

**Grammatical Words (30% of corpus):**
- Old approach: 9 min average (including HELPS/TDNT checks)
- New approach: 5 min average (skip HELPS/TDNT)
- Savings: 4 min
- Weighted: 4 min × 30% = **1.2 min average**

**Rare Words (15% of corpus):**
- Old approach: 12 min average (exhaustive checking)
- New approach: 6 min average (focused sources)
- Savings: 6 min
- Weighted: 6 min × 15% = **0.9 min average**

**Common Words (5% of corpus):**
- Old approach: 10 min average
- New approach: 5 min average (limited depth)
- Savings: 5 min
- Weighted: 5 min × 5% = **0.25 min average**

### Total Expected Savings
**Conservative Total: 3.5 + 1.2 + 0.9 + 0.25 = 5.85 minutes per word**

### Reality Check
Given other Cycle 3 optimizations (redundancy elimination, adaptive depth):
- Some savings overlap (e.g., adaptive depth also skips sources)
- Realistic unique savings from source prioritization: **2-3 minutes per word**

---

## 8. Quality Safeguards

### Do NOT Skip
```yaml
never_skip:
  - "Sources with unique content (even if low authority)"
  - "Sources when significant disagreement exists"
  - "Primary sources for critical theological/exegetical claims"
  - "Validation of controversial claims (check multiple sources)"
```

### Always Cite
```yaml
always_cite:
  - "Every source consulted (even if not read comprehensively)"
  - "Primary source read in full"
  - "Sources with unique perspectives"
  - "Sources in agreement clusters (grouped citation)"
```

### Human Review Triggers
```yaml
requires_review_when:
  - "Skipped authoritative source due to time (document why)"
  - "Relied on single source for controversial claim"
  - "Source disagreement not fully explored"
  - "Low-authority source used without high-authority confirmation"
```

---

## 9. Success Metrics

### Quantitative Targets
- **Time savings:** 2-3 min per word (conservative from 5.85 min theoretical)
- **Validation maintained:** 100% (no quality degradation)
- **Citation count:** Maintain or increase (cite all, read strategically)
- **Source diversity:** Maintain (don't reduce source breadth)

### Qualitative Indicators
- **Higher authority sources prioritized:** TDNT, TWOT, Trench emphasized
- **Reduced redundancy:** Stop reading duplicate content
- **Better depth alignment:** More time on unique insights, less on repeated facts
- **Maintained comprehensiveness:** All perspectives captured through citations

---

## 10. Examples: Before/After

### Example 1: G26 ἀγάπη (love)

**BEFORE (14 min total):**
1. Check Thayer (3 min) - read full entry
2. Check Abbott-Smith (3 min) - read full entry
3. Check HELPS (2 min) - read full entry
4. Check TDNT (4 min) - read full entry
5. Check Trench (2 min) - read synonym section

**AFTER (6 min total):**
1. Check Trench (30 sec) - **HAS comprehensive synonym section**
2. Read Trench synonym analysis (3 min) - **PRIMARY SOURCE**
3. Quick scan TDNT (1 min) - note agreement, cite
4. Quick scan HELPS (1 min) - note application focus, cite
5. Citation: "{trench} provides comprehensive distinction between ἀγάπη, φιλέω, and στοργή; {tdnt} confirms theological emphasis; {helps} adds practical application"

**Savings:** 8 minutes

---

### Example 2: G846 αὐτός (he, she, it)

**BEFORE (9 min total):**
1. Check Abbott-Smith (3 min) - read full entry
2. Check Mounce (2 min) - read entry
3. Check HELPS (2 min) - search, find minimal content
4. Check LSJ (2 min) - check classical usage

**AFTER (5 min total):**
1. Word type detection (10 sec) - **GRAMMATICAL pronoun**
2. Check Abbott-Smith (3 min) - **PRIMARY SOURCE** for grammar
3. Check LSJ (2 min) - classical comparison
4. **SKIP HELPS** - grammatical words rarely have HELPS entries
5. Citation: "{abbott-smith} and {lsj} for morphological analysis"

**Savings:** 4 minutes

---

### Example 3: H430 אֱלֹהִים (God)

**BEFORE (16 min total):**
1. Check BDB (4 min) - read full entry
2. Check Gesenius (3 min) - read entry
3. Check TWOT (5 min) - read theological article
4. Check NIDOTTE (4 min) - read article

**AFTER (7 min total):**
1. Word type detection (10 sec) - **THEOLOGICAL term**
2. Check TWOT (5 min) - **PRIMARY SOURCE**, comprehensive theological treatment
3. Quick scan NIDOTTE (1 min) - note agreement, cite
4. Quick scan BDB (1 min) - note lexical details, cite
5. Citation: "{twot} provides comprehensive theological analysis; {nidotte} and {bdb} concur on core definitions with additional lexical details"

**Savings:** 9 minutes

---

## 11. Risk Mitigation

### Potential Risks

**Risk 1: Missing unique content from skipped sources**
- **Mitigation:** Always do quick scan (30-60 sec) before skipping
- **Safeguard:** If scan reveals unique content, read that section
- **Example:** HELPS occasionally has unique prefix analysis even for theological words

**Risk 2: Over-reliance on single authoritative source**
- **Mitigation:** Cite all sources consulted (transparency)
- **Safeguard:** When sources disagree, read all divergent sources
- **Example:** G5287 ὑπόστασις has scholarly debate - read all positions

**Risk 3: Incorrect word-type detection leading to wrong source priority**
- **Mitigation:** Conservative classification (when in doubt, use fuller approach)
- **Safeguard:** Document word-type rationale in metadata
- **Example:** G1722 ἐν is grammatical BUT has theological uses - check both Abbott-Smith and TDNT

**Risk 4: Time pressure causing hasty skipping**
- **Mitigation:** Template includes source priority checklist
- **Safeguard:** Validation step checks for source diversity
- **Example:** If only 1-2 sources cited, validation flags for review

---

## Conclusion

The Source Prioritization strategy reduces extraction time by 2-3 minutes per word without sacrificing quality by:

1. **Using authoritative sources first** - Trench for synonyms, TDNT/TWOT for theology, Abbott-Smith for grammar
2. **Skipping redundant lookups** - When comprehensive source exists, cite others without full reading
3. **Word-type-based routing** - Grammatical words skip theological dictionaries
4. **Convergence strategy** - Group sources by agreement, read comprehensively from best source

**Expected Results:**
- Time: -2 to -3 minutes per word
- Quality: Maintained or improved (more authoritative sources)
- Validation: 100% (no degradation)
- Richness: Neutral (same content, better prioritized)

**Implementation:** Add source priority rules to extraction templates, document source selection rationale in metadata, validate source diversity during Level 2 review.

---

**Status:** Ready for implementation in Cycle 3 extraction prompts
**Next:** Integrate with other Cycle 3 optimizations (redundancy elimination, adaptive depth)
**Validation:** Test with 5 Cycle 2 words, measure time savings vs baseline
