# TBTA-Strong's Linking Script - Improved Implementation Plan

## Executive Summary

This plan details the implementation of a Python script to extract TBTA linguistic nodes and link them to Strong's Concordance numbers, creating enriched Strong's data files. The script will aggregate distinct TBTA nodes per Strong's word with example verses.

**Key Challenge Identified**: TBTA data does NOT contain direct Strong's numbers or Macula IDs. Linking requires cross-referencing via verse coordinates with the Macula dataset.

## Critical Findings from Analysis

### 1. TBTA Data Structure (JSON/XML)
- **Hierarchical tree structure**: Clauses → NP/VP/etc → Words
- **No Strong's numbers**: TBTA contains only English glosses (e.g., "God", "create")
- **No Macula IDs**: TBTA is independent of source language alignment
- **Rich linguistic features**: 59+ attributes per node (Constituent, LexicalSense, Part, Number, Person, etc.)
- **Verse-level files**: One file per verse (e.g., `00_001_001_Genesis.json`)

### 2. Linking Strategy

**Required Data Sources**:
1. **TBTA Dataset** (GitHub: AllTheWord/tbta_db_export) - Linguistic features
2. **Macula Dataset** (.data/commentary/{BOOK}/{ch:03d}/{verse:03d}/{BOOK}-{ch:03d}-{verse:03d}-macula.yaml) - Strong's mapping

**Linking Process**:
```
TBTA verse file → Macula verse file → Strong's numbers → Aggregate nodes
```

**Example Flow**:
```
GEN 1:1 TBTA node "God"
→ Lookup GEN-001-001-macula.yaml
→ Find Hebrew word "אֱלֹהִים" (position 1)
→ Extract Strong's H0430
→ Aggregate TBTA node attributes to H0430-tbta.yaml
```

### 3. Edge Cases & Challenges

| Challenge | Impact | Solution |
|-----------|--------|----------|
| TBTA uses English glosses, not source language | Cannot directly link to Strong's | Cross-reference via Macula alignment at verse level |
| Multiple words may map to same gloss | Positional ambiguity | Use word position + context from Macula alignment |
| TBTA covers only 37% of Bible (11,649 verses) | Incomplete Strong's coverage | Document coverage stats, prioritize covered words |
| TBTA may have multiple nodes per verse for same word | Duplicate/variant nodes | Deduplicate by node attributes, keep distinct patterns |
| Macula files may not exist for all TBTA verses | Missing linking data | Skip verses without Macula, log warnings |

## Implementation Plan

### Phase 1: Data Acquisition & Setup

**Goal**: Download datasets and verify structure

**Tasks**:
1. Clone TBTA repository (already handled by extract_feature.py pattern)
2. Verify Macula dataset availability in .data/commentary
3. Create output directory: .data/strongs/{H|G}{num:04d}/
4. Set up logging infrastructure

**Verification**:
- [ ] TBTA JSON files accessible (~11,649 files)
- [ ] Sample Macula files readable
- [ ] Output directory writable
- [ ] Git sparse-checkout considerations documented

### Phase 2: Verse-Level Linking Algorithm

**Goal**: Map TBTA nodes → Strong's numbers via Macula

**Algorithm**:
```python
For each TBTA verse file:
  1. Parse TBTA JSON → extract linguistic nodes with attributes
  2. Load corresponding Macula YAML for same verse
  3. For each TBTA node:
     a. Match node position/gloss to Macula word alignment
     b. Extract Strong's number from Macula word entry
     c. Store: (Strong's #, TBTA node attributes, verse reference)
  4. Handle missing Macula files gracefully (log warning)
```

**Data Structures**:
```python
{
  "H0430": {
    "nodes": [
      {
        "Constituent": "God",
        "LexicalSense": "A",
        "Part": "Noun",
        "Number": "Singular",
        "Person": "Third",
        # ... all TBTA attributes
        "verses": ["GEN.001.001", "GEN.001.003", ...]  # First 100 examples
      },
      # ... other distinct nodes for H0430
    ]
  }
}
```

**Edge Case Handling**:
- **Missing Macula file**: Log warning, skip verse, continue processing
- **Ambiguous alignment**: Use position-based matching with fuzzy tolerance
- **Multiple TBTA nodes per word**: Keep distinct nodes separately
- **Verse cap**: Max 100 example verses per node (configurable)

### Phase 3: Node Aggregation & Deduplication

**Goal**: Aggregate distinct TBTA nodes per Strong's word

**Deduplication Strategy**:
```python
def deduplicate_nodes(nodes):
    """
    Two nodes are considered DISTINCT if they differ in ANY linguistic attribute.
    Use all TBTA attributes as deduplication key (excluding verse list).
    """
    unique_nodes = {}
    for node in nodes:
        # Create signature from all attributes (except verses)
        signature = hash(frozenset(node.items() - {'verses'}))

        if signature not in unique_nodes:
            unique_nodes[signature] = node
        else:
            # Merge verse lists (cap at 100)
            existing_verses = unique_nodes[signature]['verses']
            new_verses = node['verses']
            unique_nodes[signature]['verses'] = (existing_verses + new_verses)[:100]

    return list(unique_nodes.values())
```

**Performance Optimization**:
- Process verses in batches (1000 files/batch)
- Use dict for O(1) Strong's number lookup
- Stream write aggregated data periodically
- Memory limit: ~2GB for full dataset

### Phase 4: YAML Output Generation

**Goal**: Generate standardized Strong's YAML files

**Output Format** (per STANDARDIZATION.md):
```yaml
# File: .data/strongs/H0430/H0430-tbta.yaml

strongs: H0430
word: "אֱלֹהִים"
gloss: "God, gods"
tbta_coverage: 847  # Total verses with TBTA data for this word

nodes:
  - Constituent: God
    LexicalSense: A
    Part: Noun
    SemanticComplexityLevel: '1'
    Number: Singular
    Person: Third
    ParticipantTracking: Routine
    ParticipantStatus: Not Applicable
    Proximity: Not Applicable
    Polarity: Affirmative
    verses:
      - GEN.001.001
      - GEN.001.003
      - GEN.001.006
      # ... max 100 examples

  - Constituent: God
    LexicalSense: B
    Part: Noun
    # ... different node pattern
    verses:
      - GEN.001.026
      # ... max 100 examples

metadata:
  generated: 2025-11-15T18:30:00Z
  tbta_commit: abc1234
  tbta_verses_processed: 11649
  source: AllTheWord/tbta_db_export
```

**File Naming**:
- Hebrew: `.data/strongs/H0430/H0430-tbta.yaml`
- Greek: `.data/strongs/G0026/G0026-tbta.yaml`

**Validation**:
- All required fields present
- Verse references in standard format (BOOK.###.###)
- No duplicate verses within same node
- YAML parses without errors

### Phase 5: Testing & Validation

**Test Cases**:

1. **Basic Linking Test**:
   - Input: GEN.001.001 TBTA + Macula
   - Expected: H0430 (God), H1254 (create), H8064 (heaven), H0776 (earth)
   - Verify: Node attributes match TBTA source

2. **Missing Macula Test**:
   - Input: TBTA verse without Macula file
   - Expected: Warning logged, verse skipped, no crash

3. **Multiple Nodes Test**:
   - Input: Verse with repeated Strong's number but different TBTA nodes
   - Expected: Separate nodes in output, distinct by attributes

4. **Verse Cap Test**:
   - Input: Strong's word appearing >100 times
   - Expected: Exactly 100 verses in output, first occurrences preserved

5. **Performance Test**:
   - Input: Full TBTA dataset (11,649 verses)
   - Expected: <10 minutes runtime, <2GB memory, all files generated

**Validation Checklist**:
- [ ] Output files match SCHEMA.md structure
- [ ] All Strong's numbers in range (H0001-H8674, G0001-G5624)
- [ ] No fabricated data (all from TBTA source)
- [ ] Verse references validate against Bible structure
- [ ] Git sparse-checkout doesn't filter created files

## Performance Considerations

**Expected Statistics**:
- TBTA verses: 11,649
- Unique Strong's words covered: ~2,000-3,000 (estimate)
- Average nodes per Strong's word: 5-10 distinct patterns
- Total output files: ~2,000-3,000 YAML files
- Processing time: 5-10 minutes (single-threaded)
- Memory usage: ~1-2GB peak

**Optimization Strategies**:
1. **Batch processing**: Process 1000 verses → aggregate → write
2. **Lazy loading**: Load Macula files on-demand, not all at once
3. **Streaming writes**: Write Strong's files as completed, don't hold all in memory
4. **Index caching**: Cache Macula file paths for faster lookup

**Scaling**:
- Current: Single-threaded, adequate for 11K verses
- Future: Parallel processing for full Bible coverage expansion

## Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    TBTA-Strong's Linking Pipeline            │
└─────────────────────────────────────────────────────────────┘

Input Sources:
┌──────────────────┐        ┌──────────────────────────┐
│  TBTA Repository │        │  Macula Dataset          │
│  (GitHub)        │        │  (.data/commentary/)     │
│                  │        │                          │
│  JSON/XML files  │        │  YAML files with         │
│  11,649 verses   │        │  Strong's alignment      │
└────────┬─────────┘        └───────────┬──────────────┘
         │                              │
         │                              │
         ▼                              ▼
┌─────────────────────────────────────────────────────────────┐
│              Step 1: Verse-Level Processing                  │
│                                                              │
│  For each TBTA verse file (e.g., 00_001_001_Genesis.json): │
│  1. Parse TBTA tree → Extract nodes with attributes         │
│  2. Load Macula YAML for same verse                         │
│  3. Align TBTA nodes → Macula words → Strong's numbers      │
│  4. Collect: (Strong's #, Node attributes, Verse ref)       │
└────────┬─────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│           Step 2: Aggregation by Strong's Number            │
│                                                              │
│  Group by Strong's #:                                        │
│  H0430 → [node1, node2, ...]                                │
│  H1254 → [node1, ...]                                        │
│  G0026 → [node1, node2, ...]                                │
└────────┬─────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│         Step 3: Deduplication & Verse Capping               │
│                                                              │
│  For each Strong's number:                                   │
│  1. Deduplicate nodes by attribute signature                 │
│  2. Cap verse examples at 100 per node                       │
│  3. Sort nodes by frequency (most common first)              │
└────────┬─────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│              Step 4: YAML File Generation                    │
│                                                              │
│  Write to: .data/strongs/{H|G}{num:04d}/{num}-tbta.yaml    │
│                                                              │
│  Structure:                                                  │
│  - strongs: H0430                                           │
│  - nodes: [distinct TBTA patterns]                          │
│  - metadata: generation info                                │
└────────┬─────────────────────────────────────────────────────┘
         │
         ▼
Output:
┌──────────────────────────────────────────────────────────────┐
│  ~2,000-3,000 Strong's YAML files                           │
│                                                              │
│  .data/strongs/H0430/H0430-tbta.yaml                        │
│  .data/strongs/H1254/H1254-tbta.yaml                        │
│  .data/strongs/G0026/G0026-tbta.yaml                        │
│  ...                                                         │
└──────────────────────────────────────────────────────────────┘
```

## Risk Analysis & Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **Macula files incomplete for TBTA verses** | High | Medium | Graceful skipping, coverage reporting |
| **Positional alignment errors** | Medium | High | Fuzzy matching, manual validation sample |
| **Memory overflow on full dataset** | Low | High | Batch processing, streaming writes |
| **Git sparse-checkout filtering outputs** | Medium | High | Pre-configure sparse-checkout, document setup |
| **TBTA structure changes in future** | Low | Medium | Version pinning, schema validation |
| **Duplicate Strong's numbers (rare variants)** | Very Low | Low | Use canonical Strong's numbering |

## Next Steps

### Immediate Actions
1. **Researcher**: Investigate Macula file structure and alignment strategy
2. **Researcher**: Sample 10-20 verses to verify linking feasibility
3. **Coder**: Implement prototype linking algorithm for Genesis 1
4. **Analyst**: Review prototype results, validate accuracy

### Implementation Sequence
1. **Week 1**: Prototype verse linking (Genesis 1 only)
2. **Week 2**: Full pipeline implementation
3. **Week 3**: Testing & validation
4. **Week 4**: Production run & documentation

## Success Criteria

- [ ] Script processes all 11,649 TBTA verses without crashes
- [ ] Linking accuracy >95% (validated on sample)
- [ ] Output files conform to STANDARDIZATION.md and SCHEMA.md
- [ ] Coverage report shows Strong's words enriched
- [ ] Documentation complete (usage, limitations, future work)
- [ ] Git sparse-checkout instructions prevent data loss
- [ ] Runtime <10 minutes on standard hardware
- [ ] Memory usage <2GB peak

## References

- **TBTA Source**: https://github.com/AllTheWord/tbta_db_export
- **Macula Dataset**: .data/commentary/ (mybibletoolbox-data repo)
- **Strong's Format**: /workspaces/mybibletoolbox-code/STANDARDIZATION.md
- **YAML Schema**: /workspaces/mybibletoolbox-code/SCHEMA.md
- **Extract Feature Pattern**: /workspaces/mybibletoolbox-code/src/ingest-data/tbta/extract_feature.py

---

**Document Status**: Initial analysis complete
**Last Updated**: 2025-11-15
**Analyst**: Code Analyzer Agent (tbta-strongs hive mind)
