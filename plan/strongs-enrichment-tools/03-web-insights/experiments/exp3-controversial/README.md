# Experiment 3: Controversial Word (Error Correction Focus)

**Strong's Number:** G1411
**Lemma:** δύναμις (dynamis)
**Gloss:** "power, ability, miracle"
**Occurrences:** 120 times in NT

---

## Purpose

Test Tool 3's ability to document and correct common misconceptions. This word has a well-known false etymology ("dynamis = dynamite") that needs expert refutation.

**What We're Testing:**
- Can we find expert corrections of false etymologies?
- Is error + refutation + evidence pattern complete?
- Do sources provide teaching guidance on avoiding errors?
- Are corrections authoritative (not just opinion)?
- Does Tool 3 effectively handle controversy documentation?

---

## The Known Error

**Common False Claim:**
"The Greek word dynamis is where we get our English word 'dynamite,' showing the explosive power of God!"

**Why It's False:**
- Dynamite was invented by Alfred Nobel in 1867
- NT written ~50-95 AD (1,800 years before dynamite)
- Etymology reversal: dynamite comes FROM Greek dynamis, not vice versa
- Error type: Anachronism + etymological fallacy

**Why It Matters:**
- Perpetuated in sermons, teaching, books
- Undermines credibility when corrected
- Teaches wrong methodology (etymological fallacy)
- Distracts from actual NT meaning

---

## Expected Sources

### Expert Corrections (MEDIUM authority)
- **Bill Mounce:** Known for correcting Greek word study errors
- **Michael Heiser:** Addresses popular misconceptions
- **Daniel Wallace:** Greek scholar, addresses teaching errors
- **Rob Plummer:** Exegetical precision emphasis

### Lexicon/Reference Sites (MEDIUM-HIGH)
- **STEPBible.org:** Etymology notes
- **NetBible.org:** May have translator notes addressing this
- **BibleHub forums/articles:** Possibly expert responses

### Teaching Resources (MEDIUM-LOW)
- **Precept Austin:** May document error and correction
- **Bible.org:** Possibly articles on word study methodology

---

## Search Strategy

### Phase 1: Find Error Correction Content
```
WebSearch queries:
1. "dynamis dynamite" error OR fallacy OR myth
2. "G1411 dynamis" etymological fallacy
3. "dynamis does not mean dynamite" site:billmounce.com
4. "Greek word study errors" dynamis
5. "dynamis power" etymology site:bible.org
6. "δύναμις" Alfred Nobel OR anachronism
```

### Phase 2: Find Positive Teaching Content
```
WebSearch queries:
7. "G1411 dynamis" meaning site:netbible.org
8. "dynamis power" NT usage site:stepbible.org
9. "dynamis" theological significance
```

### Phase 3: Content Extraction
For each source:
1. Extract error statement (if present in source)
2. Extract expert refutation
3. Extract evidence for correction
4. Extract positive teaching (correct understanding)
5. Verify author credentials for correction authority

---

## Expected Content Categories

### Error Corrections (PRIMARY FOCUS)

**Error Documentation:**
```yaml
error_corrections:
  - error_id: 1
    error_type: "etymological_fallacy"
    common_claim: "Dynamis means dynamite, showing God's explosive power"
    prevalence: "widespread"
    sources_of_error:
      - "Popular preaching"
      - "Devotional books"
      - "Church teaching materials"
```

**Expert Refutation:**
```yaml
    expert_refutation:
      correction: "Dynamite invented 1867, NT written 50-95 AD. Impossible connection."
      evidence:
        - "Historical: Alfred Nobel invented dynamite in 1867 {historical-fact}"
        - "Chronological: NT predates dynamite by 1,800 years {llm-cs45}"
        - "Directional: English 'dynamite' derives FROM Greek dynamis, not reverse {mounce}"
      scholarly_source:
        author: "William D. Mounce"
        url: "{actual URL when found}"
        authority_level: "MEDIUM"
```

**Correct Understanding:**
```yaml
    correct_teaching:
      actual_meaning: "Power, ability, might - both divine and human in NT usage {thayer}"
      usage_examples:
        - "Divine power: Acts 1:8 'power of Holy Spirit' {netbible}"
        - "Human ability: Matt 25:15 'according to ability' {netbible}"
        - "Miraculous power: Luke 10:13 'mighty works' {netbible}"
```

### Modern Insights

**Linguistic Analysis:**
- Etymology: From δύναμαι (to be able)
- Semantic range: power, ability, miracle, strength
- NT usage patterns: Divine power vs. human ability

**Theological Significance:**
- Power of God in salvation (Rom 1:16)
- Power of Holy Spirit (Acts 1:8)
- Power in weakness (2 Cor 12:9)

### Practical Applications

**For Preachers:**
- How to teach word studies correctly (avoid etymological fallacy)
- Accurate illustrations of divine power
- Correcting the error graciously if previously taught

**For Teachers:**
- Methodology: meaning from context, not etymology alone
- How to evaluate word study resources for accuracy
- Red flags for false etymologies

**For Students:**
- Critical thinking about popular teaching
- Verify claims with lexicons
- Understand anachronism errors

### Teaching Helps

**Positive Methodology:**
- "Focus on NT usage, not English derivatives"
- "Check dates: Is claimed connection chronologically possible?"
- "Etymology shows history, context shows meaning"

---

## Validation Criteria

### Level 1: CRITICAL (Must Pass)
- [ ] Error clearly documented (not just vague "some say...")
- [ ] Expert refutation present with credentials
- [ ] Evidence for correction provided (chronological, historical)
- [ ] Correct teaching included (not just negative)
- [ ] Authority level marked for correction source
- [ ] No continuation of error in Tool 3 output

### Level 2: HIGH PRIORITY (80%+)
- [ ] Multiple sources for correction (if available)
- [ ] Error prevalence accurately described
- [ ] Sources of error identified
- [ ] Positive teaching methodology included
- [ ] Gracious tone (not mocking those who made error)

### Level 3: MEDIUM PRIORITY (60%+)
- [ ] Cross-reference to Tool 1 (correct etymology)
- [ ] Teaching helps on avoiding similar errors
- [ ] Practical guidance for correcting if previously taught

---

## Expected Challenges

**Challenge 1: Finding explicit error correction**
- Solution: Search for "dynamis dynamite error" - scholars have addressed this
- If not found explicitly, extract from etymology discussions

**Challenge 2: Tone management**
- Solution: Document error factually, correct graciously
- Avoid: Mockery, condescension, harsh language
- Include: Understanding of how error spreads

**Challenge 3: Distinguishing error from correct teaching**
- Solution: Clear structure: error section, refutation section, correct teaching section
- Don't let error contaminate positive content

**Challenge 4: Authority verification for corrections**
- Solution: Corrections need MEDIUM+ authority (Ph.D. or M.Div. with sources)
- Don't rely on anonymous forum posts

---

## Success Indicators

**Experiment succeeds if:**
- ✅ Error correction content found from expert sources
- ✅ Complete pattern: error + refutation + evidence
- ✅ Correct teaching provided alongside correction
- ✅ Authority levels appropriate (MEDIUM+ for corrections)
- ✅ Tone is gracious and educational

**Experiment reveals issues if:**
- ❌ Cannot find expert correction content
- ❌ Only negative (error) without positive (correct teaching)
- ❌ Authority insufficient for correction claims
- ❌ Tone is harsh or mocking

---

## Comparison to Experiments 1-2

| Aspect | Exp 1 (Agape) | Exp 2 (Righteous) | Exp 3 (Dynamis) |
|--------|---------------|-------------------|-----------------|
| **Primary Focus** | Insights + Apps | Moderate coverage | Error correction |
| **Expected Sources** | 5+ | 2-3 | 3-5 (error-focused) |
| **Key Content** | Applications | Theological | Corrections |
| **Special Challenge** | Abundance | Scarcity | Controversy |

---

## Decision Points

After this experiment, determine:
1. Is error correction content reliably available for controversial words?
2. What's the minimum authority level for corrections? (MEDIUM required?)
3. Should we proactively search for errors even if not widely known?
4. How to balance error correction with positive teaching?

---

## Output Files

After experiment completion:
1. `G1411-output.yaml` - Full output with error correction section
2. `G1411-learnings.md` - Error correction methodology notes
3. `G1411-sources-log.md` - Search for corrections, what was found
4. `G1411-validation.md` - Validation with focus on correction quality

---

## Timeline

- **Phase 1 (Find Corrections):** 40 minutes
- **Phase 2 (Find Positive Teaching):** 30 minutes
- **Phase 3 (Synthesis):** 30 minutes (careful error/correction separation)
- **Validation:** 20 minutes
- **Total:** ~2 hours

---

## Next Steps After Experiment

1. Document error correction methodology
2. Create list of other controversial words to check
3. Establish authority requirements for corrections
4. Proceed to Experiment 4 (translator-focused)

---

**Status:** Experiment design complete, ready to execute
**Expected Outcome:** Successful - well-documented error, likely to find corrections
