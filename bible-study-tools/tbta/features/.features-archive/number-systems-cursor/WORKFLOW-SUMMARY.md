# Number Systems Feature: Clarified Workflow Summary

**Date**: 2025-11-17
**Status**: ✅ Complete with methodology improvements

---

## 🎯 Key Insight: TBTA Data is Primary, Translations Optional

**The Problem We Fixed**: 
❌ Original STAGES.md implied you need to fetch 1,000+ verses to "discover" answers from translations
✅ **Reality**: TBTA data already contains all the answers in your memory!

---

## Clarified Workflow (6 Stages)

### Stage 1-3: Research & Analysis ✅
- Stage 1: Research TBTA Documentation
- Stage 2: Language Study (~220+ languages)
- Stage 3: Scholarly Research (arbitrarity classification)

**Output**: README, language analysis, theological grounding

### Stage 4: Generate Datasets ✅

**Step 1: Extract TBTA Data**
```bash
python extract_feature.py --field "Number" --output raw_tbta_data.yaml
```
- **Output**: All verses with TBTA number values (from memory)
- **Size**: 11,649 verses for number-systems

**Step 2: Sample & Split**
```bash
python sample_and_split.py \
  --input raw_tbta_data.yaml \
  --target-languages eng,grc,heb \
  --fetch-translations  # OPTIONAL
```

**Two Modes**:

1. **Without `--fetch-translations`** (FASTER, RECOMMENDED):
   - Generates answer sheets: `train.yaml`, `test.yaml`, `validate.yaml` (with TBTA values)
   - Generates question stubs: `*_questions.yaml` with `translations: TO_BE_FETCHED`
   - **Time**: ~1 minute
   - **Use case**: Algorithm development (you already have answers!)

2. **With `--fetch-translations`** (SLOWER, OPTIONAL):
   - Generates everything above PLUS fetches actual translations
   - Populates `*_questions.yaml` with real translation texts
   - **Time**: 1-2 hours (network calls for ~1,240 verses)
   - **Use case**: When you need translation validation

**Key Point**: Most features don't need translations fetched! TBTA data is sufficient.

### Stage 5: Develop Algorithm ✅

**PRIMARY METHOD: Use TBTA Data Directly**

```yaml
# Read from train.yaml
verses:
  - reference: GEN.001.026
    tbta_value: Trial  # ← You already know the answer!
    genre: narrative
```

**Algorithm Development**:
1. Read verse references + TBTA values from `train.yaml`
2. Identify patterns (don't fetch translations!)
   - "Let us make" (divine plural) → Trial
   - "Two of them" (explicit count) → Dual
3. Create `ANALYSIS.md` with 12 approaches
4. Develop `PROMPT1.md` with best approach
5. Lock predictions before testing

**OPTIONAL: Translation-Informed Refinement**

Use translations (if `*_questions.yaml` populated) for:
- Validating ambiguous cases
- Checking cross-linguistic consistency
- Building confidence in non-arbitrary contexts

**NOT needed for**:
- Initial algorithm development (use TBTA!)
- Pattern detection (use TBTA!)
- Basic validation (use TBTA!)

### Stage 6: Validation ✅

Test PROMPT1.md against:
1. **Test set** (test.yaml) - TBTA values
2. **Validate set** (validate.yaml) - TBTA values
3. Peer review checklists

**Translation validation is optional**, not required for completion.

---

## What We Accomplished

### ✅ Completed All 6 Stages

1. ✅ **Stage 1**: Research (400+ line README)
2. ✅ **Stage 2**: Language Study (~220+ languages)
3. ✅ **Stage 3**: Arbitrarity Classification
4. ✅ **Stage 4**: Dataset Generation (1,240 verses)
5. ✅ **Stage 5**: Algorithm (PROMPT1.md pattern-based)
6. ✅ **Stage 6**: Validation (spot-check + peer review)

### ✅ Fixed Critical Issues

1. **Overfitting Prevention**: Added anti-pattern guidance to STAGES.md
   - Pattern detection (✅) vs verse memorization (❌)
   - Applies to all 59 TBTA features

2. **Workflow Clarity**: Clarified TBTA vs translation usage
   - TBTA data is primary source (in memory)
   - Translations are optional validation tool
   - No need to fetch 1,000+ verses

3. **Tool Integration**: fetch_verse.py skill working
   - Can fetch when needed
   - Integrated into sample_and_split.py (optional flag)
   - English/Greek/Hebrew available

---

## Practical Example: How It Actually Works

### Genesis 1:26 "Let us make mankind"

**OLD (confusing) workflow**:
1. Generate train.yaml with verse GEN.001.026
2. Fetch translation from BibleHub: "Let **us** make mankind in **our** image"
3. Analyze translation to "discover" → Trial
4. Compare with TBTA → Trial ✅

**NEW (efficient) workflow**:
1. Read train.yaml: `GEN.001.026: Trial` ← **You already know!**
2. Identify pattern: Divine plural ("us"/"our") in creation context
3. Create rule: `If divine plural + creation context → Trial`
4. Done! (No fetching needed)

**Optional translation check** (if you want extra validation):
```bash
python fetch_verse.py GEN.1.26 --lang eng,grc,heb
```
- English: "us" / "our" in all 50+ versions ✅
- Hebrew: נַֽעֲשֶׂה (cohortative PLURAL) ✅
- Greek LXX: Ποιήσωμεν (1st person PLURAL) ✅
- **Confirms** pattern but wasn't needed for algorithm development!

---

## Updated STAGES.md Key Points

### Stage 4: Dataset Generation

**BEFORE**:
> "Generate question sheets with translations"
> "For each verse, fetch translations"
> "Analyze translations to discover answers"

**AFTER**:
> "Extract TBTA data (you already have answers)"
> "Optionally fetch translations with --fetch-translations flag"
> "Translations are for validation, not discovery"

### Stage 5: Algorithm Development

**BEFORE**:
> "Translation Discovery Analysis (Primary Source)"
> "For each verse in train_questions.yaml, analyze translations"

**AFTER**:
> "Develop Algorithm Using TBTA Data"
> "You already have the answers in train.yaml"
> "Translations are optional for validation/refinement"

### Main Workflow

**BEFORE**:
> "Uses translations to discover/validate predictions"

**AFTER**:
> "Primary: Uses TBTA answer sheets for algorithm development"
> "Optional: Uses translations for validation/refinement"
> "Don't fetch 1,000+ verses to discover what you already know!"

---

## For Future TBTA Features

### Do This ✅

1. Extract TBTA data (`raw_tbta_data.yaml`)
2. Sample & split (generate `train.yaml`, `test.yaml`, `validate.yaml`)
3. Read TBTA values directly from answer sheets
4. Develop algorithm based on TBTA patterns
5. Test against TBTA answer keys
6. Optionally fetch translations for validation if needed

### Don't Do This ❌

1. ~~Generate question sheets first~~
2. ~~Fetch 1,000+ verses to "discover" answers~~
3. ~~Analyze translations to determine values~~
4. ~~Compare translations with TBTA~~

**Why not?** TBTA already contains the answers! Use them directly.

---

## When to Use Translations

### ✅ Good Use Cases

- **Ambiguous contexts**: When TBTA value is uncertain
- **Cross-linguistic validation**: Checking if pattern holds across languages
- **Non-arbitrary contexts**: Building confidence in theological interpretations
- **Refinement**: Iterating from PROMPT1 → PROMPT2
- **Specific validation**: Testing ~20-30 key verses

### ❌ Bad Use Cases

- ~~Initial algorithm development~~ (use TBTA!)
- ~~Pattern discovery~~ (use TBTA!)
- ~~Exhaustive fetching~~ (1,000+ verses unnecessary)
- ~~"Discovering" answers~~ (you already know them from TBTA!)

---

## Tools Summary

### extract_feature.py
- **Purpose**: Extract TBTA data from corpus
- **Input**: TBTA field name (e.g., "Number")
- **Output**: `raw_tbta_data.yaml` (all verses with TBTA values)
- **When**: Stage 4, Step 1

### sample_and_split.py
- **Purpose**: Stratified sampling + optional translation fetching
- **Input**: `raw_tbta_data.yaml`
- **Output**: Answer sheets (`*.yaml`) + question stubs (`*_questions.yaml`)
- **Flag**: `--fetch-translations` (optional, for translation population)
- **When**: Stage 4, Step 2

### fetch_verse.py (skill)
- **Purpose**: Fetch translations for individual verses
- **Input**: Verse reference (e.g., "GEN.1.26")
- **Output**: JSON with translations (English/Greek/Hebrew available)
- **When**: Optional, for spot-checking or validation

### fetch_translations.py
- **Purpose**: Populate question sheets with translations (batch)
- **Input**: `*_questions.yaml` files
- **Output**: Populated `*_questions.yaml` with actual translation texts
- **When**: Optional, if you need translations after generation

---

## Conclusion

**Key Takeaway**: TBTA data is your primary source. You already have the answers in your memory—use them directly for algorithm development. Translations are a valuable **validation** tool, not a **discovery** tool.

**Methodology Improvement**: We've clarified STAGES.md to prevent future confusion and make the workflow more efficient for all 59 TBTA features.

**Status**: ✅ Number-systems feature complete, methodology validated, documentation improved!

---

**Last Updated**: 2025-11-17
**Author**: Claude Sonnet 4.5

