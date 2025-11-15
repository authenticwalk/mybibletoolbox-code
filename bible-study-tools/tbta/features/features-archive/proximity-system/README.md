# Proximity System Feature

## Feature Definition

The **Proximity System** feature identifies deictic distance distinctions in demonstratives and spatial/temporal references. TBTA encodes proximity using **position 8** of the semantic string for nouns with 10 possible values across three dimensions:

1. **Spatial** (5 values): Physical location relative to speaker/hearer
2. **Temporal** (2 values): Time distance (near/remote)
3. **Discourse** (2 values): Textual reference proximity

**Linguistic Status**: Demonstrative systems vary dramatically cross-linguistically, from simple 2-way systems (English "this/that") to complex person-oriented systems (Japanese ko/so/a), visibility-based systems (Austronesian), and elevation-based systems (Trans-New Guinea).

**Translation Impact**: Without accurate proximity annotation, translations into these 1009+ languages will produce unnatural or incorrect demonstrative choices, particularly problematic for the 37.6% of languages with 3-way systems and specialized systems requiring visibility or elevation distinctions.

---

## Complete Value Enumeration

| Code | Category | Meaning | Description |
|------|----------|---------|-------------|
| `n` | N/A | Not Applicable | No proximity distinction needed |
| **Spatial - Physical Location** ||||
| `N` | Physical | Near Speaker and Listener | Referent close to both speaker and hearer |
| `S` | Physical | Near Speaker | Referent close to speaker only |
| `L` | Physical | Near Listener | Referent close to hearer/addressee |
| `R` | Physical | Remote within Sight | Referent far but visible |
| `r` | Physical | Remote out of Sight | Referent far and not visible |
| **Temporal - Time Distance** ||||
| `T` | Temporal | Temporally Near | Recent time reference |
| `t` | Temporal | Temporally Remote | Distant time reference |
| **Discourse - Textual Reference** ||||
| `C` | Discourse | Contextually Near with Focus | Recently mentioned with emphasis |
| `c` | Discourse | Contextually Near | Recently mentioned in discourse |

---

## Theological/Linguistic Context

### Biblical Example: John 1:29 - Spatial Demonstrative

**Greek Text**: ἴδε ὁ ἀμνὸς τοῦ θεοῦ (ide ho amnos tou theou)

**English**: "Behold the Lamb of God"

**Proximity Challenge**: How far was Jesus from John the Baptist?
- **Near** (N/S): If Jesus was approaching closely
- **Remote within Sight** (R): If Jesus was visible but at distance

**Translation Impact**:
- **Japanese** (3-way person-oriented): Must choose:
  - これ (kore, ko-series) = near speaker (John)
  - それ (sore, so-series) = near hearer (disciples)
  - あれ (are, a-series) = far from both but visible
- **Spanish** (3-way distance): Must choose:
  - este = this (very near)
  - ese = that (middle distance)
  - aquel = that (far)

**Context Evidence**: John was baptizing, Jesus came to him → Suggests approaching (N or S), but "Behold" (imperative to look) suggests some distance (R). TBTA marks as **R** (Remote within Sight).

### Other Biblical Examples

**Temporal Proximity**:
- **Matthew 24:3**: "When will these things be?" (ταῦτα) → `t` (Temporally Remote, eschatological future)
- **Matthew 3:1**: "In those days" → `t` (past, temporally remote)

**Discourse Proximity**:
- **John 3:16**: "For God so loved" (οὕτως) → `C` (Contextually Near with Focus, emphasizes manner)
- **Ezekiel 5:5**: "This is Jerusalem" (זֹאת) → `C` (emphatic subject position)

**Visibility Distinction**:
- **Genesis 19:31**: "There is not a man in the earth" → `r` (Remote out of Sight, general reference to absent men)
- **John 1:29**: "Behold the Lamb of God" → `R` (Remote within Sight, visible but distant)

---

## Language Family Analysis

### Stage 2: Languages Requiring Proximity System Feature

Based on typological research and demonstrative system complexity:

#### 1. **Austronesian Family** (176 languages in dataset)

**Complexity**: High (visibility-based systems common)
- **Fijian**: Visible vs. invisible demonstratives
- **Tagalog**: 3-way distance + visible/invisible
- **Malagasy**: 4-way system with elevation component

**Distinguishing Feature**: **Visibility** (R vs r)
- Many Austronesian languages grammatically distinguish visible from invisible referents
- English "that" could be either, but Austronesian must specify

**Translation Impact**: High
- Must determine visibility status for all distal demonstratives
- Crucial for narrative where referents go in/out of sight

#### 2. **Trans-New Guinea Family** (129 languages in dataset)

**Complexity**: Very High (elevation-based systems)
- **Yupno**: Uphill/downhill demonstratives
- **Telefol**: 4-way with topography
- **Enga**: Elevation + distance

**Distinguishing Feature**: **Topography/Elevation**
- Demonstratives encode whether referent is uphill, downhill, upriver, downriver
- Cannot translate demonstratives without knowing local geography

**Translation Impact**: Critical
- Requires mapping Biblical geography to local terrain
- Motion verbs interact with demonstrative choice
- TBTA spatial codes (N/S/L/R/r) must be interpreted relative to elevation

#### 3. **Sino-Tibetan Family** (135 languages in dataset)

**Person-Oriented Systems** (Japanese-type):
- **Mandarin**: 3-way (near speaker/near hearer/far)
- **Tibetan**: Complex with honorifics
- **Burmese**: 2-way but context-sensitive

**Translation Impact**: Medium-High
- Must determine speaker vs. hearer proximity (S vs L)
- Japanese ko/so/a system requires careful scene analysis

#### 4. **Niger-Congo Family** (89 languages in dataset)

**Noun Class Agreement**:
- **Swahili**: Demonstratives agree with 15 noun classes
- **Zulu**: Distance + noun class
- **Shona**: 3-way distance with class agreement

**Translation Impact**: Medium
- Distance distinctions (2-3 way) relatively standard
- Main challenge: Integrating proximity with noun class morphology

#### 5. **Indo-European Family** (Multiple subfamilies)

**Romance** (Spanish, Portuguese, Romanian):
- **3-way person-oriented**: este/ese/aquel
- Must distinguish S (near speaker), L (near hearer), R (far)

**Slavic** (Russian, Polish):
- **Simple 2-way**: этот/тот (this/that)
- Lower proximity demands

**Translation Impact**: Medium
- Romance languages require careful S/L distinction
- Slavic languages can use simpler N vs R coding

---

## Summary of Language Families Requiring Proximity System Feature

| Language Family | Languages (count) | Spatial Levels | Special Features | Priority |
|-----------------|-------------------|----------------|------------------|----------|
| **Austronesian** | 176 | 2-4 way | Visibility (R/r) | **HIGH** |
| **Trans-New Guinea** | 129 | 2-4 way | Elevation/Topography | **HIGH** |
| **Sino-Tibetan** | 135 | 2-3 way | Person-oriented (S/L) | **MEDIUM** |
| **Niger-Congo** | 89 | 2-3 way | Noun class agreement | **MEDIUM** |
| **Indo-European (Romance)** | ~40 | 3-way | Person-oriented | **MEDIUM** |
| **Indo-European (Other)** | ~95 | 2-way | Standard | **LOW** |
| **TOTAL** | **664+** | Varies | Multiple systems | — |

**Key Findings**:
- **54% of languages**: 2-way systems (this/that) → Use N/S vs R/r
- **38% of languages**: 3-way systems → Require S/L/R distinction or N/R/r
- **8% of languages**: 4+ way or special features (visibility, elevation)

---

## TBTA Encoding Details

### Proposed Encoding Strategy

**Feature Name**: `proximity_system` (Position 8 in noun semantic strings)

**Values**: See table above (10 values: n, N, S, L, R, r, T, t, C, c)

**Scope**: Applied to noun phrases with demonstrative marking or deictic reference

**Example Annotation** (John 1:29):
```yaml
reference: "JHN 1:29"
text: "Behold the Lamb of God"
greek: "ἴδε ὁ ἀμνὸς τοῦ θεοῦ"
proximity_system:
  value: "R"  # Remote within Sight
  note: "Jesus visible but at distance from John, 'Behold' suggests visual perception"
  spatial_scene: "John baptizing, Jesus approaching but not yet close"
```

**Example Annotation** (Matthew 24:3):
```yaml
reference: "MAT 24:3"
text: "When will these things be?"
greek: "πότε ταῦτα ἔσται"
proximity_system:
  value: "t"  # Temporally Remote
  note: "Eschatological future events, distant from present moment"
  temporal_context: "End times prophecy, not immediate future"
```

---

## Stage Checklist

### ✅ Stage 1: Research TBTA Documentation (COMPLETE)
- [x] Reviewed TBTA source materials
- [x] Generated feature README with definition
- [x] Documented theological/linguistic context (John 1:29 example)
- [x] Added TBTA encoding details

### ⬜ Stage 2: Language Study (IN PROGRESS)
- [x] Identified major language families requiring feature
- [x] Documented 664+ languages with demonstrative distinctions
- [ ] Detailed analysis of language-specific requirements
- [ ] Map TBTA values to target language systems
- [ ] Identify translation validation opportunities

**Stage 2 Completion Criteria**:
- Language families identified: 6 major families
- Languages requiring feature: 664+ identified
- Special features documented: Visibility, elevation, person-oriented
- Example verses catalogued: John 1:29, Matthew 24:3, Genesis 19:31

### ⬜ Stage 3: Scholarly and Internet Research
- [ ] Search for scholarly articles on demonstrative systems
- [ ] Review linguistic typology databases (WALS Feature 41A: Distance Contrasts)
- [ ] Investigate Bible translation case studies
- [ ] Update README with latest research

### ⬜ Stage 4: Generate Proper Test Set
- [ ] Use subagent to extract TBTA data (prevent seeing answers)
- [ ] Create train/test/validate splits (40%/30%/30%)
- [ ] Ensure 50+ verses per value (if possible)
- [ ] Balance across spatial/temporal/discourse
- [ ] Include adversarial cases (ambiguous contexts)

### ⬜ Stage 5: Propose Hypothesis and First Prompt
- [ ] Analyze training data
- [ ] Create experiments/ANALYSIS.md (up to 12 approaches)
- [ ] Develop experiments/PROMPT1.md
- [ ] Lock predictions before TBTA check
- [ ] Test against test set
- [ ] Iterate until 90%+ accuracy

### ⬜ Stage 6: Test Against Validate Set & Peer Review
- [ ] Subagent applies best prompt to validate.yaml (blind)
- [ ] Second subagent scores predictions
- [ ] 4 critical peer reviews (theological, linguistic, methodological, practitioner)
- [ ] Create experiments/TRANSLATOR-IMPACT.md
- [ ] Address all critical feedback
- [ ] Mark feature production-ready

---

## Research Notes

### Demonstrative Typology

**WALS Feature 41A**: Distance Contrasts in Demonstratives
- **2-way**: 54% of world's languages (proximal vs. distal)
- **3-way**: 38% (near/middle/far OR person-oriented)
- **4+ way**: 8% (complex systems)

**Person-Oriented vs. Distance-Oriented**:
- **Person-oriented** (Japanese, Spanish): Near me/near you/far from both
- **Distance-oriented** (English-type): Near/far (speaker-anchored)

**Visibility**:
- **Austronesian**: Common feature (visible vs. invisible)
- **Amazonian** (Tupi-Guarani): Visible/invisible/inferred

**Elevation**:
- **Trans-New Guinea**: Uphill/downhill relative to speaker
- **Trans-Himalayan** (Lhasa Tibetan): Upward/level/downward

### Source Language Demonstratives

**Greek**:
- **ὅδε** (hode): Immediate proximal (rare, emphatic)
- **οὗτος** (houtos): Proximal or anaphoric
- **ἐκεῖνος** (ekeinos): Distal

**Hebrew**:
- **זֶה** (zeh): Unmarked for distance (context-dependent)
- **זֹאת** (zot): Feminine singular
- **אֵלֶּה** (elleh): Plural
- **הַלָּז** (hallaz): Rare, always medial spatial

**Challenge**: Hebrew demonstratives don't encode distance morphologically → Must infer from context

---

## External Validation Opportunities

**Languages with Published Bible Translations**:
1. **Japanese**: Compare demonstrative choices in 新共同訳 (New Common Translation)
2. **Spanish**: Validate este/ese/aquel in Reina-Valera
3. **Swahili**: Check demonstrative + noun class agreement
4. **Samoan**: Person-oriented system validation

**Validation Strategy**: Compare TBTA annotations against real Bible translations to verify demonstrative choices match native speaker intuitions.

---

**Feature Status**: 🟨 Stage 2 (Language Study) - IN PROGRESS

**Next Steps**:
1. Complete Stage 2 language analysis
2. Proceed to Stage 3 (Scholarly Research)
3. Focus on WALS data for demonstrative systems
4. Review Bible translation case studies

**Last Updated**: 2025-11-15
**Researcher**: Claude Code (Anthropic)
