# Proximity System Feature - TODO

## Current Status: Stage 2 In Progress

**Last Updated**: 2025-11-15

---

## Stage Progress

### ✅ Stage 1: Research TBTA Documentation (COMPLETE)
- [x] Reviewed TBTA source materials
- [x] Generated feature README with definition
- [x] Documented 10-value proximity system (spatial/temporal/discourse)
- [x] Added TBTA encoding details
- [x] Documented examples (John 1:29, Matthew 24:3, Genesis 19:31)

### ⬜ Stage 2: Language Study (IN PROGRESS)
- [x] Identified major language families requiring feature (6 families, 664+ languages)
- [x] Documented special features:
  - Visibility (Austronesian R vs r)
  - Elevation (Trans-New Guinea topography)
  - Person-oriented (Japanese, Spanish S/L distinction)
  - Noun class agreement (Niger-Congo)
- [ ] Detailed mapping of TBTA values to target language requirements
- [ ] Analysis of demonstrative system frequency (2-way 54%, 3-way 38%, 4+ way 8%)
- [ ] Identify specific Bible translation validation opportunities

**Completion Evidence So Far**:
- Language families: Austronesian (176), Trans-New Guinea (129), Sino-Tibetan (135), Niger-Congo (89), Indo-European (135+)
- Total: 664+ languages with demonstrative distinctions identified
- Special systems documented: 3 types (visibility, elevation, person-oriented)

**Remaining Stage 2 Tasks**:
- [ ] Map each TBTA value (n/N/S/L/R/r/T/t/C/c) to language-specific requirements
- [ ] Document which language families use which values
- [ ] Create language family → value mapping table
- [ ] Identify translation validation targets (published Bibles in complex demonstrative languages)

### ⬜ Stage 3: Scholarly and Internet Research (NEXT)
- [ ] Search WALS Online (Feature 41A: Distance Contrasts in Demonstratives)
- [ ] Review scholarly literature:
  - Demonstrative typology (Diessel 1999)
  - Person-oriented systems (Anderson & Keenan 1985)
  - Visibility marking (Burenhult 2003)
- [ ] Investigate Bible translation case studies
- [ ] Update README with research findings

**Target Resources**:
- WALS Feature 41A (Distance Contrasts)
- WALS Feature 42A (Pronominal and Adnominal Demonstratives)
- Glottolog demonstrative system documentation
- SIL/Wycliffe translation notes for complex demonstrative languages

### ⬜ Stage 4: Generate Proper Test Set
- [ ] Use subagent to extract TBTA proximity annotations (prevent seeing answers)
- [ ] Create train/test/validate splits (40%/30%/30%)
- [ ] Target: 50+ verses per value if possible
  - Spatial (N/S/L/R/r): High priority
  - Temporal (T/t): Medium priority
  - Discourse (C/c): High priority
- [ ] Balance across:
  - Source languages (Greek NT, Hebrew OT)
  - Genres (narrative, teaching, prophecy)
  - Proximity domains (spatial/temporal/discourse)
- [ ] Include adversarial cases:
  - Ambiguous demonstratives (Greek οὗτος can be spatial or discourse)
  - Hebrew זֶה (unmarked for distance)
  - Boundary cases (visible vs. invisible inference)

### ⬜ Stage 5: Propose Hypothesis and First Prompt
- [ ] Analyze training data patterns
- [ ] Create experiments/ANALYSIS.md (evaluate up to 12 approaches):
  1. Source form mapping (Greek ὅδε/οὗτος/ἐκεῖνος → values)
  2. Temporal noun detection (day, hour, time → T/t)
  3. Spatial scene analysis (present/absent, visible/invisible)
  4. Discourse emphasis detection (emphatic position → C vs c)
  5. Person-oriented inference (speaker vs. hearer proximity)
  6. Visibility inference rules (R vs r)
  7. Hebrew contextual analysis (זֶה unmarked → infer from narrative)
  8. Elevation/topography mapping (for TNG languages)
  9. Multi-feature approach (combine source + context + emphasis)
  10. Genre-specific rules (narrative vs. discourse vs. prophecy)
  11. Quoted speech perspective (re-center on speaker)
  12. Cross-linguistic validation (test against target language requirements)
- [ ] Develop experiments/PROMPT1.md (best approach)
- [ ] Lock predictions before TBTA check
- [ ] Test against test set
- [ ] Iterate until 90%+ accuracy (or best achievable)

### ⬜ Stage 6: Test Against Validate Set & Peer Review
- [ ] Subagent applies best prompt to validate.yaml (blind)
- [ ] Second subagent scores predictions
- [ ] 4 critical peer reviews:
  - **Theological review**: Accuracy of Biblical examples, doctrinal sensitivity
  - **Linguistic review**: Demonstrative typology accuracy, cross-linguistic validity
  - **Methodological review**: Test set design, prediction protocol, error analysis
  - **Translation practitioner review**: Usability for actual Bible translators
- [ ] Create experiments/TRANSLATOR-IMPACT.md
- [ ] Address all critical feedback
- [ ] Mark feature production-ready

---

## Experimental Work (Available in experiments/)

The `experiments/` directory contains initial research:
- **LEARNINGS.md**: Reproduction thesis and expected accuracy (80-85%)

**Key Insights from LEARNINGS.md**:
1. **Greek demonstratives are predictive** (ὅδε/οὗτος/ἐκεῖνος have clear mappings)
2. **Hebrew requires context inference** (זֶה unmarked for distance)
3. **Three-step process**:
   - Step 1: Identify demonstrative context
   - Step 2: Classify proximity type (spatial/temporal/discourse)
   - Step 3: Assign TBTA code
4. **Confidence levels**:
   - High (90-95%): Greek ἐκεῖνος, temporal nouns, anaphoric discourse
   - Medium (70-85%): Greek οὗτος in scenes, Hebrew spatial contexts
   - Low (50-70%): Spatial vs. discourse boundaries, visibility inference

**Reproduction Method** (from LEARNINGS.md):
```python
# Phase 1: Rule-based baseline (60-70% expected)
# Phase 2: Context-enhanced rules (75-80% expected)
# Phase 3: ML refinement optional (85-90% expected)
```

---

## Critical Gaps Requiring Research (Stage 3+)

### Gap 1: Visibility Inference Rules (R vs r)
**Status**: How to infer visible vs. invisible when not explicit in text?
**Example**: "That city" - visible or not?
**Impact**: Affects Austronesian languages requiring visibility marking
**Action**: Stage 3 needs to document inference heuristics

### Gap 2: Person-Oriented Distinction (S vs L)
**Status**: When to use "near speaker" vs. "near hearer"?
**Evidence**: Greek rarely encodes this, must infer from context
**Impact**: Critical for Japanese, Spanish, other person-oriented systems
**Action**: Stage 4 test set needs examples with clear speaker/hearer positioning

### Gap 3: Hebrew Contextual Inference
**Status**: Hebrew זֶה unmarked for distance
**Challenge**: Must infer spatial proximity from narrative context
**Impact**: ~50% of OT demonstratives require sophisticated analysis
**Action**: Stage 5 algorithm must develop Hebrew-specific rules

### Gap 4: Discourse Emphasis Detection (C vs c)
**Status**: What qualifies as "focus" vs. routine reference?
**Evidence**: Syntactic position (subject, fronting) may indicate emphasis
**Impact**: Affects 20-30% of discourse proximity annotations
**Action**: Stage 5 needs quantitative emphasis scoring

### Gap 5: Elevation/Topography Mapping
**Status**: How to map Biblical geography to local terrain?
**Challenge**: Trans-New Guinea languages require uphill/downhill
**Impact**: Critical for 129 TNG languages
**Action**: May require geographic metadata layer (out of scope for initial work)

---

## Recommendations for Stage 2 Completion

### Remaining Language Study Tasks

1. **Create TBTA Value → Language Family Mapping Table**:
   ```
   | TBTA Value | Required By | Example Languages | Notes |
   |------------|-------------|-------------------|-------|
   | N/S/L | Person-oriented 3-way | Japanese, Spanish | Must distinguish speaker/hearer |
   | R vs r | Visibility-marking | Austronesian, Amazonian | Visible/invisible critical |
   | T/t | Temporal systems | Most languages | Relatively straightforward |
   | C/c | Discourse | All languages | Emphasis detection challenging |
   ```

2. **Identify Translation Validation Targets**:
   - Japanese New Testament (新共同訳): Test person-oriented S/L
   - Spanish Bible (Reina-Valera): Test este/ese/aquel
   - Fijian Bible: Test visibility (R vs r)
   - Samoan Bible: Test 3-way person-oriented

3. **Document Genre-Specific Expectations**:
   - **Narrative** (Genesis, Acts): High spatial (30-40%)
   - **Teaching** (Epistles): High discourse (15-20%)
   - **Prophecy** (Isaiah): High temporal (10-15%)

### Expected Outcomes from Stage 2

- [ ] Complete value-to-language mapping table
- [ ] List of 10+ translation validation targets
- [ ] Genre-specific baseline statistics
- [ ] Stage 2 completion criteria fully met

---

## Recommendations for Stage 3

### Scholarly Research Priorities

1. **WALS Online Queries**:
   - Feature 41A: Distance Contrasts in Demonstratives
   - Feature 42A: Pronominal and Adnominal Demonstratives
   - Cross-reference: Demonstrative systems by language family

2. **Key Literature**:
   - Diessel (1999): "Demonstratives: Form, Function, and Grammaticalization"
   - Anderson & Keenan (1985): "Deixis" in Language Typology
   - Burenhult (2003): "Attention, accessibility, and the addressee"
   - Hanks (1990): "Referential Practice"

3. **Bible Translation Resources**:
   - SIL Semantic and Structural Summaries
   - Translator's Notes on demonstrative systems
   - Comparative translations (parallel corpus analysis)

### Expected Outcomes from Stage 3

- [ ] Comprehensive demonstrative typology understanding
- [ ] Visibility inference rule documentation
- [ ] Person-oriented system analysis
- [ ] Translation case studies documented

---

## Production Readiness Criteria

Before marking this feature production-ready:

1. **Data Coverage**: ≥40% TBTA test verse availability (proximity is sparser than number)
2. **Accuracy**: ≥90% on validate set (Stage 6) - lower than number due to complexity
3. **Testament Balance**: Both OT (Hebrew) and NT (Greek) examples
4. **Value Coverage**: All 10 values tested (n/N/S/L/R/r/T/t/C/c)
5. **Domain Coverage**: Spatial, temporal, discourse all validated
6. **Peer Reviews**: 4 critical reviews passed
7. **Translator Impact**: Real-world validation with published translations

**Current Status**: NOT production-ready (requires Stages 2-6)

**Note**: Proximity is inherently more challenging than Number due to:
- Greater cross-linguistic variation (2-way to 4+ way systems)
- Inference requirements (visibility, elevation, emphasis)
- Source language limitations (Hebrew unmarked for distance)
- Context-dependency (spatial vs. discourse disambiguation)

---

## Next Action

**Immediate**: Complete Stage 2 language study
- Create value-to-language mapping table
- Document translation validation targets
- Finalize genre-specific expectations

**Then**: Begin Stage 3 scholarly research
- WALS queries (Features 41A, 42A)
- Review Diessel (1999) and other key literature
- Compile translation case studies

**Timeline Estimate**:
- Stage 2 completion (2 days)
- Stage 3 (3-4 days)
- Stage 4 (1 week)
- Stage 5 (2-3 weeks iteration)
- Stage 6 (1 week validation)

---

**Maintainer Notes**:
- Proximity is more complex than Number (greater cross-linguistic variation)
- Hebrew contextual inference is major challenge (unmarked forms)
- Visibility and person-oriented distinctions require sophisticated analysis
- Expected accuracy: 80-85% (per LEARNINGS.md), lower than Number's 90-95%
- Translation validation critical (compare to published Bibles)
- This feature directly impacts 664+ languages (37.6% of all languages)
