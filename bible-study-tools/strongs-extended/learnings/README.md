# Strong's Extended: Consolidated Learnings

**Purpose**: Comprehensive synthesis of insights from Strong's enrichment experiments and research
**Source Documents**: 50+ planning files from lexicon-core and web-insights experiments
**Format**: Progressive disclosure - key insights with references to detailed documentation
**Last Updated**: 2025-11-14

---

## Executive Summary

Three experimental tracks validated systematic Strong's word enrichment:

1. **Lexicon-Core (Tool 1)**: Extract scholarly lexical data (etymology, semantics, cross-refs) - 12 experiments across Greek/Hebrew, frequency spectrum
2. **Web-Insights (Tool 3)**: Modern expert insights, controversies, practical application - 5 adversarial experiments
3. **TBTA Hints (Planned)**: Grammatical patterns from 900+ translations for AI translation assistance

**Critical Discovery**: Word type matters MORE than frequency for extraction value. Theologically significant rare words (5 occurrences) yield richer data than ultra-high-frequency grammatical terms (5,597 occurrences).

**Validation Success**: 100% pass rate on critical requirements across 17 experiments with zero fabrication.

---

## I. Methodology Learnings (What Works)

### A. Word Prioritization Strategy

**Discovery**: Traditional frequency-based prioritization is WRONG for lexical enrichment.

**Evidence from Experiments**:
- G5287 ὑπόστασις (5x, rare theological) → 35 unique data points, HIGH value
- G0846 αὐτός (5,597x, ultra-high grammatical) → 15 unique data points, MODERATE value
- **Ratio**: Rare theological term has 2.3x MORE data than ultra-high grammatical term

**Correct Priority Tiers**:
1. **HIGHEST ROI**: Medium-frequency theological terms (50-500x) - rich web data, manageable scope
2. **HIGH ROI**: Theologically significant rare words (1-10x) - requires restraint but rich scholarly treatment
3. **MODERATE ROI**: High-frequency theological (500+) - likely comprehensive but needs testing
4. **LOW ROI**: Ultra-high grammatical (1000+) - limited unique web data, focus on stats only

**Primary Variables (in order of importance)**:
1. Word type (theological vs grammatical) - STRONGEST predictor
2. Theological significance - SECONDARY predictor
3. Frequency tier - TERTIARY predictor within word type category

**Source**: `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/EXPERIMENTS-COMPARISON.md` lines 601-618

---

### B. Quality Standards & Validation

**3-Level Validation Framework** (universally successful across 17 experiments):

**Level 1 - CRITICAL (Must Pass 100%)**:
- No fabricated data (all claims from real sources)
- Inline citations present: `content {source}`
- No percentages/predictions without exact counts
- Base file read FIRST before web extraction
- All sources documented in ATTRIBUTION.md

**Level 2 - HIGH PRIORITY (Must Pass 80%+)**:
- Etymology from 2+ lexicons (not just Strong's)
- Semantic categories appropriate for frequency (2 for rare, 5-8 for common)
- Usage statistics match concordances exactly
- Convergence documented (3+ lexicons agreeing)
- Divergence noted (Classical vs Koine, theological vs linguistic)

**Level 3 - MEDIUM PRIORITY (Must Pass 60%+)**:
- Cross-reference codes extracted (TDNT, TWOT, Trench, BDAG)
- Diachronic analysis when relevant (Classical → Koine development)
- Fair use compliance (convergence grouping, transformative analysis)
- Related words documented (roots, derivatives, synonyms)

**Achievement**: All experiments passed Level 1 (100%), Level 2 (85-100%), Level 3 (75-100%)

**Source**: `/plan/strongs-enrichment-tools/01-lexicon-core/validation/quality-checklist.md`

---

### C. Fair Use Patterns

**Critical Learnings** (prevents copyright violations):

**1. Convergence Grouping** (when lexicons agree):
```yaml
# ✅ CORRECT (fair use)
etymology: "From δύναμαι (to be able) {thayer} {helps} {abbott-smith}"
convergence_note: "Etymology consistent across all major Greek lexicons"

# ❌ WRONG (copyright violation)
thayers_entry: "δύναμις, -εως, ἡ (δύναμαι), from Homer down..."
helps_entry: "1411 dýnamis (from 1410 /dýnamai) – properly, power..."
```

**2. Divergence in Comparative Context** (when lexicons disagree):
```yaml
# ✅ CORRECT (transformative scholarly analysis)
lexical_divergence:
  - semantic_area: "Classical to Koine semantic shift"
    classical_usage: "natural physical strength {lsj-abridged}"
    koine_usage: "miraculous divine power {thayer} {helps}"
    analysis: "Semantic shift reflects supernatural application in NT {llm-cs45}"
```

**Why This Works**:
- Cannot reconstruct any single lexicon from output
- Transformative analysis adds scholarly commentary
- Limited quotation (brief excerpts only)
- Collective citations for convergence

**Source**: `/plan/strongs-enrichment-tools/01-lexicon-core/research/convergence-patterns.md`

---

### D. Standards Hierarchy

**Critical Correction** (from peer review):

**When standards conflict, use this hierarchy**:
1. **STANDARDIZATION.md** (project standard) - file naming, paths, codes
2. **SCHEMA.md** (data structure standard) - YAML structure, citation format
3. **CLAUDE.md** (workflow/limits) - progressive disclosure (≤200 lines), git workflow
4. **REVIEW-GUIDELINES.md** - validation levels, quality criteria
5. **ATTRIBUTION.md** - source codes, citations
6. **Existing tools** - patterns to follow (but VERIFY against standards first)

**Never**:
- Assume existing tools are correct without verification
- Use Tool 1 as authority (it's a reference, not standard)
- Trust patterns without checking standards

**Source**: `/plan/strongs-enrichment-tools/03-web-insights/PEER-REVIEW-LEARNINGS.md` lines 10-50

---

## II. Experimental Findings by Tool

### A. Lexicon-Core (Tool 1) - 12 Experiments

**Frequency Spectrum Testing** (Greek & Hebrew):

| Experiment | Word | Type | Freq | Data Points | Value |
|------------|------|------|------|-------------|-------|
| Exp1 | G0846 αὐτός | Grammatical pronoun | 5,597x | ~15 | Moderate |
| Exp2 | G1411 δύναμις | Theological noun | 120x | ~45 | High |
| Exp3 | G5287 ὑπόστασις | Theological noun | 5x | ~35 | High |
| Exp4 | H430 אֱלֹהִים | Theological noun | 2,606x | ~50 | Very High (9.7/10) |

**Key Insights**:

**1. Theological Significance > Statistical Frequency**
- LSJ entry for ὑπόστασις (5x) MORE detailed than for δύναμις (120x)
- Reason: Philosophical significance (Aristotle's substance concept) drives lexicographer attention
- HELPS Word-studies covers theologically significant rare words, skips ultra-common grammatical terms

**2. Hebrew = Greek Methodology + Minor Additions**
- BDB extracts like Thayer's (no workflow changes needed)
- Same 3-source approach works: BibleHub, StudyLight, Blue Letter Bible
- Hebrew additions (bonus content, not different process):
  - TWOT instead of TDNT (same function)
  - Pictographic etymology (Ancient Hebrew Lexicon bonus)
  - Plural-singular morphology notes (e.g., H430 אֱלֹהִים)

**3. Rare Word Restraint Protocol** (prevents fabrication):
- Complete occurrence list required for <20 occurrences
- Semantic categories limited: 1-3 for very rare (vs 5-8 for common)
- Confidence markers mandatory (HIGH/MEDIUM/LOW)
- Explicit rarity notation: "Limited occurrences prevent comprehensive analysis"
- Leverage classical Greek (LSJ) to supplement sparse NT data

**4. Controversy Detection Highly Feasible**
- False etymologies leave clear refutation trails online
- Example: "dynamis = dynamite" fallacy - found 6 expert refutations (Carson, Cara, Mounce)
- 5-Part Error Correction Structure discovered:
  1. Error statement (clear, non-mocking)
  2. Classification (name the fallacy type: "semantic anachronism")
  3. Multi-layered refutation (4-5 evidence types)
  4. Expert validation (stack authorities with quotes)
  5. Correct alternative (better analogy, proper methodology)
- Gracious pedagogical tone is standard across all refutations

**5. Web Source Complementarity** (for theological terms):
- HELPS: Practical/devotional application
- Thayer's: Comprehensive categorical breakdown
- Mounce: Pedagogical emphasis for students
- Papyri sources: Historical/diachronic development
- Abbott-Smith: Balanced scholarly precision
- LSJ: Classical philological depth

**Source**: `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/` (exp1-4 LEARNINGS.md files)

---

### B. Web-Insights (Tool 3) - 5 Adversarial Experiments

**Adversarial Testing Philosophy**: Test hard cases (rare words, scholarly disagreement), not easy wins.

| Experiment | Word | Type | Result | Key Finding |
|------------|------|------|--------|-------------|
| Exp1 | G4151 πνεῦμα | Scholarly disagreement | ✅ Success | Found 4 types of real disagreement - must present multiple views fairly |
| Exp2 | G2160 εὐτραπελία | Rare hapax integrity test | ✅ Success* | Expected 0-1 sources, found 12 (virtue ethics discipline) |
| Exp3 | G1161 δέ | Scope boundary | ✅ Success | Correctly identified grammatical particle as outside Tool 3 scope |
| Exp4 | G1411 δύναμις | Error correction | ✅ Success | Found 6 sources, 3 VERY HIGH authority - 5-part correction pattern |
| Exp5 | G1577 ἐκκλησία | Cultural debate | ✅ Success | 12+ sources with divergent views - multi-perspective framework validated |

**Critical Discoveries**:

**1. Authority Doesn't Always Resolve Disagreement**
- Duke Ph.D. scholars disagree with each other (Levison vs Keener on pneuma capitalization)
- Major commentators disagree after 2000 years (Romans 8:10)
- Tool must present multiple credible views, not pick sides
- Need status markers: "ongoing debate" vs "scholarly consensus"

**2. Coverage is Discipline-Specific**
- Eutrapelia: Excellent in virtue ethics, limited in Bible study platforms
- Must search multiple disciplines: theology, linguistics, philosophy, translation studies
- Specialized coverage is legitimate (requires appropriate framing)
- Peer-reviewed journal article (Moreana, 2015) found for 1x hapax

**3. Multi-Perspective Framework Required** (for controversial terms):
```yaml
translation_approaches:
  traditional:
    rendering: "church"
    strengths: ["theological continuity", "covenantal identity", "established usage"]
    considerations: ["possible building confusion", "historical baggage"]

  reformist:
    rendering: "assembly"
    strengths: ["Greek semantic range", "civic overtones", "avoids building focus"]
    considerations: ["loses theological resonance", "sounds secular"]
```

**4. Bias Detection Methods**:
- **Reversal Test**: Could you reverse presentation without changing implications?
- **Respect Test**: Would advocates of each view feel fairly represented?
- **Evidence Test**: Did you present strongest arguments for ALL positions?

**5. Scope Boundaries Work**:
- Grammatical particles: Tool 1 territory (lexicon-core)
- Modern debates, practical insights, error corrections: Tool 3 territory (web-insights)
- Skip decision = SUCCESS (appropriate self-restraint)

**Source**: `/plan/strongs-enrichment-tools/03-web-insights/experiments/EXPERIMENTS-COMPLETE-SUMMARY.md`

---

## III. Workflow & Process Learnings

### A. Extraction Workflow

**Successful Pattern** (proven across 17 experiments):

**Step 1: Pre-Flight Check**
- Read base Strong's file FIRST (check what's already present)
- Check word frequency → select appropriate template
- Identify word type (theological vs grammatical) → determines extraction strategy

**Step 2: Web Extraction**
- BibleHub: HELPS, Thayer's, Strong's
- StudyLight: Multiple lexicons for comparison, TWOT (Hebrew), pictographic etymology
- Blue Letter Bible: KJV usage statistics, outline of biblical usage, TDNT codes

**Step 3: Convergence Synthesis**
- Group lexicons that agree (convergence pattern)
- Note areas of divergence (Classical vs Koine, theological vs linguistic)
- Apply fair use patterns (collective citations, transformative analysis)

**Step 4: Validation** (run checks during extraction, not just after)
- Level 1: CRITICAL checks (inline citations, no fabrication)
- Level 2: HIGH PRIORITY (convergence, appropriate categories)
- Level 3: MEDIUM (cross-refs, diachronic analysis)

**Step 5: Learnings Documentation**
- What worked well
- What failed or was missing
- Edge cases discovered
- Recommendations for next cycle

---

### B. Progressive Disclosure

**Hard Limit** (from CLAUDE.md line 75-76):
- README files: ≤200 lines (self-contained overview)
- Topic files: ≤400 lines (detailed treatment)
- Plan ahead: if content will exceed limits, create directory structure from start

**Application**: This README targets <400 lines for comprehensive synthesis with references to detailed documentation.

---

### C. Git Workflow

**Critical Pattern** (from CLAUDE.md):
- **Commit BEFORE editing files** when moving them (preserves git history)
- **Push after EVERY commit**: `git commit → git push` (never batch)
- Pattern: make change → commit → push → repeat

**File Organization**:
- NEVER save working files, text/mds, tests to root folder
- Use appropriate subdirectories: `/plan`, `/docs`, `/tests`, `/src`

---

## IV. Technical Implementation

### A. Schema Patterns

**Inline Citation Format** (CRITICAL for Level 1 validation):
```yaml
# ✅ CORRECT
etymology: "From δύναμαι (to be able) {thayer} {helps}"

# ❌ WRONG (separate citation fields)
etymology: "From δύναμαι (to be able)"
citation: {thayer} {helps}  # DON'T DO THIS!
```

**Confidence Markers** (required for rare words <10x):
```yaml
etymology:
  confidence: HIGH  # Multiple lexicons, clear compound structure

semantic_category:
  confidence: HIGH  # Well-attested, theologically central

cross_language_equivalent:
  confidence: MEDIUM  # Cross-language proximity data, plausible but not certain
```

---

### B. Source Evaluation

**Web Source Reliability Tiers**:

**VERY HIGH Authority**:
- D.A. Carson (Ph.D. Cambridge, Trinity Evangelical)
- Robert Cara (Ph.D., chief academic officer)
- William Mounce (Ph.D., NT Greek expert)

**Minimum Requirements** (error corrections):
- 2 sources (MEDIUM-HIGH or higher)
- At least 1 HIGH or VERY HIGH authority
- Multiple evidence types (3+)

---

## V. Coverage & Timeline

### A. Realistic Coverage Estimates

**Revised Estimate** (based on experimental complexity):
- High-priority: ~300 words (scholarly debates, known errors, cultural issues)
- Medium-priority: ~800 words (good coverage, practical insights)
- Low-priority: ~400 words (specialized or opportunistic)
- **Total: ~1,500 words** (more realistic given quality standards)

**Skip Categories**: ~12,500 words (grammatical particles, no expert coverage, fully covered by Tool 1)

---

### B. Time Per Word

**From Experiment Time Logs**:
- High-frequency theological (100+x): ~60 min extraction, ~30 min validation
- Medium-frequency theological (50-100x): ~60 min extraction, ~30 min validation
- Rare theological significant (1-10x): ~90 min extraction (Classical Greek research), ~30 min validation
- Ultra-high grammatical (1000+x): ~45 min extraction (stats-focused), ~20 min validation
- Web-insights multi-perspective synthesis: ~4-5 hours (interdisciplinary research)

---

## VI. Known Pitfalls & Solutions

### A. Fabrication Temptations

**Temptation 1**: Creating elaborate semantic categories for rare words
- **Solution**: Complete occurrence lists, explicit rarity notes, limit categories (1-3 for very rare)

**Temptation 2**: Inventing usage patterns from limited examples
- **Solution**: Leverage classical Greek (LSJ) instead of fabricating NT patterns

**Temptation 3**: Reproducing individual lexicons (copyright violation)
- **Solution**: Convergence grouping, transformative analysis, comparative context

---

### B. Scope Creep

**What to SKIP**:
- Grammatical particles with no semantic content (δέ, καί, etc.)
- Words fully covered by Tool 1 with no modern insights (Tool 3)
- Ultra-high frequency grammatical terms with limited unique web data

**Skip Decision = SUCCESS** (demonstrates appropriate boundaries)

---

### C. Bias in Controversial Terms

**Detection Methods**:
1. **Reversal Test**: Could you swap position order without implications changing?
2. **Respect Test**: Would advocates of each view feel fairly represented?
3. **Evidence Test**: Strongest arguments presented for ALL positions?

**Prevention**: Multi-perspective framework with strengths + considerations for each view

---

## VII. Next Steps & Recommendations

### A. Production Priorities

**Tier 1 - Highest ROI** (start here):
- Medium-frequency theological terms (50-500x)
- Known error corrections (dynamis, etc.)
- Active scholarly debates (pneuma, logos)

**Tier 2 - High ROI** (despite rarity):
- Theologically significant rare words (1-10x)
- Cultural translation challenges (lamb, snow, bread)

**Skip**:
- Ultra-high grammatical (1000+) unless stats needed
- Grammatical particles with no semantic content

---

### B. Tool Integration

**Shared Infrastructure**:
- All three tools (lexicon-core, web-insights, TBTA hints) analyze same 900+ translation corpus
- Extraction synergy: TBTA extracts grammatical patterns, Cultural Challenges extracts semantic adaptations
- Pipeline reusability: Single corpus → multiple extractors → separate YAML files per tool

---

## VIII. References

### Primary Planning Documents

**Lexicon-Core Experiments**:
- `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/exp1-high-freq-word/LEARNINGS.md`
- `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/exp2-medium-freq/LEARNINGS.md`
- `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/exp3-rare-word/LEARNINGS.md`
- `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/exp4-hebrew-word/LEARNINGS.md`
- `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/EXPERIMENTS-COMPARISON.md`

**Web-Insights Experiments**:
- `/plan/strongs-enrichment-tools/03-web-insights/PEER-REVIEW-LEARNINGS.md`
- `/plan/strongs-enrichment-tools/03-web-insights/experiments/EXPERIMENTS-COMPLETE-SUMMARY.md`

**Research & Methodology**:
- `/plan/strongs-enrichment-tools/01-lexicon-core/research/convergence-patterns.md`
- `/plan/strongs-enrichment-tools/01-lexicon-core/validation/quality-checklist.md`

**Strategic Planning**:
- `/plan/strongs-comprehensive-strategy.md`

---

## Conclusion

**What We Validated**:
- Systematic Strong's enrichment is feasible across full rarity spectrum (1-5,597 occurrences)
- Quality standards achievable (100% critical, 85-100% high priority, 75-100% medium)
- Theological significance predicts extraction value better than frequency
- Fair use compliance patterns work reliably
- Both Greek and Hebrew follow same methodology

**What We Learned**:
- Word type (theological vs grammatical) matters MORE than frequency
- Rare theologically significant words yield richer data than common grammatical terms
- Web coverage is discipline-specific (search multiple domains)
- Authority doesn't always resolve disagreement (multi-perspective frameworks required)
- Restraint is achievable with explicit methodology (prevents fabrication)

**What's Ready**:
- Lexicon-core tool validated across 12 experiments
- Web-insights tool validated across 5 adversarial tests
- Quality validation framework (3-level checking)
- Fair use patterns (convergence grouping, transformative analysis)
- Extraction workflows (tiered by word type and frequency)

**Next Phase**: Production deployment starting with Tier 1 (medium-frequency theological terms, known errors, scholarly debates)

---

**Total Experiments**: 17 (12 lexicon-core, 5 web-insights)
**Total Documentation**: 50+ planning files, 6,361 lines
**Validation Success Rate**: 100% Level 1, 85-100% Level 2, 75-100% Level 3
**Zero Fabrication**: All claims grounded in real sources across all experiments
