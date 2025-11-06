# TBTA Reproduction - Corrected Execution Plan

**Purpose**: Define proper methodology for comprehensive TBTA reproduction based on lessons learned

**Estimated Timeline**: 8-12 weeks full-time effort
**Estimated Output**: 57 features documented, 1,009 languages covered, 400+ verses validated

---

## Phase 0: Pre-Planning (3-5 days)

### Task 0.1: Complete Feature Inventory
**Duration**: 1 day
**Output**: `FEATURE-CHECKLIST.md`

1. Read TBTA README exhaustively
2. Extract EVERY feature mentioned
3. Organize by:
   - Part of speech category (Noun, Verb, Adj, Adv, Adposition, Conjunction, Phrasal, Particle)
   - Phrase level (NP, VP, AdjP, AdvP)
   - Clause level
   - Paragraph/Episode level
4. Create visual progress tracker (0/57 complete)
5. Priority ranking (Critical, High, Medium, Low)

**Deliverable**: Markdown file with complete feature list and checkboxes

---

### Task 0.2: Test Set Design
**Duration**: 2 days
**Output**: `TEST-SET-DESIGN.md` + verse selection list

**Stratification requirements**:

| Genre | Books | Min Verses | Max Verses | Features Tested |
|-------|-------|-----------|------------|-----------------|
| Narrative | Genesis, Exodus, Matthew, Luke, Acts | 60 | 80 | Participant tracking, time remoteness, coordination |
| Poetry | Psalms, Job, Song of Songs | 50 | 60 | Parallelism, metaphor, vocatives, gnomic aspect |
| Prophecy | Isaiah, Jeremiah, Ezekiel | 50 | 60 | Prophetic perfect, performative, obligation |
| Wisdom | Proverbs, Ecclesiastes | 30 | 40 | Generic reference, gnomic aspect, conditionals |
| Epistles | Romans, 1 Cor, Galatians, Hebrews | 50 | 60 | Clusivity, theological discourse, argumentation |
| Genealogy | 1 Chronicles, Matthew 1 | 15 | 20 | Formulaic structure, coreference tracking |
| Law | Leviticus, Deuteronomy | 30 | 40 | Obligation modality, case law, conditionals |
| Apocalyptic | Daniel, Revelation | 30 | 40 | Symbolic participants, complex temporal |
| **Total** | **15+ books** | **315** | **400** | **All 57 features** |

**Additional stratification**:
- Verse length: 25% short (1-5 words), 50% medium (6-15 words), 25% long (16+ words)
- Complexity: 50% simple, 30% moderate, 20% complex (embedded clauses)
- Language features: Include verses with dual number, rare moods, evidential contexts

**Process**:
1. Select candidate verses randomly from each genre
2. Verify TBTA annotations available for each verse
3. Download and save TBTA gold standard
4. Organize by genre for systematic testing

**Deliverable**:
- List of 400 verse references
- TBTA JSON files for all 400 verses
- Genre/complexity metadata

---

### Task 0.3: Language Research Plan
**Duration**: 1 day
**Output**: `LANGUAGE-RESEARCH-PLAN.md`

**Structure to create**:
```
language-research/
├── families/
│   ├── austronesian/
│   │   ├── README.md              # Family summary
│   │   ├── philippine/
│   │   │   ├── README.md          # Sub-family summary
│   │   │   ├── languages/
│   │   │   │   ├── tgl-tagalog.md
│   │   │   │   ├── ceb-cebuano.md
│   │   │   │   └── ... (45 languages)
│   │   ├── oceanic/
│   │   │   ├── melanesian/
│   │   │   ├── polynesian/
│   │   │   └── micronesian/
│   │   └── indonesian/
│   ├── trans-new-guinea/
│   │   └── ... (129 languages)
│   └── ... (all families)
└── index/
    ├── by-iso-code.md             # Alphabetical index
    ├── by-speaker-count.md        # By population
    └── by-tbta-priority.md        # By translation priority
```

**Per-language template** (3-5 pages):
- ISO 639-3 code
- Family/sub-family path
- Geographic location, speaker population
- Bible translation status (which books available)
- Typological profile (morphology, word order, alignment)
- **Features inherited from family** (reference family doc)
- **Unique features specific to this language**
- **TBTA feature applicability matrix** (which features critical/relevant/irrelevant)
- Example verses showing unique features
- **Sources**: 3-10 scholarly sources (grammars, linguistic papers)

**Deliverable**:
- Directory structure created
- Template markdown file
- Research workflow documented

---

### Task 0.4: Execution Timeline
**Duration**: 1 day
**Output**: `EXECUTION-TIMELINE.md` with Gantt chart

**Phases**:
1. Phase 1: Feature documentation (3-4 weeks)
2. Phase 2: Language documentation (2-3 weeks)
3. Phase 3: Feature reproduction experiments (2-3 weeks)
4. Phase 4: Integration testing (1 week)
5. Phase 5: Synthesis & deliverables (1 week)

**Dependencies mapped**
**Resource allocation** (if parallel agents)
**Risk mitigation** (what if agent fails, data unavailable, etc.)

---

## Phase 1: Complete Feature Documentation (3-4 weeks)

### Approach: 3 features per week, 20 weeks → optimize to 3-4 weeks via parallelization

---

### Week 1: Critical Priority Features (7 features)

#### Day 1-2: Person Systems
**Agent task**: Research person marking cross-linguistically
**Output**: `features/person/README.md` + `LEARNINGS.md`

**Coverage**:
- First, Second, Third person
- Inclusive vs. Exclusive (critical for Austronesian)
- Formal vs. Informal (T-V distinction)
- Obviation (fourth person in Algonquian)
- Logophoric pronouns (African languages)
- How marked: pronouns, verb agreement, both

**Cross-linguistic survey**:
- Which of our 1,009 languages have clusivity
- Which have formal/informal distinction
- Which have obviation
- Mapping to TBTA person values

**Experimentation**:
- Test on 20 verses with 1st/2nd person pronouns
- Epistles critical: Romans "we", Acts "we-passages"
- Calculate accuracy

#### Day 3-4: Lexical Sense Disambiguation
**Agent task**: Research polysemy and sense disambiguation
**Output**: `features/lexical-sense/README.md` + `LEARNINGS.md`

**Coverage**:
- What is lexical sense (A, B, C...)
- How TBTA distinguishes senses
- Polysemy vs. homonymy
- Context-based disambiguation

**Methodology**:
- Identify polysemous words in test set
- Use context to select sense
- Compare with TBTA's sense assignment

**Example**: Hebrew רוּחַ (ruach)
- Sense A: wind, breath
- Sense B: spirit, Spirit (of God)
- How to disambiguate from context

#### Day 5-7: Semantic Roles
**Agent task**: Research semantic role typology
**Output**: `features/semantic-roles/README.md` + `LEARNINGS.md`

**Coverage**:
- Agent, Patient, Theme, Experiencer
- Source, Goal, Location
- Instrument, Beneficiary, Comitative
- How languages mark roles (case, adpositions, word order)
- Ergative vs. accusative alignment

**Critical for**:
- Mapping to ergative languages (Mayan, Australian, Basque)
- Understanding voice systems (Austronesian)
- Passivization

**Experimentation**:
- Annotate semantic roles for 30 verses
- Test on diverse constructions (active, passive, ergative)
- Compare with TBTA

#### Parallel Tasks (Days 1-7):

**Agent 2**: Noun List Index (Coreference Tracking)
- How TBTA tracks coreferents (1-9, A-Z, a-z)
- Cross-verse tracking
- Pronoun antecedent resolution
- Experiment on 20-verse passage

**Agent 3**: Quotation Marking (Particle Features)
- QuoteBegin, QuoteEnd particles
- Direct vs. indirect speech
- Nested quotations
- Speaker/Listener tracking integration
- Experiment on dialogue-heavy passages (Genesis 3, John 4)

**Agent 4**: Illocutionary Force
- Statement, Question, Command, Exclamation
- Rhetorical questions
- How to distinguish from syntax
- Experiment on Proverbs (imperatives), Psalms (vocatives)

**Agent 5**: Reflexivity
- Reciprocal vs. Reflexive
- Middle voice
- How languages mark (morphology, pronouns, context)
- Experiment on 20 verses with reflexive pronouns

---

### Week 2: High Priority Features (8 features)

#### Continue pattern with parallel agents...

**Features to cover**:
- Surface Realization (Noun vs. PRO vs. Personal Pronoun)
- Participant Status (Protagonist/Antagonist/Major Participant)
- Semantic Complexity Level (1-5 scale)
- Clause Type (Main, Subordinate, Relative, Complement)
- Salience Band (Pivotal, Primary, Secondary, Backgrounded)
- Speaker/Listener (Who's speaking to whom)
- Target Tense/Aspect/Mood (Language-specific guidance)
- Discourse Genre (Narrative, Direct Speech, Prayer, etc.)

**Each feature needs**:
- README.md: Linguistic theory, cross-linguistic survey, citations
- LEARNINGS.md: Methodology, decision tree, expected accuracy
- Experiment on relevant test verses
- Integration with other features

---

### Week 3-4: Medium & Lower Priority Features

**Medium Priority** (4 features):
- Adposition features (semantic role marking, polarity)
- Conjunction features (Implicit, type, coordination)
- Phrasal features (multi-word units, serial verbs)
- Sequence (coordination tracking)

**Lower Priority** (4 features):
- Thing-Thing Relationship (genitive, possessive)
- Relativized (relative clause presence)
- Rhetorical Question
- Paragraph/Episode boundaries

**Process**: 2-3 features per day with parallel agents

---

## Phase 2: Language Documentation (2-3 weeks)

### Approach: Hierarchical with parallelization

---

### Week 1: Top 100 Languages (by speaker count)

**Why start with high-population languages**:
- Better resources available
- More grammars published
- Higher translation priority
- Affects more people

**Process** (8 agents in parallel):
- Agent 1: Languages 1-12
- Agent 2: Languages 13-25
- ...
- Agent 8: Languages 88-100

**Each agent produces**:
- Individual language files (tgl-tagalog.md, etc.)
- 3-5 pages per language
- 3-10 scholarly sources cited
- TBTA feature applicability matrix

**Quality check**: Spot-check 10 random files for completeness

---

### Week 2: Remaining 909 Languages

**Batch by family** for efficiency:
- Austronesian: 172 languages (2-3 days, 8 agents = 21 langs each)
- Trans-New Guinea: 129 languages (2 days, 8 agents = 16 langs each)
- Indo-European: 135 languages (2 days, 8 agents = 17 langs each)
- Niger-Congo: 94 languages (1.5 days, 8 agents = 12 langs each)
- Other families: 379 languages (3-4 days)

**Process**:
1. Agent reads family summary
2. Identifies shared features
3. For each language, documents:
   - What's shared with family
   - What's unique to this language
   - Sources consulted

**Output**: 1,009 language files, 3,000-5,000 pages total

---

### Week 3: Indexing & Cross-Referencing

**Create indices**:
- Alphabetical by ISO code
- By speaker population
- By translation priority
- By family
- By unique features (languages with dual, trial, evidentiality, etc.)

**Cross-reference**:
- Link languages to relevant feature documentation
- Link features to languages that use them
- Create decision trees: "If target language is X, focus on features Y, Z"

---

## Phase 3: Feature Reproduction Experiments (2-3 weeks)

### Approach: Systematic testing of all 57 features across 400-verse test set

---

### Week 1: Word-Level Features (Days 1-5)

**Process** (per feature):
1. Apply methodology to all 400 test verses
2. For each verse, annotate feature
3. Compare with TBTA gold standard
4. Calculate accuracy overall and by genre
5. Identify failure patterns
6. Refine methodology
7. Re-test on failures
8. Document final accuracy and edge cases

**Features to test** (8 agents in parallel):
- Agent 1: Participant Tracking (400 verses × avg 5 nouns = 2,000 annotations)
- Agent 2: Number (same)
- Agent 3: Person (same)
- Agent 4: Proximity (same)
- Agent 5: Surface Realization (same)
- Agent 6: Participant Status (same)
- Agent 7: Polarity (nouns)
- Agent 8: Lexical Sense (nouns)

**Output per feature**:
- `experiment-genre-narrative.md`
- `experiment-genre-poetry.md`
- `experiment-genre-prophecy.md`
- ... (8 genre-specific experiments)
- `experiment-summary.md` (overall accuracy, patterns)

---

### Week 2: Verb & Modifier Features (Days 6-10)

**Verb features** (parallel agents):
- Time (400 verses × avg 3 verbs = 1,200 annotations)
- Aspect
- Mood
- Reflexivity
- Polarity
- Adjective Degree
- Lexical Sense

**Modifier features**:
- Adjective Degree
- Adverb Degree

**Same process**: Annotate, compare, calculate accuracy by genre, refine

---

### Week 3: Phrase & Clause Features (Days 11-15)

**Phrase-level** (parallel agents):
- Semantic Roles (NP level)
- Sequence (coordination)
- Thing-Thing Relationship
- Implicit
- Relativized

**Clause-level**:
- Illocutionary Force
- Clause Type
- Speaker/Listener
- Discourse Genre
- Salience Band
- Rhetorical Question

**Structural**:
- Paragraph boundaries
- Episode boundaries

**Process**: Same as above

---

### Output of Phase 3:

**For each of 57 features**:
- Overall accuracy (e.g., 94.2%)
- Accuracy by genre:
  - Narrative: 95.1%
  - Poetry: 87.3%
  - Prophecy: 91.2%
  - Wisdom: 93.7%
  - Epistles: 89.4%
  - Genealogy: 98.2%
  - Law: 92.1%
  - Apocalyptic: 86.5%
- Common error patterns
- Refined methodology
- Edge cases documented

**Aggregate statistics**:
- Features >95% accuracy (fully automated)
- Features 85-95% accuracy (semi-automated with review)
- Features <85% accuracy (human-assisted)

---

## Phase 4: Integration Testing (1 week)

### Task: Test ALL 57 features together on fresh data

---

### Day 1-2: Fresh Test Set Selection

**Select 100 new verses** (not used in Phase 3):
- 15 narrative
- 12 poetry
- 12 prophecy
- 10 wisdom
- 15 epistles
- 8 genealogy
- 12 law
- 10 apocalyptic
- **6 "wildcard"** (unusual verses, edge cases)

**Download TBTA annotations** for all 100 verses

---

### Day 3-5: Full Annotation

**For each verse**:
1. Apply ALL 57 feature methodologies
2. Generate complete TBTA-style annotation
3. Compare with gold standard field-by-field
4. Track which features match/mismatch

**Metrics**:
- Overall accuracy (all features, all verses)
- Per-feature accuracy
- Per-genre accuracy
- Per-verse accuracy (did we get the whole verse right?)

---

### Day 6-7: Analysis & Refinement

**Identify**:
- Feature interaction issues (does proximity affect participant tracking?)
- Genre-specific challenges (poetry harder than narrative?)
- Systematic errors (always wrong on X?)

**Refine**:
- Update methodologies based on integration failures
- Re-test on failures
- Document final accuracy

**Output**:
- `integration-test-results.md`
- `feature-interaction-analysis.md`
- `final-accuracy-by-genre.md`

---

## Phase 5: Synthesis & Deliverables (1 week)

### Day 1-2: Reproduction Prompt

**Create comprehensive prompt** (20,000-30,000 words):
- Introduction to TBTA
- All 57 features explained
- Decision trees for each feature
- Genre-specific guidance
- 10-15 fully worked examples (across genres)
- Output format specification (JSON schema)
- Validation checklist
- Common errors to avoid

**Test prompt**:
- Give to fresh AI instance
- Have it annotate 20 verses
- Measure accuracy
- Refine prompt based on results

---

### Day 3-4: Language Adaptation Guides

**Create adaptation guide for each family**:
- Which features are critical
- Which are irrelevant
- Feature interaction in this family
- Example language-specific workflows

**Deliverables**:
- 10 family-specific guides (major families)
- 50 language-specific guides (top 50 languages)
- Index linking all 1,009 languages to relevant guides

---

### Day 5: Improvements Documentation

**Document**:
- Schema extensions (with evidence from experiments)
- Automation roadmap (with actual accuracy data)
- Methodology improvements
- Future research directions

---

### Day 6-7: Executive Summary & Documentation

**Create**:
- Honest executive summary (with limitations acknowledged)
- Project completion report
- Future work recommendations
- User guides for translators

**Update**:
- All accuracy claims with genre breakdowns
- All documentation with cross-references
- README files at every level

---

## Quality Assurance Throughout

### After Each Phase:

1. **Completeness check**: Did we cover everything planned?
2. **Accuracy check**: Spot-check 10% of outputs
3. **Citation check**: All claims have sources?
4. **Cross-reference check**: Links work, no broken references?
5. **User testing**: Can someone else understand the docs?

### Red Flags to Watch:

- Accuracy claims without genre breakdown
- Features documented but not tested
- Languages documented without sources cited
- Test sets that aren't diverse
- Premature "completion" announcements

---

## Success Criteria

### Minimum for "TBTA Reproduction Complete":

- ✅ All 57 features documented (README + LEARNINGS)
- ✅ All 57 features tested on 400-verse diverse set
- ✅ Accuracy >80% on EACH feature (averaged across genres)
- ✅ Accuracy >85% overall (all features, all verses)
- ✅ All 1,009 languages have individual documentation
- ✅ Test coverage across 8+ genres
- ✅ Integration test on 100 fresh verses passes
- ✅ Reproduction prompt achieves >80% accuracy when used by others

### Optional for "Comprehensive":

- All 57 features >90% accuracy
- 1,000+ verse test set
- Multiple AI systems tested (Claude, GPT-4, etc.)
- Human annotator comparison (inter-annotator agreement)
- Published paper documenting methodology

---

## Resource Requirements

### Time:
- **Minimum**: 8 weeks full-time (320 hours)
- **Comfortable**: 10 weeks full-time (400 hours)
- **Comprehensive**: 12 weeks full-time (480 hours)

### Compute:
- 8 parallel AI agents for 8 weeks
- ~320 agent-hours (if 8 agents × 40 hours/week × 8 weeks / 8 parallel = 40 hours per agent)
- API costs: $500-2,000 depending on model choice

### Data:
- TBTA database (free, publicly available)
- Bible texts in 1,009 languages (mostly free, some restricted)
- Scholarly papers (university access or $500-1,000 for purchases)
- Grammars ($1,000-3,000 for 1,009 language grammars - many free via SIL)

---

## Comparison: Original vs. Corrected Plan

| Aspect | Original Plan | Corrected Plan |
|--------|--------------|----------------|
| Timeline | 12 hours | 8-12 weeks |
| Features covered | 6 | 57 |
| Features tested | 3 | 57 |
| Test verses | 20 | 400 |
| Genres | 1 (narrative) | 8 |
| Languages documented | 0 individual | 1,009 individual |
| Accuracy claims | 97.8% overall | Per-feature, per-genre |
| Production ready | Claimed yes | Only after completion |
| **Realism** | **Overoptimistic** | **Realistic** |

---

## Conclusion

The original 12-hour attempt was a **proof of concept**, not a complete reproduction.

This corrected plan provides a **realistic roadmap** to:
- Cover all 57 TBTA features
- Document all 1,009 languages individually
- Test across 8 genres with 400+ verses
- Achieve validated accuracy claims
- Produce production-ready deliverables

**Estimated effort**: 8-12 weeks full-time work
**Estimated cost**: $1,500-5,000 (compute + resources)
**Output**: Comprehensive, validated, honest TBTA reproduction

---

**Document Status**: Corrected Execution Plan
**Next Action**: Use this plan if attempting TBTA reproduction again
**Key Learning**: Ambitious goals need realistic timelines
