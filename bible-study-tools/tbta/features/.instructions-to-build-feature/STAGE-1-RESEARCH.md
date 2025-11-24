# Stage 1: Research & Definition

**Role**: Researcher / Linguist / Theologian
**Input**: Feature Name (e.g., "Number", "Allocution", "Mood")
**Output**:

- `features/{feature}/README.md` (Overview)
- `features/{feature}/RESEARCH.md` (Deep Dive Findings)
- `features/{feature}/ARBITRARITY-CLASSIFICATION.md` (Theological Logic)

## Goal

Define the feature comprehensively. You are not just copying TBTA docs; you are synthesizing linguistic typology, theological doctrine, and translation theory to guide the algorithm. You are laying the foundation for the data scientists.

## Execution Strategy

**Use Subagents Proactively**:

- Assign subagents to run in parallel: TBTA Review, Language Analysis, Theological Research.
- Synthesize findings into the final deliverables.

## Tasks

### 1. TBTA Documentation Review (The "What")

**Location**: `research/tbta/`
**Source**: `../../tbta-source/` (recursively search for `DATA-STRUCTURE.md`, feature lists, etc.)
**Action**:

- **Define the Concept**: What is it conceptually? (e.g., Number = count of entities)
- **List Values**: Exactly what values does TBTA support? (e.g., Singular, Dual, Trial...)
- **Locate Encoding**: Where is it in the JSON? (e.g., Noun Position 2)
- **CRITICAL: Source Language Encoding Check**: Is this feature EXPLICITLY encoded in Hebrew/Greek morphology? (e.g., Number is marked morphologically, Clusivity is NOT)
  - If source-encoded: Can extract from Macula morphology data (Tier 0-1)
  - If not source-encoded: Must predict from other languages/context/theology (Tier 2-3)
  - **Note**: TBTA only covers ~40% of Bible - goal is to PREDICT for entire Bible, not copy existing annotations
- **Identify Constraints**: What "Gateway Features" control this? (e.g., Mood → Aspect)
- **Document Policy**: How does TBTA label this?
  - **Semantic vs Morphological**: Does TBTA prioritize semantic meaning over morphological form? (e.g., Hebrew dual morphology → Singular if semantically one entity)
  - **Part-of-Speech Rules**: Do pronouns vs nouns follow different logic? (e.g., pronouns follow morphology, nouns follow semantics)
- **Value Inventory**: List all possible values from TBTA documentation (not frequency - that's Stage 2)
  - **Theoretical vs Productive**: Note which values are documented but may be rare (from linguistic literature, not data analysis)
  - **Rare Value Discovery**: Values appearing <5% may require 100+ verses to confirm existence (don't assume non-existence from small samples)
- **Mixed Annotations**: Can constituents receive multiple values simultaneously? (e.g., Degree allows "Intensified" + "'too'")
  - **Note**: Some features commonly use mixed annotations (20+ instances per 100 verses), not just edge cases
- **Context Dependency**: Does same construction map to different values based on context? (e.g., Hebrew מִן → Comparative vs 'too' vs 'less')
  - Document specific patterns: construction + context triggers → value mapping
  - Test multiple verses to validate each pattern

### 2. Language Family & Typology Analysis (The "Who")

**Location**: `research/languages/`
**Source**: `../../languages/`, WALS, Grambank
**Action**:

- **Identify Required Families**: List specific families (e.g., "Austronesian", "Bantu") that _grammatically require_ this feature.
- **Determine Which Languages Use This Feature**: Must determine which languages use this feature, unique needs between them
- **Analyze Available Languages**: Do an analysis of which languages we have (check `../../languages/` directory)
- **Identify Control Languages**: Which major languages (English, Spanish) _lack_ this feature?
- **Select Candidates**: Propose 5-10 languages for the Translation Database (Stage 2) based on this analysis.
  - _Criteria_: Mix of marking vs. non-marking, diverse families, accessible via eBible.
  - **Priority**: Languages with EXPLICIT GRAMMATICAL marking of this feature (e.g., clusivity → Tagalog/Indonesian, number systems → Fijian/Slovenian)
  - **Cultural Nuances**: Note any honorifics, taboos, or social distinctives.

### 3. Scholarly Research (The Deep Dive)

**Location**: `research/scholarly/`
**Source**: Google Scholar, WALS, Grambank, General Web
**Output**: `research/scholarly/RESEARCH.md`

**TEMPLATE for RESEARCH.md**:

```markdown
# Research: [Feature Name]

## Executive Summary

[Brief summary of linguistic typologies and theological challenges. e.g., "Number systems vary from 2-way (singular/plural) to 5-way. Theological challenges arise in Trinitarian contexts..."]

## 1. Scholarly Sources

### [Author Name] ([Year]). _[Title]_

- **Key Findings**: [Bullet points of relevant linguistic rules]
- **Citation Code**: {[author-year-keyword]}
- **Relevance**: [Why this matters for our algorithm]

## 2. Typological Databases

### WALS Feature [XX]

- **Values**: [List values tracked by WALS]
- **Implication**: [How this helps us predict target language behavior]

## 3. Translation Case Studies

### [Language Name] ([Family])

- **Feature Handling**: [How they handle this feature]
- **Specific Verse**: [Example verse where this feature is critical]
- **Insight**: [What this teaches us about the "correct" answer]

## 4. Bibliography

[List all sources with citation codes]
```

**Requirements**:

- **Scholarly Sources**: Cite standard references (Corbett, Comrie, etc.).
- **Typological Databases**: Reference WALS feature numbers or Grambank IDs.
- **Translation Case Studies**: Find 2-3 real examples of how this feature is handled in translation (e.g., "How Fijian handles Gen 1:26").
  - **CRITICAL**: Document actual Bible translations (eBible, YouVersion, BibleGateway) - these provide strongest validation
  - **Cross-Linguistic Consensus**: Note where 5-10 languages agree (high confidence) vs disagree (translator choice point)
- **Verse Analysis**: Identify key biblical verses where this feature is critical.
  - **Theological Passages**: Trinity contexts, incarnation, messianic prophecies
  - **Edge Cases**: Ambiguous contexts, rare values, mixed annotations

### 4. Arbitrarity Classification (The Theological Core)

**Source**: Theological analysis, Commentaries, `STAGES.md`
**Output**: `research/ARBITRARITY-CLASSIFICATION.md`

**CRITICAL**: This classification determines which contexts require 100% accuracy (non-arbitrary) vs acceptable uncertainty (arbitrary).

**TEMPLATE for ARBITRARITY-CLASSIFICATION.md**:

```yaml
feature: { feature-name }
default_classification: arbitrary # Default: choice is stylistic/optional
theological_significance: EXISTS # Flag: Does this ever matter doctrinally?

# SECTION 1: NON-ARBITRARY (Theologically Critical)
non_arbitrary_contexts:
  - verse_pattern: 'Gen 1:26 (Trinity references)'
    affected_values: [trial, plural]
    theological_stakes: HIGH
    affected_doctrines:
      - Trinity (nature of God)
      - Creation theology

    # Why is this non-arbitrary?
    non_arbitrary_rationale: |
      Choice affects doctrine. Trial number (exactly 3) encodes Trinity.
      Plural is acceptable but less precise. Dual is HERETICAL (Arianism).

    # What is the Orthodox view?
    christian_orthodox_position:
      preferred_value: trial
      theological_basis: 'God is One Essence, Three Persons.'
      translator_guidance: |
        - Use TRIAL if available.
        - NEVER use Dual (implies only 2 persons).
        - Footnote recommended for Plural.

    # What are the alternatives/heresies?
    non_orthodox_alternatives_awareness:
      - interpretation: 'Divine Council (God + Angels)'
        used_by: [Jewish non-Messianic]
        christian_assessment: REJECTED (Angels do not create)
      - interpretation: 'Polytheism'
        used_by: [Mormon/LDS]
        christian_assessment: HERETICAL (Violates Monotheism)

# SECTION 2: ARBITRARY (Stylistic/Contextual)
arbitrary_contexts:
  - pattern: "Crowd sizes (e.g., 'multitude')"
    rationale: 'Exact count irrelevant to doctrine.'
    estimated_percentage: 85%
```

**Requirement**: Distinguish between _Stylistic_ (Arbitrary) and _Doctrinal_ (Non-Arbitrary) choices.
**Structure**:

- **Non-Arbitrary Contexts**:
  - **Verse Pattern**: e.g., "Gen 1:26 (Trinity)"
  - **Theological Stakes**: High/Medium/Low
  - **Affected Doctrines**: Trinity, Christology, Ethics
  - **Orthodox Position**: What is the Christian orthodox view?
  - **Heresy Warning**: What must be avoided? (e.g., Arianism, Polytheism)
  - **Translator Guidance**: Specific warnings.
- **Arbitrary Contexts**:
  - Patterns where choice doesn't matter (e.g., "Crowd sizes", "Travel companions").
  - Estimated percentage (default ~85%).

## Deliverables

### 1. Edit `features/{feature}/README.md`

(Progressive Disclosure: ≤200 lines)

- **Feature Name & Description**: One sentence summary.
- **Target Audience**: List of language families.
- **Theological Context**: Link to Arbitrarity classification.
- **TBTA Encoding**: Technical details.

### 2. `features/{feature}/research/README.md`

- Comprehensive findings from Task 2 & 3 using the TEMPLATE above.
- Include Executive Summary, Sources, Database links, and Case Studies.

### 3. `features/{feature}/research/ARBITRARITY-CLASSIFICATION.md`

- Structured YAML/Markdown using the TEMPLATE above.
- **Must** include specific verse examples, doctrinal analysis, and denominational considerations.
- **Multi-Answer Format**: For non-arbitrary contexts, document:
  - Preferred value (Christian orthodox position)
  - Alternative values with theological assessment
  - Non-orthodox interpretations (for translator awareness)
  - Translator guidance with specific warnings

### 4. `features/{feature}/research/FEATURE-COMPLEXITY.md` (Optional but Recommended)

- Document feature complexity tier (Tier 0-3) based on source language encoding
- Expected accuracy ranges based on tier
- Data requirements (Macula morphology vs verse text vs discourse context)
- Prediction strategy (morphological extraction vs hierarchical prompts vs multi-factor convergence)
- **Note**: All features require prediction - TBTA coverage is incomplete (~40%), goal is full Bible coverage
