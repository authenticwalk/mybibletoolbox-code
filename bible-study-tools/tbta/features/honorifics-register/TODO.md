# Honorifics and Register - TODO

**Current Status**: 🟢 Production-Ready Documentation Complete
**Last Updated**: 2025-11-15

## Summary

Honorifics/Register system encompasses **6 speaker demographics features** that work together to enable accurate honorific system selection in Bible translation. Production-ready with TIER 1-2 documentation complete.

**Target Languages**: Japanese, Korean, Javanese, Thai, Vietnamese, Hindi (and other languages with grammaticalized social register systems)

## The 6 Features

1. **Speaker** - Who is speaking (character codes)
2. **Listener** - Who is being addressed (character codes)
3. **Speaker's Attitude** - Social register (Neutral, Polite, Honorable, Familiar, Endearing)
4. **Speaker's Age** - Life stage (Child, Young Adult, Adult, Elder)
5. **Speaker-Listener Age Relationship** - Relative age (5 levels)
6. **Speech Style** - Discourse context (Formal, Informal, Liturgical, Prophetic, Didactic, etc.)

## Current Stage Status

### ✅ Complete Documentation
- README.md (research overview)
- SPEAKER-DEMOGRAPHICS-README.md (TIER 1-2 comprehensive feature documentation)
- SPEAKER-LISTENER-CODES.md (complete character enumeration)
- ATTITUDE-EXAMPLES.md (20+ concrete verse examples)
- AGE-RELATIONSHIP-GUIDE.md (calculation guide for age features)
- LANGUAGE-APPLICATIONS.md (Japanese, Korean, Javanese, Thai, Vietnamese, Hindi)
- LANGUAGE-MATRIX.md (cross-language comparison)
- VALIDATION-CHECKLIST.md (step-by-step validation procedures)

### ⏳ Next Steps Required

**Priority 1: Tool Implementation**
- [ ] Create automated speaker/listener detection
- [ ] Implement attitude inference algorithm
- [ ] Build age calculation system
- [ ] Develop speech style classifier

**Priority 2: Language-Specific Testing**
- [ ] Validate with Japanese honorific system (keigo)
- [ ] Test Korean speech levels (-yo/-습니다)
- [ ] Verify Thai royal language (Ratchasap)
- [ ] Check Vietnamese pronoun system
- [ ] Validate Hindi formal/informal registers

**Priority 3: Integration with Other Features**
- [ ] Cross-reference with Surface Realization (formal → more nouns)
- [ ] Coordinate with Illocutionary Force (imperative register variation)
- [ ] Test interaction with Person/Number (T-V distinction in Indo-European)

## Files Migrated

**Core Documentation** (TIER 1-2 complete):
- README.md (overview + research)
- SPEAKER-DEMOGRAPHICS-README.md (main feature spec)
- SPEAKER-LISTENER-CODES.md (Biblical character codes)
- ATTITUDE-EXAMPLES.md (concrete verses)
- AGE-RELATIONSHIP-GUIDE.md (calculation methodology)

**Language-Specific Resources**:
- LANGUAGE-APPLICATIONS.md (6 language families)
- LANGUAGE-MATRIX.md (comparative analysis)
- VALIDATION-CHECKLIST.md (QA procedures)

## Key Capabilities (Production-Ready)

### 1. Speaker/Listener Identification
- 100+ Biblical character codes (Jesus, disciples, Pharisees, crowds, etc.)
- Systematic approach for dialogue attribution
- Handles direct speech, reported speech, narrative voice

### 2. Attitude/Register Classification
- **Neutral** (default, unmarked)
- **Polite** (respect without high honor)
- **Honorable** (high respect, reverence)
- **Familiar** (intimate, close relationship)
- **Endearing** (affection, tenderness)

### 3. Age Feature Calculation
- **Speaker's Age**: Child (0-12), Young Adult (13-25), Adult (26-60), Elder (60+)
- **Relative Age**: Much Younger, Younger, Peer, Older, Much Older
- Biblical ages documented (e.g., Jesus ≈30, disciples varied, Pharisees typically elders)

### 4. Speech Style Context
- **Formal** (official, legal, ceremonial)
- **Informal** (casual conversation, family settings)
- **Liturgical** (prayer, worship, ritual)
- **Prophetic** (divine pronouncement, judgment)
- **Didactic** (teaching, instruction)
- **Exhortative** (encouragement, admonition)

## Language Family Implementation Status

### 🟢 Ready for Implementation
- **Japanese**: Complete keigo mapping (sonkeigo, kenjougo, teineigo)
- **Korean**: Speech level system documented (-yo, -습니다, -하십시오)
- **Javanese**: Ngoko/Krama/Krama Inggil distinctions
- **Thai**: Formal particles (ครับ/ค่ะ), royal language notes

### 🟡 Documented, Needs Testing
- **Vietnamese**: Pronoun system (anh/chị/em, ông/bà)
- **Hindi**: Formal/informal (आप/तुम/तू), respect particles (-जी)

### ⏳ T-V Distinction (Indo-European)
- [ ] French (tu/vous)
- [ ] Spanish (tú/usted)
- [ ] German (du/Sie)
- [ ] Russian (ты/вы)
- [ ] Polish (ty/pan/pani)

## Theological Considerations

**Jesus's Speech Patterns**:
- To disciples → Familiar register (intimate teaching)
- To crowds → Polite/Neutral (accessible, non-elite)
- To Pharisees → Variable (respectful challenge vs harsh rebuke)
- To demons → Direct/Harsh (absolute authority)
- To God (prayer) → Honorable (Father) vs Familiar (Abba)

**Translation Implications**: Wrong register choice can convey unintended authority dynamics, theological distortion (e.g., Jesus too casual to God, too harsh to disciples, too deferential to Pharisees).

## Next Actions Detail

### Stage 1: Tool Development (Priority 1)
- [ ] Parse biblical text for dialogue markers
- [ ] Extract speaker and listener from context
- [ ] Infer attitude from discourse markers (illocutionary force, lexical choices)
- [ ] Calculate age from biblical chronology data
- [ ] Classify speech style from genre and context

### Stage 2: Language Testing (Priority 2)
- [ ] Create test verses covering all 6 feature combinations
- [ ] Apply to Japanese translation, verify honorific choices
- [ ] Apply to Korean translation, check speech levels
- [ ] Document systematic divergences (cultural adaptation vs error)

### Stage 3: Cross-Feature Integration (Priority 3)
- [ ] Test with Surface Realization (formal → noun vs informal → pronoun/zero)
- [ ] Check Illocutionary Force (imperative register variation)
- [ ] Validate Person/Number (T-V in plural "you")

### Stage 4: Validation & Peer Review
- [ ] Theological review: Are register choices theologically sound?
- [ ] Native speaker review: Japanese, Korean, Thai, Vietnamese, Hindi speakers
- [ ] Translation practitioner feedback: Real-world testing

## Open Questions

1. **Cultural Adaptation**: When translations adapt (e.g., more formal than source), is this error or valid choice?
2. **Ancient vs Modern**: How to handle register shifts over 2000 years (Greek koine → Modern Greek)?
3. **T-V Distinction in Prayer**: Theological debate (tu vs vous to God) - document both traditions?

## Learnings for Other Features

**Multi-Feature Coordination Pattern**: Honorifics demonstrates how 6 features work together to enable complex linguistic phenomena. Similar patterns may exist for other feature clusters.

## References

- Main feature spec: SPEAKER-DEMOGRAPHICS-README.md
- Language applications: LANGUAGE-APPLICATIONS.md
- Validation procedures: VALIDATION-CHECKLIST.md

## Migration Notes

Migrated from: `/plan/tbta-rebuild-with-llm/features/honorifics-register/`
Migration date: 2025-11-15
Status: Production-ready documentation, implementation phase required
