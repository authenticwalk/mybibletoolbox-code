# Number Systems Feature

**Feature Status**: 🟨 Stage 1 Complete (Research & Definition)  
**Last Updated**: 2025-01-27  
**TBTA Tier**: A - Essential (affects 1000+ languages)

---

## Feature Definition

**Number Systems** identify grammatical number distinctions beyond the basic singular/plural dichotomy found in English and Biblical source languages (Hebrew, Aramaic, Greek).

**Values**:
- **S** (Singular): One entity
- **D** (Dual): Exactly two entities
- **T** (Trial): Exactly three entities
- **Q** (Quadrial): Exactly four entities (contested - no linguistic evidence)
- **p** (Paucal): A few entities (small inexact group, typically 3-15)
- **P** (Plural): Multiple entities (more than paucal or unspecified)

**Translation Impact**: Approximately **337+ languages** in our dataset grammatically require these distinctions. Source languages (Hebrew/Greek) do **NOT** encode trial/paucal/quadrial morphologically, requiring translators to infer from context, explicit numbers, or theological knowledge.

---

## Target Audience

### Language Families Requiring Number Systems

**Mandatory** (~337 languages):
- **Austronesian Oceanic** (~87 languages): Dual/trial/paucal required
- **Trans-New Guinea** (~129 languages): Dual required, paucal optional
- **Australian** (~36 languages): Dual required, paucal optional

**Optional** (~45 languages):
- **Austronesian Philippine** (~45 languages): Dual may exist

**Absent** (~627 languages):
- Most Indo-European, Niger-Congo, other families

**See**: [research/LANGUAGES.md](research/LANGUAGES.md) for detailed language family analysis

---

## Examples: Why This Matters

### Example 1: Genesis 1:26 - Trinity Reference (Trial Required)

**Verse**: "Then God said, 'Let us make man in our image'"

**Challenge**: Hebrew uses plural "us" (`נַֽעֲשֶׂה` na'aseh), but how many persons? English "us" is ambiguous (2, 3, or many).

**Translation Impact**: 
- **Trial-marking languages** (e.g., Kilivila, Larike) must choose:
  - **Trial**: "Let us-three make" → Indicates Trinity (Father, Son, Holy Spirit) ✅
  - **Plural**: "Let us-many make" → Can indicate divine council or angels (acceptable but less precise)
  - **Dual**: "Let us-two make" → **HERETICAL** (Arianism - implies only 2 persons, denying Holy Spirit's deity) ❌

**TBTA Annotation**: **Trial** (exactly 3 persons)

**Theological Significance**: Choice affects doctrine. Trial encodes Trinity; dual implies only 2 persons (heresy).

**See**: [research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml) for theological analysis

---

### Example 2: Luke 24:13 - Explicit Number (Dual Required)

**Verse**: "Two of them were going"

**Challenge**: Greek explicitly states "two" (`δύο` dyo), but dual-marking languages must use dual form throughout passage.

**Translation Impact**:
- **Dual-marking languages** (e.g., Mian, Telefol, Yimas) must use dual pronouns/verbs for "two of them"
- Consistency required: All references to this pair should be dual

**TBTA Annotation**: **Dual** (explicit "two")

**Theological Significance**: Low (arbitrary - exact count doesn't affect doctrine, but accuracy matters)

---

### Example 3: Natural Pairs - Body Parts (Dual Required)

**Verse**: "His eyes were opened" (various)

**Challenge**: Body parts naturally occur in pairs. Dual-marking languages expect dual for natural pairs.

**Translation Impact**:
- **Dual-marking languages** must use dual for body parts (eyes, hands, feet, ears)
- Hebrew dual morphology (`-ayim` suffix) confirms dual for body parts
- Using plural sounds unnatural and may confuse readers

**TBTA Annotation**: **Dual** (natural pairs)

**Theological Significance**: Low (grammatical accuracy, not doctrine)

---

### Example 4: Hebrew Lexicalized Duals → Semantic Singular

**Verse**: Genesis 1:1 "the heavens" (`הַשָּׁמַיִם` ha-shamayim)

**Challenge**: Hebrew has dual morphology (`-ayim` suffix) but semantically refers to singular concept.

**Translation Impact**:
- **TBTA Policy**: Semantic meaning overrides morphological form
- Marked as **Singular** (semantic priority)
- Translators see morphological plural but understand semantic singular

**TBTA Annotation**: **Singular** (lexicalized dual, semantically singular)

**Theological Significance**: Low (grammatical accuracy)

**See**: [research/TBTA.md](research/TBTA.md) for TBTA policy details

---

## TBTA Encoding

**Technical Details**:
- **Location**: Noun feature (Position 2 in character-based encoding)
- **Applies to**: Nouns, pronouns, noun phrases
- **Policy**: Semantic meaning overrides morphological form
- **Values**: S, D, T, Q, p, P (6 values)

**Gateway Features**:
- **Part of Speech**: Applies primarily to nouns and pronouns
- **Person System**: Interacts with number (First Inclusive + Trial = Trinity)

**Constraints**:
- Quadrial controversial (no linguistic evidence - see research)
- Morphological vs. semantic distinction not explicitly documented

**See**: [research/TBTA.md](research/TBTA.md) for complete TBTA documentation review

---

## Research Documentation

**Stage 1 Research Complete**:

1. **[TBTA Documentation Review](research/TBTA.md)**: Values, policies, constraints, edge cases
2. **[Language Family Analysis](research/LANGUAGES.md)**: Required families, candidate languages, typological classification
3. **[Scholarly Research](research/SCHOLARLY.md)**: Typology, translation theory, case studies, bibliography
4. **[Theological Analysis](research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)**: Arbitrarity classification (non-arbitrary vs. arbitrary contexts)

**Summary**: [research/README.md](research/README.md)

---

## Key Insights

### 1. Source Language Limitation
Hebrew/Greek do **NOT** encode trial/paucal/quadrial morphologically. Translators must infer from:
- Explicit numbers ("two", "three", "four")
- Theological knowledge (Trinity → trial)
- Context (small group vs. large crowd → paucal vs. plural)

### 2. Theological Precision Required
Trinity references (Genesis 1:26, Genesis 3:22, Matthew 28:19) require **trial number** to preserve doctrinal precision. Using dual would be heretical (Arianism).

### 3. Semantic Priority Policy
TBTA prioritizes semantic meaning over morphological form. Hebrew lexicalized duals (`שָׁמַיִם` shamayim "heavens") are marked as singular (semantic priority).

### 4. Quadrial Controversy
TBTA includes Quadrial in schema, but **no natural language has true grammatical quadrial** (Corbett 2000). Should distinguish lesser paucal (~3-4) from greater paucal (~4-10).

---

## Next Steps

**Stage 2**: Analysis & Hypothesis Validation
- Extract data from existing TBTA system
- Analyze patterns and verify data coverage
- Generate "Smart" datasets aligned with Strong's numbers
- Split data into Train/Test/Validate sets

**See**: [../.instructions-to-build-feature/STAGE-2-ANALYSIS.md](../.instructions-to-build-feature/STAGE-2-ANALYSIS.md) for Stage 2 instructions

---

**Related Features**: [Person System](../person-system/README.md), [Participant Tracking](../participant-tracking/README.md)

