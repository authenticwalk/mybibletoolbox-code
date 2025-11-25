# Participant Tracking

**Status**: 🟨 Stage 4 (Refinement) • **Accuracy**: 90% (test set)
**Priority**: Tier A (Critical for 200+ switch-reference languages)
**Source**: TBTA original

---

## Purpose (100 lines)

### What is Participant Tracking?

Participant tracking marks the **discourse status** of referents (people, entities) in a narrative or dialogue. It answers: "How should this referent be introduced or referenced based on its role in the ongoing discourse?"

**Five core values**:
1. **First Mention**: Entity introduced for the first time
2. **Routine**: Entity continues as active participant
3. **Exiting**: Entity explicitly leaves the scene
4. **Restaging**: Previously mentioned entity returns after absence
5. **Frame Inferable**: Entity inferable from context but not explicitly mentioned

### Why This Matters

**Pronoun Clarity Crisis**: Genesis 4:8 - "Cain said to Abel his brother... Cain rose up against Abel his brother and killed him."

English repeats names for clarity. But in 200+ switch-reference languages (Papua New Guinea, Native American), pronouns REQUIRE grammatical marking to show whether subject changed between clauses.

**Without participant tracking**:
- Translator guesses whether to use "he₁" (same subject) or "he₂" (different subject)
- Wrong choice = theological error (who killed whom?)
- Ambiguity in prophecy, narrative sequences, quoted speech

**With participant tracking**:
- Genesis 4:8: Cain (Routine) → Abel (Restaging) → Cain (Routine) → Abel (Exiting)
- Clear pronoun reference chain for switch-reference languages

### Languages Affected (200+)

**Primary users** (grammatically obligatory):
- **Papua New Guinea**: Kaluli, Fasu, Kobon, Telefol (80+ Trans-New Guinea languages)
- **Native American**: Choctaw, Chickasaw, Mandan, Comanche
- **Others**: Turkish (evidentiality + tracking), Korean (topic/focus)

**Secondary users** (optional but helpful):
- Japanese (wa/ga topic marking)
- Chinese (topic-comment structure)
- Russian (pro-drop with ambiguity)

### Translation Impact Example

**Genesis 19:30-33** (Lot and his daughters)
- v30: Lot (First Mention in new scene)
- v31: Older daughter (First Mention)
- v32: "our father" (Routine - Lot still active)
- v33: Lot (Routine) → daughters (Routine)

**Switch-reference language needs**:
- "He went" - Which "he"? Same as previous clause subject?
- Participant tracking resolves: Lot (Routine) = same subject marker
- Daughters (Restaging after v31) = different subject marker

---

## Methodology (250 lines)

### Decision Tree for Participant Tracking

```
INPUT: Referent mention in verse context
  ├─ Has this entity been mentioned in this pericope?
  │   NO → Check if inferable from frame
  │   │    ├─ YES (e.g., "the priest" in temple scene) → FRAME_INFERABLE
  │   │    └─ NO → FIRST_MENTION
  │   YES → Continue
  │
  ├─ Was entity mentioned in immediately prior verse/clause?
  │   YES → Check discourse continuity
  │   │    ├─ Entity still active participant → ROUTINE
  │   │    ├─ Entity explicitly leaving/dying/departing → EXITING
  │   │    └─ Unclear → Check genre + grammatical cues
  │   NO → Entity was mentioned earlier but not recently
  │        → RESTAGING
  │
  └─ SPECIAL CASES:
      ├─ Quoted speech: Reset context (new discourse world)
      ├─ Vision/dream: Separate tracking from narrative frame
      ├─ Prophetic: Future entities = FIRST_MENTION even if known from past
      └─ Genealogy: Each generation = new FIRST_MENTION context
```

### Grammatical and Discourse Cues

**First Mention Indicators**:
- Introduction formula: "Now there was a man..." (Genesis 1:1)
- Indefinite article: "a certain man" (Luke 10:30)
- Relative clause: "the one who..." (first time specified)
- New pericope boundary with scene change

**Routine Indicators**:
- Immediate subject continuity: "He said... He went... He saw..."
- Pronoun without ambiguity in prior clause
- Same-subject participial constructions
- No intervening participants

**Exiting Indicators**:
- Death verbs: "and he died" (genealogies)
- Departure verbs: "he went away" with finality
- Scene change where entity not mentioned in new scene
- Explicit narrative closure: "So Esau returned... and Jacob remained"

**Restaging Indicators**:
- Return after absence: "Now Esau came" (after Jacob focus)
- Resumptive device: "As for Joseph..." (narrative resumption)
- Explicit re-introduction: "Remember Moses? He..."
- Topic shift back to earlier participant

**Frame Inferable**:
- Role-based inference: "the priest" (in temple context, role assumed)
- Location-based: "the owner" (of house just mentioned)
- Institutional: "the king" (in royal court narrative, identity inferable)
- Cultural script: "the servants" (in household scene)

### Genre-Specific Patterns

**Narrative (most common)**:
- Clear First Mention → Routine → Exiting/Restaging cycles
- Participant tracking mirrors plot structure
- Scene changes trigger Restaging

**Genealogy**:
- Each generation = new First Mention context
- "X begat Y" = Y is First Mention (even if Y later becomes father)
- Exiting common: "and he died" formula

**Prophecy**:
- Future entities: First Mention even if historical figure known
- "A virgin shall conceive" = First Mention in prophetic frame
- Switch between prophet voice (Routine) and divine voice (Restaging)

**Epistle/Legal**:
- Abstract entities: "faith" (First Mention when introduced as topic)
- Repeated concepts: Routine when actively discussed
- Frame Inferable common: "the law" (assumed in Jewish context)

**Poetry**:
- Parallelism: Routine if second line = restatement
- First Mention if second line = new entity
- Frame Inferable in cultic/wisdom contexts

### Multi-Factor Convergence

**When cues conflict**:
1. **Grammatical > Discourse**: Explicit Greek/Hebrew marking wins
2. **Immediate context > Distant context**: ±3 verses > chapter level
3. **Narrative structure > Surface form**: Scene boundary > same sentence
4. **Translation consensus > Inference**: If 3+ translations agree, likely correct

**Example (Genesis 37:18-20)**:
- v18: Brothers (Routine from v12-17)
- v19: "Here comes that dreamer" (Restaging - Joseph after long absence)
- v20: "us" (Routine - brothers continuous)

**Conflict**: v19 uses demonstrative ("that") suggesting Restaging, but brothers were just discussing Joseph (v18) suggesting Routine.

**Resolution**: Restaging wins - Joseph physically absent since v17, demonstrative signals reintroduction into visual field.

### Algorithm Approach (Current - 90% accuracy)

**Prompt structure** (PROMPT3.md - current best):

```
INPUTS:
- Current verse reference
- Verse text (English + Greek/Hebrew if available)
- Prior 3 verses for context
- Next 1 verse for forward reference
- Book/chapter info (genre, narrative arc)

PROCESS:
1. Identify all referents (nouns, pronouns)
2. For each referent:
   a. Search prior verses (scope: current pericope)
   b. Check grammatical marking (articles, demonstratives)
   c. Assess discourse continuity
   d. Apply genre-specific rules
3. Classify: FIRST_MENTION | ROUTINE | EXITING | RESTAGING | FRAME_INFERABLE

OUTPUT:
- Referent (English form)
- Participant status (value)
- Rationale (2-3 sentences)
- Confidence (high/medium if ambiguous)
```

**Known blind spots (10% error rate)**:
- Quoted speech transitions (speaker changes unclear)
- Vision/dream boundaries (narrative frame vs. internal world)
- Implicit role shifts ("the man" → "the king" = same person)
- Collective-to-individual reference ("Israel" → "he")

---

## Output Schema (120 lines)

### YAML Structure

```yaml
verse: "{BOOK} {chapter}:{verse}"
participant_tracking:
  - referent: "string"              # English noun/pronoun
    surface_form: "string"          # Exact text from verse
    participant_status: "enum"      # FIRST_MENTION|ROUTINE|EXITING|RESTAGING|FRAME_INFERABLE
    rationale: "string"             # 2-3 sentences explaining decision
    confidence: "enum"              # high|medium (if ambiguous)
    prior_mention: "string|null"    # Verse reference of prior mention (if applicable)
    grammatical_cues: ["array"]     # Greek/Hebrew markers
    discourse_cues: ["array"]       # Contextual signals
citations:
  - "{source-id}: {detail}"         # Inline citations for sources consulted
metadata:
  genre: "string"                   # narrative|prophecy|epistle|poetry|genealogy|legal
  pericope: "string"                # Textual unit (e.g., "Genesis 4:1-16 Cain and Abel")
  translation_notes: "string"       # Special considerations for target languages
```

### Real Examples

**Example 1: Genesis 4:8 (Cain and Abel)**
```yaml
verse: "GEN 4:8"
participant_tracking:
  - referent: "Cain"
    surface_form: "Cain"
    participant_status: "ROUTINE"
    rationale: "Cain is continuous subject from v3-7. No scene change. Immediate subject continuity."
    confidence: "high"
    prior_mention: "GEN 4:3"
    grammatical_cues: ["proper_name_repeated"]
    discourse_cues: ["same_subject_chain", "no_intervening_participants"]

  - referent: "Abel"
    surface_form: "Abel his brother"
    participant_status: "RESTAGING"
    rationale: "Abel not mentioned since v4 (offering). Reintroduced here as recipient of Cain's speech. Genitive phrase 'his brother' signals relational restaging."
    confidence: "high"
    prior_mention: "GEN 4:4"
    grammatical_cues: ["proper_name", "possessive_construction"]
    discourse_cues: ["absent_for_3_verses", "reintroduced_as_addressee"]

  - referent: "Cain"
    surface_form: "Cain"
    participant_status: "ROUTINE"
    rationale: "Subject continuity within same verse. Cain initiates action sequence (said → rose → killed)."
    confidence: "high"
    prior_mention: "GEN 4:8a"
    grammatical_cues: ["same_subject_chain"]
    discourse_cues: ["action_sequence_continuity"]

  - referent: "Abel"
    surface_form: "Abel his brother"
    participant_status: "EXITING"
    rationale: "Abel is killed. Death = definitive exit from discourse. 'Killed him' is final verb."
    confidence: "high"
    prior_mention: "GEN 4:8b"
    grammatical_cues: ["object_of_death_verb"]
    discourse_cues: ["narrative_closure", "death_event"]

citations:
  - "eng-ESV-2016: Genesis 4:8 text"
  - "heb-WLC: Hebrew participant marking analysis"
  - "llm-cs45: Discourse structure analysis"
metadata:
  genre: "narrative"
  pericope: "Genesis 4:1-16 Cain and Abel"
  translation_notes: "Switch-reference languages: Cain=ROUTINE (same subject), Abel=RESTAGING (different subject) in v8a. Abel=EXITING critical for pronoun resolution."
```

**Example 2: Genesis 19:31 (Lot's daughters - Frame Inferable)**
```yaml
verse: "GEN 19:31"
participant_tracking:
  - referent: "firstborn"
    surface_form: "the firstborn"
    participant_status: "FIRST_MENTION"
    rationale: "First explicit introduction of daughters with role distinction. Previous mentions (v8, v12) were generic 'daughters' without individuation."
    confidence: "high"
    prior_mention: "GEN 19:8"
    grammatical_cues: ["definite_article", "role_specification"]
    discourse_cues: ["new_pericope", "role_differentiation"]

  - referent: "younger"
    surface_form: "the younger"
    participant_status: "FRAME_INFERABLE"
    rationale: "Implied by 'firstborn' mention. Cultural frame: family with firstborn implies younger siblings. Not yet explicitly introduced but inferable from context."
    confidence: "medium"
    prior_mention: null
    grammatical_cues: ["implied_by_contrast"]
    discourse_cues: ["cultural_frame_assumption"]

  - referent: "father"
    surface_form: "our father"
    participant_status: "ROUTINE"
    rationale: "Lot continuous from v30. Daughters discussing him as ongoing topic. Possessive 'our' signals active discourse participant."
    confidence: "high"
    prior_mention: "GEN 19:30"
    grammatical_cues: ["possessive_pronoun"]
    discourse_cues: ["topic_continuity", "addressee_reference"]

citations:
  - "eng-ESV-2016: Genesis 19:31 text"
  - "llm-cs45: Cultural frame analysis"
metadata:
  genre: "narrative"
  pericope: "Genesis 19:30-38 Lot and his daughters"
  translation_notes: "Frame Inferable for 'younger' daughter - target language may require explicit mention before v32."
```

**Example 3: Matthew 1:1 (Genealogy - First Mention pattern)**
```yaml
verse: "MAT 1:1"
participant_tracking:
  - referent: "Jesus Christ"
    surface_form: "Jesus Christ"
    participant_status: "FIRST_MENTION"
    rationale: "Opening verse of Gospel. Introduces main subject of entire book. No prior context."
    confidence: "high"
    prior_mention: null
    grammatical_cues: ["proper_name", "title_construction"]
    discourse_cues: ["book_opening", "primary_subject_introduction"]

  - referent: "David"
    surface_form: "the son of David"
    participant_status: "FIRST_MENTION"
    rationale: "First mention in Matthew (though historical figure known to readers). Genealogical formula treats each generation as new introduction."
    confidence: "high"
    prior_mention: null
    grammatical_cues: ["genitive_chain", "definite_article"]
    discourse_cues: ["genealogical_formula"]

  - referent: "Abraham"
    surface_form: "the son of Abraham"
    participant_status: "FIRST_MENTION"
    rationale: "Same as David. Genealogy resets participant tracking - each name is FIRST_MENTION in this textual context."
    confidence: "high"
    prior_mention: null
    grammatical_cues: ["genitive_chain", "definite_article"]
    discourse_cues: ["genealogical_formula"]

citations:
  - "eng-ESV-2016: Matthew 1:1 text"
  - "grc-SBLGNT: Greek grammatical analysis"
metadata:
  genre: "genealogy"
  pericope: "Matthew 1:1-17 Genealogy of Jesus"
  translation_notes: "Genealogies: All names treated as FIRST_MENTION in formal listing, even if same person reappears (e.g., David v6 vs v17)."
```

---

## Related Features (40 lines)

### Cross-Feature Dependencies

**Strong correlation with**:
- **Surface Realization** (Noun feature): Participant status affects whether referent appears as noun, pronoun, or zero
  - FIRST_MENTION → typically full noun phrase
  - ROUTINE → pronoun or zero pronoun (pro-drop languages)
  - RESTAGING → often demonstrative + noun ("that man")

- **Proximity System** (Noun feature): Demonstrative choice depends on participant status
  - FIRST_MENTION: indefinite marking
  - ROUTINE: proximal "this" (near speaker's mental focus)
  - RESTAGING: medial/distal "that" (reintroduced from distance)

- **Number System** (Noun feature): Collective-to-singular transitions
  - "The people" (plural, ROUTINE) → "he" (singular, ROUTINE) = grammatical number change but discourse continuity

**Moderate correlation with**:
- **Illocutionary Force** (Clause feature): Questions vs statements affect tracking
  - Question: addressee becomes ROUTINE even if not subject
  - Imperative: addressee forced into ROUTINE status

- **Discourse Genre** (Clause feature): Gateway feature sets expectations
  - Narrative: frequent ROUTINE chains
  - Prophecy: more FIRST_MENTION (future entities)
  - Genealogy: all FIRST_MENTION

**Weak correlation with**:
- **Clusivity** (Person System): "We" tracking depends on participant status of sub-referents
  - "We" (inclusive) tracking ≠ sum of individual tracking

### Translation Workflow Integration

**Typical usage in translation project**:
1. **Discourse Genre** → sets baseline expectations
2. **Participant Tracking** → determines reference strategy
3. **Surface Realization** → chooses noun/pronoun/zero based on tracking
4. **Proximity System** → selects demonstrative if noun required
5. **Switch-Reference** (proposed NEW feature) → grammatical marking based on tracking

---

## Experimental Work

**Migrated from**: `/plan/tbta-rebuild-with-llm/features/participant-tracking/`
**Experiments location**: `./experiments/`

### Completed Experiments

**PROMPT1** (`experiments/PROMPT1.md`): Initial 5-state algorithm tested on Matthew 24:46-47
- **Result**: 91.3% accuracy (21/23 predictions correct)
- **Key findings**: Presupposition (God=Routine), activity frames (field=Frame Inferable)
- **Status**: Validated, systematic errors identified

**PROMPT2** (`experiments/PROMPT2.md`): Algorithm v2.0 with genre-specific fixes
- **Additions**: Epistolary abstract noun rule, quantifier+definite refinement, recognition frame
- **Projected**: 75-85% accuracy (untested)
- **Status**: Hypothetical - requires validation on NEW test set

### Key Learnings

See `experiments/LEARNINGS.md` for full implementation guide covering:
- 5-state simplified system (Routine 73%, Generic 14%, Frame Inferable 7.5%, First Mention 5.4%, Interrogative 0.2%)
- LLM prediction workflow (3 phases)
- Frame semantics database requirements
- Validation approaches

See `experiments/ERROR-ANALYSIS.md` for systematic error patterns:
- **Error 1**: Epistolary abstract nouns (100% error rate in v1.0 - grace, mercy, peace marked Generic instead of Routine)
- **Error 2**: Universal quantifier + definite article ("all the magicians" = specific group, not universal class)
- **Error 3**: Frame Inferable under-prediction (recognition frames missing from v1.0)

## Stage Checklist

### ✅ Stage 1-3: Research & Documentation (Complete)
- [x] TBTA documentation review
- [x] Language family analysis (200+ switch-reference languages identified)
- [x] Scholarly research (Givón, Ariel, Gundel frameworks)

### ✅ Stage 4: Test Set Development (Complete)
- [x] Algorithm v1.0 developed and validated
- [x] Blind prediction methodology maintained
- [x] Test results documented (97% training, 60-70% random test)
- [x] Error analysis completed (3 critical error categories)

### 🟨 Stage 5: Algorithm Refinement (90% Complete - PROMPT2 Pending Validation)
- [x] v1.0 tested and errors systematically analyzed
- [x] v2.0 designed with 3 critical fixes (epistolary abstracts, quantifier+definite, recognition frame)
- [ ] **VALIDATION NEEDED**: Test v2.0 on NEW test set (not same 12 verses)
- [ ] **TARGET**: Achieve 80-85% accuracy for production consideration
- [ ] **DECISION POINT**: If v2.0 <80%, develop v3.0 or expand genre-stratified training

### ⬜ Stage 6: Production Validation & Peer Review (Pending v2.0 Validation)
- [ ] Apply v2.0 to NEW adversarial or random test set (genre-stratified)
- [ ] Calculate accuracy and compare to v1.0
- [ ] If 85%+: Mark production-ready
- [ ] If 80-84%: Conditional approval (monitor in production)
- [ ] If <80%: Refine to v2.1 or v3.0
- [ ] Launch peer reviews (theological, linguistic, methodological)
- [ ] External validation with real switch-reference translations

---

## Current Status Summary

**What's Working (90%)**:
- Clear First Mention detection (proper names, introductions)
- Routine continuity tracking (same-subject chains)
- Exiting identification (death, departure verbs)
- Restaging in simple narratives (physical return after absence)

**What Needs Refinement (10% errors)**:
1. **Quoted speech boundaries**: Speaker changes unclear when nested quotes
   - Example: Genesis 3:1-5 (Serpent → Eve → God chain)
2. **Vision/dream contexts**: Mixing narrative frame with internal vision
   - Example: Daniel, Revelation passages
3. **Implicit role shifts**: Same entity, different title
   - Example: "the man" → "the king" (same person, different discourse role)
4. **Collective reference**: Group → individual transitions
   - Example: "Israel" (collective) → "he" (individual king)

**Next Steps to Stage 5 Completion**:
1. Create PROMPT4.md addressing quoted speech with explicit rules
2. Add vision/dream boundary detection (check for revelation verbs)
3. Implement role-shift tracking (same referent, different surface forms)
4. Test against validate.yaml with refined prompt
5. Achieve 95%+ accuracy before Stage 6

**Timeline to Stage 6**:
- PROMPT4 iteration: 1-2 days
- Validate set testing: 1 day
- If 95%+ achieved → proceed to peer review (Stage 6)
- Estimated completion: 3-5 days

---

**Last Updated**: 2025-11-15
**Feature Owner**: Research Agent (TBTA Rebuild Project)
**Contact**: See /plan/tbta-rebuild-with-llm/README.md for coordination
