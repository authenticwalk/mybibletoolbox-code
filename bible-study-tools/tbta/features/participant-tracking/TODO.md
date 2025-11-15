# Participant Tracking: TODO & Roadmap

**Current Status**: Stage 4 Complete (90% accuracy v1.0, v2.0 designed but untested)
**Priority**: High (Tier A - Critical for 200+ switch-reference languages)
**Next Milestone**: Stage 5 - Validate Algorithm v2.0 on NEW test set

---

## Critical Path to Production

### 1. Validate Algorithm v2.0 (HIGH PRIORITY - Required for Production)

**Status**: ⚠️ BLOCKED - v2.0 is hypothetical (designed but untested)
**Blocker**: Cannot test on same 12 verses used for error analysis (introduces bias)
**Required**: NEW test set (adversarial or different random sample)

**Tasks**:
- [ ] **Select NEW test set** (choose one approach):
  - Option A: Execute adversarial test (10 verses from Stage 4 design)
  - Option B: NEW random sample (12-15 verses, genre-stratified: 50% narrative, 30% epistle, 15% poetry, 5% prophecy)
  - Option C: Cross-validation (split original 215 TBTA verses into train/test)
- [ ] **Apply Algorithm v2.0 blindly**:
  - Lock v2.0 predictions with git commit BEFORE accessing TBTA
  - No TBTA access during prediction phase
  - Maintain methodological integrity
- [ ] **Calculate accuracy and compare to v1.0**:
  - v1.0 baseline: 60-70% (random test), 97% (training)
  - v2.0 target: 80%+ (production consideration), 85%+ (production-ready)
- [ ] **Decision point**:
  - ✅ If v2.0 ≥85%: Mark production-ready, proceed to Stage 6
  - ⚠️ If v2.0 80-84%: Conditional approval, monitor in production
  - ❌ If v2.0 <80%: Refine to v2.1 or develop v3.0

**Timeline**: 1-2 sessions (v2.0 validation + possible iteration)

---

### 2. Address Known Error Patterns (MEDIUM PRIORITY - Depends on v2.0 Results)

**Current v2.0 fixes** (from ERROR-ANALYSIS.md):
1. ✅ Epistolary abstract noun rule (grace, mercy, peace → Routine in epistles)
2. ✅ Refined quantifier+definite rule ("all the X" bounded group detection)
3. ✅ Recognition frame addition (identity markers in "they knew that it was he...")

**Remaining known issues** (10% error rate from v1.0):
- [ ] **Quoted speech transitions**: Speaker changes unclear in nested quotes
  - Example: Genesis 3:1-5 (Serpent → Eve → God chain)
  - Solution: Add discourse boundary detection, track speaker shifts
- [ ] **Vision/dream boundaries**: Mixing narrative frame with internal vision
  - Example: Daniel, Revelation passages
  - Solution: Detect revelation verbs ("saw vision", "dreamed"), separate tracking contexts
- [ ] **Implicit role shifts**: Same entity, different title
  - Example: "the man" → "the king" (same person, different discourse role)
  - Solution: Build epithet/title coreference database
- [ ] **Collective reference**: Group → individual transitions
  - Example: "Israel" (collective) → "he" (individual king)
  - Solution: Track collective-to-singular mapping

**Implementation approach**:
- If v2.0 achieves 80-84%: Address these in v2.1
- If v2.0 achieves 85%+: Document as known edge cases, defer to future
- If v2.0 <80%: Prioritize most common error pattern for v3.0

---

### 3. Genre-Stratified Training Expansion (OPTIONAL - If v2.0 <80%)

**Current training**: 15 verses (4 tested, all narrative/teaching)
**Problem**: Training lacked genre diversity → algorithm missed epistolary patterns

**Genre-stratified training proposal**:
- [ ] Expand from 15 to 48 verses (3 per state × 4 genres)
- [ ] **Narrative** (12 verses): Genesis, Gospels, Acts, OT narratives
  - 3 Routine examples
  - 3 Generic examples
  - 3 Frame Inferable examples
  - 3 First Mention examples
  - (Interrogative rare - find where possible)
- [ ] **Epistle** (12 verses): Paul, general epistles
  - Focus on theological abstracts (grace, mercy, peace)
  - Include possessive constructions
  - Include greeting/blessing formulas
- [ ] **Poetry/Wisdom** (12 verses): Psalms, Proverbs, Job
  - Emphasize generic/timeless statements
  - Include metaphorical language
- [ ] **Prophecy** (12 verses): Isaiah, Jeremiah, Daniel, Revelation
  - Include vision/dream contexts
  - Future entities (First Mention in prophetic frame)
- [ ] **Retrain algorithm** with genre-specific rules
- [ ] **Validate** on mixed-genre test set

**Trigger condition**: Only if v2.0 validation shows continued genre gaps

---

### 4. Rare State Discovery (LOW PRIORITY - Can Defer)

**Status**: Stage 4 incomplete - adversarial search designed but not executed
**Rare states**: Restaging (0%), Integration (0%), Exiting (0%), Offstage (<0.001%)

**Adversarial search strategy** (100+ verse approach):
- [ ] **Restaging** (participant returns after absence):
  - Joseph narrative (GEN 37-50): Joseph absent → returns
  - David narrative (1-2 SAM): David flees, returns
  - Paul journeys (ACT 13-28): Paul leaves, comes back
  - Target: Find 1-4 examples
- [ ] **Integration** (peripheral → central):
  - Judas betrayal (MAT 26): Judas background → central to plot
  - Centurion confession (MAT 27:54): Soldier → confessing believer
  - Zacchaeus (LUK 19): Bystander → host
  - Target: Find 1-4 examples
- [ ] **Exiting** (explicit departure):
  - Judas exit (JHN 13:30): "and it was night"
  - Jesus withdrawals (MAT 12:15, 14:13): Explicit departures
  - Disciples sent (MAT 10:5): Mission departure
  - Target: Find 1-4 examples
- [ ] **Offstage** (background modifier):
  - Validate <0.001% frequency (1 instance in 171,875 annotations)
  - "Samaritan" in JHN 4:7 confirmed as only example

**Purpose**: Complete TBTA 9-state coverage, validate degree feature lesson (rare ≠ non-existent)

**Timeline**: Future session (not blocking production)

---

## Stage 5 → Stage 6 Transition Checklist

**Stage 5 Complete when**:
- [x] Algorithm v1.0 tested (60-70% random, 97% training)
- [x] Error analysis complete (3 critical categories identified)
- [x] Algorithm v2.0 designed with targeted fixes
- [ ] ⚠️ **v2.0 validated on NEW test set** (PENDING)
- [ ] ⚠️ **v2.0 achieves 80%+ accuracy** (PENDING)

**Stage 6 Prerequisites**:
- [ ] v2.0 validated and production-ready (≥80% accuracy)
- [ ] NEW test set results documented
- [ ] Decision made on production deployment

**Stage 6 Activities** (after v2.0 validation):
- [ ] **Theological review**: Check doctrinal soundness of predictions
  - Test on Trinitarian passages (avoid theological errors)
  - Test on messianic prophecies (ensure Christological accuracy)
- [ ] **Linguistic review**: Validate genre/grammar handling
  - Hebrew pro-drop patterns
  - Greek article usage
  - Septuagint vs. Hebrew tracking differences
- [ ] **Methodological review**: Assess rigor and reproducibility
  - Blind prediction protocol maintained?
  - Sample size adequate?
  - Error analysis systematic?
- [ ] **Translation practitioner review**: Real-world testing
  - Test with 2-3 switch-reference language translators
  - Papua New Guinea languages (Kaluli, Fasu, Kobon)
  - Native American languages (Choctaw, Chickasaw)
  - Assess: Does participant tracking data help pronoun resolution?
- [ ] **Cross-linguistic translation validation (THESIS)**:
  - Identify 3-5 published Bible translations in switch-reference languages
  - Target languages from Stage 2:
    - **Papua New Guinea**: Kaluli, Fasu, Kobon (switch-reference obligatory)
    - **Native American**: Choctaw, Chickasaw (switch-reference obligatory)
    - **Turkish**: Evidentiality + tracking markers
  - Select 10-15 test verses with known participant tracking challenges
  - Analyze how these translations handled participant reference
  - Compare: Do translation choices align with TBTA predictions?
  - Document patterns: What strategies do translators use for Frame Inferable, Restaging?
  - Create: experiments/EXTERNAL-VALIDATION.md with cross-linguistic findings

---

## Known Issues & Technical Debt

### Issue 1: Participant Extraction Incompleteness

**Problem**: Manual text-based extraction missed 50-70% of participants
- Acts 2:1: Predicted 5, actual 19 (74% under-count)
- Ephesians 3:20: Predicted 4, actual 22 (82% under-count)

**Solution**: Extract participants from TBTA YAML first, THEN predict
**Status**: Methodological fix documented, not blocking

---

### Issue 2: Frame Database Incompleteness

**Current frames** (v1.0): 7 frames
- Creation, inn, household, legal, travel, meal, temple

**Missing frames** (identified in v2.0):
- Recognition/identification (added in v2.0)
- Possession
- Transformation
- Comparison

**Needed**: Systematic Biblical frame catalog
- Narrative frames (200+ verses)
- Epistle frames (theological exposition)
- Poetry frames (metaphorical language)
- Prophecy frames (vision/revelation)

**Status**: Frame expansion ongoing

---

### Issue 3: Presupposition Database Minimal

**Current presupposed entities**: God, Yahweh, Lord, Jesus (4 entities)

**Needed**:
- Major place names (Jerusalem, Egypt, Babylon)
- Cosmic entities (sun, moon, stars)
- Universal concepts (heaven, earth, sea)
- Cultural institutions (temple, Sabbath)

**Status**: Presupposition expansion needed

---

## Success Metrics & Exit Criteria

### Minimum Viable Product (MVP)

**Criteria for production deployment**:
- ✅ Algorithm achieves 80%+ accuracy on diverse test set
- ✅ Genre-stratified validation (narrative, epistle, poetry, prophecy)
- ✅ Systematic error patterns addressed (epistolary abstracts, quantifier+definite, recognition frame)
- ✅ Peer reviews passed (theological, linguistic, methodological)
- ✅ Translation practitioner validation positive

### Ideal Production-Ready

**Gold standard criteria**:
- ✅ Algorithm achieves 85%+ accuracy
- ✅ All 5 active states validated (Routine, Generic, Frame Inferable, First Mention, Interrogative)
- ✅ Rare states documented (Restaging, Integration, Exiting found and tested)
- ✅ External validation with real switch-reference translations
- ✅ Cross-linguistic testing (Hebrew, Greek, Septuagint)

---

## Timeline Estimate

**Critical path** (v2.0 validation → production):
- **Week 1**: Select NEW test set, apply v2.0, calculate accuracy
- **Week 2**:
  - If v2.0 ≥85%: Proceed to peer review (Stage 6)
  - If v2.0 80-84%: Refine to v2.1, re-test
  - If v2.0 <80%: Analyze errors, develop v3.0
- **Week 3-4**: Peer reviews (theological, linguistic, methodological, translation practitioner)
- **Week 5**: Integrate feedback, finalize documentation

**Total estimated**: 4-6 weeks to production-ready

**Rare state discovery** (optional, parallel track): 2-3 weeks

---

## Coordination with Other Features

### Upstream dependencies (none blocking)
- Discourse Genre: Would help genre detection (epistle vs. narrative)
- Surface Realization: Validates tracking → pronoun/noun choice correlation

### Downstream dependencies (this feature blocks)
- Switch-Reference (proposed NEW feature): Requires participant tracking for SS/DS morpheme selection
- Proximity System: Demonstrative choice depends on participant status (First Mention vs. Routine)

---

## Migration Status

**Completed**:
- [x] Migrated README.md (enhanced with experimental work)
- [x] Created experiments/ directory
- [x] Migrated LEARNINGS.md → experiments/LEARNINGS.md
- [x] Migrated ERROR-ANALYSIS.md → experiments/ERROR-ANALYSIS.md
- [x] Migrated PEER-REVIEW.md → experiments/PEER-REVIEW.md
- [x] Migrated COMPLETION-SUMMARY.md → experiments/COMPLETION-SUMMARY.md
- [x] Migrated experiment-001.md → experiments/PROMPT1.md
- [x] Migrated ALGORITHM-v2.0.md → experiments/PROMPT2.md
- [x] Created comprehensive TODO.md (this file)

**Remaining** (if needed):
- [ ] Check for train/test data in old adversarial-test/ and random-test/
- [ ] Migrate any test YAML files if present

---

**Last Updated**: 2025-11-15
**Status**: Stage 4 Complete (90%), Stage 5 Pending (v2.0 validation)
**Blocker**: v2.0 requires NEW test set (cannot use same 12 verses)
**Next Action**: Select test approach (adversarial, random, or cross-validation) and validate v2.0
