# Stage 1: Research & Definition

**Role**: Researcher / Linguist / Theologian
**Input**: Feature Name (e.g., "Number", "Allocution", "Mood")
**Output**:

NOTE: the relative directory is /bible-study-tools/tbta/features/{feature}/
NOTE: the TBTA-DIR is /bible-study-tools/tbta/

- `features/{feature}/README.md` (Overview)
- `features/{feature}/research/README.md` (Deep Dive Findings)
- `features/{feature}/research/{one-per-section}.md`

## Goal

Do extensive research (50 sources) into this linguistic feature. Define the feature comprehensively. You are not just copying TBTA docs; you are synthesizing linguistic typology, theological doctrine, and translation theory to guide the algorithm. You are laying the foundation for the data scientists.

## Out of Scope

- You are _not_ writing any scripts or computing frequencies, that belongs to the Analysis. You _are_ doing the foundational background research to prepare for the analysis stage.
- You are _not_ designing experiments or validating results. You are _not_ predicting the feature yet. You _are_ preparing all the background research to inform future experiments.

## Execution Strategy

**Use Subagents Proactively**:

- Assign subagents to run in parallel for each section: ex (TBTA Review, Language Analysis, Theological Research, etc)
- Then Synthesize findings into the final deliverables.

## Tasks



### 1. TBTA Documentation Review (The "What")

IMPORTANT: Do not guess, cite every detail you extract to it's source document. Prefer "Not listed" as an answer over hallucinations/guesses or unconfident answers

**Location**: `research/TBTA.md`
**Source**: `TBTA-DIR/tbta-source/*` (review all files), `https://github.com/AllTheWord/tbta_db_export`, 
**Action**:

- **Define the Concept**: What is this feature conceptually? (e.g., Number = count of entities)
- **List Values**: Exactly what values does TBTA support? (e.g., Singular, Dual, Trial...)
- **Identify Constraints**: What "Gateway Features" control this? (e.g., Mood → Aspect)
  - **Definition**: A "Gateway Feature" is a controlling grammatical category (like Part of Speech, Mood, or Sentence Type) that determines if a sub-feature is valid. (e.g., 'Aspect' is only relevant if 'Mood' is Indicative; 'Case' is only relevant if 'Part of Speech' is Noun).
- **Document Policy**: How does TBTA label this?
  - **Semantic vs Morphological**: Does TBTA prioritize semantic meaning over morphological form? (e.g., Hebrew dual morphology → Singular if semantically one entity)
  - **Part-of-Speech Rules**: Do pronouns vs nouns follow different logic? (e.g., pronouns follow morphology, nouns follow semantics)
- **Past Learnings**: What has TBTA learnt about this feature already (consider changes in policy, best practices in their docs or our docs about them)
- **Edge Cases**: What are the edge cases, how are they handled?
- **Value Inventory**: List all possible values from TBTA documentation (not frequency - that's Stage 2)
  - **Theoretical vs Productive**: Note which values are documented but may be rare (from linguistic literature, not data analysis)
  - **Rare Value Discovery**: Note potential rare values mentioned in linguistic literature (do not attempt to calculate frequencies yet)
- **Mixed Annotations**: Can constituents receive multiple values simultaneously? (e.g., Degree allows "Intensified" + "'too'")
  - **Note**: Some features commonly use mixed annotations (20+ instances per 100 verses), not just edge cases

### 2. Language Family & Typology Analysis (The "Who")

**Location**: `research/LANGUAGES.md`
**Source**: `TBTA-DIR/languages/`, WALS, Grambank
**Action**:

- **CRITICAL: Source Language Encoding Check**: Is this feature EXPLICITLY encoded in Hebrew/Greek morphology? (e.g., Number is marked morphologically, Clusivity is NOT)
- **Identify Required Families**: List specific families (e.g., "Austronesian", "Bantu") that _grammatically require_ this feature.
- **Analyze Available Languages**: Do an analysis of which languages we have translations for (check `/src/constants/languages.tsv` and classify the feature's necessity in the target languages: is it Mandatory, Optional; (for Absent ignore those languages to save output tokens)  NOTE if a language is mentioned in your/our cited research use that; otherwise user your internal knowledge and mark it as (unverified) to bypass the no hullucination rule.(omit all languages that don't have this feature).
  - **Typological Classification**: For your selected control languages, classify the feature's status:
    - **Mandatory**: The language MUST mark this feature (e.g., Gender in Spanish).
    - **Optional**: The language CAN mark it but it's not required.
    - **Absent**: The language does not use this feature.
- **Determine Distinctions Between these Languages about this Feature**: Must determine which languages use this feature, unique needs between them (use (ISO-639-3) for language codes)
- **Identify Root Languages**: Which major Bible translation languages (Greek, Hebrew, Latin, English, Spanish, German, French, Arabic, Indonesian, Swahili) have this feature?  A root language is a language translators often start with with priority to Hebrew, Greek but often smaller languages begin with the parent langauge of their greater region.
- **Select Candidates**: Propose 5-10 languages for the Translation Database (Stage 2) based on this analysis and why you chose them. 
  - _Criteria_: Mix of marking vs. non-marking, diverse families, from list
- **Cultural Nuances**: Note any honorifics, taboos, or social distinctives.

### 3. Scholarly Research (The Deep Dive)

**Location**: `research/SCHOLARLY.md`
**Source**: Google Scholar, WALS, Grambank, Reputable linguistic databases, academic websites, translation resources. Avoid forums, blogs, or unverified content. All web sources must be cited with URLs..

**TEMPLATE for SCHOLARLY.md**:

```markdown
# Research: [Feature Name]

## Executive Summary

[Brief summary of linguistic typologies and theological challenges. e.g., "Number systems vary from 2-way (singular/plural) to 5-way. Theological challenges arise in Trinitarian contexts..."]

## 1. Scholarly Sources

### [Author Name] ([Year]). _[Title]_

- **Key Findings**: [Bullet points of relevant linguistic rules]
- **Citation Code**: {author-year-keyword}
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

- **Scholarly Sources**: Cite standard references (Corbett, Comrie, etc.). (min 25)
- **Typological Databases**: Reference WALS feature numbers or Grambank IDs.
- **Translation Case Studies**: Find 2-3 real examples of how this feature is handled in translation (e.g., "How Fijian handles Gen 1:26").
- **Verse Analysis**: Identify key biblical verses where this feature is critical.

### 4. Arbitrarity Classification (The Theological Core)

**Source**: Theological analysis, Commentaries
**Output**: `research/THEOLOGICALLY-SIGNIFICANT-GROUPS.md`
**CRITICAL**: This classification determines which contexts require 100% accuracy (non-arbitrary) vs acceptable uncertainty (arbitrary).

You need to discover if this feature is arbitrary (any value could be picked) or non-arbitrary. More specifically you need to discover the different severities of arbitrary

1a. Non-Arbitrary-Theological - If you get it wrong the translation may lead to heresy, ex. Trinity
1b. Non-Arbitrary-Contextual - If you get it wrong it will confuse the reader (Paul and Silas where speaking. They (5 people) said... (that is wrong b/c in context we know it was 2 people)). This would have readers question the accuracy of the translation
2. Arbitrary - It doesn't matter what you pick

We want to guess all the non-arbitrary reason codes. To do that use your internal memory of Scripture and infer (the rules about non-hallucination do not apply here) which verses would have this feature and group them together into similar types so that all the non-arbitrary reasons can be grouped together to exhaustively cover all edge cases.  In order to use your internal memory you must mark it as (unverified) as it may be hallucinated.

**TEMPLATE for THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml**:

```yaml
feature: { feature-name }
default_classification: arbitrary # Default: choice is stylistic/optional
theological_significance: EXISTS # Flag: Does this ever matter doctrinally?

# SECTION 1: NON-ARBITRARY (Theologically Critical)
non_arbitrary_contexts:
  - verse_pattern: 'Gen 1:26 (Trinity references) (unverified)'
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


Summarize all the docs in a very concise form (Progressive Disclosure: ≤200 lines see /.claude/skills/progressive-disclosure/SKILL.md) so most AI systems only need to read the README.md and only need to load the details for the fuller explanation.  Don't reproduce all the sections just aggregate into an executive summary then key bullet points.

### 1. `{TBTA-DIR}/features/{feature}/research/README.md`

Max 200 lines

- Summarize what this feature is and it's key values
- Foreach research section above summarize the most important points and link to the file
- Note any discrepencies where sections disagree and note (ex. tbta and research disagree)

### 2. Create `{TBTA-DIR}/features/{feature}/README.md`

Max 75 lines

- **Feature Name & Description**: One sentence summary.
- **Target Audience**: List of language families and most important distinctions between them. link to language research file.
- **Examples**: Provide 3-5 examples of why this matters using actual verses and translations as case study (link to THEOLOGICALLY-SIGNIFICANT-GROUPS.md)
- **TBTA Encoding**: Technical details and link to TBTA file
