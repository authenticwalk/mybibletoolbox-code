# TBTA Local Analysis Workflow

## Overview

This workflow describes how to perform **local analysis** of TBTA features using the actual Bible translation data in `.data/commentary/`. This complements the global research already completed by validating findings against real translation texts.

## The Goal

For each TBTA feature, create an `ebible-analysis.md` file that:
1. Identifies minimum verse fragments that demonstrate all states of the feature
2. Extracts actual translations from ebible files for languages that encode this feature
3. Compares how different languages/language families handle the feature
4. Documents any disagreements or variation patterns
5. Cross-references with TBTA annotations to validate understanding

## Prerequisites

### 1. Data Directory Setup

The `.data/` directory uses sparse-checkout to limit downloaded files:

```bash
# Check current sparse-checkout
cd .data && git sparse-checkout list

# Output will show:
# commentary/GEN/001
# commentary/JHN/003
# commentary/MAT/005
# strongs
```

### 2. Adding More Verses

When you need verses not in the current sparse-checkout:

**Option A: Add specific verses/chapters**
```bash
cd .data
git sparse-checkout add commentary/ROM/008
git sparse-checkout add commentary/1CO/013
```

**Option B: Disable sparse-checkout temporarily**
```bash
cd .data
git sparse-checkout disable
# WARNING: This downloads ALL commentary files (~GB of data)
```

**Option C: Re-enable sparse-checkout later**
```bash
cd .data
git sparse-checkout init --cone
git sparse-checkout set commentary/GEN/001 commentary/JHN/003 strongs
```

## Workflow Steps

### Step 1: Identify Verse Fragments

**Goal**: Find the MINIMUM verse fragments that cover EVERY state of the feature.

**Example for Number Systems** (Singular, Dual, Trial, Plural):
- If the feature has 4 states, you need at least 4 fragments
- If you're testing 3 languages, that's 3 × 4 = 12 data points minimum
- Add a few more for validation

**How to choose**:
1. Review the feature README in `plan/tbta-project-local/features/{feature}/`
2. Look at TBTA data to find verses with the feature (check `experiments/{feature}/`)
3. Pick verses that:
   - Show clear grammatical distinctions
   - Are available in sparse-checkout OR
   - Add them to sparse-checkout

### Step 2: Select Target Languages

**Goal**: Choose languages you KNOW encode this feature AND are available in ebible.

**How to select**:
1. Review `plan/tbta-project-local/languages/{family}/README.md`
2. Check `src/constants/languages.tsv` for language codes
3. Pick languages where you CONFIDENTLY know the feature:
   - Tagalog (tgl): clusivity - `tayo` vs `kami`
   - Indonesian (ind): clusivity - `kita` vs `kami`
   - German (deu): grammatical gender
   - Japanese (jpn): honorifics and proximity

**Aim for diversity**:
- At least 3 languages from different families
- Include languages with DIFFERENT encoding strategies if possible
- Balance between well-known (for validation) and interesting edge cases

### Step 3: Extract Verse Texts

**File locations**:
```
.data/commentary/{BOOK}/{chapter:03d}/{verse:03d}/{BOOK}-{chapter:03d}-{verse:03d}-translations-ebible.yaml
```

**Example**: John 3:16
```
.data/commentary/JHN/003/016/JHN-003-014-translations-ebible.yaml
```

**How to extract**:

```bash
# Read the ebible file
cat .data/commentary/JHN/003/016/JHN-003-014-translations-ebible.yaml

# Find specific languages
grep "tgl-" .data/commentary/JHN/003/016/JHN-003-014-translations-ebible.yaml
grep "ind-" .data/commentary/JHN/003/016/JHN-003-014-translations-ebible.yaml
```

**Language code format**: `{iso-639-3}-{version}`
- `tgl-TGL`: Tagalog
- `ind-INO`: Indonesian
- `deu-TKW`: German (Textbibel)
- `jpn-RCB`: Japanese

### Step 4: Analyze the Translations

**What to look for**:

For each verse fragment × language combination:
1. **Identify the relevant grammatical element**
   - Pronouns for person/number systems
   - Verb forms for aspect/mood
   - Demonstratives for proximity

2. **Document the linguistic encoding**
   ```markdown
   **Genesis 1:26 - "Let us make"**

   - **Tagalog (tgl-TGL)**: "Gumawa **tayo**..."
     - Uses *tayo* (inclusive we) = Trial number (3 persons of Trinity)
     - Confirms First Inclusive person

   - **Indonesian (ind-INO)**: "**Kita** akan menjadikan..."
     - Uses *kita* (inclusive we)
     - Also confirms First Inclusive

   - **English (eng-EMTV)**: "Let **us** make..."
     - Generic plural, no clusivity distinction
     - Cannot determine if inclusive/exclusive from grammar alone
   ```

3. **Look for disagreements**
   - Do some languages choose different interpretations?
   - Example: Some translations might use plural where others use dual
   - Document WHY the disagreement exists (ambiguity? theological interpretation?)

### Step 5: Check TBTA Annotations

**File locations**:
```
.data/commentary/{BOOK}/{chapter:03d}/{verse:03d}/{BOOK}-{chapter:03d}-{verse:03d}-tbta.yaml
```

**How to use**:

```bash
# View TBTA annotation for the verse
cat .data/commentary/JHN/003/016/JHN-003-014-tbta.yaml

# Search for specific features
grep "Number:" .data/commentary/GEN/001/026/GEN-001-026-tbta.yaml
grep "Person:" .data/commentary/GEN/001/026/GEN-001-026-tbta.yaml
```

**What to validate**:
1. Does TBTA encode what the translations show?
2. Do the TBTA values match your analysis?
3. Are there edge cases TBTA captures that translations miss?

### Step 6: Document Findings

**Create**: `plan/tbta-project-local/features/{feature}/ebible-analysis.md`

**Template**:

```markdown
# {Feature Name} - eBible Local Analysis

## Feature States Tested

List all possible values of the feature:
- Singular
- Dual
- Trial
- Plural

## Verse Selection

### Verse 1: {Reference}
**Why chosen**: Shows {state 1} clearly

### Verse 2: {Reference}
**Why chosen**: Shows {state 2} with minimal context

### Verse 3: {Reference}
**Why chosen**: Contrasts {state 1} and {state 3} in same verse

## Languages Analyzed

1. **Language 1 (code)**: {Why it's relevant}
2. **Language 2 (code)**: {Why it's relevant}
3. **Language 3 (code)**: {Why it's relevant}

## Analysis by Verse

### {Reference} - "{English fragment}"

#### Source (Greek/Hebrew)
[Brief note about source grammar if relevant]

#### Translations

**Language 1 (code-VER)**:
```
[Full verse text]
```
- **Analysis**: [What grammatical form is used, what it means]
- **Feature encoding**: {State} = [specific word/morpheme]

**Language 2 (code-VER)**:
```
[Full verse text]
```
- **Analysis**: ...

[Repeat for each language]

#### TBTA Annotation

```yaml
[Relevant snippet from TBTA file]
```

**Validation**: ✅ Matches / ❌ Disagrees / ⚠️ Ambiguous

#### Key Findings

- All languages agree on {aspect}
- Languages X and Y disagree on {aspect} because...
- TBTA encodes {value} which correctly predicts...

## Cross-Language Patterns

### Pattern 1: {Description}
Languages: [list]
Reasoning: ...

### Pattern 2: Disagreement on {aspect}
- **Camp A** (languages X, Y): Choose {interpretation A}
- **Camp B** (languages Z): Choose {interpretation B}
- **Reason**: Theological tradition / Grammatical ambiguity / ...

## TBTA Validation

### What TBTA Got Right
1. {Feature X} correctly encoded as {value}
2. Matches {language family} pattern

### What TBTA Encoded That Isn't Surface-Visible
1. {Implicit information}
2. Helps with {target language type}

### Limitations or Questions
1. {Any ambiguities}
2. {Edge cases}

## Recommendations

For translators working in {language types}:
1. {Practical guidance}
2. {Key verse considerations}
3. {Common pitfalls to avoid}

## Data Files Referenced

- TBTA: `.data/commentary/{BOOK}/{chap}/{verse}/{file}-tbta.yaml`
- eBible: `.data/commentary/{BOOK}/{chap}/{verse}/{file}-translations-ebible.yaml`
- Macula: `.data/commentary/{BOOK}/{chap}/{verse}/{file}-macula.yaml`

## Coverage

- **Verse fragments tested**: {number}
- **Languages analyzed**: {number}
- **Language families**: {list}
- **Feature states confirmed**: {list}
- **Data points**: {verse × language count}
```

## Tips for Success

### 1. Focus on Minimum Viable Coverage

Don't try to analyze ALL languages. Pick 3-5 languages you REALLY understand for this feature.

### 2. Quote Accurately

Always copy-paste the EXACT text from the ebible files. Never paraphrase or translate.

### 3. Note Disagreements

Disagreements are VALUABLE data! They show:
- Theological interpretation differences
- Grammatical ambiguity in source
- Target language constraints

### 4. Cross-reference TBTA

The TBTA files show what expert annotators encoded. Use them to:
- Validate your understanding
- Learn about implicit information
- Find edge cases you might miss

### 5. Stay Focused

Each `ebible-analysis.md` should cover ONE feature. Don't try to analyze 10 features at once.

## Example: Clusivity in Genesis 1:26

See `plan/tbta-project-local/features/person-systems/ebible-analysis.md` (to be created) for a complete example.

**Quick preview**:
- **Feature**: First Person Inclusive vs Exclusive
- **Verse**: Genesis 1:26 "Let us make"
- **Languages**: Tagalog (tayo/kami), Indonesian (kita/kami), Fijian (kedaru/keirau)
- **Finding**: All three agree on INCLUSIVE ("us" = Trinity members addressing each other)
- **TBTA**: Confirms `Person: First Inclusive`
- **Validation**: ✅ Perfect match

## Questions?

Check existing experiment files in:
- `plan/tbta-project-local/experiments/person-systems/experiment-001.md`
- `plan/tbta-project-local/experiments/number-systems/experiment-001.md`

These show the GLOBAL research approach. Your local analysis adds VALIDATION with real texts.

---

**Next Steps**: Create your first `ebible-analysis.md` for a feature you want to validate!
