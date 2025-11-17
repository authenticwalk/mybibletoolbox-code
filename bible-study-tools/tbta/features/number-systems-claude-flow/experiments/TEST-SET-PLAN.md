# Test Set Generation Plan for Number Systems Feature

**Feature**: number-systems
**Stage**: 4 (Generate Test Set with Translation Data)
**Date**: 2025-11-17
**Planner**: Tester Agent (Claude Sonnet 4.5)

---

## Executive Summary

This document outlines the strategy for generating train/test/validate datasets for the number-systems feature, following Stage 4 requirements. The plan emphasizes **discovering answers from real translations** rather than just validating against TBTA annotations.

**Key Philosophy**: "There is nothing new under the sun" - with ~1000 Bible translations, translators have already grappled with number system distinctions. We extract their wisdom.

---

## 1. Extraction Parameters

### TBTA Field to Extract
- **Field Name**: `"Number"`
- **Values**: Singular (S), Dual (D), Trial (T), Paucal (p), Plural (P), Quadrial (Q - if present)
- **Source**: TBTA JSON annotations in `.data/commentary/{BOOK}/{chapter:03d}/{BOOK}-{chapter:03d}-{verse:03d}-tbta.yaml`

### Extraction Script Command
```bash
python src/ingest-data/tbta/extract_feature.py \
  --field "Number" \
  --max-per-value 2000 \
  --output bible-study-tools/tbta/features/number-systems-claude-flow/experiments/raw_tbta_data.yaml
```

### Expected Output Structure
```yaml
feature: number-systems
extraction_date: 2025-11-17
total_verses: ~10000+
values:
  - name: "Singular"
    count: ~5000+
    verses: [...]
  - name: "Dual"
    count: ~200-300
    verses: [...]
  - name: "Trial"
    count: ~50-100
    verses: [...]
  - name: "Paucal"
    count: ~100-200
    verses: [...]
  - name: "Plural"
    count: ~4000+
    verses: [...]
  - name: "Quadrial"
    count: ~0-5 (highly contested)
    verses: [...]
```

---

## 2. Sample Size Targets

### Per-Value Targets (Minimum)

| Number Value | Target Sample | Rationale |
|--------------|---------------|-----------|
| **Singular** | 150 verses | Common (need robust validation) |
| **Dual** | 120 verses | Moderate frequency, critical for validation |
| **Trial** | 100 verses | Low frequency, high theological importance |
| **Paucal** | 100 verses | Low frequency, important distinction |
| **Plural** | 150 verses | Very common, need diverse contexts |
| **Quadrial** | 10-20 verses | Extremely rare, include if present |

**Total Dataset**: ~630-640 verses minimum

**Split Strategy**:
- **Train**: 40% (~250 verses)
- **Test**: 30% (~190 verses)
- **Validate**: 30% (~190 verses)

**Rationale for 100+ per value**:
- Statistical power to distinguish algorithm quality from chance
- Stage 6 requires ≥100 verses for 100% accuracy claims
- Insufficient for Trial/Paucal? → Oversample and balance with resampling techniques

---

## 3. Stratification Strategy

### Dimension 1: Testament Distribution
- **Target**: Proportional to actual Bible composition (~77% OT, ~23% NT)
- **Per value**:
  - Singular: 77 OT / 73 NT
  - Dual: 92 OT / 28 NT
  - Trial: 77 OT / 23 NT
  - Paucal: 77 OT / 23 NT
  - Plural: 115 OT / 35 NT

**Rationale**: Reflects actual biblical text distribution; prevents NT-only or OT-only overfitting

### Dimension 2: Genre Distribution
**Classify each verse into**:
- **Narrative**: Historical accounts, stories (Genesis, Exodus, Matthew, Acts)
- **Poetry**: Psalms, Song of Songs, Lamentations
- **Prophecy**: Isaiah, Jeremiah, Ezekiel, Revelation
- **Epistle**: Romans, Corinthians, Ephesians, 1 Peter
- **Wisdom**: Proverbs, Ecclesiastes, Job
- **Law**: Leviticus, Deuteronomy (legal codes)

**Target**: Balanced across genres (no single genre >40% of dataset)

**Per value example (Trial, 100 verses)**:
- Narrative: 30 verses (Genesis 1:26 Trinity, travel pairs)
- Epistle: 25 verses (Paul's letters, apostolic references)
- Prophecy: 20 verses (divine speech contexts)
- Poetry: 15 verses (Psalms, worship contexts)
- Law: 10 verses (legal contexts)

**Rationale**: Genres have different linguistic patterns (direct speech vs. narrative description)

### Dimension 3: Book Distribution
**Target**: Verses from at least 20 different books
- **Avoid concentration**: No single book >15% of dataset
- **Diverse authorship**: Mix Torah, historical books, prophets, gospels, epistles

**Rationale**: Prevents overfitting to single author's style or vocabulary

### Dimension 4: Difficulty Distribution
**Typical Cases (70%)**:
- Clear, unambiguous number contexts
- Explicit count given (δύο = "two", τρεῖς = "three")
- Straightforward translation consensus expected

**Adversarial Cases (30%)**:
- **Ambiguous count contexts**: "A few people", "some disciples" (paucal vs plural)
- **Genre boundaries**: Quoted speech within narrative
- **Theological edge cases**: Genesis 1:26 (Trinity), Acts 15:25 (apostolic authority)
- **Multiple valid interpretations**: Collective singular vs distributive plural
- **Translation-divergent passages**: Known disagreements across language families

**Rationale**: Adversarial cases expose algorithm blind spots

---

## 4. Non-Arbitrary Verse Inclusion

### Mandatory Non-Arbitrary Verses (from ARBITRARITY-CLASSIFICATION.md)

**Reason Group 1: Trinity References** (≥3 verses)
- **Genesis 1:26**: "Let us make mankind in our image" → Trial vs Plural (HIGH stakes)
- **Genesis 1:27**: "So God created mankind in his own image" → Singular (follow-up context)
- **Genesis 11:7**: "Come, let us go down" → Trial vs Plural (similar construction)

**Reason Group 2: Apostolic Authority** (≥2 verses)
- **Acts 15:25**: "It seemed good to us" → Plural (council context)
- **Acts 15:28**: "It seemed good to the Holy Spirit and to us" → Plural (apostolic decision)

**Reason Group 3: Paired Disciples/Witnesses** (≥10 verses)
- **Luke 24:13**: "Two of them were going" → Dual (explicit count)
- **Acts 13:2**: "Set apart Barnabas and Saul" → Dual (2 missionaries)
- **Mark 6:7**: "Sent them out two by two" → Dual (paired sending)
- **Luke 10:1**: "Sent them two by two" → Dual emphasis
- Additional paired contexts (7 more verses)

**Reason Group 4: Small Group vs Large Assembly** (≥5 verses)
- **Matthew 18:20**: "Where two or three gather" → Paucal (small group)
- **Matthew 26:26**: "While they were eating" → Paucal (12 disciples)
- **Acts 2:46**: "Broke bread in their homes" → Paucal (house church)
- **Acts 2:41**: "About 3,000 were added" → Plural (large assembly) [contrast case]
- Additional worship contexts (2 more verses)

**Reason Group 5: Corporate Solidarity** (≥20 verses)
- Israel as collective singular vs individuals plural (10+ verses)
- Church as corporate body vs individual members (10+ verses)

**Total Non-Arbitrary**: ~40+ verses (6% of 640 total)

**Distribution Across Splits**:
- **Train**: 16 non-arbitrary verses (40%)
- **Test**: 12 non-arbitrary verses (30%)
- **Validate**: 12 non-arbitrary verses (30%)

**Rationale**: Ensures algorithm learns both arbitrary and non-arbitrary patterns

---

## 5. Translation Language Selection

### Selection Criteria
1. **Grammatical marking**: Language MUST grammatically encode number distinctions
2. **Language family diversity**: Cover multiple families (Austronesian, Slavic, Trans-New Guinea, Australian)
3. **Availability**: Online access (eBible, Bible.com, or API)
4. **Source lineage**: Mix direct (Greek/Hebrew) and derived translations
5. **Priority ranking**: Same family as typical target translations

### Selected Languages (8-10 total)

#### Trial-Marking Languages (Genesis 1:26 validation)
1. **Fijian (fij)** - Austronesian/Oceanic
   - **Trial pronouns**: `kedatou` (we-three-inclusive), `keirau` (we-three-exclusive)
   - **Availability**: eBible (Fijian Bible, multiple versions)
   - **Source**: Direct from Greek/Hebrew by missionary translators
   - **Priority**: HIGH (active Bible translation context)

2. **Tok Pisin (tpi)** - Creole/Austronesian-influenced
   - **Trial pronouns**: `mitripela` (we-three-exclusive), `yumitripela` (we-three-inclusive)
   - **Availability**: eBible (Tok Pisin Nupela Testamen)
   - **Source**: Direct from Greek/English
   - **Priority**: HIGH (Papua New Guinea, active translation)

3. **Hawaiian (haw)** - Austronesian/Polynesian
   - **Trial pronouns**: `kākou` (we-three-inclusive)
   - **Availability**: Bible.com (Hawaiian Bible, Baibala Hemolele)
   - **Source**: Direct from Hebrew/Greek (19th century)
   - **Priority**: MEDIUM (historical, well-documented)

#### Dual-Marking Languages (Luke 24:13, Mark 6:7 validation)
4. **Samoan (smo)** - Austronesian/Polynesian
   - **Dual pronouns**: `lāua` (they-two), `tāua` (we-two-inclusive), `māua` (we-two-exclusive)
   - **Availability**: eBible (Samoan Bible)
   - **Source**: Direct from Greek/Hebrew
   - **Priority**: HIGH (active translation community)

5. **Slovenian (slv)** - Indo-European/Slavic
   - **Obligatory dual**: All nouns, verbs, adjectives for count 2
   - **Availability**: Bible.com (Slovenian Bible, Slovenski standardni prevod)
   - **Source**: Direct from Greek/Hebrew (modern translation 1996)
   - **Priority**: MEDIUM (European context, different language family)

6. **Upper Sorbian (hsb)** - Indo-European/Slavic
   - **Complete dual system**: Nouns, verbs, pronouns
   - **Availability**: Physical copy (Biblija.de), possibly eBible
   - **Source**: Direct from Luther's German + Greek/Hebrew (1728)
   - **Priority**: LOW (rare, but valuable for dual validation)

#### Paucal-Marking Languages (Matthew 18:20 validation)
7. **Warlpiri (wbp)** - Australian/Pama-Nyungan
   - **Paucal system**: Dual + Paucal (3-15) + Plural (many)
   - **Availability**: Check eBible or contact Wycliffe Australia
   - **Source**: Direct from Greek/Hebrew by SIL translators
   - **Priority**: HIGH (if accessible - best paucal example)

8. **Bislama (bis)** - Creole/Austronesian-influenced (Vanuatu)
   - **Paucal pronouns**: `yumitrifala` (we-three-inclusive)
   - **Availability**: eBible (Bislama Baebol)
   - **Source**: Direct from Greek/English
   - **Priority**: MEDIUM (similar to Tok Pisin, paucal-like trial)

#### Non-Marking Languages (Control - verify annotations useful even without feature)
9. **Indonesian (ind)** - Austronesian (but lost number marking)
   - **No grammatical number**: Singular/plural optionally marked with numerals
   - **Availability**: eBible (Terjemahan Baru, multiple versions)
   - **Source**: Direct from Greek/Hebrew (modern translations)
   - **Priority**: HIGH (major translation base for SE Asia)

10. **Spanish (spa)** - Indo-European/Romance
    - **Basic singular/plural only**: No dual/trial/paucal
    - **Availability**: Bible.com (Reina-Valera, NVI, multiple versions)
    - **Source**: Direct from Greek/Hebrew (historical + modern)
    - **Priority**: MEDIUM (control, widely known)

### Translation Database Documentation
Create `experiments/TRANSLATION-DATABASE.md` with:
- Full metadata for each language (ISO code, family, source lineage)
- Availability URLs and API endpoints
- Grammatical number system details
- Sample verses showing number distinctions
- Selection rationale per language

---

## 6. Adversarial Selection Criteria

### Category 1: Ambiguous Count Contexts (30 verses)
**Examples**:
- "A few people" (πλῆθος = crowd, but how many?)
- "Some disciples" (τινές = some, paucal or plural?)
- "The brothers" (οἱ ἀδελφοί = brothers, count unclear)

**Purpose**: Test algorithm's handling of lexical ambiguity

### Category 2: Genre Boundaries (20 verses)
**Examples**:
- Quoted speech within narrative (Genesis 1:26 - God speaking)
- Epistolary salutation (Galatians 1:2 - "all the brothers with me")
- Vision contexts (Revelation - symbolic numbers)

**Purpose**: Test genre-switching robustness

### Category 3: Theological Edge Cases (15 verses)
**Examples**:
- Genesis 1:26 (Trinity - trial vs plural)
- Acts 15:25 (apostolic authority - clusivity + number)
- Matthew 18:20 (small group - paucal vs plural)
- Corporate solidarity verses (Israel as singular vs plural)

**Purpose**: Test non-arbitrary context handling

### Category 4: Translation-Divergent Passages (25 verses)
**Examples**:
- Verses where dual-marking languages disagree
- Verses where trial languages use trial vs plural
- Verses where paucal languages use paucal vs plural

**Purpose**: Discover legitimate perspective differences

### Category 5: Rare Discourse Structures (10 verses)
**Examples**:
- Vocative address ("O you of little faith" - plural)
- Imperative commands to groups
- Conditional statements with plural subjects

**Purpose**: Test syntactic complexity handling

**Total Adversarial**: ~100 verses (15% of dataset, but 30% of test set)

---

## 7. Data Extraction Workflow (Subagent)

### Step 1: Sparse Checkout Setup
```bash
cd .data
git sparse-checkout add 'commentary/**/*-tbta.yaml'
git sparse-checkout add 'commentary/**/*-ebible.yaml'
```

**Rationale**: Limit git scope to TBTA + eBible translations only

### Step 2: Extract Raw TBTA Data
```bash
python src/ingest-data/tbta/extract_feature.py \
  --field "Number" \
  --max-per-value 2000 \
  --output bible-study-tools/tbta/features/number-systems-claude-flow/experiments/raw_tbta_data.yaml
```

**Expected Output**: ~10,000+ verses with Number annotations

### Step 3: LLM-Assisted Stratified Sampling (Subagent Task)
**Subagent receives**: `raw_tbta_data.yaml` (TBTA values visible)

**Subagent responsibilities**:
1. Classify each verse by:
   - Testament (OT/NT)
   - Genre (Narrative/Poetry/Prophecy/Epistle/Wisdom/Law)
   - Difficulty (Typical/Adversarial)
   - Arbitrarity (Arbitrary/Non-Arbitrary with reason group)

2. Sample 640 verses with stratification targets

3. Use Quote Bible skill to verify translation availability:
   ```
   /quote-bible GEN 1:26
   ```
   Check if selected languages (fij, tpi, haw, smo, slv, wbp, bis, ind, spa) are present

4. Adjust language selection if unavailable (e.g., if Warlpiri not in eBible, substitute Bislama)

5. Split into train/test/validate (40/30/30)

6. Generate answer sheets (TBTA values) and question sheets (translations only)

### Step 4: Generate Question Sheets

**Option A: Manual with Quote Bible Skill**
For each verse in train/test/validate:
```
/quote-bible {BOOK} {chapter}:{verse}
```
Extract translations for selected languages, create YAML

**Option B: Script-Based (if implemented)**
```bash
python src/ingest-data/generate_question_sheet.py \
  --answer-sheet bible-study-tools/tbta/features/number-systems-claude-flow/experiments/train.yaml \
  --translations fij,tpi,haw,smo,slv,wbp,bis,ind,spa \
  --output bible-study-tools/tbta/features/number-systems-claude-flow/experiments/train_questions.yaml
```

### Output Files
```
experiments/
├── raw_tbta_data.yaml              # Full TBTA extraction
├── train.yaml                      # Answer sheet (250 verses, TBTA values)
├── train_questions.yaml            # Question sheet (translations only)
├── test.yaml                       # Answer sheet (190 verses, TBTA values)
├── test_questions.yaml             # Question sheet (translations only)
├── validate.yaml                   # Answer sheet (190 verses, TBTA values)
├── validate_questions.yaml         # Question sheet (translations only)
└── TRANSLATION-DATABASE.md         # Language selection documentation
```

---

## 8. Translation Database Requirements

### Documentation Fields (per language)

**Language Metadata**:
- ISO 639-3 code (e.g., `fij`, `tpi`, `haw`)
- Language name (English + native)
- Language family (Austronesian/Oceanic, Indo-European/Slavic, etc.)
- Speaker population and geographic distribution

**Grammatical Number System**:
- Number values marked (Singular/Dual/Trial/Paucal/Plural)
- Obligatory vs facultative (optional)
- Morphological realization (pronouns, verb agreement, noun inflection)
- Examples of number distinctions in pronouns

**Translation Details**:
- Translation name and version (e.g., "Fijian Bible 1923, Na iVola Tabu")
- Source lineage (Direct from Greek/Hebrew? Derived from English/Indonesian/German?)
- Translator attribution (missionary, SIL, local church, etc.)
- Year of publication
- Availability (eBible URL, Bible.com URL, API endpoint)

**Sample Verses**:
- Genesis 1:26 (if trial-marking)
- Luke 24:13 (if dual-marking)
- Matthew 18:20 (if paucal-marking)
- Demonstrate number distinction in actual text

**Selection Rationale**:
- Why this language chosen for this feature
- Priority ranking (HIGH/MEDIUM/LOW)
- Expected insights from this language

### Example Entry

```markdown
## Fijian (fij)

**Language Family**: Austronesian > Malayo-Polynesian > Oceanic > Central Pacific > East Fijian

**Speaker Population**: ~500,000 (Fiji)

**Number System**:
- **Marked Values**: Singular, Dual, Trial, Paucal, Plural
- **Obligatory**: Pronouns (obligatory), nouns (optional with numerals)
- **Morphological Realization**:
  - Dual: `rau` (they-two), `daru` (we-two-exclusive), `kedrau` (we-two-inclusive)
  - Trial: `ratou` (they-three), `dratou` (we-three-exclusive), `kedratou` (we-three-inclusive)
  - Paucal: `ira` (they-few, 4-10)
  - Plural: `ira na tamata` (they-many)

**Translation**:
- **Name**: Na iVola Tabu (Fijian Bible)
- **Version**: 1923, revised 2007
- **Source**: Direct from Greek/Hebrew by Methodist missionary John Hunt (1847)
- **Availability**: eBible (https://ebible.org/find/details.php?id=fij)

**Sample Verses**:
- **Genesis 1:26**: "Me keda vakayacora na tamata ena nomu ulutaga" (kedatou = we-three-inclusive → Trinity)
- **Luke 24:13**: "Sa lako talega rau dua" (rau = they-two → Dual)
- **Matthew 18:20**: "Me ratou vunau kina na rua se na tolu" (ratou = they-few → Paucal)

**Selection Rationale**: HIGH priority - trial-marking language, active translation context, accessible online, direct from source texts

**Expected Insights**: Genesis 1:26 trial pronoun usage reveals Trinitarian interpretation; dual validation for paired disciples
```

---

## 9. Success Metrics

### Data Quality Metrics
- ✅ **Sample size**: ≥100 verses per value (100% of values)
- ✅ **Testament balance**: 77% OT / 23% NT (±5% tolerance)
- ✅ **Genre diversity**: No single genre >40% of dataset
- ✅ **Book diversity**: ≥20 different books represented
- ✅ **Adversarial coverage**: 30% of test set is adversarial
- ✅ **Non-arbitrary inclusion**: All 5 reason groups represented (≥2 verses each)

### Translation Coverage Metrics
- ✅ **Language diversity**: 8-10 languages across 4+ language families
- ✅ **Feature coverage**: Trial (3 langs), Dual (5 langs), Paucal (2 langs)
- ✅ **Availability**: 100% of selected languages accessible online or via API
- ✅ **Control languages**: ≥1 non-marking language (Indonesian/Spanish)

### Process Validation Metrics
- ✅ **Blind testing**: Subagent never sees answer sheets until scoring
- ✅ **Locked predictions**: Git commits before TBTA comparison
- ✅ **Translation discovery**: Question sheets generated with translations only

---

## 10. Next Steps for Stage 4 Execution

### Immediate Actions (Main Agent)
1. **Create subagent task** for data extraction (blind to final answer sheets)
2. **Verify Quote Bible skill** works for selected languages
3. **Create TRANSLATION-DATABASE.md** with language metadata

### Subagent Tasks (Delegated)
1. **Run TBTA extraction script** → `raw_tbta_data.yaml`
2. **Classify verses** (testament, genre, difficulty, arbitrarity)
3. **Stratified sampling** (640 verses, balanced across dimensions)
4. **Verify translation availability** (Quote Bible skill spot checks)
5. **Generate answer sheets** (train.yaml, test.yaml, validate.yaml)
6. **Generate question sheets** (train_questions.yaml, test_questions.yaml, validate_questions.yaml)
7. **Document sampling decisions** in each YAML file

### Main Agent Post-Subagent
1. **Review sample quality** (but NOT answer sheet contents)
2. **Proceed to Stage 5** with question sheets only
3. **Lock predictions** before comparing to answer sheets

---

## 11. Risk Mitigation

### Risk 1: Insufficient Trial/Paucal Verses
**Mitigation**:
- If <100 Trial verses exist in TBTA, oversample to 80 minimum + note limitation
- Use resampling techniques (bootstrap) for statistical power
- Acknowledge limitation in Stage 6 validation

### Risk 2: Translation Unavailability
**Mitigation**:
- Verify language availability BEFORE finalizing selection
- Have backup languages ready (e.g., Bislama if Warlpiri unavailable)
- Minimum 5 languages (3 dual + 2 trial) acceptable if paucal unavailable

### Risk 3: Subagent Exposure to Answers
**Mitigation**:
- Subagent generates BOTH answer sheets and question sheets separately
- Main agent receives question sheets only
- Answer sheets stored in separate directory, not loaded until scoring

### Risk 4: Inadequate Genre/Book Diversity
**Mitigation**:
- Monitor distributions during sampling
- Reject samples that exceed concentration thresholds (>40% single genre, >15% single book)
- Iterate sampling until balance achieved

---

## 12. Validation Checklist (Post-Execution)

- [ ] `raw_tbta_data.yaml` exists with ~10,000+ verses
- [ ] `train.yaml`, `test.yaml`, `validate.yaml` generated (640 total verses)
- [ ] `train_questions.yaml`, `test_questions.yaml`, `validate_questions.yaml` generated (translations only)
- [ ] `TRANSLATION-DATABASE.md` created with 8-10 language profiles
- [ ] Sample size ≥100 per value (or documented limitation if unavoidable)
- [ ] Testament balance 77% OT / 23% NT (±5%)
- [ ] Genre diversity: No single genre >40%
- [ ] Book diversity: ≥20 different books
- [ ] Adversarial cases: 30% of test set
- [ ] Non-arbitrary verses: All 5 reason groups represented (≥2 each)
- [ ] Translation availability: 100% of selected languages accessible
- [ ] Main agent has NOT viewed answer sheets (blind testing preserved)

---

## Appendix A: Sample YAML Structures

### Answer Sheet Format (train.yaml)
```yaml
feature: number-systems
dataset: train
total_verses: 250
translation_database:
  languages: [fij, tpi, haw, smo, slv, wbp, bis, ind, spa]
  families: [Austronesian, Slavic, Australian, Creole]
  rationale: "Trial-marking (fij, tpi, haw), Dual-marking (smo, slv), Paucal-marking (wbp, bis), Control (ind, spa)"

values:
  - name: "Trial"
    count: 40
    distribution:
      OT: 31
      NT: 9
    genres:
      narrative: 15
      epistle: 10
      prophecy: 8
      poetry: 5
      law: 2
    books: [GEN, EXO, ISA, MAT, LUK, ACT, ROM, GAL, REV, ...] # 15+ books
    verses:
      - reference: "GEN.001.026"
        tbta_value: "Trial"
        genre: "narrative"
        difficulty: "adversarial"
        arbitrarity: "non-arbitrary"
        reason_group: "Trinity references"
        theological_stakes: "high"
        affected_doctrines: ["Trinity", "nature of God"]
        notes: "Genesis 1:26 - 'Let us make mankind' - Trinity reference"

      - reference: "GEN.011.007"
        tbta_value: "Trial"
        genre: "narrative"
        difficulty: "adversarial"
        arbitrarity: "non-arbitrary"
        reason_group: "Trinity references"
        notes: "Similar construction to Gen 1:26"

      # ... 38 more Trial verses

  - name: "Dual"
    count: 50
    distribution:
      OT: 38
      NT: 12
    # ... similar structure
```

### Question Sheet Format (train_questions.yaml)
```yaml
feature: number-systems
dataset: train_questions
total_verses: 250
translations_included: [fij, tpi, haw, smo, slv, wbp, bis, ind, spa]

verses:
  - reference: "GEN.001.026"
    translations:
      fij: "Me keda vakayacora na tamata ena nomu ulutaga keda sa vakatagana kei keda, me ratou qarava na ka oga mai nanuma, kei na manumanu, kei na ka sa karawa yani ena vanua, kei na ka sa bibi ena vanua ka na ka bulabula kecega e na vanua."
      tpi: "God i tok, 'Nau mas wokim ol man bilong stap olsem mipela yet. Ol i mas bosim ol pis bilong solwara, na ol pisin bilong skai, na ol bulmakau, na olgeta samting i stap long graun, na olgeta animal i wokabaut long graun.'"
      haw: "A ʻōlelo aku ke Akua, 'E hana kākou i kanaka e like me kākou iho, a e noho aliʻi lakou maluna o nā iʻa o ke kai, a me nā manu o ka lewa, a me nā holoholona, a me ka honua āpau, a me nā mea kolo āpau e kolo ana ma ka honua.'"
      smo: "Ona fetalai mai lea o le Atua, 'Tatou te faia se tagata e pei o i tatou, ia pule foi i ʻia i lalo o le sami, ma manu o le lagi, ma manu vaefa, ma le lalolagi uma, ma mea fetolofi uma e fetolofi i le lalolagi.'"
      slv: "Potem je Bog rekel: »Narediva človeka po svoji podobi, kakor sva midva, naj gospoduje nad ribami morja in nad pticami neba, nad živino, nad vso zemljo in nad vsemi plazilci, ki se plazijo po zemlji!«"
      ind: "Berfirmanlah Allah: 'Baiklah Kita menjadikan manusia menurut gambar dan rupa Kita, supaya mereka berkuasa atas ikan-ikan di laut dan burung-burung di udara dan atas ternak dan atas seluruh bumi dan atas segala binatang melata yang merayap di bumi.'"
      spa: "Y dijo Dios: 'Hagamos al hombre a nuestra imagen, conforme a nuestra semejanza; y tenga potestad sobre los peces del mar, las aves de los cielos y las bestias, sobre toda la tierra y sobre todo animal que se arrastra sobre la tierra.'"

  - reference: "LUK.024.013"
    translations:
      fij: "Edaidai, era dua talega sa lako yani ki na koro e vaka na Emaus, ka so na maili e tini na siga kalawa mai Jerusalemi."
      # ... other translations

  # ... 248 more verses (NO TBTA values included!)
```

---

**Status**: Plan Complete
**Next Action**: Execute Stage 4 with subagent (blind data extraction)
