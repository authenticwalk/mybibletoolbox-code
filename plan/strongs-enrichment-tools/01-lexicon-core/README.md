# Tool 1: Strong's Lexicon Core

**Status:** Research Phase
**Priority:** HIGHEST - Foundation for all other tools
**Authority:** HIGH - Published lexicons only
**Coverage:** All 14,197 Strong's words

---

## Purpose

Extract authoritative lexical data (etymology, semantic range, usage statistics) from published lexicons to create the foundation for all Strong's enrichment work.

**Why This Tool Matters:**
- Foundation for all 14,197 Strong's words
- Provides core lexical data that other tools build upon
- Uses only HIGH authority sources (published lexicons)
- Fair use compliant (convergence grouping, no reconstruction)

---

## Methodology Overview

### 4-Step Extraction Process

**Step 1: Read Base Strong's File** (ALWAYS FIRST!)
- Location: `./bible/words/strongs/{number}/{number}.strongs.yaml`
- Contains: Pre-imported lexicon data (BDB, Thayer's, unfoldingWord, LSJ)
- Extract: Cross-reference codes (BDAG, TDNT, Louw-Nida, etc.)
- **Purpose:** Avoid duplicating existing data, use codes for additional searches

**Step 2: Extract from BibleHub** (Parallel)
- URL: `https://biblehub.com/greek/{number}.htm`
- Extract: Thayer's, HELPS Word-studies, usage statistics
- Focus: Data NOT already in base file

**Step 3: Extract from StudyLight** (Parallel)
- URL: `https://www.studylight.org/lexicons/eng/greek/{number}.html`
- Extract: LSJ (abridged), Abbott-Smith, Vocabulary of Greek NT
- Focus: Unique lexicons not elsewhere

**Step 4: Extract from Blue Letter Bible** (Parallel)
- URL: `https://www.blueletterbible.org/lexicon/g{number}/...`
- Extract: TDNT references, Trench's Synonyms, cross-reference codes
- Focus: Theological resources

### Synthesis Process

**Main Agent Combines:**
1. Identify convergence: "Most lexicons agree X {thayer} {bdb} {lsj}"
2. Document divergence: "Classical vs Koine differs: Classical {lsj} vs NT {thayer}"
3. Fair use compliance: Convergence grouping, inline citations
4. Quality check: No fabrication, all claims sourced

---

## Research Phase

**Location:** `./research/`

**Documents:**
1. `source-inventory.md` - Complete inventory of available lexicons per site
2. `extraction-methods.md` - Step-by-step extraction from each source
3. `convergence-patterns.md` - How to identify agreement vs. divergence

**Key Research Questions:**
- What data is already in base files? (avoid duplication)
- Which lexicons on each aggregator site? (Thayer's, BDB, LSJ, etc.)
- How to identify convergence? (3+ lexicons agree)
- How to document divergence? (scholarly debate exists)
- How to handle missing data? (rare words with <10 occurrences)

---

## Experimentation Phase

**Location:** `./experiments/`

**5 Experiments Planned:**

1. **exp1-high-freq-word/** - G846 (αὐτός - he/she/it)
   - Why: 5,597 occurrences - most data available
   - Test: Comprehensive semantic range extraction

2. **exp2-medium-freq/** - G1411 (δύναμις - power)
   - Why: 120 occurrences - theologically significant
   - Test: Convergence patterns, controversy handling

3. **exp3-rare-word/** - Word with <10 occurrences
   - Why: Test limited data handling
   - Test: Honest about limitations, no fabrication

4. **exp4-hebrew-word/** - H430 (אֱלֹהִים - Elohim)
   - Why: Test Hebrew extraction (BDB vs Thayer's)
   - Test: Different lexicon structure

5. **exp5-word-family/** - Love words (G25, G26, G5368)
   - Why: Test convergence detection across related words
   - Test: Distinctions clear, patterns emerge

**Each Experiment Produces:**
- Output YAML file following schema
- Learnings document (what worked, what failed)
- Quality validation results

---

## Output Schema

**File Location:** `./bible/words/strongs/{number}/{number}-lexicon-core.yaml`

**Schema Location:** `./schema.yaml`

**Key Sections:**
- Metadata (Strong's number, language, lemma, transliteration)
- Base data (from pre-existing file)
- Etymology (root words, derivation)
- Semantic range (convergence-grouped)
- Usage statistics (frequency, distribution)
- Lexical convergence (where lexicons agree)
- Lexical divergence (where lexicons disagree)
- Cross-reference codes (BDAG, TDNT, etc.)

---

## Validation Phase

**Location:** `./validation/`

**Quality Checklist:** (3 levels)

**Level 1: CRITICAL (100% pass required)**
- No fabricated data
- Inline citations: `content {source}`
- No percentages (use "most", "many", "some")
- Base file read FIRST
- All sources in ATTRIBUTION.md

**Level 2: HIGH PRIORITY (80%+ pass required)**
- Etymology from multiple lexicons
- 2+ semantic categories (for 20+ occurrences)
- Usage statistics match sources
- Convergence patterns documented
- Divergence noted when exists

**Level 3: MEDIUM PRIORITY (60%+ pass required)**
- Cross-reference codes extracted
- Diachronic analysis (Classical→Koine)
- Fair use compliance verified

---

## Subagent Strategy

**Main Agent:** Orchestrate extraction and synthesis

**Subagent 1:** Base File Reader (SEQUENTIAL)
- Read `./bible/words/strongs/{num}/{num}.strongs.yaml`
- Extract existing data, cross-ref codes
- Identify what's already present

**Subagent 2-4:** Parallel Extraction
- **Subagent 2:** BibleHub (Thayer's, HELPS, usage stats)
- **Subagent 3:** StudyLight (LSJ, Abbott-Smith, Vocab of Greek NT)
- **Subagent 4:** Blue Letter Bible (TDNT refs, Trench's Synonyms)

**Main Agent:** Synthesis
- Combine data from all sources
- Identify convergence patterns
- Document divergence
- Apply fair use compliance
- Generate lexicon-core.yaml

---

## Implementation Timeline

**Week 1-2:** Research Phase
- Complete source inventory
- Document extraction methods
- Design convergence detection

**Week 3-4:** Experimentation Phase
- Run 5 experiments
- Capture learnings
- Refine methodology

**Week 5:** Validation Phase
- Validate experiment outputs
- Refine schema based on learnings
- Document quality criteria

**Week 6-14:** Production Phase
- Top 300 high-frequency words (Week 6-8)
- Theologically significant (~500 words, Week 9-10)
- All remaining Greek (~5,000 words, Week 11-12)
- All Hebrew (~8,600 words, Week 13-14)

---

## Success Metrics

**Coverage:** 14,197/14,197 words completed
**Quality:** 95%+ pass Level 1 validation
**Fair Use:** 100% convergence grouping compliance
**Authority:** All sources marked HIGH

---

## Next Steps

1. Complete research phase documents (Week 1-2)
2. Design and run experiments (Week 3-4)
3. Validate and refine (Week 5)
4. Begin production (Week 6+)

---

**See:**
- `/plan/strongs-enrichment-sources/README.md` - Overall strategy
- `/plan/strongs-enrichment-sources/IMPLEMENTATION-PLAN.md` - All 7 tools
- `/plan/policy/fair-use.md` - Fair use compliance
