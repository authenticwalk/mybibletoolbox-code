# TBTA Feature Reproduction Framework

## Objective
Reproduce TBTA's linguistic annotations using LLM-based analysis to create prompts that accurately predict the correct linguistic features for Bible translation.

## Methodology

### Phase 1: Feature Isolation
Test individual features in isolation to understand prediction patterns:
1. Number systems (singular, dual, trial, paucal, plural)
2. Person systems (inclusive/exclusive)
3. Participant tracking
4. Proximity/demonstratives
5. Time granularity
6. Honorifics/register

### Phase 2: Feature Combination
Test combinations of features that interact:
1. Number + Person (e.g., dual inclusive)
2. Time + Aspect + Mood
3. Participant tracking + Proximity
4. Speaker demographics + Register

### Phase 3: Language-Specific Testing
Test complete feature sets for specific language families:
1. Austronesian languages
2. Trans-New Guinea languages
3. East Asian languages with honorifics

## Experiment Structure

Each experiment should:
1. Select a verse with known TBTA annotations
2. Create a hypothesis/prompt for predicting the feature
3. Test the prompt WITHOUT knowing the answer
4. Compare prediction to actual TBTA data
5. Record success/failure and reasons
6. Refine hypothesis based on errors
7. Retest with refined approach

## Success Metrics

- **Accuracy**: % of features correctly predicted
- **Precision**: When we predict a feature, is it correct?
- **Recall**: Do we catch all instances of a feature?
- **F1 Score**: Harmonic mean of precision and recall

## Error Analysis Categories

1. **Missing Context**: Need more surrounding verses
2. **Language Knowledge**: Need specific language family information
3. **Theological Knowledge**: Need doctrinal understanding
4. **Cultural Knowledge**: Need cultural/historical context
5. **Ambiguity**: Multiple valid interpretations
6. **TBTA Error**: Possible annotation error in source data

## Documentation Requirements

For each experiment, document:
- Verse reference
- Feature being tested
- Initial hypothesis/prompt
- Prediction made
- Actual TBTA value
- Success/failure
- Error category (if failed)
- Refined hypothesis
- Lessons learned