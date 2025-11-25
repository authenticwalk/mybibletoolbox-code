# TBTA NounListIndex - Summary and Practical Applications

## Executive Summary
The TBTA NounListIndex system provides verse-level entity coreference tracking essential for Bible translation into morphologically complex languages, particularly those with switch-reference systems.

## Key Findings

### 1. Verse-Scoped Indexing
- **Indices restart at 1 for each verse**
- No cross-verse index continuity
- Complete coreference data within each verse boundary

### 2. Consistent Entity Tracking
- Each unique entity receives one index per verse
- All mentions of the same entity share the index
- Includes pronouns, repeated nouns, and implicit references

### 3. Validated Test Case (Matthew 24:46-47)

**Verse 46 Entities:**
- Index 1: Master (3 occurrences)
- Index 2: House (1 occurrence)
- Index 3: Servant (3 occurrences)
- Index 4: Things/tasks (2 occurrences)

**Verse 47 Entities:**
- Index 1: Jesus/Speaker
- Index 2: Followers/Audience
- Index 3: Truth
- Index 4: Servant (continuation from v46, new index)
- Index 5: Master (continuation from v46, new index)
- Index 6: Things/possessions (2 occurrences)

## Practical Applications

### 1. Switch-Reference Languages

Languages like those in Papua New Guinea mark verb continuity/discontinuity:

```
Example: Hua language marking
v46: servant-ERG work do-SAME.SUBJ master order-PAST
     (same subject marker because servant does what servant was ordered)

v47: master-ERG servant-ACC appoint-DIFF.SUBJ-FUT
     (different subject from previous clause)
```

The NounListIndex enables automated determination of these markers.

### 2. Pronoun Systems

For languages with complex pronoun systems based on:
- **Proximity** (proximal/medial/distal)
- **Visibility** (visible/non-visible)
- **Previous mention** (new/given information)

The index system tracks which entities are "given" vs "new" in discourse.

### 3. Zero Anaphora Languages

Languages like Japanese/Korean often drop pronouns entirely:

```
Japanese rendering concept:
v46: [servant-wa] shigoto-o shi-te-iru toki, [∅] kaette-kuru master-wa...
     (servant drops in second clause, tracked by index)
```

### 4. Ergative-Absolutive Alignment

For ergative languages, tracking whether an entity is agent or patient across clauses affects case marking:

```
Index 3 (servant) in v46:
- First as absolutive (intransitive subject): "servant does"
- Then as ergative (transitive agent): "servant does things"
- Then as absolutive (object): "master orders servant"
```

## Implementation Guidelines

### For Bible Translation Software

```python
class CrossVerseEntityTracker:
    def __init__(self):
        self.entity_map = {}  # Maps (verse, index) -> entity_id
        self.entity_properties = {}  # Stores semantic info

    def process_verse(self, verse_ref, tbta_data):
        indices = extract_noun_indices(tbta_data)

        for index, occurrences in indices.items():
            # Determine if this continues a previous entity
            entity_id = self.match_or_create_entity(
                verse_ref, index, occurrences
            )

            # Store mapping
            self.entity_map[(verse_ref, index)] = entity_id

    def get_switch_reference(self, verse1, idx1, verse2, idx2):
        """Determine if two references are same/different subject."""
        entity1 = self.entity_map.get((verse1, idx1))
        entity2 = self.entity_map.get((verse2, idx2))
        return 'SAME' if entity1 == entity2 else 'DIFFERENT'
```

### For Linguistic Analysis

1. **Discourse Prominence**: Entities with more index occurrences are discourse-prominent
2. **Information Structure**: First index typically = topic, later indices = new information
3. **Participant Tracking**: "Routine" vs "Frame Inferable" annotations show given/new status

### For Quality Assurance

Validation checks:
```python
def validate_tbta_indices(verse_data):
    checks = []

    # 1. Sequential numbering
    indices = extract_all_indices(verse_data)
    expected = range(1, max(indices) + 1)
    if missing := set(expected) - set(indices):
        checks.append(f"Missing indices: {missing}")

    # 2. Consistent constituents
    if duplicates := find_split_constituents(verse_data):
        checks.append(f"Same word, different indices: {duplicates}")

    # 3. Pronouns have antecedents
    if unresolved := find_unresolved_pronouns(verse_data):
        checks.append(f"Pronouns without antecedents: {unresolved}")

    return checks
```

## Future Research Directions

1. **Multi-verse Coreference Chains**: Build entity tracking across entire passages
2. **Ambiguous Reference Resolution**: Handle verses where pronoun reference is unclear
3. **Quote Attribution**: Track speakers in dialogue (who said what)
4. **Event Coreference**: Extend beyond entities to track event mentions
5. **Cross-lingual Validation**: Compare index assignments across language translations

## Conclusion

The TBTA NounListIndex provides crucial infrastructure for:
- Accurate Bible translation into morphologically complex languages
- Automated checking of translation consistency
- Linguistic research on Biblical discourse structure
- Training data for coreference resolution systems

While currently verse-scoped, the systematic indexing enables building higher-level cross-verse entity tracking systems essential for languages with grammaticalized reference tracking.