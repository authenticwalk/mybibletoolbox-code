# Strong's Enrichment Tools: Implementation Plan

**Created:** 2025-11-08
**Status:** Planning
**Approach:** Progressive disclosure with deep research, experimentation, and validation per tool

---

## Overview

This document outlines the implementation strategy for 7 Strong's enrichment tools based on Proposal D (Hybrid - Use Case + Authority). Each tool follows the TBTA pattern:

1. **Research Phase** - Deep investigation of sources and methods
2. **Experimentation Phase** - Test on sample words with learnings capture
3. **Validation Phase** - Quality checks and refinement
4. **Production Phase** - Scale to target word set

---

## Directory Structure

```
/plan/strongs-enrichment-tools/
├── README.md                           # This overview
├── IMPLEMENTATION-PLAN.md              # This file
├── 01-lexicon-core/
│   ├── README.md                       # Research findings (≤200 lines)
│   ├── research/
│   │   ├── source-inventory.md        # Available lexicons
│   │   ├── extraction-methods.md      # How to extract without duplication
│   │   └── convergence-patterns.md    # How to identify agreement/disagreement
│   ├── experiments/
│   │   ├── exp1-high-freq-word/       # Test: G846 (he/she/it) - 5597 occurrences
│   │   ├── exp2-medium-freq/          # Test: G1411 (dunamis) - 120 occurrences
│   │   ├── exp3-rare-word/            # Test: rare word <10 occurrences
│   │   ├── exp4-hebrew-word/          # Test: H430 (Elohim)
│   │   └── LEARNINGS.md               # Aggregated learnings
│   ├── schema.yaml                    # Output schema definition
│   └── validation/
│       ├── quality-checklist.md       # Validation criteria
│       └── test-results.md            # Experiment validation results
│
├── 02-scholarly-analysis/
│   ├── README.md
│   ├── research/
│   │   ├── journal-access.md          # How to find academic sources
│   │   ├── cross-ref-usage.md         # Using BDAG/TDNT/Louw-Nida codes
│   │   └── authority-ranking.md       # Source authority classification
│   ├── experiments/
│   │   ├── exp1-theological-word/     # Test: G26 (agape)
│   │   ├── exp2-controversial/        # Test: G3056 (logos)
│   │   └── LEARNINGS.md
│   ├── schema.yaml
│   └── validation/
│
├── 03-web-insights/
│   ├── README.md
│   ├── research/
│   │   ├── expert-blog-inventory.md
│   │   └── authority-detection.md
│   ├── experiments/
│   │   └── LEARNINGS.md
│   ├── schema.yaml
│   └── validation/
│
├── 04-community-discussions/
│   ├── README.md
│   ├── research/
│   │   ├── controversy-patterns.md
│   │   └── refutation-sources.md
│   ├── experiments/
│   │   ├── exp1-dunamis-dynamite/     # Known controversy
│   │   └── LEARNINGS.md
│   ├── schema.yaml
│   └── validation/
│
├── 05-relationships/
│   ├── README.md
│   ├── research/
│   │   ├── synonym-sources.md
│   │   └── semantic-domain-systems.md
│   ├── experiments/
│   │   ├── exp1-love-word-family/     # Test: agape, phileo, eros
│   │   └── LEARNINGS.md
│   ├── schema.yaml
│   └── validation/
│
├── 06-translation-patterns/
│   ├── README.md
│   ├── research/
│   │   ├── corpus-access.md           # eBible, parallel corpora
│   │   ├── feature-extraction.md      # How to identify linguistic features
│   │   └── confidence-scoring.md      # Statistical methods
│   ├── experiments/
│   │   ├── exp1-clusivity/            # Test: G2249 (we) - inclusive/exclusive
│   │   ├── exp2-proximity/            # Test: G3778 (this) - demonstrative distance
│   │   ├── exp3-number-system/        # Test: dual/trial detection
│   │   └── LEARNINGS.md
│   ├── schema.yaml
│   └── validation/
│
└── 07-specialized-linguistics/
    ├── README.md
    ├── research/
    │   ├── lxx-tools.md
    │   ├── papyri-databases.md
    │   ├── classical-access.md
    │   └── cognate-databases.md
    ├── experiments/
    │   ├── exp1-lxx-semantic-shift/   # Word with Classical→Koine change
    │   └── LEARNINGS.md
    ├── schema.yaml
    └── validation/
```

---

## Tool 1: strongs-lexicon-core (HIGHEST PRIORITY)

### Overview
**Purpose:** Authoritative lexical foundation for all 14,197 Strong's words
**Authority:** HIGH - Published lexicons only
**Target Coverage:** All 14,197 words
**Timeline:** 2 months (research 2 weeks, experiments 2 weeks, production 6 weeks)

### Research Phase (Week 1-2)

**Research Questions:**
1. What data is already in base Strong's files? (avoid duplication)
2. Which lexicons are available on each aggregator site?
3. How to identify convergence vs. divergence patterns?
4. What's the optimal extraction order? (base → BibleHub → StudyLight → BLB)
5. How to handle missing data for rare words?

**Research Outputs:**
- `/01-lexicon-core/research/source-inventory.md`
  - Complete inventory: Base files, BibleHub, StudyLight, BLB
  - Which lexicons on each site: Thayer's, BDB, LSJ, HELPS, etc.
  - Data fields available: etymology, semantic range, usage stats

- `/01-lexicon-core/research/extraction-methods.md`
  - Step-by-step extraction process
  - How to read base file first
  - How to avoid duplicating pre-imported data
  - WebFetch patterns for each site

- `/01-lexicon-core/research/convergence-patterns.md`
  - How to identify when lexicons agree (convergence)
  - How to document divergence (scholarly debates)
  - Fair use compliance: convergence grouping strategy

**Subagent Strategy:**
```
Main Agent: Orchestrate extraction and synthesis
├── Subagent 1: Base File Reader
│   └── Read ./bible/words/strongs/{num}/{num}.strongs.yaml
│       Extract: existing lexicon data, cross-ref codes
│
├── Subagent 2: BibleHub Extractor (PARALLEL)
│   └── WebFetch: https://biblehub.com/greek/{num}.htm
│       Extract: Thayer's, HELPS, usage statistics
│       Avoid: duplicating base file data
│
├── Subagent 3: StudyLight Extractor (PARALLEL)
│   └── WebFetch: https://www.studylight.org/lexicons/eng/greek/{num}.html
│       Extract: LSJ, Abbott-Smith, Vocabulary of Greek NT
│       Focus: unique data not in base or BibleHub
│
└── Subagent 4: Blue Letter Bible Extractor (PARALLEL)
    └── WebFetch: https://www.blueletterbible.org/lexicon/g{num}/...
        Extract: TDNT references, Trench's Synonyms
        Focus: cross-reference codes

Main Agent: Synthesize into lexicon-core.yaml
├── Identify convergence: "Most lexicons agree X {thayer} {bdb} {lsj}"
├── Document divergence: "Classical vs Koine usage differs..."
└── Quality check: inline citations, no fabrication
```

### Experimentation Phase (Week 3-4)

**Experiment 1: High-Frequency Word (G846 - αὐτός)**
- **Why:** 5,597 occurrences - most data available, test extraction completeness
- **Focus:** Can we extract comprehensive semantic range? Usage statistics accurate?
- **Output:** `/01-lexicon-core/experiments/exp1-high-freq-word/G846-output.yaml`
- **Validation:** Does output have 3+ semantic categories? Usage stats match sources?

**Experiment 2: Medium-Frequency Theological Word (G1411 - δύναμις)**
- **Why:** 120 occurrences - theologically significant, known controversy
- **Focus:** Convergence patterns across lexicons, controversy handling
- **Output:** `/01-lexicon-core/experiments/exp2-medium-freq/G1411-output.yaml`
- **Validation:** Etymology correct? 7 usage categories documented (from Thayer's)?

**Experiment 3: Rare Word (<10 occurrences)**
- **Why:** Test handling of limited data - 80% of Strong's entries are rare
- **Focus:** Honest about data limitations, no fabrication
- **Output:** `/01-lexicon-core/experiments/exp3-rare-word/GXXXX-output.yaml`
- **Validation:** Explicitly notes rarity? Doesn't fabricate elaborate semantic ranges?

**Experiment 4: Hebrew Word (H430 - אֱלֹהִים)**
- **Why:** Test Hebrew extraction (different lexicons: BDB instead of Thayer's)
- **Focus:** BDB data extraction, Hebrew-specific patterns
- **Output:** `/01-lexicon-core/experiments/exp4-hebrew-word/H430-output.yaml`
- **Validation:** BDB data present? Hebrew morphology handled correctly?

**Experiment 5: Word Family Convergence Test**
- **Why:** Test convergence detection across multiple related words
- **Select:** Love words (G25 agapao, G26 agape, G5368 phileo)
- **Focus:** Do convergence patterns emerge correctly?
- **Output:** `/01-lexicon-core/experiments/exp5-word-family/`
- **Validation:** Convergence grouping accurate? Distinctions clear?

**Learnings Document:**
- `/01-lexicon-core/experiments/LEARNINGS.md`
- Capture: What worked? What failed? Patterns discovered? Edge cases?

### Schema Design

**Output File:** `./bible/words/strongs/{num}/{num}-lexicon-core.yaml`

```yaml
# === METADATA ===
strongs_number: "{number}"
language: "{greek|hebrew}"
lemma: "{lexical_form}"
transliteration: "{romanized}"

tool:
  name: "strongs-lexicon-core"
  version: "1.0.0"
  generated_date: "YYYY-MM-DD"

# === BASE DATA (from pre-existing file) ===
base_data:
  strongs_number: "{number}"
  definition: "{base definition}" {strongs}
  kjv_usage: "{KJV usage}" {strongs}
  derivation: "{derivation}" {strongs}
  # Pre-imported lexicon data (if present)
  imported_lexicons:
    thayers: "{data}" {thayer}
    bdb: "{data}" {bdb}
    lsj: "{data}" {lsj-abridged}

# === ETYMOLOGY (high authority) ===
etymology:
  root_words:
    - word: "{root_word_1}"
      strongs: "{number}"
      meaning: "{root meaning}" {biblehub-lexicon}
  derivation_notes: "{detailed etymology}" {thayer} {biblehub-lexicon}
  convergence_note: "Etymology consistent across lexicons {thayer} {bdb} {lsj}"

# === SEMANTIC RANGE (high authority) ===
semantic_range:
  convergence_note: "Major lexicons agree on 3 primary meanings {thayer} {bdag-ref} {helps}"

  categories:
    - category_id: 1
      definition: "{primary meaning}" {thayer} {helps}
      biblical_examples:
        - ref: "{BOOK}.{chapter}.{verse}"
          context: "{how used here}" {biblehub-interlinear}

    - category_id: 2
      definition: "{secondary meaning}" {thayer}
      divergence_note: "Classical usage differs {lsj}: {classical meaning}"

# === USAGE STATISTICS (high authority) ===
usage_statistics:
  total_occurrences: {count} {biblehub-lexicon}
  source_verification: "Verified against multiple concordances"
  grammatical_forms: {count} {biblehub-lexicon}
  testament_distribution:
    old_testament: {count}
    new_testament: {count}
  kjv_translation_frequency:
    - translation: "{English word}"
      count: {number} {biblehub-lexicon}
      percentage: {calculated}

# === CONVERGENCE PATTERNS (fair use compliance) ===
lexical_convergence:
  primary_meaning: "{core agreed definition}"
  lexicons_agreeing: [thayer, bdag-ref, helps, lsj-abridged, bdb]
  confidence: "high"
  note: "Strong consensus across published lexicons"

# === DIVERGENCE PATTERNS (fair use compliance) ===
lexical_divergence:
  - semantic_area: "{area of disagreement}"
    approach_1:
      definition: "{first interpretation}"
      sources: [thayer, helps]
      context: "NT usage focuses on X"
    approach_2:
      definition: "{second interpretation}"
      sources: [lsj-abridged]
      context: "Classical usage emphasizes Y"
    note: "Diachronic shift from Classical → Koine Greek" {llm-cs45}

# === CROSS-REFERENCE CODES ===
cross_references:
  bdag: "{code}"          # If available
  tdnt: "{reference}"     # If available
  louw_nida: "{domain}"   # If available
  gk: "{number}"          # If available

# === QUALITY METADATA ===
metadata:
  extraction_date: "YYYY-MM-DD HH:MM:SS"
  sources_consulted:
    - base_file: "./bible/words/strongs/{num}/{num}.strongs.yaml"
    - biblehub: "https://biblehub.com/{greek|hebrew}/{num}.htm"
    - studylight: "https://www.studylight.org/lexicons/eng/greek/{num}.html"
    - blb: "https://www.blueletterbible.org/lexicon/{g|h}{num}/..."
  data_quality:
    inline_citations: true
    convergence_grouping: true
    no_fabrication: true
  authority_level: "HIGH"
  tokens_used: {count}
```

### Validation Phase (Week 5)

**Quality Checklist:** `/01-lexicon-core/validation/quality-checklist.md`

**Level 1: CRITICAL (Must Pass 100%)**
- [ ] No fabricated data - all facts extracted from real sources
- [ ] Inline citations: `content {source}` (not separate fields)
- [ ] No percentages (use qualitative: "most", "many", "some")
- [ ] Base file read FIRST (avoid duplication)
- [ ] All new sources in ATTRIBUTION.md

**Level 2: HIGH PRIORITY (80%+ to Pass)**
- [ ] Etymology verified from multiple lexicons (not invented)
- [ ] At least 2 semantic range categories for words with 20+ occurrences
- [ ] Usage statistics match source data exactly
- [ ] Convergence patterns documented when lexicons agree
- [ ] Divergence documented when lexicons disagree

**Level 3: MEDIUM PRIORITY (60%+ to Pass)**
- [ ] Cross-reference codes extracted when available
- [ ] Diachronic analysis when Classical→Koine shift significant
- [ ] Fair use compliance: convergence grouping present

**Test Results:** `/01-lexicon-core/validation/test-results.md`
- Document: Pass/fail per experiment
- Identify: Patterns that work, patterns that fail
- Refine: Schema and methodology based on learnings

### Production Phase (Week 6-14)

**Priority Tiers:**
1. **Top 300 high-frequency words** (Week 6-8) - 4% of words, 85% of text coverage
2. **Theologically significant words** (Week 9-10) - ~500 words
3. **All remaining Greek words** (Week 11-12) - ~5,000 words
4. **All Hebrew words** (Week 13-14) - ~8,600 words

**Automation Strategy:**
- Batch processing with parallel subagents
- Quality spot-checks every 100 words
- Flag low-confidence outputs for human review

**Success Metrics:**
- Coverage: 14,197/14,197 words completed
- Quality: 95%+ pass Level 1 validation
- Fair use: 100% convergence grouping compliance
- Authority: All sources marked HIGH authority

---

## Tool 2: strongs-scholarly-analysis (HIGH VALUE)

### Overview
**Purpose:** Academic insights and theological analysis
**Authority:** HIGH - Peer-reviewed sources only
**Target Coverage:** ~1,000 theologically significant words
**Timeline:** 3 months (research 3 weeks, experiments 3 weeks, production 10 weeks)

### Research Phase (Week 1-3)

**Research Questions:**
1. How to access academic journals without subscriptions? (open access, .edu sites)
2. How to use cross-reference codes (BDAG, TDNT, Louw-Nida) for discovery?
3. Which words qualify as "theologically significant"?
4. How to distinguish peer-reviewed from blog posts?
5. What constitutes "scholarly insight" vs. "opinion"?

**Research Outputs:**
- `/02-scholarly-analysis/research/journal-access.md`
  - Open access journals (Google Scholar, DOAJ)
  - .edu site search strategies
  - PDF preprint sources (ResearchGate, Academia.edu)
  - Seminary faculty publication pages

- `/02-scholarly-analysis/research/cross-ref-usage.md`
  - How to search by BDAG codes: `"BDAG {code}"`
  - How to search by TDNT references: `"TDNT {reference}"`
  - How to search by Louw-Nida domains: `"Louw-Nida {domain}"`
  - Why academic papers cite these systems

- `/02-scholarly-analysis/research/authority-ranking.md`
  - Peer-reviewed journals: HIGH authority
  - Seminary faculty papers: HIGH authority
  - Conference proceedings: HIGH authority
  - Thesis/dissertations: MEDIUM-HIGH authority
  - Blog posts by scholars: MEDIUM authority (separate tool)

**Subagent Strategy:**
```
Main Agent: Orchestrate scholarly research
├── Subagent 1: Journal Searcher (PARALLEL)
│   └── Google Scholar search: "{word} OR Strong's {num}"
│       Filter: peer-reviewed, .pdf available
│       Extract: theological insights, scholarly debates
│
├── Subagent 2: .edu Site Crawler (PARALLEL)
│   └── Search: site:.edu "{transliteration} biblical"
│       Extract: seminary papers, course materials
│       Verify: academic affiliation
│
├── Subagent 3: Cross-Reference Searcher (PARALLEL)
│   └── If base file has BDAG/TDNT/Louw-Nida codes:
│       Search: "BDAG {code}" OR "TDNT {ref}" OR "Louw-Nida {domain}"
│       Extract: scholarly articles citing these systems
│
└── Subagent 4: PDF Scanner (PARALLEL)
    └── Search: "{word} New Testament" filetype:pdf
        Extract: preprints, thesis excerpts
        Verify: academic credentials

Main Agent: Synthesize into scholarly-analysis.yaml
├── Theological significance: Why this word matters
├── Scholarly debates: Document divergent views with evidence
├── Cultural context: Historical/social background
└── Diachronic development: Classical → Koine → Modern shifts
```

### Experimentation Phase (Week 4-6)

**Experiment 1: Theologically Central Word (G26 - ἀγάπη)**
- **Why:** Core NT concept, extensive scholarship, known debates
- **Focus:** Can we find sufficient peer-reviewed sources? Theological significance clear?
- **Output:** `/02-scholarly-analysis/experiments/exp1-theological-word/G26-output.yaml`
- **Validation:** 5+ scholarly sources cited? Theological significance explained?

**Experiment 2: Controversial Interpretation (G3056 - λόγος)**
- **Why:** Multiple theological interpretations (word, reason, Logos/Christ)
- **Focus:** Document scholarly debates fairly, represent multiple views
- **Output:** `/02-scholarly-analysis/experiments/exp2-controversial/G3056-output.yaml`
- **Validation:** Multiple scholarly views documented? Evidence for each view?

**Experiment 3: Cultural Context Word**
- **Select:** Word with significant cultural background (e.g., tax collector, Pharisee)
- **Focus:** Extract cultural/historical context from scholarly sources
- **Output:** `/02-scholarly-analysis/experiments/exp3-cultural/GXXXX-output.yaml`
- **Validation:** Cultural context explained? Historical background documented?

**Learnings Document:**
- `/02-scholarly-analysis/experiments/LEARNINGS.md`
- Capture: How to find peer-reviewed sources? How to handle paywalls? Cross-ref success rate?

### Schema Design

**Output File:** `./bible/words/strongs/{num}/{num}-scholarly-analysis.yaml`

```yaml
# === METADATA ===
strongs_number: "{number}"
tool:
  name: "strongs-scholarly-analysis"
  version: "1.0.0"
  generated_date: "YYYY-MM-DD"

# === THEOLOGICAL SIGNIFICANCE (peer-reviewed sources) ===
theological_significance:
  importance_level: "{central|significant|moderate|minimal}"
  key_themes:
    - theme: "{theological concept}"
      explanation: "{how word relates}" {journal-citation}
      biblical_foundation: "{key verses}" {llm-cs45}
  doctrinal_relevance:
    - doctrine: "{doctrine name}"
      role: "{word's role in doctrine}" {peer-reviewed-source}

# === SCHOLARLY DEBATES (peer-reviewed) ===
scholarly_debates:
  - debate_topic: "{specific question or controversy}"
    view_1:
      position: "{first scholarly view}"
      proponents: ["{Scholar A}", "{Scholar B}"]
      sources: ["{journal-citation}", "{book-citation}"]
      evidence: "{arguments/evidence}" {source}
    view_2:
      position: "{second scholarly view}"
      proponents: ["{Scholar C}"]
      sources: ["{journal-citation}"]
      evidence: "{arguments/evidence}" {source}
    consensus_status: "{no-consensus|emerging-consensus|settled}"

# === CULTURAL & HISTORICAL CONTEXT (scholarly sources) ===
cultural_context:
  historical_period: "{1st century Palestine, Greco-Roman world, etc.}"
  social_context: "{social practices, customs}" {scholarly-source}
  cultural_significance: "{why culturally important}" {scholarly-source}
  biblical_era_usage: "{how used in biblical times}" {archaeological-source}

# === DIACHRONIC DEVELOPMENT (scholarly analysis) ===
diachronic_analysis:
  classical_usage:
    period: "Classical Greek (5th-4th century BCE)"
    meaning: "{classical meaning}" {lsj} {scholarly-article}
    sources: "Homer, Plato, Aristotle, etc."

  koine_usage:
    period: "Koine Greek (3rd BCE - 3rd CE)"
    meaning: "{NT meaning}" {thayer} {scholarly-article}
    semantic_shift: "{how meaning changed}" {scholarly-analysis}

  modern_usage:
    period: "Modern Greek"
    meaning: "{modern meaning}" {scholarly-source}
    continuity: "{preserved or shifted?}" {llm-cs45}

# === SCHOLARLY INSIGHTS (specific observations) ===
scholarly_insights:
  - insight: "{specific scholarly observation}"
    source: {journal-citation}
    significance: "{why this matters}" {llm-cs45}
    field: "{NT studies, linguistics, theology, etc.}"

# === INTERTEXTUAL CONNECTIONS (scholarly work) ===
intertextual_connections:
  old_testament:
    - connection: "{how word relates to OT concept}"
      hebrew_equivalent: "{Hebrew word}" {Strong's H####}
      scholarly_source: {citation}

  greco_roman_literature:
    - parallel: "{usage in classical literature}"
      author: "{Plato, Josephus, etc.}"
      scholarly_analysis: {citation}

# === QUALITY METADATA ===
metadata:
  authority_level: "HIGH"
  source_types:
    - peer_reviewed_journals: {count}
    - academic_books: {count}
    - seminary_papers: {count}
  cross_references_used: [bdag, tdnt, louw_nida]
  requires_human_review: false
  tokens_used: {count}
```

### Validation Phase

**Quality Checklist:**

**Level 1: CRITICAL**
- [ ] All sources are peer-reviewed or equivalent academic authority
- [ ] Inline citations for every claim
- [ ] No LLM-generated theology (must cite scholars)
- [ ] Scholarly debates present both sides fairly

**Level 2: HIGH PRIORITY**
- [ ] Theological significance explained (not just asserted)
- [ ] Cultural context documented from scholarly sources
- [ ] Diachronic analysis when Classical→Koine shift documented
- [ ] At least 3 scholarly sources per word

**Production Phase:**
- Priority: Theologically central words first (love, grace, sin, salvation, etc.)
- Target: ~1,000 words
- Timeline: 10 weeks (100 words/week)

---

## Tool 3: strongs-web-insights (MEDIUM AUTHORITY)

### Overview
**Purpose:** Modern insights and practical applications from expert sources
**Authority:** MEDIUM - Expert blogs, structured sites (clearly marked)
**Target Coverage:** ~2,000 words with good web resources
**Timeline:** 2 months (research 2 weeks, experiments 2 weeks, production 4 weeks)

### Research Phase

**Research Questions:**
1. How to distinguish expert blogs from amateur?
2. Which websites have consistently reliable word studies?
3. How to mark authority levels clearly?
4. What qualifies as "practical application" vs. speculation?

**Research Outputs:**
- `/03-web-insights/research/expert-blog-inventory.md`
  - Vetted blogs: credentials, track record, citations
  - Sites: WordStudyTools, GotQuestions, etc.

- `/03-web-insights/research/authority-detection.md`
  - Credentials: seminary degree, published works
  - Citation patterns: does author cite sources?
  - Red flags: unsupported claims, no credentials

### Schema Design

**Output File:** `./bible/words/strongs/{num}/{num}-web-insights.yaml`

```yaml
strongs_number: "{number}"
tool:
  name: "strongs-web-insights"
  version: "1.0.0"

# === MODERN INSIGHTS (expert web sources) ===
modern_insights:
  - insight: "{modern perspective on word}"
    source: {blog-url}
    author: "{name}"
    credentials: "{seminary degree, published books}"
    authority_note: "MEDIUM - expert blog, not peer-reviewed"

# === PRACTICAL APPLICATIONS ===
practical_applications:
  for_translators:
    - application: "{translation guidance}"
      source: {url}
      authority: "MEDIUM"

  for_preachers:
    - application: "{sermon illustration or teaching point}"
      source: {url}
      authority: "MEDIUM"

metadata:
  authority_level: "MEDIUM"
  source_types:
    - expert_blogs: {count}
    - word_study_sites: {count}
```

---

## Tool 4: strongs-community-discussions (LOW AUTHORITY)

### Overview
**Purpose:** Document common questions, misconceptions, and controversies
**Authority:** LOW - Community sources (Stack Exchange, forums)
**Target Coverage:** ~500 words with known controversies or common questions
**Timeline:** 1.5 months (research 2 weeks, experiments 2 weeks, production 3 weeks)

### Research Phase

**Research Questions:**
1. What are the most common misconceptions about biblical words?
2. How to find scholarly refutations of popular errors?
3. How to document controversy patterns?

**Research Outputs:**
- `/04-community-discussions/research/controversy-patterns.md`
  - Types of errors: etymological fallacies, anachronisms, false cognates
  - Detection patterns: "X means Y in English therefore..."

- `/04-community-discussions/research/refutation-sources.md`
  - Where to find scholarly corrections
  - How to document error + refutation + evidence

### Experimentation Phase

**Experiment 1: Known Controversy (G1411 - δύναμις/dynamite)**
- **Why:** Well-documented false etymology
- **Focus:** Can we find error, refutation, and evidence?
- **Expected:** Error: "dunamis = dynamite", Refutation: etymological fallacy, Evidence: dynamite invented 1867

### Schema Design

**Output File:** `./bible/words/strongs/{num}/{num}-community-discussions.yaml`

```yaml
strongs_number: "{number}"
tool:
  name: "strongs-community-discussions"
  version: "1.0.0"

# === CONTROVERSIES & MISCONCEPTIONS ===
controversies:
  - type: "{misconception|scholarly_debate|popular_error}"
    claim: "{the controversial claim}"
    prevalence: "{widespread|moderate|uncommon}"
    source_of_error: "{Stack Exchange, common teaching}"
    authority_note: "LOW - community discussion"

    scholarly_refutation:
      correction: "{what's actually true}"
      source: {scholarly-article or expert-blog}
      evidence: "{why correction is accurate}"
      authority_note: "HIGH/MEDIUM - scholarly source"

    error_type: "{etymological_fallacy|anachronism|false_cognate}"

# === COMMON QUESTIONS ===
common_questions:
  - question: "{frequently asked question}"
    source: "{Stack Exchange discussion URL}"
    answers:
      - answer: "{community answer}"
        votes: {count}
        authority: "LOW - community"
      - expert_answer: "{scholarly response if available}"
        source: {citation}
        authority: "HIGH/MEDIUM"

metadata:
  authority_level: "LOW"
  purpose: "Document controversies and common errors"
  requires_human_review: true
```

---

## Tool 5: strongs-relationships (CROSS-CUTTING VALUE)

### Overview
**Purpose:** Document related words, synonyms, semantic domains
**Authority:** Mixed (mark per source)
**Target Coverage:** All 14,197 words (relationships vary by word)
**Timeline:** 2 months (research 2 weeks, experiments 2 weeks, production 6 weeks)

### Research Phase

**Research Questions:**
1. Where to find synonym data? (Trench's, TDNT, lexicon notes)
2. How to document meaningful distinctions? (not just "synonyms")
3. What semantic domain systems exist? (Louw-Nida, SDBH)

**Research Outputs:**
- `/05-relationships/research/synonym-sources.md`
  - Trench's "Synonyms of the NT" (accessible via BLB)
  - TDNT word groups (theological dictionary)
  - Lexicon cross-references

- `/05-relationships/research/semantic-domain-systems.md`
  - Louw-Nida: Greek semantic domains (expensive, sometimes cited)
  - SDBH: Hebrew semantic domains (UBS project)
  - BibleHub topical analysis

### Experimentation Phase

**Experiment 1: Love Word Family**
- **Words:** G25 (agapaō), G26 (agapē), G5368 (phileō), G5373 (philia)
- **Focus:** Can we document meaningful distinctions?
- **Expected:** Clear differences between divine love vs. friendship love

### Schema Design

**Output File:** `./bible/words/strongs/{num}/{num}-relationships.yaml`

```yaml
strongs_number: "{number}"
tool:
  name: "strongs-relationships"
  version: "1.0.0"

# === SYNONYM ANALYSIS ===
synonyms:
  - word: "{related Greek/Hebrew word}"
    strongs: "{number}"
    gloss: "{English gloss}"
    distinction: "{how meanings differ}" {trench} {tdnt} {biblehub}
    usage_contrast: "{when to use each}" {llm-cs45}
    authority_note: "HIGH - Trench's Synonyms"

# === RELATED WORDS ===
related_words:
  - relationship_type: "{root|derived|compound|antonym}"
    word: "{related word}"
    strongs: "{number}"
    connection: "{how related}" {lexicon-source}

# === SEMANTIC DOMAINS ===
semantic_domains:
  - system: "{louw_nida|sdbh|biblehub_topical}"
    domain_code: "{code}"
    domain_name: "{domain name}"
    related_words_in_domain: ["{Strong's numbers}"]
    authority_note: "{HIGH|MEDIUM based on system}"

metadata:
  authority_level: "MIXED"
  synonym_count: {count}
  semantic_domains_count: {count}
```

---

## Tool 6: strongs-translation-patterns (INNOVATIVE!)

### Overview
**Purpose:** Extract cross-linguistic translation patterns from 900+ translations (TBTA approach)
**Authority:** EMPIRICAL - Based on actual translation data
**Target Coverage:** Top 300 high-frequency words (diminishing returns after that)
**Timeline:** 4 months (research 4 weeks, experiments 4 weeks, production 8 weeks)

### Research Phase (CRITICAL - This is the innovative part)

**Research Questions:**
1. How to access eBible corpus? (github.com/BibleNLP/ebible)
2. How to extract linguistic features from translations?
3. How to calculate confidence scores?
4. Which words benefit most? (pronouns, demonstratives, particles)
5. What's the minimum evidence threshold? (need 5+ languages agreeing)

**Research Outputs:**
- `/06-translation-patterns/research/corpus-access.md`
  - eBible corpus structure
  - How to map Strong's numbers to translation words
  - Data format and parsing

- `/06-translation-patterns/research/feature-extraction.md`
  - Clusivity: How to detect inclusive/exclusive in translations?
  - Proximity: How to identify demonstrative distance markers?
  - Number: How to detect dual/trial number?
  - Method: Compare translations with known linguistic features

- `/06-translation-patterns/research/confidence-scoring.md`
  - Formula: agreement_count / total_languages_checked
  - Thresholds: 0.95+ = high confidence, 0.70-0.94 = moderate, <0.70 = low
  - Minimum: Need 5+ languages to establish pattern

**Subagent Strategy:**
```
Main Agent: Orchestrate corpus analysis for one Strong's number
├── Subagent 1: Clusivity Analyzer (PARALLEL)
│   └── For pronouns (we, you-plural):
│       Load all verses with this Strong's number
│       Check Austronesian languages (5+): Tagalog, Malay, Fijian, etc.
│       Identify: "kami" (exclusive) vs "tayo" (inclusive) patterns
│       Group by context: divine speech, church unity, etc.
│       Calculate confidence: agreement_rate
│
├── Subagent 2: Proximity Analyzer (PARALLEL)
│   └── For demonstratives (this, that):
│       Check Japanese: これ (near speaker), それ (near listener), あれ (far)
│       Check Spanish: este, ese, aquel
│       Identify distance patterns
│       Calculate confidence
│
├── Subagent 3: Number System Analyzer (PARALLEL)
│   └── For pronouns with ambiguous number:
│       Check Hawaiian: lākou (trial = 3 persons)
│       Check Samoan: lāua (dual = 2 persons)
│       Identify rare number patterns
│       Calculate confidence
│
├── Subagent 4: Polarity Analyzer (PARALLEL)
│   └── For particles:
│       Check negative markers across languages
│       Identify systematic polarity patterns
│
├── Subagent 5: Lexical Sense Analyzer (PARALLEL)
│   └── For polysemous words:
│       Check which sense is translated in which context
│       Group translations by semantic sense
│       Calculate confidence per sense
│
└── Subagent 6: Surface Realization Analyzer (PARALLEL)
    └── For pronouns:
        Check pro-drop languages (Spanish, Japanese)
        Identify when pronoun is dropped vs. expressed
        Document patterns

Main Agent: Synthesize into translation-patterns.yaml
├── Combine evidence from all features
├── Calculate overall confidence scores
├── Document contexts where patterns apply
└── Flag ambiguous cases (low agreement)
```

### Experimentation Phase (CRITICAL)

**Experiment 1: Clusivity (G2249 - ἡμεῖς "we")**
- **Why:** Known clusivity patterns in Tagalog, Malay, Fijian
- **Expected Patterns:**
  - Genesis 1:26 "Let us make man" → Tagalog "kami" (exclusive - Trinity members only)
  - 1 Cor 12:13 "we all" → Tagalog "tayo" (inclusive - all believers)
- **Success Criteria:** Can we detect these patterns? Confidence scores >0.90?
- **Output:** `/06-translation-patterns/experiments/exp1-clusivity/G2249-output.yaml`

**Experiment 2: Proximity (G3778 - οὗτος "this")**
- **Why:** Demonstrative with known distance marking in Japanese, Spanish
- **Expected Patterns:**
  - Near speaker: Japanese これ (kore), Spanish este
  - Near listener: Japanese それ (sore), Spanish ese
  - Far from both: Japanese あれ (are), Spanish aquel
- **Success Criteria:** Can we map distance patterns? Consistent across languages?
- **Output:** `/06-translation-patterns/experiments/exp2-proximity/G3778-output.yaml`

**Experiment 3: Trial Number (Trinity references)**
- **Why:** Hawaiian uses "lākou" (trial = exactly 3 persons) for Genesis 1:26
- **Expected Pattern:** Trinity references → trial number in Hawaiian
- **Success Criteria:** Can we detect this rare feature? Is it systematic?
- **Output:** `/06-translation-patterns/experiments/exp3-number-system/trial-output.yaml`

**Validation Strategy:**
- Cross-check patterns across language families
- Verify with linguistic literature (do patterns match known typology?)
- Test on held-out verses (patterns should generalize)

### Schema Design

**Output File:** `./bible/words/strongs/{num}/{num}-translation-patterns.yaml`

```yaml
strongs_number: "{number}"
tool:
  name: "strongs-translation-patterns"
  version: "1.0.0"

# === TBTA HINTS (cross-linguistic patterns) ===
tbta_hints:
  # Feature: Clusivity (for pronouns)
  clusivity:
    - context: "{when this pattern applies}"
      pattern: "{convergence description}"
      evidence:
        languages_checked: [tgl, msa, fij, ...]  # ISO 639-3 codes
        agreement_count: 5
        total_count: 5
      examples:
        - lang: "tgl"  # Tagalog
          word: "kami"
          meaning: "exclusive (speaker + others, not listener)"
          verses: ["GEN.1.26", "ACT.15.25"]
        - lang: "msa"  # Malay
          word: "kami"
          meaning: "exclusive"
      confidence: 0.98
      interpretation: "Very high confidence - strong cross-linguistic agreement"

  # Feature: Proximity (for demonstratives)
  proximity:
    - distance: "{near_speaker|near_listener|far_from_both}"
      pattern: "{description}"
      evidence:
        languages_checked: [jpn, spa, ...]
        agreement_count: 8
        total_count: 10
      examples:
        - lang: "jpn"  # Japanese
          word: "これ"
          romanization: "kore"
          meaning: "near speaker"
        - lang: "spa"  # Spanish
          word: "este"
          meaning: "near speaker"
      confidence: 0.85

  # Feature: Number System
  number_system:
    - number: "{dual|trial|paucal}"
      context: "{when this applies}"
      evidence:
        languages_checked: [haw, ...]
        pattern: "Hawaiian uses trial number for Trinity references"
      examples:
        - lang: "haw"  # Hawaiian
          word: "lākou"
          meaning: "exactly 3 persons (trial)"
          verses: ["GEN.1.26"]
      confidence: 0.95
      rarity_note: "Trial number is rare; well-documented in Hawaiian"

# === LINGUISTIC FEATURE SUMMARY ===
linguistic_features:
  person: "{1st|2nd|3rd|4th (obviative)}"
  number: "{singular|dual|trial|plural}"
  clusivity: "{inclusive|exclusive|neutral|ambiguous}"
  proximity: "{proximal|medial|distal|multi_way}"
  polarity: "{affirmative|negative}"
  lexical_sense: "{primary|secondary|contextual}"
  surface_realization: "{pronoun|zero_anaphora|clitic}"

# === TRANSLATION GUIDANCE ===
translation_guidance:
  for_translators:
    - feature: "clusivity"
      guidance: |
        When translating to languages with inclusive/exclusive distinction:
        - Divine speech (Trinity) → exclusive (kami/kami/keirau)
        - Church unity passages → inclusive (tayo/kita)
      confidence: "HIGH"
      evidence_summary: "5/5 Austronesian languages agree"

# === QUALITY METADATA ===
metadata:
  authority_level: "EMPIRICAL"
  corpus_source: "eBible (900+ translations)"
  languages_analyzed: {count}
  patterns_found: {count}
  confidence_score_average: {float}
  focus_note: "Top 300 high-frequency words only (diminishing returns)"
```

### Production Phase

**Priority:**
1. **Top 50 pronouns** (Week 1-4) - Highest variation, clearest patterns
   - he/she/it, we, you, this, that
2. **Demonstratives** (Week 5-6) - Proximity patterns
3. **Top 150 particles and verbs** (Week 7-12)
4. **Top 100 nouns with special features** (Week 13-16)

**Validation:**
- Linguistic expert review for top 50 words
- Cross-check with typological literature
- Test pattern predictions on held-out verses

---

## Tool 7: strongs-specialized-linguistics (ADVANCED)

### Overview
**Purpose:** Deep linguistic research (LXX, papyri, classical literature, cognates)
**Authority:** HIGH - Scholarly linguistic sources
**Target Coverage:** ~200 complex words needing advanced analysis
**Timeline:** 3 months (research 3 weeks, experiments 3 weeks, production 9 weeks)

### Research Phase

**Research Questions:**
1. How to access LXX data? (Septuagint tools, databases)
2. Where are papyri attestations? (Duke Databank, etc.)
3. How to search classical literature? (Perseus, TLG)
4. Which cognate databases exist? (CAL for Aramaic, etc.)

**Research Outputs:**
- `/07-specialized-linguistics/research/lxx-tools.md`
  - CCAT/CATSS Parallel Hebrew-Greek database
  - How to trace Hebrew → Greek → NT usage

- `/07-specialized-linguistics/research/papyri-databases.md`
  - Duke Databank of Documentary Papyri (DDBDP)
  - Vocabulary of Greek NT (Moulton-Milligan) - on StudyLight

- `/07-specialized-linguistics/research/classical-access.md`
  - Perseus Digital Library
  - LSJ usage in classical authors

- `/07-specialized-linguistics/research/cognate-databases.md`
  - Comprehensive Aramaic Lexicon (CAL) - free online
  - Akkadian, Ugaritic resources

### Experimentation Phase

**Experiment 1: LXX Semantic Shift**
- **Select:** Word with known Classical → LXX → NT semantic development
- **Focus:** Can we trace the semantic journey?
- **Output:** Document Classical usage → LXX rendering → NT interpretation

### Schema Design

**Output File:** `./bible/words/strongs/{num}/{num}-specialized-linguistics.yaml`

```yaml
strongs_number: "{number}"
tool:
  name: "strongs-specialized-linguistics"
  version: "1.0.0"

# === LXX CONNECTIONS (for NT Greek words) ===
lxx_connections:
  hebrew_source:
    - hebrew_word: "{Hebrew word}"
      strongs_hebrew: "H####"
      lxx_translation: "{this Greek word}"
      frequency: "{how often LXX uses this translation}"
      semantic_transfer: "{meaning shift from Hebrew to Greek}" {llm-cs45 citing scholarly-source}

  contextual_influence:
    note: "{how LXX usage influenced NT writers}" {scholarly-source}

# === PAPYRI ATTESTATIONS ===
papyri_attestations:
  everyday_usage:
    - source: "{papyri reference}"
      date: "{century}"
      context: "{business document, personal letter, etc.}"
      meaning: "{how used in non-literary context}" {moulton-milligan}
  significance: "{shows word wasn't just literary}" {llm-cs45}

# === CLASSICAL LITERATURE ===
classical_usage:
  authors:
    - author: "{Homer, Plato, Aristotle, etc.}"
      work: "{specific work}"
      meaning: "{classical meaning}" {lsj}
      reference: "{book/line citation}"
  semantic_shift_to_koine: "{how meaning changed}" {scholarly-analysis}

# === COGNATE DATA (for Hebrew words) ===
cognate_data:
  aramaic:
    - word: "{Aramaic cognate}"
      source: "CAL (Comprehensive Aramaic Lexicon)"
      meaning: "{Aramaic meaning}"
      connection: "{semantic relationship}" {llm-cs45}

  akkadian:
    - word: "{Akkadian cognate}"
      meaning: "{Akkadian meaning}"
      scholarly_source: {citation}

metadata:
  authority_level: "HIGH"
  specialized_research: true
  requires_expert_review: true
```

---

## Cross-Tool Dependencies

### Execution Order

**Phase 1: Foundation (Parallel)**
- Tool 1: strongs-lexicon-core (all 14,197 words)
- Tool 5: strongs-relationships (can run in parallel)

**Phase 2: Enrichment (After Phase 1)**
- Tool 2: strongs-scholarly-analysis (~1,000 theological words)
- Tool 6: strongs-translation-patterns (top 300 high-frequency words)
- Tool 7: strongs-specialized-linguistics (~200 complex words)

**Phase 3: Supplementary (After Phase 2)**
- Tool 3: strongs-web-insights (~2,000 words)
- Tool 4: strongs-community-discussions (~500 words with controversies)

### Data Flow

```
Base Strong's File (pre-existing)
    ↓
Tool 1: Lexicon Core (foundation for all)
    ↓
    ├→ Tool 2: Scholarly Analysis (uses lexicon + cross-ref codes)
    ├→ Tool 3: Web Insights (builds on lexicon)
    ├→ Tool 4: Community (identifies gaps in lexicon)
    ├→ Tool 5: Relationships (uses lexicon data)
    ├→ Tool 6: Translation Patterns (uses Strong's number as key)
    └→ Tool 7: Specialized (deep dive on lexicon findings)
```

---

## Success Metrics

### Overall Project Success

**Coverage:**
- Tool 1 (Lexicon Core): 14,197/14,197 words (100%)
- Tool 2 (Scholarly): 1,000+ theologically significant words
- Tool 3 (Web Insights): 2,000+ words with good web resources
- Tool 4 (Community): 500+ words with controversies
- Tool 5 (Relationships): 14,197/14,197 words (varies in detail)
- Tool 6 (Translation Patterns): 300 high-frequency words
- Tool 7 (Specialized): 200 complex words

**Quality:**
- Level 1 validation: 95%+ pass rate (no fabrication, inline citations)
- Level 2 validation: 80%+ pass rate (comprehensive data)
- Fair use compliance: 100% (convergence grouping, inline citations)

**Timeline:**
- Phase 1 (Foundation): 3 months
- Phase 2 (Enrichment): 4 months (parallel execution)
- Phase 3 (Supplementary): 2 months (parallel execution)
- **Total: 9 months**

**Authority Distribution:**
- HIGH authority sources: Tools 1, 2, 7
- MEDIUM authority: Tool 3
- LOW authority: Tool 4
- EMPIRICAL: Tool 6
- MIXED: Tool 5

---

## Next Steps

1. **Create directory structure** (Week 1)
   - Set up all 7 tool directories with research/experiments/validation subdirs

2. **Start with Tool 1 research phase** (Week 1-2)
   - Deep dive into lexicon sources
   - Document extraction methodology
   - Design schema

3. **Tool 1 experimentation** (Week 3-4)
   - Run 5 experiments (high-freq, medium-freq, rare, Hebrew, word family)
   - Capture learnings

4. **Tool 1 validation and production start** (Week 5+)
   - Validate experiments
   - Begin batch processing

5. **Initiate Tool 5 research in parallel** (Week 3)
   - Can run alongside Tool 1 production

6. **Sequential tool development** following dependency chain

---

**Key Success Factor:** Follow the TBTA pattern - deep research, systematic experimentation, validation before production, capture learnings throughout.
