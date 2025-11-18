The following summarizes the correct stages to build a new feature. If you are improving a feature you should validate that it has done all of these stages.

# 1. Research TBTA Documentation

Review the source documentation of TBTA for this feature:
- Official TBTA documentation: See `../tbta-source/README.md` for links to source materials

Generate the README.md for the feature with the information learnt:
- Include: Feature definition, theological/linguistic context, TBTA encoding details
- Add stage checklist (copy from this file)

# 2. Language Study

Review language families to determine which languages need this feature:
- Check: `../languages/` directory
- Reference: Language codes and families
- Consider: Which language families grammatically encode this feature?  Are there any unique cultural distinctives in any language families or languages where they treat this feature differently than others with this feature.  For instance in North America there has grown a sensitivity towards inclusive language so cases where brothers is said but refers to the whole church some would be offended it did not say brothers and sisters.

Update README.md with language analysis:
- List: Language families that require this feature
- Note: Languages where feature is grammatically obligatory vs optional
- Note: Distinct cultural adaptations and unique concerns.
- Example: Target translation scenarios

# 3. Scholarly and Internet Research

- Look for scholarly articles about this subject to get the latest research into it
- Look into general web information
- Update the README

## Identify Arbitrary vs Non-Arbitrary Contexts

**Critical theological requirement**: Not all lexical choices have equal theological weight.

### Classification Criteria

A feature value is **NON-ARBITRARY** (theologically significant) if it affects:
1. **Doctrine** (Trinity, salvation, God's nature, etc.)
2. **Divine speech** (commands, promises, judgments)
3. **Interpretation** (literal vs figurative, resolves theological ambiguity)
4. **Church practice** (authority, worship, ethics)
5. **Denominational differences** (interpretations vary by tradition)

**Default**: Assume ARBITRARY unless proven otherwise

### Required Analysis

Create `experiments/ARBITRARITY-CLASSIFICATION.md`:
```yaml
feature: {feature-name}
default_classification: arbitrary  # Only mark non-arbitrary when significant

non_arbitrary_contexts:
  - verse_pattern: "Gen 1:26 (Trinity references)"
    affected_values: [trial, plural]
    theological_stakes: high
    affected_doctrines: [Trinity, nature of God]
    denominational_implications: true
    cultural_sensitivity: [monotheistic contexts]

  - verse_pattern: "Matt 6:9 (prayer contexts)"
    affected_values: [inclusive, exclusive]
    theological_stakes: medium
    affected_doctrines: [prayer theology, corporate worship]
    denominational_implications: false
    cultural_sensitivity: [individualist vs collectivist]

arbitrary_contexts:
  - pattern: "Crowd sizes, travel narratives"
    rationale: "Theology unchanged by specific number"
    percentage_of_feature: 85%
```

**Key principle**: Space-saving design - only mark non-arbitrary (default=arbitrary not stored)

# 4. Generate Test Set with Translation Data

**CRITICAL**: This stage MUST be done in a subagent to prevent seeing the answers!

**Philosophy**: "There is nothing new under the sun" - with ~1000 Bible translations, someone has already dealt with your unique linguistic feature. Don't just validate against TBTA - **discover answers from what real translators actually did**.

## Dataset Requirements

**Data Source**: Use only verses that have TBTA data (complete annotation)

**Sample Size**: 100 verses per value minimum
- Small datasets (<50 verses) cannot support claims of 100% accuracy
- Need statistical power to distinguish algorithm quality from chance
- Include at least 2 cases of each kind of non-arbitrary reason group.

**Balanced Sampling** across multiple dimensions:
1. **Testament**: Proportional OT/NT distribution
2. **Genre**: Narrative, Poetry, Prophecy, Epistle, etc.
3. **Book Distribution**: Avoid concentration in single book
4. **Difficulty**: Include both typical cases AND adversarial cases

## Non-arbitrary reason groups

Some decisions are arbitrary (there where 3 or 4 maybe 5 people in a group, we don't know, the original text does not say, something just needs to be picked).  Others are non-arbitrary.  Gen 1:1 let "us" (how many people is us; making the wrong choice could greatly influence theology.

 - Think deeply about all the verses determining which are arbitrary/non-arbitrary
 - For all arbitrary group them into reasons (ex. Trinity)
 - Include at least 2 occurances (or more) for each group.

### Theological Stratification (Non-Arbitrary Features)

For features with non-arbitrary contexts:

**Sample Requirements**:
- ✅ Include ALL identified non-arbitrary verses (Trinity, divine commands, etc.)
- ✅ Mark with theological metadata: `arbitrarity: non-arbitrary`
- ✅ Note affected doctrines and cultural sensitivities
- ✅ Ensure balanced representation across theological contexts

**Example**:
```yaml
verses:
  - reference: "GEN.001.026"
    tbta_value: "trial"  # or plural
    arbitrarity: non-arbitrary
    theological_stakes: high
    affected_doctrines: [Trinity, creation]
    requires_multi_answer: true
    notes: "Trinity doctrine - prefer trial but document plural alternative"
```

**Arbitrary verses**: Don't add metadata (space-saving - default is arbitrary)

## Adversarial Selection Strategy

For the **test set** (30%), deliberately include challenging non-arbitrary cases:
- Edge cases where multiple values might apply
- Verses with theological ambiguity
- Contexts where annotation rules might conflict
- Genre boundaries (e.g., quoted speech, vision contexts)
- Translation-divergent passages
- Rare or complex discourse structures

**Purpose**: Find algorithm blind spots, not just confirm what works

## Translation Language Selection (Core Workflow)

For every feature, identify which languages grammatically mark this feature:

**Step 1: Language Family Analysis** (from Stage 2)
- Which language families grammatically require this feature?
- Example: Dual number → Austronesian (176 langs), Trans-New Guinea (129 langs)
- Example: Clusivity → 200+ languages (Tagalog, Malay, Fijian, Vietnamese, many Native American)

**Step 2: Build Translation Database**
For each marking language, document:
- **Translation name, version, year**
- **Language family classification**
- **Source lineage**: Direct from Greek/Hebrew? Or derived from Indonesian/Swahili/French/German?
- **Availability**: Online (eBible, Bible.com), API access, physical copy
- **Priority ranking**:
  1. Same language family as typical target translations
  2. Same source lineage (e.g., all derived from Indonesian)
  3. Direct from source text by local translators

**Step 3: Select 5-10 Representative Translations**
- Cover multiple language families
- Mix of direct (Greek/Hebrew) and derived translations
- Prioritize accessible online translations
- Document in `experiments/TRANSLATION-DATABASE.md`

**Purpose**: Not just validation, but DISCOVERY - analyze what these translators chose to understand the correct answer

## Data Extraction Process (Integrated TBTA + Translations)

**Dual Output Strategy**: For every verse, generate BOTH answer sheet (TBTA values) AND question sheet (real translations)

### Step 1: Extract TBTA Data (Answer Sheet)

**Using extract_feature.py script**:
```bash
python src/ingest-data/tbta/extract_feature.py \
  --field "Person" \
  --max-per-value 2000 \
  --output features/{feature}/raw_tbta_data.yaml
```

**Script outputs**:
- All verses with this TBTA feature
- Frequency counts per value
- OT/NT and book distribution
- Up to 2000 verses per value (LRU cache)

### Step 2: LLM Sample Selection (Subagent)

**Subagent responsibilities** (with access to raw TBTA data only):
1. **Ensure sparse checkout of translation data**:
   ```bash
   cd .data
   git sparse-checkout add 'commentary/**/*-ebible.yaml'
   ```

2. **Sample with stratification**:
   - Testament: Proportional OT/NT
   - Genre: Classify as narrative/poetry/prophecy/epistle
   - Difficulty: Mark typical vs adversarial cases
   - Book distribution: Avoid concentration

3. **Use Quote Bible skill**:
   - In /.claude/skills/quote-bible/SKILL.md
   - Query 3-5 sample verses
   - Identify available translation languages/codes
   - Verify accessibility

4. **Select representative translations** (5-10 languages):
   - Prioritize languages that mark this feature
   - Cover multiple language families
   - Mix direct (Greek/Hebrew) and derived translations
   - Document selection rationale

5. **Split into train/test/validate** (40%/30%/30%)

### Step 3: Generate Question Sheets (Translation Data)

**For each split (train, test, validate)**, generate question sheet with real translations:

**Script usage** (concept - to be implemented):
```bash
python src/ingest-data/generate_question_sheet.py \
  --answer-sheet features/{feature}/experiments/train.yaml \
  --translations tgl,mri,fij,smo,ind \
  --output features/{feature}/experiments/train_questions.yaml
```

**Script responsibilities**:
- Read answer sheet verses
- For each verse, lookup `.data/commentary/{BOOK}/{chapter:03d}/{verse:03d}/{BOOK}-{chapter:03d}-{verse:03d}-ebible.yaml`
- Extract specified translation language texts
- Format as question sheet (translations only, NO TBTA values)

**Alternative (manual process)**:
- Use Quote Bible skill for each verse
- Extract selected language translations
- Create question YAML manually

### Output File Structure

**Answer Sheet** (TBTA values - for scoring only):
```yaml
# features/{feature}/experiments/train.yaml (or test.yaml, validate.yaml)
feature: {feature-name}
translation_database:
  languages: [tgl, mri, fij, smo, ind, ...]  # Selected for this feature
  families: [Austronesian, Polynesian, ...]
  rationale: "Why these languages selected"
value:
  - specific_value: {specific-value}
    total_verses: {count}
    distribution:
      OT: {count}
      NT: {count}
      Books: {GEN: X, EXO: Y, ...}
    genres:
      narrative: {count}
      poetry: {count}
      prophecy: {count}
      epistle: {count}
    verses:
      - reference: "{BOOK}.{chapter:03d}.{verse:03d}"
        tbta_value: "{value}"
        genre: "{genre}"
        difficulty: "typical|adversarial"
        notes: "Why adversarial (if applicable)"
```

**Question Sheet** (real translations - for analysis):
```yaml
# features/{feature}/experiments/train_questions.yaml (or test_questions.yaml, validate_questions.yaml)
feature: {feature-name}
translations_included: [tgl, mri, fij, smo, ind, ...]
verses:
  - reference: "{BOOK}.{chapter:03d}.{verse:03d}"
    translations:
      tgl: "{Tagalog text}"
      mri: "{Māori text}"
      fij: "{Fijian text}"
      smo: "{Samoan text}"
      ind: "{Indonesian text}"
      # ... other selected languages
```

**File Organization**:
```
features/{feature}/experiments/
  ├── train.yaml              # Answer sheet (TBTA values)
  ├── train_questions.yaml    # Question sheet (translations)
  ├── test.yaml              # Answer sheet (TBTA values)
  ├── test_questions.yaml    # Question sheet (translations)
  ├── validate.yaml          # Answer sheet (TBTA values)
  ├── validate_questions.yaml # Question sheet (translations)
  └── TRANSLATION-DATABASE.md # Documentation of translation selection
```

**Main Agent Workflow**:
- Receives only paths to question sheets (never sees answer sheets until scoring)
- Uses translations to discover/validate predictions
- Compares against TBTA answers only after predictions are locked

# 5. Analyze Translations & Develop Algorithm

**Core Principle**: Discover answers from what real translators did, not just from TBTA annotations alone.

## Translation Discovery Analysis (Primary Source)

For each verse in `train_questions.yaml`, analyze what real translators chose:

### Step 1: Translation Pattern Analysis

**For each training verse**:
1. **Read the translations** (from train_questions.yaml)
2. **Identify the feature value** each translation reveals
   - Example (clusivity): Tagalog uses "tayo" (inclusive) vs "kami" (exclusive)
   - Example (dual): Fijian uses dual pronoun vs plural
3. **Check for consensus**:
   - **High agreement** (80%+ translations agree) → Strong signal
   - **Split decision** (mixed) → Investigate why
   - **Unclear** (feature not observable) → Flag for TBTA check

**Document patterns in `experiments/TRANSLATION-PATTERNS.md`**:
```markdown
## Verse GEN.001.026
**Translations**:
- Tagalog: "tayo" (inclusive we) → INCLUSIVE
- Māori: "tātou" (inclusive we) → INCLUSIVE
- Fijian: "kedatou" (inclusive we, trial) → INCLUSIVE
- Samoan: "tatou" (inclusive we) → INCLUSIVE
- Indonesian: "kita" (inclusive we) → INCLUSIVE

**Consensus**: 100% (5/5) → INCLUSIVE
**Confidence**: Very High
```

### Step 2: Compare with TBTA Values

After translation analysis, compare with TBTA (from train.yaml):

**Case A: Translations AGREE with TBTA** (90%+ of cases)
- ✅ **High confidence**: Both sources confirm same answer
- Document: "Validated by translations (5/5 consensus)"
- Use this verse for algorithm training

**Case B: Translations DISAGREE with TBTA** (rare, <5%)
- ⚠️ **Investigate carefully**: Why the divergence?
  - Is TBTA correct but translators missed it?
  - Is this a valid perspective difference (translation vs. discourse analysis)?
  - Is TBTA potentially incorrect?
- Document analysis in `experiments/DIVERGENCE-ANALYSIS.md`
- Flag for review (see Step 6)

**Case C: Translations UNCLEAR** (feature not observable in translations)
- 📝 **Rely on TBTA**: Use TBTA value
- Lower confidence: Cannot verify with translations
- Document: "TBTA only (feature not observable in selected translations)"

### Step 3: Integration Analysis

Review `../learnings/README.md` for transferable patterns, then create `experiments/ANALYSIS.md`:

**Dual-Source Analysis**:
For each approach (up to 12), consider:
- **Translation evidence**: What do translators consistently do?
- **TBTA patterns**: What does discourse analysis reveal?
- **Convergence**: Where do both sources agree?
- **Theological factors**: Divine speech, prayer, prophecy patterns
- **Grammatical cues**: Person markers, verb forms, context
- **Discourse patterns**: Genre, speaker, participant tracking
- **Genre signals**: Narrative vs. epistle vs. poetry

**Weight pros/cons** of each approach:
- ✅ Supported by translation consensus
- ✅ Matches TBTA patterns
- ⚠️ Translations unclear for this approach
- ❌ Contradicts translation evidence

## Ramification Analysis for Non-Arbitrary Contexts

**Required for verses marked `arbitrarity: non-arbitrary`**

Create `experiments/THEOLOGICAL-ANALYSIS.md` documenting:

### Framework Template

For each non-arbitrary context:

```yaml
verse: GEN.001.026
feature: number-system
arbitrarity: non-arbitrary
theological_stakes: high
affected_doctrines: [Trinity, nature of God, creation theology]

preferred_answer:
  value: trial
  rationale: "Trinity doctrine - Father, Son, Spirit create together"
  confidence: high
  theological_support:
    - "NT Trinitarian revelation (Matt 28:19, 2 Cor 13:14)"
    - "Church fathers' interpretation (Augustine, Athanasius)"
    - "Creedal statements (Nicene, Athanasian)"
  translation_support:
    - "Fijian: 'kedatou' (trial inclusive)"
    - "Hawaiian: 'kākou' (trial)"
    - "8/9 trial-marking translations use trial"

alternative_answers:
  - value: plural_3_or_more
    rationale: "Could include angels in divine council"
    christian_orthodox_assessment:
      status: "REJECTED by Christian orthodoxy"
      theological_problems:
        - "Implies angels participate in creation (contra Isa 44:24 'I alone')"
        - "Diminishes uniqueness of Trinity"
        - "Opens door to polytheistic misunderstanding"
      why_rejected: "Conflicts with NT Trinitarian revelation and Isa 44:24; not compatible with Christian theology"

    non_orthodox_use:
      - tradition: "Jewish (non-Messianic)"
        status: "May use this interpretation"
        notes: "Valid within Judaism with proper clarification that creation is by God alone"
        supporting_texts: "Psalm 82, Job 1-2 (divine assembly imagery)"

  - value: majestic_plural
    rationale: "Royal 'we' - singular God speaking majestically"
    christian_orthodox_assessment:
      status: "WEAK / LESS PREFERRED"
      theological_problems:
        - "Doesn't explain plural 'our image'"
        - "Weak linguistic evidence for Hebrew majestic plural"
        - "Doesn't account for NT Trinitarian revelation"
      why_less_preferred: "Inconsistent with 'Let us' + 'our image' construction; Trinity is clearer interpretation"

    non_orthodox_use:
      - tradition: "Islamic"
        status: "May use this interpretation"
        notes: "Preserves Tawhid (strict monotheism); valid within Islam but not Christian orthodox interpretation"

theological_framework:
  christian_orthodox_position:
    interpretation: "Trinity (Father, Son, Spirit in creative dialogue)"
    textual_basis: "NT revelation (Matt 28:19, John 1:1-3, 2 Cor 13:14), Nicene Creed"
    church_fathers: "Augustine, Athanasius - unanimous on Trinity in creation"
    denominational_unity:
      - "Protestant: Trinity affirmed, trial number if language has it"
      - "Catholic: Trinity affirmed, trial number if language has it"
      - "Orthodox: Trinity affirmed, trial number if language has it"
      - "Coptic: Trinity affirmed, trial number if language has it"
    denominational_variations: "Minor differences in explaining 'persons' vs 'hypostases', but Trinity doctrine is unified"
    recommended_translation: "Trial number if available (grammatically encodes Trinity), plural with footnote if not"

  non_orthodox_views_for_awareness:
    - group: "Jehovah's Witnesses (cult)"
      interpretation: "Jehovah + Michael the Archangel creating"
      why_rejected_by_christianity: "Denies deity of Christ (John 1:1 'and the Word was God'); makes 'us' = God + created being, introducing Arian heresy"
      translator_warning: "CRITICAL: This interpretation enables false teaching about Christ's nature"

    - group: "Mormons / LDS (cult)"
      interpretation: "Council of gods creating"
      why_rejected_by_christianity: "Polytheism; contradicts biblical monotheism (Deut 6:4, Isa 44:6-8)"
      translator_warning: "CRITICAL: Violates monotheism, introduces polytheistic heresy"

    - group: "Jewish (non-Messianic)"
      interpretation: "Majestic plural or divine council (God + angels, but creation by God alone)"
      why_not_christian_orthodox: "Rejects NT Trinitarian revelation; does not recognize Jesus as Messiah or second person of Trinity"
      notes: "Valid within Judaism; translators serving Jewish communities may use this interpretation"
      textual_concern: "Divine council view must clarify Isa 44:24 'I alone' - angels do not participate in creation"

    - group: "Islamic"
      interpretation: "Majestic plural (singular God speaking royally)"
      why_not_christian_orthodox: "Rejects Trinity (Tawhid - strict monotheism); denies deity of Christ"
      notes: "Valid within Islam; not compatible with Christian theology"
      textual_concern: "Weak Hebrew linguistic evidence for majestic plural; doesn't explain 'our image'"

cultural_application_notes:
  - context: "Polytheistic background communities"
    consideration: "May misunderstand plural as multiple gods"
    christian_guidance: "Emphasize biblical monotheism (Deut 6:4) AND Trinity (one God, three persons)"
    clarification: "Trinity ≠ three gods; Trinity = three persons, one God"

  - context: "Honor/shame cultures (e.g., East Asian)"
    consideration: "Plural of modesty/dignity culturally resonant"
    christian_guidance: "Can connect Trinity with cultural understanding of honorific speech while maintaining theological accuracy"

translator_guidance:
  for_christian_translators:
    - "Trinity is the orthodox Christian interpretation of Gen 1:26"
    - "Trial number (if your language has it) grammatically encodes Trinity"
    - "Plural with footnote explaining Trinity if trial unavailable"
    - "NEVER obscure Trinity reference - this is core Christian doctrine"
    - "NEVER suggest angels participate in creation (contradicts Isa 44:24)"

  denominational_considerations:
    - "Protestant/Catholic/Orthodox/Coptic: Unified on Trinity, minor variations in technical terminology"
    - "Messianic Jewish: Affirm Trinity within Hebrew scripture context"

  avoiding_heresy:
    - "JW/Arian interpretation (Jesus as created being): REJECT - contradicts John 1:1-3"
    - "Mormon/polytheistic interpretation (council of gods): REJECT - contradicts Deut 6:4"
    - "Unitarian interpretation (denies Trinity): REJECT - contradicts NT revelation and creeds"
```

### Multi-Answer Output Format

For non-arbitrary cases, prompt must output:

```yaml
verse: GEN.001.026
feature: number-system
arbitrarity: non-arbitrary  # Flag this!
preferred: trial
alternatives:
  - value: plural
    rationale: "Divine council interpretation"
    problems: ["Diminishes Trinity", "Contra Isa 44:24"]
  - value: majestic_plural
    rationale: "Royal we"
    problems: ["Weak linguistic evidence"]

# Provide to Christian translators:
christian_orthodox_guidance: |
  TRINITY is the Christian orthodox interpretation of Genesis 1:26.

  Recommended Translation:
  - TRIAL number if your language has it (grammatically encodes Father, Son, Spirit)
  - PLURAL with footnote explaining Trinity if trial not available
  - Example footnote: "The plural 'us' and 'our' refers to the Trinity—Father, Son, and Holy Spirit (cf. John 1:1-3, Matt 28:19)"

  CRITICAL WARNINGS:
  - NEVER obscure the Trinity reference - this is core Christian doctrine
  - NEVER suggest angels participate in creation (contradicts Isa 44:24 "I alone")
  - NEVER use interpretations that deny Christ's deity (JW/Arian heresy)

  Denominational Unity:
  - Protestant/Catholic/Orthodox/Coptic: Unified on Trinity doctrine
  - Minor variations in technical terminology, but substance is identical

non_christian_translators_awareness: |
  If translating for non-Christian communities (Jewish, Islamic, etc.):
  - Non-orthodox interpretations exist (majestic plural, divine council)
  - These are NOT Christian orthodox; they reject NT revelation
  - Translators should understand WHY these differ from Christian interpretation
  - Purpose: Avoid accidentally introducing non-Christian theology into Christian translations
```

**Arbitrary cases**: Single answer only (no alternatives needed)

## First Prompt Development

### Multi-Path Prompts for Non-Arbitrary Features

**If feature has non-arbitrary contexts**, prompt must:

1. **Detect arbitrarity**:
   ```
   First, determine: Is this verse arbitrary or non-arbitrary?
   - Check theological significance
   - Check denominational implications
   - Check cultural sensitivity
   ```

2. **Branching logic**:
   ```
   IF ARBITRARY:
     → Output single best answer

   IF NON-ARBITRARY:
     → Output preferred + alternatives with ramifications
     → Flag for theological review
     → Provide translator guidance
   ```

3. **Output format**:
   ```yaml
   arbitrarity: arbitrary | non-arbitrary

   # If arbitrary:
   answer: {single value}
   confidence: {high/medium/low}

   # If non-arbitrary:
   preferred: {value}
   preferred_rationale: "{why}"
   alternatives:
     - value: {alternative}
       problems: ["{issue1}", "{issue2}"]
       when_appropriate: "{context where this might be used}"
   translator_warning: "{critical guidance}"
   ```

- Given the top methods, create `experiments/PROMPT1.md` with most likely approach
- **LOCKED PREDICTIONS**: Before testing against TBTA, commit predictions to git
  ```bash
  # Create predictions file first
  # Commit: "feat({feature}): lock PROMPT1 predictions before TBTA check"
  # Push to remote
  # Record commit SHA in LEARNINGS.md
  ```

### ⚠️ CRITICAL: Pattern Detection vs Verse Memorization

When developing your algorithm in `PROMPT1.md`, you MUST use **generalizable patterns**, not verse-specific memorization:

**❌ OVERFITTING (Verse Memorization)**:
```
If verse reference is GEN.001.026:
  → Return Trial

If verse reference is MAT.028.019:
  → Return Trial
```
**Why this fails**: The algorithm memorizes specific verses instead of learning the underlying pattern. It will fail on any new Trinity reference not in the training data.

**✅ CORRECT (Pattern Detection)**:
```
If verse contains divine first-person plural ("us", "our") in these contexts:
- Creation contexts (God creating/forming/making)
- Divine judgment contexts (God going down to judge)
- Divine deliberation (God speaking in council)

Detection criteria:
- Speaker is God/Lord/YHWH
- Uses first person plural pronouns
- Context involves divine action

→ Return Trial (Christian Trinitarian interpretation)
```
**Why this works**: The algorithm learns the *theological and linguistic pattern* (divine plural in creation/judgment contexts). It will correctly classify **any** Trinity reference, including verses not in training data.

**Examples of Pattern-Based Rules**:
- ✅ "If explicit numeric word ('two', 'three', 'four') → Dual/Trial/Quadrial"
- ✅ "If 'both' referring to paired entities → Dual"
- ✅ "If 'where two or three gather' (small indefinite group) → Paucal"
- ✅ "If 'many'/'crowd'/'multitude' → Plural"
- ❌ "If John 3:16 → Singular" (verse-specific)
- ❌ "If Matthew 28:19 → Trial" (verse-specific)

**Testing for Overfitting**:
After developing your algorithm, ask: "If I removed this verse from the training data, would my algorithm still predict it correctly using the pattern?" If no, you've overfit.

- Apply prompt to each verse in test set, predicting main value
  - If one clear option: predict only the value
  - If multiple good options: predict dominant with rationale (which may include language family preferences)

## Success Criteria & Iteration

**Accuracy Targets** (with sufficient sample size ≥100 verses):
- **Stated values** (single answer): 100% accuracy goal
  - The text is God's inerrant word - less than 100% means we're missing something
  - **Caveat**: Small datasets (<50 verses) cannot reliably demonstrate 100% - need larger samples
- **Dominant values** (primary + rationale): 95% accuracy goal

## Systematic Error Analysis (6-Step Process)

For EVERY error, follow this rigorous debugging process:

**Step 1: Verify Data Accuracy**
- Check TBTA annotation is correct for this verse
- Verify verse reference matches (no transcription errors)
- Confirm value encoding is what you think it is

**Step 2: Re-analyze Source Text**
- Read Greek/Hebrew if applicable
- Check multiple translations
- Look for linguistic details missed initially

**Step 3: Re-analyze Context**
- Read surrounding verses (±3 verses minimum)
- Check chapter context
- Consider book-level patterns

**Step 4: Cross-Reference Sources**
- Check 3+ Bible translations
- Review LXX/Vulgate if OT
- Consult commentaries if available
- **ATTRIBUTION**: URL-templatable sources go in ATTRIBUTION.md (BibleHub, StudyLight, etc.)
- **One-off sources**: Add citation at bottom of individual YAML file (unique articles, specific blog posts)

**Step 5: Test Hypotheses**
- Why did algorithm predict X when answer is Y?
- What rule/pattern led to wrong prediction?
- What should algorithm have noticed?
- Would a different approach have succeeded?

**Step 6: Final Determination**
- Is TBTA annotation correct? (95%+ of time: yes)
- Is this a valid perspective difference? (rare, document carefully)
- Is this a potential TBTA annotation error? (very rare, flag for review)
- What algorithmic change would fix this without overfitting on this error

Document analysis in `experiments/LEARNINGS.md` with:
- Verse reference
- Predicted vs. actual
- Error category
- Root cause
- Proposed fix

## Iterative Refinement

- **PROMPT2.md**: Focus on different approaches first (try alternatives before refining)
- **PROMPT3+.md**: Refine winning approach using:
  - Prompt engineering (clearer language)
  - Examples (few-shot learning)
  - Logic flowcharts (decision trees)
  - Minimal prompt optimization (remove unnecessary complexity)
- Repeat until you cannot achieve better results
- Each iteration: Lock predictions → Test → Analyze errors → Refine
- Typical iterations: 3-5 prompts (v1.0 → v2.0 → v2.1 etc.)
- Stop when: Accuracy plateaus or reaches target

## Translation-Informed Algorithm Development

**Continuous Integration**: As you develop PROMPT1.md, PROMPT2.md, etc., incorporate translation evidence:

**Algorithm Design Principles**:
1. **Prioritize high-consensus patterns**: If 90%+ of translations agree, algorithm should match
2. **Handle split decisions**: When translations disagree, algorithm should consider:
   - Language family preferences (same family as target language)
   - Source lineage (direct from Greek/Hebrew vs. derived)
   - Cultural context
   - Theological tradition
3. **Document confidence**: Mark verses where translations agree vs. unclear
4. **Learn from divergence**: When TBTA ≠ translations, investigate and document why

**Example (Clusivity)**:
```markdown
# PROMPT1.md

## Rule 1: Divine Speech (Trinity)
IF speaker includes God AND multiple persons referenced
THEN: Check translations
  - IF 80%+ use inclusive pronouns → INCLUSIVE
  - IF split or unclear → Apply theological analysis
```

## Documentation

Summarize top learnings in `experiments/LEARNINGS.md`:
- What worked best and why
- Common error patterns
- 6-step analysis results for failures
- Algorithm evolution (v1 → v2 → v3...)

Update `../learnings/README.md` with transferable patterns:
- Successful approaches reusable for other features
- Error analysis techniques
- Validation strategies
- If learnings README exceeds 400 lines, apply progressive disclosure - try reducing duplicates aggregating first then (split into topic files if still too large)

# 6. Test Against Validate Set & Peer Review

## Subagent Validation (Blind Testing)

**Subagent 1**: Apply best prompt to validate.yaml (blind - never sees answers)
- Generate predictions file
- Lock predictions with git commit
- Return only predictions file path to main agent

**Subagent 2**: Score predictions against TBTA
- Load validate.yaml (has TBTA answers)
- Load predictions file
- Calculate accuracy (stated values, dominant values)
- Identify errors for analysis
- Return only: accuracy percentages + list of error verse references (NOT the answers)

**Main agent**: Analyze errors using 6-step process
- If accuracy < 95%: return to Stage 5, refine prompt
- If accuracy ≥ 95%: proceed to peer review

## Critical Peer Review (4 Subagents)

Launch 4 subagents for independent critical review:

**Subagent 3 (Theological Reviewer)**: Assume junior wrote this with theological blind spots

**Enhanced for Arbitrarity**:
- Review prompt for theological soundness
- Check if prompt handles key doctrinal distinctions
- Look for oversimplifications or category errors
- Consider how translators might accidentally create theological issues
- Test edge cases: Does prompt handle divine speech correctly? Prayer contexts? Prophetic literature?

Additional checks for non-arbitrary features:
- [ ] All non-arbitrary contexts identified correctly?
- [ ] Preferred answer theologically sound?
- [ ] Alternative answers fairly represented?
- [ ] Theological problems with alternatives documented?
- [ ] Denominational flexibility respected?
- [ ] False teaching risks identified and prevented?
- [ ] Cultural ramifications considered?
- [ ] Translator warnings clear and actionable?
- [ ] Multi-answer output format correct?

**Test cases**: Apply prompt to known non-arbitrary verses:
- Gen 1:26 (Trinity) - should output trial + alternatives
- Matt 6:9 (prayer) - should flag cultural sensitivity
- Deut 6:4 (monotheism) - should not introduce polytheism

**Subagent 4 (Linguistic Reviewer)**: Assume junior missed linguistic nuances
- Review prompt for linguistic accuracy
- Check if prompt handles genre differences
- Look for grammar vs. semantics confusion
- Apply best practices, standards, edge cases in linguistics
- Consider for what languages will this not work and why?
- Test discourse complexity: Quoted speech? Multiple speakers? Narrative vs. direct address?

**Subagent 5 (Methodological Reviewer)**: Assume junior cut corners
- Check sample size adequacy (is n=100+ per value?)
- Verify balanced sampling (OT/NT, genres)
- Review error analysis rigor (6-step process followed?)
- Check locked predictions discipline (git commits present?)
- Verify external validation attempted (if applicable)

**Subagent 6 (Translation Practitioner)**: Assume role of Bible translator in target language
- **Context**: "I'm translating the Bible into [language with this feature]. I have the TBTA data for this feature."
- **Practical Questions**:
  - Is this data actually useful for translation decisions?
  - What's helpful vs. confusing in the annotations?
  - What mistakes might I make when using this data?
  - Does the algorithm guidance match real translation challenges?
- **Test Scenarios**: Pick 5-10 verses and translate them using the TBTA data
  - What went right? (What mistakes did I avoid?)
  - What went wrong? (What errors did I make? Why?)
  - What was missing? (What information did I need but couldn't find?)
  - What was confusing? (What annotations led me astray?)
- **Language Diversity**: Test with 2-3 different language families
  - Example: Austronesian (has clusivity) vs. Romance (doesn't have clusivity)
  - Do annotations make sense for both marking and non-marking languages?
- **Report Format**: Create `experiments/TRANSLATOR-IMPACT.md` with findings

## TBTA Reviewer Communication

When significant confusion or divergence exists, create a concise `experiments/TBTA-REVIEW.md` focusing only on specific unclear cases:

```markdown
# TBTA Review Request: {Feature Name}

**Feature**: {feature-name}
**Algorithm Accuracy**: {stated}% / {dominant}%

## Key Questions

1. **Annotation Philosophy**: {Specific unclear scenario}
   - Example: {verse reference}
   - Question: {specific question about annotation approach}

2. **Edge Cases**: {List 2-3 most confusing cases}
   - {Verse + specific question}

## Divergence Examples

| Verse | Our Prediction | TBTA Value | Question |
|-------|----------------|------------|----------|
| {REF} | {our value} | {TBTA value} | {Why we're uncertain} |

## Translator Impact

**What confused translators**: {Brief summary of translation testing issues}
**Question**: Are these annotations correct but need better documentation?

---
**Contact**: {Your information}
**Date**: {YYYY-MM-DD}
```

## Practical Application Testing

Create `experiments/TRANSLATOR-IMPACT.md` documenting real-world translation scenarios:

```markdown
# Translation Practitioner Impact Assessment: {Feature Name}

## Executive Summary
- Feature: {feature-name}
- Languages tested: {list 2-3 language families}
- Verses translated: {5-10 sample verses}
- Overall utility: {High/Medium/Low}
- Key findings: {1-sentence summary}
- **Note**: AI simulation using {model-name-and-version}

## Translation Scenarios

### Scenario 1: {Language Name} ({Language Family})
**Language Profile**:
- Does this language grammatically mark {feature}? {Yes/No}
- If yes: How? {brief description}
- Target audience: {Bible translation project context}

**Translation Test** (Pick 3-5 verses from validate set):

| Verse | English Text | TBTA Value | My Translation | What Helped | What Confused | Mistakes Avoided | Mistakes Made |
|-------|-------------|------------|----------------|-------------|---------------|------------------|---------------|
| {REF} | "{snippet}" | {value} | "{my translation}" | {What was useful} | {What was unclear} | {Errors prevented} | {Errors introduced} |

**Overall Assessment**:
- **Useful**: {What annotations helped most}
- **Confusing**: {What led me astray}
- **Missing**: {What I needed but didn't have}
- **Mistakes Avoided**: {Specific translation errors prevented by TBTA data}
- **Mistakes Made**: {Errors I made despite (or because of) TBTA data}

### Scenario 2: {Different Language} ({Different Family})
[Repeat structure above]

### Scenario 3: Non-Marking Language (e.g., English, Spanish)
**Question**: If my language doesn't grammatically mark this feature, is TBTA data still useful?

**Translation Test**:
[Test how annotations help even when language doesn't require explicit marking]

## Cross-Language Patterns

### What Works Across All Languages:
1. {Pattern 1: What was universally helpful}
2. {Pattern 2: What avoided common mistakes}
3. {Pattern 3: What clarified ambiguity}

### What Doesn't Work:
1. {Issue 1: What confused translators}
2. {Issue 2: What led to mistakes}
3. {Issue 3: What was irrelevant or misleading}

## Real Translation Mistakes Analysis

### Mistake Type 1: {Category}
**Example**: {Specific verse where translator made error}
- **TBTA Value**: {what TBTA said}
- **What I Translated**: {incorrect translation}
- **Why I Made Mistake**: {What in TBTA data confused me or what was missing}
- **Correct Translation**: {what it should have been}
- **Fix Needed**: {How algorithm/annotations should improve}

### Mistake Type 2: {Category}
[Repeat structure]

## Mistakes Successfully Avoided

### Avoidance 1: {Specific error type}
**Example**: {Verse where TBTA data prevented common error}
- **Common Mistake**: {What translators typically get wrong}
- **TBTA Guidance**: {What annotation prevented this}
- **My Translation**: {Correct result}
- **Why TBTA Helped**: {Specific insight that made difference}

## Recommendations for Algorithm Improvement

### Critical (Would prevent translation errors):
1. {Specific improvement to prevent Mistake Type 1}
2. {Specific improvement to prevent Mistake Type 2}

### Important (Would reduce confusion):
1. {Clarity improvement}
2. {Additional context needed}

### Nice-to-have (Would enhance usability):
1. {Convenience feature}

## Production Readiness from Translator Perspective

**Would I recommend this to translation teams?** {Yes/No/With caveats}

**Reasoning**: {Why or why not, what needs to change}

**Minimum Viable**: {What must be fixed before this is usable}

**Ideal State**: {What would make this truly excellent for translators}
```

Test with both marking and non-marking languages:
- Marking language: Language that grammatically requires this feature
- Non-marking language: Language that doesn't grammatically distinguish this feature
- Document whether annotations are useful for both

Identify translation-critical issues:
- What mistakes would a translator make WITHOUT this data?
- What mistakes might they make WITH this data?
- What's the net benefit?

## Integration & Iteration

Review all peer review feedback and categorize:
- **Critical**: Must fix before production
- **Important**: Should fix if possible
- **Nice-to-have**: Consider for future iterations

If material feedback exists: Return to Stage 5
- Refine prompt based on feedback
- Re-test on validate set
- Repeat peer review

When peer reviewers are satisfied (non-material feedback only):
- Mark Stage 6 complete
- Document final accuracy
- Update README.md with production status

## Production Readiness Checklist

- ✅ **Accuracy**: ≥ 100% on validate set for claims (≥100 verses)

- ✅ **Peer review complete** (4 critical reviews passed):
  - Theological reviewer approval
  - Linguistic reviewer approval
  - Methodological reviewer approval
  - Translation practitioner approval

- ✅ **Translation-Informed Development** (integrated throughout):
  - Translation database built in Stage 4 (language families, source lineages documented in TRANSLATION-DATABASE.md)
  - Question sheets generated (train_questions.yaml, test_questions.yaml, validate_questions.yaml)
  - Training analysis used translations as primary evidence (TRANSLATION-PATTERNS.md)
  - Algorithm incorporates translation consensus patterns
  - Divergences analyzed and documented (DIVERGENCE-ANALYSIS.md if applicable)
  - Agreement rate ≥ 90% (algorithm predictions match translator consensus)
  - High-confidence coverage ≥ 80% (verses with clear 80%+ translation agreement)

- ✅ **Arbitrarity handling** (if feature has non-arbitrary contexts):
  - All non-arbitrary contexts identified (ARBITRARITY-CLASSIFICATION.md)
  - Ramification analysis complete (THEOLOGICAL-ANALYSIS.md)
  - Multi-answer output format implemented
  - Preferred + alternatives documented
  - Theological problems identified
  - Cultural considerations addressed
  - Translator guidance provided
  - Denominational flexibility respected
  - No false teaching enabled

- ✅ **Methodological rigor**:
  - Error analysis documented (6-step process for all failures)
  - Locked predictions throughout (git commits present)
  - Blind testing protocol maintained (subagent validation)
  - Sample sizes adequate (≥100 verses per value)

- ✅ **Practical application testing** (TRANSLATOR-IMPACT.md):
  - Tested with marking language(s)
  - Tested with non-marking language(s)
  - Net benefit is positive (more mistakes avoided than introduced)
  - Translation teams would recommend using this data

- ✅ **Documentation complete**:
  - TBTA review feedback integrated (if applicable)
  - README.md updated with final status
  - Transferable insights added to `../learnings/README.md`

**Only when all above complete**: Mark feature as production ready
