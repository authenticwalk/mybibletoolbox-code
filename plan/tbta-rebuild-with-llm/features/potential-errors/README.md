# Potential TBTA Annotation Errors

**Purpose**: Document cases where exhaustive debugging suggests TBTA annotations may be incorrect, pending review by TBTA team.

**Standard**: Only flag as potential error AFTER completing all 6 debugging steps from CROSS-FEATURE-LEARNINGS.md

---

## Review Process

### When to Flag
A mismatch should ONLY be flagged as potential TBTA error when:
1. ✅ Data accuracy verified (correct verse, feature, constituent)
2. ✅ Source text exhaustively analyzed (morphology, semantics, lexicons, commentaries)
3. ✅ Context fully examined (discourse structure, theology, parallels)
4. ✅ Multiple sources cross-referenced (3+ translations, 2+ commentaries, linguistic databases)
5. ✅ Alternative hypotheses tested (different algorithms, edge cases, special handling)
6. ✅ After ALL above, our prediction still appears more accurate than TBTA

### Documentation Requirements

Each potential error must include:
```markdown
## [Feature]-[Verse]-[Constituent]

**Verse**: [Reference]
**Feature**: [Number/Degree/Person/etc.]
**Constituent**: [Specific word/phrase]

### TBTA Annotation
- **Value**: [What TBTA marked]
- **Rationale** (if known): [Why TBTA might have chosen this]

### Our Prediction
- **Value**: [What we predicted]
- **Rationale**: [Why we believe this is correct]

### Debugging Evidence

#### 1. Data Verification
- Verse reference: ✅ Confirmed
- Feature extraction: ✅ Correct feature/constituent
- Data version: [TBTA version/date]

#### 2. Source Text Analysis
- **Morphology**: [Greek/Hebrew form, morphological markers]
- **Semantics**: [Lexical meaning, semantic analysis]
- **Lexicons**: [Citations from BDAG, BDB, etc.]
- **Commentaries**: [Citations from scholarly works]

#### 3. Context Analysis
- **Preceding context**: [Summary]
- **Following context**: [Summary]
- **Discourse structure**: [Paragraph/chapter analysis]
- **Theological factors**: [Doctrinal considerations]
- **Parallel passages**: [Cross-references]

#### 4. Cross-Reference Sources
- **Translation 1**: [How rendered, why relevant]
- **Translation 2**: [How rendered, why relevant]
- **Translation 3**: [How rendered, why relevant]
- **Commentary 1**: [Citation and analysis]
- **Commentary 2**: [Citation and analysis]
- **Linguistic databases**: [WALS/Glottolog findings]

#### 5. Alternative Hypotheses Tested
- **Hypothesis 1**: [Tested and rejected because...]
- **Hypothesis 2**: [Tested and rejected because...]
- **Edge case possibility**: [Considered and evaluated]

#### 6. Final Assessment
- **Confidence in our prediction**: [High/Medium/Low]
- **Possible TBTA reasoning**: [Best guess at why TBTA chose this]
- **Recommendation**: [Review/Accept/Reject]

### Supporting Materials
- [Links to lexicon entries, commentary scans, etc.]
- [Screenshots if helpful]
- [Additional linguistic evidence]

### Status
- [ ] Awaiting TBTA team review
- [ ] Under discussion
- [ ] Confirmed as TBTA error
- [ ] Confirmed as correct TBTA (we were wrong)
- [ ] Ambiguous case (both valid)
```

---

## Current Potential Errors

### Number Systems

#### [To be analyzed - 3 mismatches from experiment-001]
- Genesis 1:1 - "heavens" (Hebrew שָׁמַיִם)
- Genesis 1:2 - "waters" (Hebrew מַיִם)
- Matthew 5:3 - "heaven" (Greek οὐρανῶν)

**Note**: These were initially classified as "TBTA prefers semantic over morphological" but need exhaustive debugging to confirm this is a consistent pattern vs. potential errors.

---

## Categories of Potential Errors

### Type 1: Morphology vs Semantics Disagreement
**Frequency**: Most common
**Example**: Hebrew dual morphology but TBTA marks singular
**Resolution**: Usually TBTA is correct (semantic > morphological), but verify exhaustively

### Type 2: Theological Interpretation Disagreement
**Frequency**: Rare but high impact
**Example**: Trinity contexts, messianic prophecies
**Resolution**: Requires theological scholarship consultation

### Type 3: Discourse Context Disagreement
**Frequency**: Medium
**Example**: Participant tracking across verses, discourse role assignments
**Resolution**: Expand context window, check narrative structure

### Type 4: Edge Case / Ambiguous
**Frequency**: Medium
**Example**: Borderline comparative/superlative, intensity levels
**Resolution**: May be genuinely ambiguous, document as translator choice point

### Type 5: Data Entry Error
**Frequency**: Rare
**Example**: Typos, wrong verse, wrong constituent
**Resolution**: Easy to confirm, report immediately

---

## Statistics

**Total Potential Errors Flagged**: 0 (pending exhaustive debugging)
**Confirmed TBTA Errors**: 0
**Confirmed Correct TBTA** (we were wrong): 0
**Ambiguous Cases**: 0
**Under Review**: 0

---

## Workflow

```
Mismatch detected
    ↓
Complete 6-step debugging (from CROSS-FEATURE-LEARNINGS.md)
    ↓
Still believe our prediction correct?
    ↓ YES
Create potential-error document in this folder
    ↓
Submit for TBTA team review
    ↓
[Await response]
    ↓
Update status + incorporate learnings
```

---

## Notes for TBTA Team

We understand that:
1. TBTA annotations are expert human work, not perfect
2. Some cases are genuinely ambiguous (both interpretations valid)
3. Our goal is 100% accuracy through learning OR flagging errors
4. We approach potential errors with humility and thorough research
5. We prioritize learning from mismatches over proving TBTA wrong

If you review a flagged potential error:
- **Agree it's an error**: Thank you! We'll update TBTA data and our records
- **Disagree (TBTA correct)**: Please explain reasoning so we can learn the pattern
- **Ambiguous**: Please note as "translator choice" so we document appropriately

---

**Last Updated**: 2025-11-07
**Features Analyzed**: number-systems (3 mismatches pending exhaustive debugging)
**Next Steps**: Apply 6-step debugging to number-systems mismatches
