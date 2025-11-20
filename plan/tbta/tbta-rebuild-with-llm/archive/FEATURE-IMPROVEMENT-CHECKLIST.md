# TBTA Feature Improvement Checklist
## Feature-by-Feature Action Items

**Purpose**: Practical checklist for improving each feature based on FEATURE-QUALITY-ANALYSIS.md
**Format**: ✅ = Complete, 🟨 = Partial, ❌ = Missing, ⏭️ = Skip (not applicable)

---

## How to Use This Checklist

1. Pick a feature (start with Tier A)
2. Check which TIER 1-3 elements are complete/missing
3. Add missing elements (start with TIER 1)
4. Update this file as you complete items
5. When all TIER 1 complete → feature is "minimally useful"
6. When all TIER 1+2 complete → feature is "production-ready"
7. When all TIER 1+2+3 complete → feature is "excellent"

---

## TIER 1: MUST-HAVE (5 elements)
1. Translation Impact (2-3 sentences at top with star ratings)
2. Complete Value Enumeration (table with all possible values)
3. Baseline / Dominant Value (one statistic: "XX% are value Y")
4. Quick Translator Test (3-5 yes/no questions)
5. Concrete Verse Examples (3-5 minimum with reasoning)

## TIER 2: HIGH-VALUE (4 elements)
6. Hierarchical Prompt Template (5-level: theological → discourse → grammar → gateway → baseline)
7. Gateway Features / Correlations (what to check first, XX% correlation stats)
8. Common Errors & Solutions (3-5 error patterns with fixes)
9. Validation / Accuracy Metrics (tested on N verses, XX% accuracy)

## TIER 3: EXCELLENCE (4 elements)
10. Language Family Table (which families need this most, star ratings)
11. Cross-Linguistic Typology (summary of major patterns, WALS references)
12. Cross-Feature Interactions (which features correlate, validation rules)
13. Methodology / Annotation Process (step-by-step how to annotate)

---

## TIER A FEATURES (19 total - Essential)

### 1. Person System (Clusivity) ⭐ Priority 1
**Current**: person-systems/README.md (336 lines), clusivity experiments complete
**Status**: Very Good, missing prediction elements

| Element | Status | Notes |
|---------|--------|-------|
| 1. Translation Impact | ✅ | Executive summary present |
| 2. Value Enumeration | ✅ | 9 values documented |
| 3. Baseline | ❌ | Missing statistics (need: "XX% of 'we' are exclusive in narrative") |
| 4. Quick Test | 🟨 | Implicit in text, not formatted as checklist |
| 5. Examples | ✅ | 14 verses analyzed (7 inclusive + 7 exclusive) |
| 6. Prompt Template | ❌ | Missing hierarchical prompts (exists in TRANSFERABLE-LEARNINGS.md but not in README) |
| 7. Gateway Features | ❌ | Missing (e.g., "Check if speaker=divine → usually exclusive") |
| 8. Common Errors | 🟨 | Mentioned in context but not systematized |
| 9. Validation Metrics | ✅ | 100% accuracy (11/11), 98% translation consensus |
| 10. Language Family Table | ✅ | Extensive lists by family |
| 11. Typology | 🟨 | Lists languages but not typological patterns |
| 12. Cross-Features | ❌ | Missing |
| 13. Methodology | 🟨 | Validation workflow exists |

**Action Items**:
- [ ] Add baseline statistics (analyze 50-100 first-person plurals, calculate %)
- [ ] Format Quick Test as checklist: "1. Does your language have different words for inclusive vs exclusive 'we'? 2. ..."
- [ ] Extract prompt template from TRANSFERABLE-LEARNINGS.md into person-systems/METHODOLOGY.md
- [ ] Document gateway features: "If speaker=God + addressee=humans → 95% exclusive"
- [ ] Categorize common errors: "Error 1: Assuming all prayer is exclusive → Solution: Check if intercessory prayer"
- [ ] Consider splitting if adding TIER 2 makes README >200 lines

**Estimated effort**: 4-6 hours

---

### 2. Number System ⭐ Priority 2
**Current**: number-systems/README.md
**Status**: Good foundation, needs prediction method

| Element | Status | Notes |
|---------|--------|-------|
| 1. Translation Impact | ✅ | Shows impact on dual/trial/paucal languages |
| 2. Value Enumeration | ✅ | 8 values listed |
| 3. Baseline | ❌ | Need: "XX% of nouns are singular, YY% plural, ZZ% marked" |
| 4. Quick Test | ❌ | Missing checklist |
| 5. Examples | ✅ | Examples present |
| 6. Prompt Template | ❌ | Missing systematic prompts |
| 7. Gateway Features | ❌ | Missing (check: "If referent=Trinity → Trial?") |
| 8. Common Errors | 🟨 | LEARNINGS mentions semantic expansions |
| 9. Validation Metrics | 🟨 | 73-85% mentioned in RESULTS-ANALYSIS.md |
| 10. Language Family Table | ✅ | Good language examples |
| 11. Typology | 🟨 | Present but could be more systematic |
| 12. Cross-Features | ❌ | Missing |
| 13. Methodology | ✅ | Decent |

**Action Items**:
- [ ] Calculate baseline from sample (expect ~70% singular, ~25% plural, ~5% marked)
- [ ] Create Quick Test: "1. Does your language distinguish dual (exactly 2)? 2. Does your language distinguish trial (exactly 3)?"
- [ ] Build prompt template: Level 1 - Theological (Trinity=trial), Level 2 - Semantic (paired body parts=dual), Level 3 - Grammar (explicit quantifiers)
- [ ] Document gateway: "If semantic type=paired body part → 90% dual"
- [ ] Systematize errors: "Error 1: Missing TBTA semantic expansions (e.g., 'things' for actions)"

**Estimated effort**: 5-7 hours

---

### 3. Participant Tracking ⭐ Priority 2
**Current**: participant-tracking/README.md
**Status**: Good, needs formalization

| Element | Status | Notes |
|---------|--------|-------|
| 1. Translation Impact | ✅ | Shows importance for switch-reference, topic-marking |
| 2. Value Enumeration | ✅ | 9 states listed |
| 3. Baseline | ❌ | Need: "XX% are Routine (D)" |
| 4. Quick Test | ❌ | Missing |
| 5. Examples | ✅ | MAT 24:46-47 analyzed |
| 6. Prompt Template | ✅ | Three methods in PREDICTION-METHODS.md |
| 7. Gateway Features | ✅ | Surface form as proxy (pronouns → 100% Routine) |
| 8. Common Errors | ✅ | Presupposition errors documented |
| 9. Validation Metrics | ✅ | 90% accuracy, 100% method agreement |
| 10. Language Family Table | 🟨 | Examples present, could be table |
| 11. Typology | 🟨 | Discourse-level analysis present |
| 12. Cross-Features | 🟨 | Mentions NounListIndex, Surface Realization |
| 13. Methodology | ✅ | Excellent 3-method validation |

**Action Items**:
- [ ] Calculate baseline (expect ~60-70% Routine, ~15% First Mention, ~10% Frame Inferable, ~5% other)
- [ ] Create Quick Test: "1. Does your language mark topic vs new information? 2. Does your language require switch-reference?"
- [ ] Format gateway features as table: "Pronoun → 100% Routine"
- [ ] Convert language examples to family impact table

**Estimated effort**: 3-4 hours (mostly formatting, substance is strong)

---

### 4. Proximity System ⭐ Priority 2
**Current**: proximity/README.md, proximity/language-typology.md
**Status**: Good content, needs prediction focus

| Element | Status | Notes |
|---------|--------|-------|
| 1. Translation Impact | ✅ | Clear importance for demonstrative systems |
| 2. Value Enumeration | ✅ | 10 values (5 spatial, 2 temporal, 2 discourse, 1 N/A) |
| 3. Baseline | ❌ | Need: "XX% are unmarked/neutral proximity" |
| 4. Quick Test | ❌ | Missing |
| 5. Examples | ✅ | Examples present |
| 6. Prompt Template | 🟨 | Framework exists, needs formalization |
| 7. Gateway Features | ❌ | Missing |
| 8. Common Errors | ❌ | Missing |
| 9. Validation Metrics | ❌ | Framework stage, no testing yet |
| 10. Language Family Table | ✅ | Excellent language-typology.md |
| 11. Typology | ✅ | 6 system types documented |
| 12. Cross-Features | ❌ | Missing |
| 13. Methodology | 🟨 | Context-based rules present |

**Action Items**:
- [ ] Test framework on 50 verses, calculate baseline (expect ~40% unmarked, ~30% near, ~20% far, ~10% other)
- [ ] Create Quick Test: "1. Does your language distinguish near vs far demonstratives? 2. How many distance levels? 3. Does visibility matter?"
- [ ] Formalize prompt template from existing framework
- [ ] Document gateway: "Check illocutionary force (Interrogative often uses discourse proximity)"
- [ ] Run validation experiment to get accuracy metrics
- [ ] Categorize common errors from validation

**Estimated effort**: 8-10 hours (includes validation experiment)

---

### 5. Time Granularity ⭐ Priority 2
**Current**: time-granularity/README.md
**Status**: Good, needs validation

| Element | Status | Notes |
|---------|--------|-------|
| 1. Translation Impact | ✅ | Shows importance for temporal distance languages |
| 2. Value Enumeration | ✅ | 16+ time values |
| 3. Baseline | ❌ | Need: "XX% are Historic Past in narrative" |
| 4. Quick Test | ❌ | Missing |
| 5. Examples | ✅ | Examples present |
| 6. Prompt Template | 🟨 | Genre-based rules exist, need formalization |
| 7. Gateway Features | 🟨 | Mentions genre affects time, needs formalization |
| 8. Common Errors | ❌ | Missing |
| 9. Validation Metrics | ❌ | Framework stage, no testing |
| 10. Language Family Table | ✅ | Yagua, ChiBemba, Kiksht examples |
| 11. Typology | ✅ | Discourse-relative anchoring explained |
| 12. Cross-Features | 🟨 | Mentions Mood, Aspect, Genre |
| 13. Methodology | 🟨 | Genre-based approach documented |

**Action Items**:
- [ ] Sample 50 narrative verses + 50 teaching verses, calculate baselines by genre
- [ ] Create Quick Test: "1. Does your language distinguish multiple past tenses by distance? 2. How many past distinctions?"
- [ ] Formalize prompt: Level 1 - Genre (narrative → Historic Past), Level 2 - Discourse frame, Level 3 - Explicit markers
- [ ] Document gateway: "If Genre=Narrative + Mood=Indicative → 70% Historic Past"
- [ ] Run validation on 50 verses across genres
- [ ] Extract common errors from validation

**Estimated effort**: 8-10 hours (includes validation)

---

### 6. Aspect (Verb TAM) ✅ EXCELLENT
**Current**: verb-tam/ (aspect experiments, 98.1% accuracy)
**Status**: Production-ready, just needs formatting

| Element | Status | Notes |
|---------|--------|-------|
| 1. Translation Impact | ✅ | Clear |
| 2. Value Enumeration | ✅ | 9 aspect types |
| 3. Baseline | ✅ | **90.7% Unmarked** |
| 4. Quick Test | ❌ | Missing (easy to add) |
| 5. Examples | ✅ | Test cases documented |
| 6. Prompt Template | ✅ | Pattern-based rules |
| 7. Gateway Features | ✅ | **Mood → Aspect 100% correlation** |
| 8. Common Errors | ✅ | 1 error analyzed |
| 9. Validation Metrics | ✅ | **98.1% accuracy (53/54)** |
| 10. Language Family Table | 🟨 | Examples, not table |
| 11. Typology | 🟨 | Perfective/imperfective patterns |
| 12. Cross-Features | ✅ | Mood, Time correlations |
| 13. Methodology | ✅ | Excellent |

**Action Items**:
- [ ] Add Quick Test: "1. Does your language obligatorily mark perfective vs imperfective? 2. Does your language distinguish inceptive (begin) / cessative (stop)?"
- [ ] Format language examples as family table
- [ ] Ensure README ≤200 lines (move excess to METHODOLOGY.md if needed)

**Estimated effort**: 2-3 hours (mostly formatting)

---

### 7. Mood (Verb TAM) ⭐ Priority 1
**Current**: verb-tam/ (mood experiments, prediction methodology)
**Status**: Good prediction framework, needs comprehensive testing

| Element | Status | Notes |
|---------|--------|-------|
| 1. Translation Impact | ✅ | Clear |
| 2. Value Enumeration | ✅ | 7+ mood types with categories |
| 3. Baseline | ✅ | **94.62% Indicative in narrative** |
| 4. Quick Test | ❌ | Easy to add |
| 5. Examples | ✅ | Matthew 24 examples |
| 6. Prompt Template | ✅ | Prediction from Greek/Hebrew morphology + semantics |
| 7. Gateway Features | ✅ | Mood IS the gateway |
| 8. Common Errors | ✅ | Edge cases documented |
| 9. Validation Metrics | 🟨 | **Methodology defined, needs comprehensive testing (100+ verses)** |
| 10. Language Family Table | ✅ | Turkish, Japanese, Greek, Arabic |
| 11. Typology | ✅ | Linguistic categories |
| 12. Cross-Features | ✅ | Time, Aspect, Force correlations |
| 13. Methodology | ✅ | Step-by-step prediction (LLM prompts, not code) |

**Action Items**:
- [ ] Add Quick Test: "1. Does your language distinguish indicative vs subjunctive? 2. Does your language have obligation mood (must/should)?"
- [ ] Run comprehensive validation: Test prediction methodology on 100+ verses across genres
- [ ] Measure actual accuracy: Compare predictions to TBTA labels (expect 85-95%)
- [ ] Document systematic errors and refine prompts based on results

**Estimated effort**: 6-8 hours (includes comprehensive testing)

---

### 8-14. Speaker Demographics (6 features) ⭐ Priority 3
**Current**: honorifics-register/
**Status**: Good, part of honorifics experiments

All 6 features (Speaker, Listener, Speaker's Attitude, Speaker's Age, Speaker-Listener Age, Speech Style) are documented together.

| Element | Status | Notes |
|---------|--------|-------|
| 1. Translation Impact | ✅ | Clear importance for honorifics |
| 2. Value Enumeration | ✅ | Values per feature |
| 3. Baseline | ❌ | Need baselines per feature |
| 4. Quick Test | ❌ | Missing |
| 5. Examples | ✅ | Examples present |
| 6. Prompt Template | 🟨 | Contextual analysis present |
| 7. Gateway Features | ❌ | Missing |
| 8. Common Errors | ❌ | Missing |
| 9. Validation Metrics | ✅ | Part of honorifics experiments |
| 10. Language Family Table | ✅ | Japanese, Korean, Javanese, Thai |
| 11. Typology | ✅ | Multi-dimensional system |
| 12. Cross-Features | ✅ | All 6 interact |
| 13. Methodology | ✅ | Cultural translation documented |

**Action Items** (for all 6):
- [ ] Calculate baseline for each (e.g., "XX% of clauses have adult speaker")
- [ ] Create Quick Test: "1. Does your language have honorifics? 2. How many levels? 3. Does age difference matter?"
- [ ] Formalize prompt template for determining speaker/listener identity
- [ ] Document gateway: "If genre=epistle → check for 'I/we' to determine speaker"

**Estimated effort**: 5-7 hours (covers all 6 features)

---

### 15. Illocutionary Force ⭐ Priority 1
**Current**: illocutionary-force/README.md
**Status**: Good, needs prediction formalization

| Element | Status | Notes |
|---------|--------|-------|
| 1. Translation Impact | ✅ | Sentence particles in East Asian |
| 2. Value Enumeration | ✅ | Declarative, Interrogative, Imperative, etc. |
| 3. Baseline | ❌ | Need: "XX% declarative in narrative, YY% in teaching" |
| 4. Quick Test | ❌ | Missing |
| 5. Examples | ✅ | Examples present |
| 6. Prompt Template | 🟨 | Speech act analysis present, needs formalization |
| 7. Gateway Features | ❌ | Missing |
| 8. Common Errors | 🟨 | Rhetorical questions mentioned |
| 9. Validation Metrics | ✅ | Experiment complete |
| 10. Language Family Table | ✅ | Japanese, Mandarin, Korean examples |
| 11. Typology | ✅ | Speech act types |
| 12. Cross-Features | 🟨 | Mentions Mood, Rhetorical Question |
| 13. Methodology | ✅ | Speech act classification |

**Action Items**:
- [ ] Sample 100 clauses across genres, calculate baseline (expect ~60% declarative, ~20% imperative, ~15% interrogative, ~5% other)
- [ ] Create Quick Test: "1. Does your language require sentence-final particles? 2. Do declarative/interrogative/imperative use different particles?"
- [ ] Formalize prompt: Level 1 - Grammatical form (question mark → Interrogative), Level 2 - Context (rhetorical?), Level 3 - Genre patterns
- [ ] Document gateway: "If contains question word → 90% Interrogative (unless rhetorical)"
- [ ] Systematize rhetorical question handling

**Estimated effort**: 4-6 hours

---

### 16. Discourse Genre ⭐ Priority 1
**Current**: discourse-genre/README.md
**Status**: Good, needs prediction method

| Element | Status | Notes |
|---------|--------|-------|
| 1. Translation Impact | ✅ | Affects register, verb selection, clause structure |
| 2. Value Enumeration | ✅ | 6 major genres |
| 3. Baseline | ❌ | Need by book (e.g., "Gospels: XX% narrative, YY% teaching") |
| 4. Quick Test | ❌ | Missing |
| 5. Examples | ✅ | Examples present |
| 6. Prompt Template | 🟨 | Genre classification present, needs formalization |
| 7. Gateway Features | ✅ | **Genre is THE gateway** for many features |
| 8. Common Errors | 🟨 | Mixed genres mentioned |
| 9. Validation Metrics | ✅ | Experiment complete |
| 10. Language Family Table | ✅ | Examples per family |
| 11. Typology | ✅ | 6 major types |
| 12. Cross-Features | ✅ | Affects Aspect, Mood, Time, Honorifics, Structure |
| 13. Methodology | ✅ | Genre analysis documented |

**Action Items**:
- [ ] Create baseline table by book (e.g., "Genesis: 60% narrative, 20% genealogy, 15% dialogue, 5% other")
- [ ] Create Quick Test: "1. Does your language use different verb forms for narrative vs teaching? 2. Does register change by genre?"
- [ ] Formalize prompt: "Identify genre based on: 1. Book type (Gospel → narrative+teaching), 2. Passage structure, 3. Verb forms"
- [ ] Document as gateway: "Check genre FIRST, constrains Time/Aspect/Mood/Honorifics"

**Estimated effort**: 4-5 hours

---

### 17. Semantic Role ⭐⭐⭐ TOP PRIORITY (Tier A, no experiment)
**Current**: 101-noun-phrases/README.md
**Status**: Documented but no experiments

| Element | Status | Notes |
|---------|--------|-------|
| 1. Translation Impact | ✅ | Critical for ergative languages |
| 2. Value Enumeration | ✅ | Agent, Patient, Theme, etc. |
| 3. Baseline | ❌ | Need: "XX% Agent, YY% Patient in narrative" |
| 4. Quick Test | ❌ | URGENT - add this |
| 5. Examples | 🟨 | Examples exist, need more |
| 6. Prompt Template | ❌ | **URGENT** - create systematic prompts |
| 7. Gateway Features | ❌ | Missing |
| 8. Common Errors | ❌ | Missing |
| 9. Validation Metrics | ❌ | **NO EXPERIMENT YET** |
| 10. Language Family Table | 🟨 | Mentions ergative, need table |
| 11. Typology | 🟨 | Accusative vs ergative |
| 12. Cross-Features | 🟨 | Voice mentioned |
| 13. Methodology | 🟨 | Basic approach |

**Action Items** (HIGH PRIORITY):
- [ ] **Run validation experiment on 50 verses** (analyze all NPs, assign roles, test accuracy)
- [ ] Calculate baseline (expect ~40% Agent, ~30% Patient, ~15% Theme, ~15% other)
- [ ] Create Quick Test: "1. Is your language ergative? 2. Does word order determine semantic role? 3. Does case marking show agent/patient?"
- [ ] Build prompt template: Level 1 - Grammatical role (subject → usually agent), Level 2 - Verb semantics (who acts on whom?), Level 3 - Case marking
- [ ] Document gateway: "If Voice=Passive → subject is usually Patient not Agent"
- [ ] Create ergative language family table

**Estimated effort**: 10-12 hours (includes experiment)

---

### 18. Salience Band ⭐⭐⭐ TOP PRIORITY (Tier A, no experiment)
**Current**: Documented in FEATURE-SUMMARY.md
**Status**: Needs full feature directory

| Element | Status | Notes |
|---------|--------|-------|
| 1. Translation Impact | ❌ | Need to create |
| 2. Value Enumeration | ✅ | Pivotal, Primary, Secondary, Background, Setting |
| 3. Baseline | ❌ | URGENT |
| 4. Quick Test | ❌ | URGENT |
| 5. Examples | ❌ | Need to create |
| 6. Prompt Template | ❌ | **URGENT** |
| 7. Gateway Features | ❌ | Missing |
| 8. Common Errors | ❌ | Missing |
| 9. Validation Metrics | ❌ | **NO EXPERIMENT YET** |
| 10. Language Family Table | ❌ | Missing |
| 11. Typology | ❌ | Missing |
| 12. Cross-Features | 🟨 | Should correlate with Notional Structure |
| 13. Methodology | ❌ | Missing |

**Action Items** (HIGH PRIORITY):
- [ ] **Create features/105-clauses/salience-band/ directory**
- [ ] **Run experiment on narrative (Genesis 1, Matthew 24)** - analyze 50 clauses, determine salience
- [ ] Calculate baseline (expect ~5% Pivotal, ~25% Primary, ~40% Secondary, ~30% Background)
- [ ] Write README with translation impact: "Critical for Bantu participant tracking, foreground/background verb forms"
- [ ] Create Quick Test: "1. Does your language distinguish foreground vs background clauses? 2. Do verbs change form by salience?"
- [ ] Build prompt: Level 1 - Notional Structure (Climax → usually Pivotal), Level 2 - Participant Tracking (First Mention → higher salience), Level 3 - Discourse flow
- [ ] Document gateway: "If Notional Structure=Climax → 80% Pivotal or Primary salience"

**Estimated effort**: 12-15 hours (creating from scratch + experiment)

---

### 19. Topic NP ⭐⭐ HIGH PRIORITY (Tier A, no experiment)
**Current**: Documented in FEATURE-SUMMARY.md
**Status**: Needs validation

| Element | Status | Notes |
|---------|--------|-------|
| 1. Translation Impact | ✅ | Critical for topic-prominent languages |
| 2. Value Enumeration | 🟨 | Boolean or list of clause positions? |
| 3. Baseline | ❌ | Need: "XX% of clauses have explicit topic marking" |
| 4. Quick Test | ❌ | URGENT |
| 5. Examples | 🟨 | Generic examples, need specific verses |
| 6. Prompt Template | ❌ | **URGENT** |
| 7. Gateway Features | ❌ | Missing |
| 8. Common Errors | ❌ | Missing |
| 9. Validation Metrics | ❌ | **NO EXPERIMENT YET** |
| 10. Language Family Table | ✅ | Japanese, Korean, Mandarin |
| 11. Typology | ✅ | Topic-prominent explained |
| 12. Cross-Features | 🟨 | Participant Tracking, Surface Realization |
| 13. Methodology | 🟨 | Basic guidance |

**Action Items** (HIGH PRIORITY):
- [ ] **Run experiment on 50 clauses** (identify topics, test if TBTA marks them)
- [ ] Calculate baseline (expect ~30% have explicit topic marking)
- [ ] Create Quick Test: "1. Does your language have topic particles (wa, eun/neun)? 2. Is topic-comment structure different from subject-predicate?"
- [ ] Build prompt: Level 1 - Participant Tracking (Restaging → often topic), Level 2 - Discourse flow (shift → new topic), Level 3 - Syntactic position (fronting)
- [ ] Document gateway: "If Participant Tracking=Restaging → 70% is Topic NP"

**Estimated effort**: 8-10 hours (includes experiment)

---

## TIER B FEATURES (20 total - Important)

*For Tier B features, focus on TIER 1 only (5 must-haves). Full documentation below but less urgent than Tier A.*

### 20. Noun List Index ✅ Good
**Current**: participant-tracking/noun-index* files
**Status**: Algorithmic, 100% validation

**Action Items**:
- [ ] Add Quick Test: "1. Does your language use switch-reference?"
- [ ] Ensure baseline documented (per-verse reset rule)

**Estimated effort**: 2 hours

---

### 21. Surface Realization
**Current**: surface-realization/README.md
**Status**: Good, needs baseline

**Action Items**:
- [ ] Calculate baseline (expect ~40% Noun, ~35% Pronoun, ~15% Zero, ~10% other)
- [ ] Add Quick Test: "1. Is your language pro-drop (can omit pronouns)? 2. Does topic continuity affect whether you use noun vs pronoun?"
- [ ] Formalize prompt template from existing framework

**Estimated effort**: 4-5 hours

---

### 22. Polarity
**Current**: polarity/README.md
**Status**: Good content, needs TIER 1 completion

**Action Items**:
- [ ] Add Translation Impact summary at top
- [ ] Calculate baseline (expect ~85% Affirmative, ~15% Negative)
- [ ] Create Quick Test: "1. Is your language negative concord (multiple negatives = single negation)?"
- [ ] Add 3-5 verse examples with reasoning

**Estimated effort**: 4-5 hours

---

### 23. Clause Type
**Current**: Documented in FEATURE-SUMMARY.md
**Status**: Needs feature directory

**Action Items**:
- [ ] Create features/105-clauses/clause-type/ directory
- [ ] Calculate baseline (expect ~40% Independent, ~30% Dependent, ~20% Relative, ~10% other)
- [ ] Create Quick Test
- [ ] Run basic validation

**Estimated effort**: 6-8 hours

---

### 24-40. Remaining Tier B Features
*Documented in FEATURE-SUMMARY.md. Create feature directories + add TIER 1 elements when resources allow.*

Features include: Implicit Information, Rhetorical Question, Relativized, Sequence (multiple), Location in Discourse, Lexical Sense (multiple), Degree, Usage, Adjective Degree, Reflexivity, Target T/A/M, etc.

**Estimated effort per feature**: 5-8 hours (create directory + TIER 1)

---

## TIER C FEATURES (20 total - Nice-to-Have)

*For Tier C features, add minimal documentation (Translation Impact, Values, Examples only) when requested or needed for specific language families.*

Features include: Participant Status, Special Adpositions, Conjunction Implicit, Particle Types, Phrase Implicit flags, Thing Relationship, Phrasal Elements, Notional Structure (complete list), Alternative Analysis, Vocabulary Alternate, etc.

**Estimated effort per feature**: 3-5 hours (minimal documentation)

---

## Efficiency Strategies

### Batch Processing
Group similar tasks across features:
1. **Baseline calculation session** (1 day): Sample 50-100 instances per feature, calculate all baselines at once
2. **Quick Test creation session** (1 day): Write 3-5 question checklists for all features
3. **Prompt template session** (2-3 days): Adapt generic 5-level template to each feature
4. **Validation session** (3-5 days): Run blind tests on 20-50 verses per feature

### Parallel Work
Work on multiple features simultaneously:
- **Morning**: Run experiments (waiting on LLM responses)
- **Afternoon**: Write documentation (while experiments run)
- **Evening**: Calculate baselines and format results

### Template Reuse
Copy-paste patterns from excellent features:
- **Translation Impact**: Copy structure from Notional Structure
- **Quick Test**: Adapt Mood's format to other features
- **Prompt Template**: Start from GENERIC-FEATURE-TEMPLATE.md
- **Language Table**: Reuse table format from Honorifics

---

## Progress Tracking

### Phase 1: Tier A Foundation (Target: 5-10 days)
- [ ] Person System (4-6 hours)
- [ ] Number System (5-7 hours)
- [ ] Participant Tracking (3-4 hours)
- [ ] Proximity (8-10 hours)
- [ ] Time Granularity (8-10 hours)
- [ ] Aspect (2-3 hours)
- [ ] Mood (1 hour)
- [ ] Speaker Demographics 6 features (5-7 hours total)
- [ ] Illocutionary Force (4-6 hours)
- [ ] Discourse Genre (4-5 hours)
- [ ] **Semantic Role** ⭐⭐⭐ (10-12 hours)
- [ ] **Salience Band** ⭐⭐⭐ (12-15 hours)
- [ ] **Topic NP** ⭐⭐ (8-10 hours)

**Total**: ~75-105 hours = 10-13 working days (8 hours/day)

### Phase 2: Tier A Prediction (Target: 10-15 days)
Add TIER 2 elements to all 19 Tier A features

**Total**: ~76-114 hours = 10-14 working days

### Phase 3: Tier B Foundation (Target: 5-7 days)
Add TIER 1 to all 20 Tier B features

**Total**: ~100-160 hours = 13-20 working days (can prioritize top 10)

---

## Summary Statistics

**Current State**:
- 19 Tier A features: 13 have experiments (68%)
- Documentation quality varies widely
- 3-5 features are excellent (Mood, Aspect, Notional Structure)
- 5-8 features are very good but missing elements
- 6+ features need significant work

**After Phase 1** (Tier A TIER 1 complete):
- All 19 Tier A features: Minimally useful for translators
- Can answer "Does my language need this?" in <5 minutes per feature
- Baseline gives instant 80-90% accuracy without complex analysis

**After Phase 2** (Tier A TIER 1+2 complete):
- All 19 Tier A features: Production-ready for AI prediction
- 85%+ accuracy achievable with prompt templates
- Systematic and reproducible across all features

**After Phase 3** (Tier B TIER 1 complete):
- 39/59 features documented to minimum standard
- Covers 95% of translation needs across all language families

---

## Next Steps

1. Review this checklist with team
2. Prioritize features based on:
   - Language family urgency (which languages need which features most?)
   - Tier (A > B > C)
   - Missing elements (TIER 1 > TIER 2 > TIER 3)
   - Current state (partially complete > needs experiment > needs creation)
3. Start with **Top 3 Priorities**:
   - ⭐⭐⭐ Semantic Role (Tier A, no experiment, critical for ergative)
   - ⭐⭐⭐ Salience Band (Tier A, no experiment, critical for Bantu)
   - ⭐⭐ Topic NP (Tier A, no experiment, critical for East Asian)
4. Work through Tier A features systematically
5. Update this checklist as features complete
6. Celebrate progress! 🎉

---

**Document Version**: 1.0
**Last Updated**: 2025-11-06
**See Also**: FEATURE-QUALITY-ANALYSIS.md (the "why" and analysis)
