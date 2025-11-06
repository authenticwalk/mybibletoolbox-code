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

**Goal**: Find 7+ diverse verses that cover EVERY state of the feature.

**Diversity Requirements**:
Must include verses from different literary genres:
1. **Narrative** - Stories, historical accounts (Genesis, Acts)
2. **Poetry** - Psalms, Proverbs, Song of Songs
3. **Prophecy** - Isaiah, Jeremiah, Revelation
4. **Law** - Leviticus, Deuteronomy
5. **Wisdom** - Job, Ecclesiastes, Proverbs
6. **Epistle** - Romans, Corinthians, Ephesians
7. **Gospel** - Matthew, Mark, Luke, John

**Example for Clusivity** (Inclusive vs Exclusive):
- Need at least 7 verses demonstrating INCLUSIVE
- Need at least 7 verses demonstrating EXCLUSIVE
- Must span different genres (narrative, poetry, epistle, etc.)

**Coverage requirement**:
- 7 verses minimum per feature state
- 7-10 languages analyzed per verse
- Diverse literary contexts

**How to choose**:
1. Review the feature README in `plan/tbta-project-local/features/{feature}/`
2. Look at TBTA data to find verses with the feature (check `experiments/{feature}/`)
3. Select verses that:
   - Show clear grammatical distinctions
   - Come from diverse literary genres
   - Are theologically or culturally significant
   - Are available in sparse-checkout OR can be added

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

**Strategic Language Selection**:

Choose languages based on these criteria:

1. **Gateway languages** - Used as source for other translations
   - English (eng): Most common translation source
   - Spanish (spa): Gateway for Latin America
   - French (fra): Gateway for Francophone Africa
   - Swahili (swh): Gateway for East Africa
   - Indonesian (ind): Gateway for Southeast Asia
   - Arabic (arb): Gateway for Middle East/North Africa
   - German (deu): Gateway for Germanic languages

2. **Well-understood by SOTA models** - Common in training data
   - English, Spanish, French, German, Russian, Chinese, Japanese, Korean
   - High-quality linguistic resources available

3. **Feature-specific exemplars** - Languages that explicitly encode this feature
   - For clusivity: Tagalog, Indonesian, Fijian, Malay (Austronesian)
   - For trial number: Fijian, Hawaiian (Oceanic)
   - For honorifics: Japanese, Korean, Javanese

**Recommended minimum**: 7-10 languages per verse
- 2-3 gateway languages
- 2-3 SOTA well-understood languages
- 2-4 feature-specific languages
- Include diverse language families

**What to analyze**:

For each verse:

1. **Phase 1: Dominant Pattern Analysis**

   Focus on gateway + SOTA languages first:
   ```markdown
   **Genesis 1:26 - "Let us make"**

   **Gateway Languages (Expected to agree)**:
   - **English (eng-LSV)**: "Let **Us** make" - ambiguous {llm-cs45}
   - **Spanish (spa-RVA)**: "Hagamos al hombre" - ambiguous {llm-cs45}
   - **Swahili (swh-ONEN)**: "**Tufanye** mtu" - Tu- prefix (likely inclusive) {llm-cs45}
   - **German (deu-TKW)**: "Laßt **uns** Menschen machen" - ambiguous {llm-cs45}

   **Feature-Specific (Explicit encoding)**:
   - **Tagalog (tgl-ULB)**: "Gawin **natin** ang tao"
     - Uses *natin* (genitive of *tayo*) = INCLUSIVE {manual}
   - **Indonesian (ind-ind)**: "Marilah **Kita** menciptakan"
     - Uses *Kita* (capitalized) = INCLUSIVE {manual}
   ```

2. **Phase 2: Comprehensive Scan for Exceptions**

   **CRITICAL**: Inspect the ENTIRE translations-ebible.yaml file

   ```bash
   # Load the full file
   cat .data/commentary/GEN/001/026/GEN.001.026-translations-ebible.yaml

   # Look for patterns that might indicate disagreement
   # - Different word choices
   # - Unusual constructions
   # - Minority interpretations
   ```

   **Questions to ask**:
   - Are there ANY languages that seem to diverge from the dominant pattern?
   - Do any translations use singular where others use plural?
   - Do any clusivity languages use exclusive where others use inclusive?
   - Are there regional patterns (e.g., African vs Asian languages)?

3. **Phase 3: Exception Investigation**

   When you find exceptions:

   **Step A: Identify the language**
   ```markdown
   **Potential Exception Found**:
   - **Language X (xxx-VER)**: [unusual translation]
   - **Differs from**: [dominant pattern]
   ```

   **Step B: Research and validate** (DO NOT ASSUME!)

   For well-known languages:
   - Consult grammar references
   - Check other verses with same feature
   - Cite sources: `{source}` or `{llm-cs45}` if using model knowledge

   For lesser-known languages:
   - **BE VERY CAREFUL** - do not make assumptions
   - Research language family and known features
   - Check linguistic databases (WALS, Ethnologue, Glottolog)
   - If you find confirmation: cite source `{wals-feature-39a}`, `{ethnologue-xxx}`
   - If you CANNOT confirm: mark as tentative `{llm-cs45, unconfirmed}`
   - If uncertain: flag for manual review

   **Step C: Diagnose the reason**
   ```markdown
   **Diagnosis**:
   - **Language family pattern**: [e.g., Niger-Congo languages tend to...]
   - **Theological tradition**: [e.g., Catholic vs Protestant translations]
   - **Cultural context**: [e.g., monarchical vs egalitarian cultures]
   - **Translation error**: [possible mistranslation]
   - **Ambiguity in source**: [Hebrew/Greek allows multiple readings]
   ```

   **Example**:
   ```markdown
   **Exception: Yoruba (yor-yor)**
   Translation: "Ẹ jẹ́ kí **a** dá ènìyàn" {yor-yor}

   Uses "a" (we) - Yoruba does not grammatically mark clusivity {llm-cs45, unconfirmed}

   **Diagnosis**: Not an exception to INCLUSIVE - Yoruba simply lacks
   grammatical clusivity marking. The choice between inclusive/exclusive
   must be inferred from context. {llm-cs45}

   **Source validation needed**: Consult Yoruba grammar reference to confirm
   clusivity is not marked. [FLAGGED FOR REVIEW]
   ```

4. **Phase 4: Document Findings**

   ```markdown
   ### Cross-Language Analysis

   **Consensus Pattern** (XX languages agree):
   - [Dominant interpretation]
   - Languages: [list]

   **Exceptions Found** (Y languages):

   **Exception 1**: [Language] - [pattern]
   - **Reason**: [diagnosis]
   - **Validation**: [cited source or flagged]

   **No-Data Languages** (Z languages):
   - Languages that don't grammatically encode this feature
   - Cannot determine feature value from grammar alone
   - Examples: English, German, Spanish (for clusivity)
   ```

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

**File Structure**:

Follow this hierarchical organization:

```
features/{feature}/
├── README.md                    # Summary (max 200 lines)
├── {subfeature}/
│   ├── README.md               # Subfeature summary (propagated from analysis)
│   ├── {value}/
│   │   ├── README.md          # Final findings for this value (max 400 lines)
│   │   ├── {BOOK}-{chap}-{verse}.md   # Detailed verse analysis
│   │   ├── {BOOK}-{chap}-{verse}.md   # (7+ verse files)
│   │   └── ...
│   └── {another-value}/
│       └── ...
└── experiments/                 # Research/experiments (optional)
```

**Example for Clusivity**:

```
features/person-systems/
├── README.md                           # Overview of person systems
└── clusivity/
    ├── README.md                      # Summary of clusivity findings
    ├── inclusive/
    │   ├── README.md                 # Summary with top 3 examples
    │   ├── GEN-001-026.md           # Genesis 1:26 detailed analysis
    │   ├── JHN-011-007.md           # John 11:7 analysis
    │   ├── PSA-095-001.md           # Psalm 95:1 analysis
    │   ├── [4 more verse files]
    │   └── ...
    └── exclusive/
        ├── README.md                 # Summary with top 3 examples
        ├── ACT-015-025.md           # Acts 15:25 detailed analysis
        ├── 1CO-001-002.md           # 1 Corinthians 1:2 analysis
        └── [5 more verse files]
```

**README.md Files** (Summaries):

Each README.md contains:
- **Feature/value overview**: What it is
- **Key findings**: Consensus patterns, exceptions
- **Top 3 examples**: With actual translations inline
- **Links to detailed analyses**: References to verse .md files
- **Max 200 lines** (parent) or **400 lines** (subfeature)

**Verse .md Files** (Detailed Analysis):

**Create**: `features/{feature}/{value}/{BOOK}-{chap}-{verse}.md`

**Template**:

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
