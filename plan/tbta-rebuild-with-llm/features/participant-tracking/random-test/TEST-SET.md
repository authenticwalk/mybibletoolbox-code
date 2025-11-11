# Participant Tracking: Random Test Set

**Date created**: 2025-11-11
**Algorithm tested**: v1.0 (commit cb388ca)
**Purpose**: Validate algorithm on representative sample reflecting natural distribution
**Target accuracy**: 85-90% (random sampling should match training performance)
**Selection method**: Random seed-based selection from Bible

---

## Test Design Strategy

**Random Selection Principles**:
1. **Seed-based reproducibility**: Use fixed random seed for verse selection
2. **Natural distribution**: Should reflect TBTA corpus frequencies (71.6% Routine, 15.8% Generic, etc.)
3. **Genre diversity**: Mix of narrative, teaching, prophecy, poetry
4. **Testament balance**: ~70% New Testament, ~30% Old Testament (reflects TBTA corpus availability)

**Random seed**: 20251111 (date: 2025-11-11)

---

## Random Test Set (12 Verses)

### Selection Methodology

**Step 1**: Generate random numbers (seed: 20251111)
**Step 2**: Map to Bible books/chapters/verses
**Step 3**: Verify TBTA availability (18 books available: GEN, EXO, JDG, RUT, 1-2SAM, NEH, EST, PSA, DAN, MAT, MRK, LUK, JHN, ACT, EPH, PHP, 2JN)
**Step 4**: Select 12 verses with participant tracking annotations

---

### Verse 1: [Random Selection - TBD]
**Reference**: [To be determined by random generation]
**English**: [TBD]
**Genre**: [Narrative/Teaching/Prophecy/Poetry]
**Testament**: [OT/NT]

**Participants to track**: [TBD after verse selection]
**Expected dominant state**: [Routine expected in 71.6% of participants]

---

### Verse 2: [Random Selection - TBD]
**Reference**: [TBD]
**English**: [TBD]
**Genre**: [TBD]
**Testament**: [TBD]

---

### Verse 3: [Random Selection - TBD]
**Reference**: [TBD]
**English**: [TBD]
**Genre**: [TBD]
**Testament**: [TBD]

---

### Verse 4: [Random Selection - TBD]
**Reference**: [TBD]
**English**: [TBD]
**Genre**: [TBD]
**Testament**: [TBD]

---

### Verse 5: [Random Selection - TBD]
**Reference**: [TBD]
**English**: [TBD]
**Genre**: [TBD]
**Testament**: [TBD]

---

### Verse 6: [Random Selection - TBD]
**Reference**: [TBD]
**English**: [TBD]
**Genre**: [TBD]
**Testament**: [TBD]

---

### Verse 7: [Random Selection - TBD]
**Reference**: [TBD]
**English**: [TBD]
**Genre**: [TBD]
**Testament**: [TBD]

---

### Verse 8: [Random Selection - TBD]
**Reference**: [TBD]
**English**: [TBD]
**Genre**: [TBD]
**Testament**: [TBD]

---

### Verse 9: [Random Selection - TBD]
**Reference**: [TBD]
**English**: [TBD]
**Genre**: [TBD]
**Testament**: [TBD]

---

### Verse 10: [Random Selection - TBD]
**Reference**: [TBD]
**English**: [TBD]
**Genre**: [TBD]
**Testament**: [TBD]

---

### Verse 11: [Random Selection - TBD]
**Reference**: [TBD]
**English**: [TBD]
**Genre**: [TBD]
**Testament**: [TBD]

---

### Verse 12: [Random Selection - TBD]
**Reference**: [TBD]
**English**: [TBD]
**Genre**: [TBD]
**Testament**: [TBD]

---

## Expected Distribution

**Based on TBTA corpus frequencies**:

| State | Corpus Frequency | Expected in 12 Verses* | Confidence |
|-------|------------------|------------------------|------------|
| **Routine (D)** | 71.6% | ~50-60 participants | High |
| **Generic (G)** | 15.8% | ~10-15 participants | Medium |
| **Frame Inferable (F)** | 6.3% | ~4-6 participants | Medium |
| **First Mention (I)** | 6.0% | ~4-6 participants | Medium |
| **Interrogative (Q)** | 0.2% | ~0-1 participants | Low (very rare) |

\* Assuming ~70 total participant annotations across 12 verses (average 5-6 participants per verse)

---

## Test Set Statistics (To Be Completed)

**Total verses**: 12
**Total participants**: [TBD after verse selection]
**Testament distribution**: [Target: ~8 NT, ~4 OT]
**Genre distribution**: [Target: narrative 60%, teaching 25%, poetry 10%, prophecy 5%]

---

## Random Selection Process (Technical)

**Reproducible random selection**:

```python
import random
random.seed(20251111)

# Available TBTA books (18 books with participant tracking)
books = ['GEN', 'EXO', 'JDG', 'RUT', '1SAM', '2SAM', 'NEH', 'EST', 'PSA',
         'DAN', 'MAT', 'MRK', 'LUK', 'JHN', 'ACT', 'EPH', 'PHP', '2JN']

# Weighted by book length (larger books more likely)
# Simplified: equal probability for now, refine if needed

selected_verses = []
for i in range(12):
    book = random.choice(books)
    # Then select random chapter/verse within book
    # Map to actual verse references
    # Verify TBTA participant tracking data exists
    selected_verses.append(f"{book} [chapter:verse]")
```

**Note**: Actual random selection requires:
1. List of all verses with participant tracking in 18 available books
2. Random sampling from that list
3. Verification that selected verses have sufficient participants for testing

**Alternative simplified approach** (for Phase 5 completion):
- Manually select 12 verses from available TBTA books
- Use intuitive "random-like" distribution (avoid clustering by book/theme)
- Ensure genre/testament diversity
- Document selection as "pseudo-random" rather than true random

---

## Methodology

### Phase 5 (Current): Test Set Design
- Design random selection methodology (above)
- Select 12 verses using random seed 20251111
- Document verse references and expected participants
- Commit and lock test set design

### Phase 6: Make Predictions
- Apply Algorithm v1.0 to 12 random verses (**NO TBTA ACCESS**)
- Predict state for each participant
- Lock predictions via git commit

### Phase 7: Validation
- Access TBTA for random verses
- Calculate accuracy per state
- Compare to expected distribution
- Error analysis

---

## Success Criteria

**Target Accuracy**: 85-90%

**Why higher than adversarial?**
- Random verses reflect natural distribution (71.6% Routine - algorithm's strength)
- No intentional edge cases or ambiguity
- Should match training performance (97%)

**Breakdown targets**:
- Routine (D): 95%+ (dominant state, algorithm trained on this)
- Generic (G): 85%+ (clear patterns learned)
- Frame Inferable (F): 80%+ (frame detection may have some errors)
- First Mention (I): 85%+ (indefinite article is reliable signal)
- Interrogative (Q): N/A (too rare to expect in 12 verses, 0.2% frequency)

---

## Next Steps

**Immediate** (Phase 5 completion):
1. Execute random selection (seed 20251111)
2. Map random numbers to actual verse references
3. Verify TBTA data availability for selected verses
4. Document verse details (reference, English text, participants)
5. Commit and lock random test set

**Phase 6** (Blind predictions):
1. Apply Algorithm v1.0 to all participants in 12 verses
2. Make predictions WITHOUT accessing TBTA
3. Lock predictions via git commit
4. Move to Phase 7 (validation)

---

**Created**: 2025-11-11
**Status**: Methodology designed, verse selection PENDING
**Algorithm**: v1.0 (locked commit cb388ca)
**Random seed**: 20251111
**Next**: Complete verse selection and document, then proceed to Phase 6
