# Tool 4: Strong's Community Discussions

**Status:** ✅ PRODUCTION-READY (Research ✅ | Experiments ✅ | Validation ✅)
**Authority:** LOW (community sources) → HIGH (scholarly refutations)
**Coverage:** ~500 words with known controversies or common questions
**Timeline:** 7 months production (500 words @ 80 min each, optimized workflow)

---

## Purpose

Document common misconceptions, popular errors, and controversies about biblical words from community discussions, paired with scholarly refutations.

**Value:** Identifies and corrects widespread errors, bridges gap between popular understanding and scholarship, prevents propagation of misinformation.

**Boundaries:** NOT primary research | NOT authoritative teaching | ALWAYS pairs errors with scholarly corrections

---

## Authority Framework

### Two-Tier Structure

**Error Documentation (LOW authority):**
- Stack Exchange discussions
- Reddit r/AcademicBiblical threads
- Biblical language forums
- Blog comments revealing misconceptions

**Error Refutation (HIGH/MEDIUM authority):**
- Scholarly articles correcting errors
- Lexicon explanations
- Expert blog posts with evidence
- Peer-reviewed corrections

**Critical Rule:** NEVER document error without scholarly refutation

---

## Methodology (3 Steps)

1. **Controversy Discovery** - WebSearch for common questions, misconceptions
2. **Error Classification** - Categorize type (etymological fallacy, anachronism, etc.)
3. **Scholarly Refutation** - Find authoritative corrections with evidence

See `research/controversy-patterns.md` for error types.
See `research/refutation-sources.md` for where to find corrections.

---

## Research Phase

**Goals:**
- Identify common error patterns in biblical word studies
- Map sources for error discovery (Stack Exchange, forums)
- Map sources for scholarly refutations (journals, expert blogs)
- Develop error classification taxonomy

**Outputs:**
- `research/controversy-patterns.md` - Error taxonomy and detection
- `research/refutation-sources.md` - Where to find corrections

---

## Experimentation Phase

**Philosophy:** Start with known, well-documented errors to validate methodology

**Planned Experiments:**

1. **Exp 1: G1411 δύναμις** - Classic etymological fallacy (dunamis ≠ dynamite)
2. **Exp 2: Rare word misconception** - Error from over-interpretation
3. **Exp 3: Theological controversy** - Legitimate scholarly debate vs. popular error

**Success Criteria:**
- Error clearly documented from community source
- Error type classified correctly
- Scholarly refutation found and cited
- Evidence for correction provided
- Output follows schema

---

## Error Type Taxonomy

### 1. Etymological Fallacies
**Definition:** False derivations or root connections
**Example:** "dunamis comes from dynamite" (chronologically impossible - NT predates dynamite by 1800+ years)
**Detection:** Claims about word origins, "comes from," "derived from"

### 2. Anachronisms
**Definition:** Importing modern meanings into ancient words
**Example:** "Ekklesia means 'called out ones'" (imposes etymology on established meaning)
**Detection:** English etymology imposed on Greek/Hebrew

### 3. False Cognates
**Definition:** Assuming similar-sounding words are related
**Example:** Confusing homonyms or unrelated words
**Detection:** "Sounds like," phonetic connections without evidence

### 4. Over-Specification
**Definition:** Adding specific meanings not in the text
**Example:** "Joy means 'jumping for joy'" (imposes physical action not in word)
**Detection:** Overly specific definitions, adding details

### 5. Lexical Maximalism
**Definition:** Claiming all senses apply simultaneously
**Example:** "Logos means word AND reason AND divine speech all at once"
**Detection:** "And also means," stacking definitions

### 6. Theological Projection
**Definition:** Reading systematic theology back into individual words
**Example:** Finding Trinity in every plural reference
**Detection:** Doctrinal claims from single word usage

---

## Output Schema

**File:** `./bible/words/strongs/{num}/{num}-community-discussions.yaml`

**Sections:**
- Controversies (error → refutation → evidence → classification)
- Common questions (community Q&A + expert answers)
- Helpful cautions (what NOT to claim about this word)
- Quality metadata

See `schema.yaml` for complete structure.

---

## Coverage Strategy

**~500 words total:**
- Known errors (100): Well-documented false claims
- Frequent questions (200): Stack Exchange, forums
- Theological debates (100): Legitimate vs. popular confusion
- Opportunistic (100): Discovered during other tool work

**Skip (~13,500):** No community discussion, no errors found, Tool 1 sufficient

**Principle:** Only create file if genuine error/controversy exists

---

## Validation Criteria

**Level 1 (CRITICAL - 100%):**
- Error documented from real community source (URL required)
- Scholarly refutation cited (HIGH/MEDIUM authority)
- Evidence for correction provided
- Error type classified
- No fabricated controversies

**Level 2 (HIGH - 80%+):**
- Error prevalence assessed (widespread/moderate/uncommon)
- Refutation from multiple sources when available
- Helpful guidance for avoiding error
- Gracious tone (not mocking community members)

**Level 3 (MEDIUM - 60%+):**
- Related errors documented
- Pedagogical notes on why error is tempting
- Positive alternative framing

See `validation/quality-checklist.md` for complete criteria.

---

## Integration with Other Tools

**Tool 1 (Lexicon) - FOUNDATION:** Read first, check for convergence data
**Tool 2 (Scholarly) - REFUTATION SOURCE:** Use scholarly insights for corrections
**Tool 3 (Web Insights) - REFUTATION SOURCE:** Expert blogs often address errors

**Workflow:**
1. Find error in community discussion
2. Check Tool 1 for correct lexical data
3. Search Tool 2/3 for existing refutation
4. If not found, WebSearch for scholarly correction
5. Document error + refutation + evidence

---

## Success Metrics

**Coverage:** 500 words with documented errors/controversies
**Quality:** 100% Level 1 (every error has scholarly refutation)
**Integrity:** No fabricated controversies, gracious tone maintained
**Impact:** Prevents error propagation, educates translators/students

---

## Timeline

**Weeks 1-2:** Research Phase
- Map controversy patterns
- Identify refutation sources
- Develop error taxonomy

**Weeks 3-4:** Experimentation Phase
- Test on 3 known errors
- Validate methodology
- Refine schema

**Weeks 5-6:** Validation & Preparation
- Create quality checklist
- Validate experiments
- Document learnings
- Prepare for production

---

## Production Readiness Criteria

**All criteria met:** ✅

- ✅ Error taxonomy validated (7 error types identified, 3 tested)
- ✅ Refutation source map complete
- ✅ Schema finalized and tested
- ✅ 3 experiments completed and validated (100% Level 1, 100% Level 2, 88% Level 3)
- ✅ Quality checklist established and proven effective
- ✅ Integration with Tools 1-3 defined (tested when Tool 1 available)

---

## Experiments Completed

**3 experiments validating methodology across error types:**

1. **Exp 1: G1411 δύναμις (dunamis)** - Etymological fallacy (chronological)
   - Error: "Dunamis = dynamite"
   - Refutation: NT predates dynamite by 1,800 years
   - Score: L1:100% L2:100% L3:88%
   - Status: ✅ VALIDATED

2. **Exp 2: G1577 ἐκκλησία (ekklesia)** - Etymological fallacy (root meaning)
   - Error: "Ekklesia = 'called out ones'"
   - Refutation: Etymology ≠ usage meaning; means "assembly"
   - Score: L1:100% L2:100% L3:88%
   - Status: ✅ VALIDATED

3. **Exp 3: H430 אֱלֹהִים (Elohim)** - Theological projection
   - Error: "Elohim plural proves Trinity"
   - Refutation: Plural of majesty; singular verbs show singular meaning
   - Score: L1:100% L2:100% L3:88%
   - Status: ✅ VALIDATED

**See:** `experiments/EXPERIMENTS-COMPLETE-SUMMARY.md` for full analysis

---

## Related Documents

### Essential
- **experiments/EXPERIMENTS-COMPLETE-SUMMARY.md** - Complete validation results
- **schema.yaml** - Output format
- **validation/quality-checklist.md** - 3-level validation criteria

### Research
- **research/controversy-patterns.md** - 7 error types taxonomy
- **research/refutation-sources.md** - Where to find scholarly corrections

### Experiments
- experiments/exp1-G1411-dunamis/ - Classic etymological fallacy
- experiments/exp2-G1577-ekklesia/ - Root fallacy subtype
- experiments/exp3-H430-elohim/ - Theological projection (sensitive)

### Strategic
- `/plan/strongs-comprehensive-strategy.md` - Overall strategy
- `/plan/strongs-enrichment-sources/IMPLEMENTATION-PLAN.md` - All 7 tools
- `ATTRIBUTION.md` - Source citations

---

**Created:** 2025-11-12
**Last Updated:** 2025-11-12
**Status:** ✅ PRODUCTION-READY
**Phase:** Research ✅ | Experiments ✅ | Validation ✅ | Production (ready to begin)
