# Participant Tracking

<<<<<<< HEAD
**Definition**: Marks how discourse entities (characters, objects) are introduced, maintained, and reactivated across narrative. Universally necessary but grammatically encoded through switch-reference, topic particles, pro-drop systems, or articles.

## Quick Facts

| Aspect | Details |
|--------|---------|
| **Values** | 9 defined: Routine (73%), Generic (14%), Frame Inferable (7.5%), First Mention (5.4%), others (<1%) |
| **Gateway** | Part = Noun or Pronoun only |
| **Coverage** | 11,649 verses (37% Bible, prioritizing narrative) |
| **Theological Risk** | **CRITICAL**: Trinity ambiguity (Gen 1:26), Christology (John 1:1), resurrection witnesses (1 Cor 15) |
| **Contextual Risk** | **HIGH**: Participant enumeration (John 21:2), pronoun ambiguity (Acts 9/22/26) |

## Critical Languages

| Strategy | Examples | Impact |
|----------|----------|--------|
| **Switch-Reference** (Mandatory) | Huli, Iatmul, Tucanoan | Requires grammatical SS/DS marking at every clause boundary |
| **Topic-Prominent** (Mandatory) | Japanese (は/が), Korean (은/는), Mandarin | Particle choice directly encodes participant tracking |
| **Pro-Drop** (Optional pronouns) | Spanish, Greek, Hebrew, Russian | Zero anaphora allowed for routine; explicit for emphasis/clarity |
| **Non-Pro-Drop** (Required pronouns) | English, German, French | Articles signal definiteness; pronouns required for clarity |

## Theological Examples

❌ **WRONG**: John 1:1 conflates Word and God (modalism—same person) → **FORBIDDEN**

✅ **RIGHT**: John 1:1 distinguishes Word from God (relational) while affirming both divine (essential)

⚠️ **CAUTION**: Gen 1:26 "us"—Trinity (orthodox) vs. divine council (rejected) vs. polytheism (heretical)

## TBTA Encoding

Position 5 or 6 in noun semantic string (9-character code). **Note**: Discrepancy between source documents; requires verification. See [research/TBTA.md](./research/TBTA.md) for full details.

---

**Stage 1 Status**: ✅ Complete | **Next**: Stage 2 Analysis | **Learn More**: [research/README.md](./research/README.md)
=======
**TBTA Feature #3** | **Tier A: Essential** | **Stage**: 1 Complete (Research & Definition)

---

## Feature Description

Participant tracking analyzes how participants (characters, entities) are introduced, referenced, and tracked throughout discourse—including pronoun use, zero anaphora, definiteness marking, and other participant management strategies.

---

## Quick Facts

| Attribute | Value |
|-----------|-------|
| **TBTA Values** | Routine (73%), Generic (14%), Frame Inferable (7.5%), First Mention (5.4%), Interrogative (0.23%), Offstage (~0%), **Restaging (0% - unused)** |
| **Total Annotations** | 171,876 instances in TBTA dataset |
| **Source Languages** | Hebrew & Greek: **NOT grammatically encoded** (pragmatic inference only) |
| **Critical Languages** | Japanese (wa/ga), Korean (neun/ga), Bantu (noun class), Quechua (-qa), Tagalog (voice) |
| **Theological Stakes** | 15% non-arbitrary (Trinity, Messianic prophecy, divine participants), 85% stylistic |
| **Gateway Feature** | Part of Speech = Noun/Pronoun |
| **Related Features** | Noun List Index (coreference), Surface Realization (noun/pronoun/zero), Number (Trinity) |

---

## Target Audiences

### Language Families Requiring This Feature

**MANDATORY Grammatical Marking** (hundreds of languages):
- **Japonic** (Japanese): Topic marker は (wa) vs. subject marker が (ga) vs. zero anaphora—90%+ subject drop for routine participants
- **Koreanic** (Korean): Topic 는/은 (neun) for episode-old, Nominative 가/이 (ga) for cross-episode restaging
- **Bantu** (Swahili, etc.): Noun class agreement (15-18 classes) disambiguates participants
- **Quechuan**: Topic marker -qa for established participants
- **Austronesian** (Tagalog, etc.): Voice/focus system interacts with participant status

**OPTIONAL Resources** (most Indo-European languages):
- **English, Spanish, German**: Definite/indefinite articles (a/the), pronominalization
- **Spanish, Italian, Greek**: Null subjects (zero vs. overt pronoun marks information structure)
- **Mandarin Chinese**: Topic marking (optional but common in topic-prominent constructions)

**Key Distinction**: Japanese/Korean REQUIRE participant tracking marking every time; English CAN mark via articles but often flexible.

### Translation Impact Examples

#### ✅ **Good**: Genesis 1:26 (Trinity Reference)

**Source** (Hebrew): אֱלֹהִים... נַעֲשֶׂה "God... Let us make"
**TBTA**: Participant = God, Tracking = Routine (problematic—see issues below), Number = Trial (3)

| Language | Strategy | Example |
|----------|----------|---------|
| **Japanese** | Presupposed topic marker は (wa) | 神は...「我々が造ろう」 (Kami **wa**... "warera ga tsukurou") |
| **Korean** | Topic marker 는 (neun) + plural 우리 (uri) | 하나님**은**... "**우리**가 만들자" (Hananim-**eun**... "**uri**-ga mandeulja") |
| **English** | Definite article "the" (presupposed) | "**The** God said, 'Let **us** make...'" |
| **Swahili** | Class 1 (divine) prefix + plural | "Mungu... **Tufanye**" (Class 1 "Let us make") |

**Theological Note**: Must ensure "us" = Trinity (3 persons), not polytheism or angels. Coordinate with Number feature (Trial preferred, Plural acceptable, Dual forbidden).

#### ⚠️ **Requires Care**: Isaiah 53 (Messianic Prophecy - Participant Identity)

**Source** (Hebrew): עַבְדִּי "My Servant" (Isaiah 52:13) → הוּא "He" (Isaiah 53:3+)

**Issue**: Is "He" routine continuation of "Servant" (same participant across chapters) or different referent?

**Christian Orthodox**: Servant = Jesus Christ (continuous from Isaiah 52:13-53:12)
**Jewish Interpretation**: Servant = Israel (corporate)

| Language | Strategy If Routine/Restaging | Strategy If Separate Referent |
|----------|-------------------------------|-------------------------------|
| **Japanese** | Topic marker は (wa) continuous | Subject marker が (ga) new participant |
| **Korean** | Topic 는 (neun) if same episode, 가 (ga) if cross-episode | Nominative 가 (ga) |
| **English** | "The servant... he" (definite = continuity) | "A servant... he" (indefinite = new) |

**Guidance**: Follow Christian orthodox interpretation (routine/restaging = same Servant = Christ). See [research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml) for full classification.

#### ❌ **Forbidden**: Genesis 1:1 (Presupposition Issue)

**Source** (Hebrew): בְּרֵאשִׁית בָּרָא אֱלֹהִים "In beginning created God"
**TBTA**: Participant = God, Tracking = **"Routine"** (PROBLEMATIC)

**Issue**: Genesis 1:1 is **first verse of Bible**—no prior textual mention of God exists. TBTA marks "Routine," conflating:
- **Cultural Presupposition**: Readers know who God is (even before reading Genesis)
- **Textual Anaphora**: Previously mentioned in text (NOT true for Gen 1:1)

**Correct Classification**: **PRESUPPOSED** (not in current TBTA schema—needs addition)

| Language | Correct Strategy | Wrong Strategy (Avoid) |
|----------|------------------|------------------------|
| **Japanese** | Topic marker は (wa) - presupposed | Subject marker が (ga) - would imply "a god" appears |
| **English** | Definite "the God" or just "God" (proper name) | Indefinite "A god" (implies polytheism) |
| **Article languages** | Definite article even at first mention | Indefinite article (theologically problematic) |

**Critical**: Even at textually first mention, God is treated as PRESUPPOSED (known entity), not FIRST MENTION (new/unknown entity).

---

## Key Translation Challenges

### 1. Presupposition vs. First Mention (God in Genesis 1:1)

**Challenge**: Source languages (Hebrew/Greek) don't distinguish presupposition from textual first mention. TBTA marks God as "Routine" despite no prior text.

**Languages Affected**: All article languages (English, Spanish, German, etc.), topic-prominent languages (Japanese, Korean, Mandarin)

**Solution**: Treat God (and other culturally presupposed entities: heaven, earth, sun, moon) as PRESUPPOSED even at first textual mention. Use definite forms, not indefinite.

### 2. Restaging After Absence (Joseph, Prophets, Gospel Characters)

**Challenge**: TBTA defines "Restaging" but 0% actual usage. Biblical text has clear examples:
- **Joseph**: Introduced Genesis 37, absent Genesis 38, **restaged** Genesis 39+
- **Prophets**: Characters reintroduced after chapters
- **Gospels**: Character reappearances across narrative gaps

**Languages Affected**: Japanese (topic marker は for restaging), Korean (nominative 가 for cross-episode), languages with explicit reintroduction markers

**Solution**: Manually identify restaging instances for Stage 2 dataset. Develop systematic criteria (e.g., "absent for X verses/chapters = restaging threshold").

### 3. Frame Inferable Participants (Semantic Predictability)

**Challenge**: 7.5% of annotations (12,815 instances) marked "Frame Inferable," but criteria subjective. Examples:
- "Jesus entered the synagogue" → **congregation** frame-inferable
- "The priest approached the altar" → **temple implements** frame-inferable

**Languages Affected**: Languages allowing null arguments (Japanese, Korean, Mandarin) vs. languages requiring overt mention (English)

**Solution**: Create systematic frame database. For Stage 2, analyze when translators include vs. omit frame-inferable participants.

---

## TBTA Encoding Details

### Position in TBTA Schema

**Category**: Noun features (Tier A, Essential #3)
**Encoding**: Position 5 in 10-position noun character codes

**Related Fields**:
- **Position 4**: Noun List Index (1-9, A-Z, a-z) - coreference tracking across verse
- **Position 9**: Surface Realization (Noun, Pronoun, Zero anaphora)
- **Position 2**: Number (interacts with Trinity references: Trial = 3, Plural = many, Dual = 2)

### JSON Export Format (from TBTA database)

```json
{
  "Constituent": "God",
  "Part": "Noun",
  "Number": "Singular",
  "Person": "Third",
  "Participant Tracking": "Routine",
  "NounListIndex": "1",
  "Semantic Role": "Most Agent-like"
}
```

### Value Distribution (171,876 total annotations)

| Value | Count | % | Example Context |
|-------|-------|---|-----------------|
| **Routine** | 125,543 | 73.04% | Continuing participant in focus |
| **Generic** | 23,856 | 13.88% | "A prophet" (generic type, not specific individual) |
| **Frame Inferable** | 12,815 | 7.46% | Predictable from context (congregation in synagogue) |
| **First Mention** | 9,267 | 5.39% | New participant introduction |
| **Interrogative** | 394 | 0.23% | "Who touched me?" (interrogative referent) |
| **Offstage** | 1 | 0.00% | Mentioned but not present in scene |
| **Restaging** | 0 | 0.00% | **NEVER USED** (should be ~50-100 instances) |
| **Integration** | 0 | 0.00% | **NEVER USED** (unclear definition) |
| **Exiting** | 0 | 0.00% | **NEVER USED** (participant leaving) |

---

## Critical Issues (from TBTA Critique)

### ❌ **Issue 1**: Presupposition Conflated with Routine Reference

**Problem**: God marked "Routine" in Genesis 1:1 despite being first verse of Bible
**Root Cause**: TBTA lacked distinct category for cultural presupposition
**Impact**: Affects ~50-100 presupposed entities (God, sun, moon, heaven, earth)
**Languages Affected**: Article languages, topic-prominent languages
**Solution Needed**: Add "Presupposed" as distinct value

### ❌ **Issue 2**: Restaging Never Used Despite Clear Need

**Problem**: 0% usage of "Restaging" value despite definition
**Evidence**: Joseph (Gen 37→39), prophets, Gospel characters clearly require restaging
**Estimated**: ~50-100 biblical instances went unmarked
**Languages Affected**: Japanese (は wa), Korean (가 ga for cross-episode), any language with explicit restaging markers
**Solution Needed**: Develop systematic restaging criteria, annotate cross-chapter reintroductions

### ⚠️ **Issue 3**: Frame Inferable Inconsistently Applied

**Problem**: Subjective judgment, no algorithmic criteria, no frame database
**Frequency**: 7.46% (12,815 instances)
**Languages Affected**: Null-argument languages (can omit) vs. overt-argument languages (must mention)
**Solution Needed**: Create systematic frame database, analyze translator behavior

---

## Research Documentation

**Full research available in [research/](research/) directory:**

- **[research/README.md](research/README.md)**: Executive summary (199 lines - start here)
- **[research/TBTA.md](research/TBTA.md)**: Complete TBTA documentation review (574 lines)
- **[research/LANGUAGES.md](research/LANGUAGES.md)**: Language family typology analysis (702 lines, 1,009 languages, 12 web sources)
- **[research/SCHOLARLY.md](research/SCHOLARLY.md)**: Scholarly literature review (1,052 lines, 22+ sources with URLs)
- **[research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)**: Theological classification (443 lines, 15% non-arbitrary)

**Key Findings Summary**:
- Source languages (Hebrew/Greek): NO grammatical PT encoding
- 1,009-language dataset: Austronesian (176), Trans-New Guinea (141), Indo-European (135) largest families
- Scholarly consensus: Universal feature, variable encoding, three tasks (semantic, processing, discourse-pragmatic)
- Theological stakes: 15% critically important (Trinity, Messianic prophecy), 85% stylistic

---

## Stage 1 Completion Status

✅ **TBTA Documentation Review** - Complete (6 source files analyzed)
✅ **Language Family Analysis** - Complete (1,009 languages classified)
✅ **Scholarly Research** - Complete (22+ sources, foundational frameworks to case studies)
✅ **Theological Classification** - Complete (non-arbitrary vs. arbitrary contexts identified)
✅ **Research Summary** - Complete (progressive disclosure format)
✅ **Feature Overview** - Complete (this README)

**Next Stage**: Stage 2 - Dataset Creation
- Sample 100+ verses per value (balanced OT/NT, genres, typical + adversarial)
- Create translation database (10 control languages: Japanese, Korean, Swahili, Quechua, Tagalog, English, Spanish, Hebrew, Greek, Mandarin)
- Generate answer sheets (TBTA annotations) + question sheets (translations only)
- Split: 40% train, 30% test, 30% validate

---

**Last Updated**: 2025-11-29
**Stage**: 1 Complete
**Status**: Ready for Stage 2
>>>>>>> origin/feat/self-learning-tbta
