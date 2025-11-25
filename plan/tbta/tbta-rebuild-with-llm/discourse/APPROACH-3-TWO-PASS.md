# Approach 3: Two-Pass Processing (Comprehensive)


**Concept**: First pass extracts chapter-level discourse structure, second pass uses that structure for verse-level feature prediction.

#### How It Works

**Pass 1: Discourse Analysis** (Chapter-level)
```python
def pass1_discourse_analysis(chapter_ref):
    """Extract discourse-level structures"""
    chapter_text = load_full_chapter(chapter_ref)

    discourse_structure = llm.analyze(f"""
    Analyze discourse structure of {chapter_ref}:

    1. Participant Registry:
       - List all entities (people, things, concepts)
       - Mark first appearance verse for each
       - Track which verses each appears in

    2. Notional Structure:
       - Identify discourse units (scenes, sections)
       - Mark boundaries

    3. Topic Flow:
       - What is the topic in each section?
       - Where do topic shifts occur?

    4. Coreference Chains:
       - Map all pronouns to antecedents

    Output as structured data.
    """)

    save_discourse_structure(chapter_ref, discourse_structure)
    return discourse_structure
```

**Pass 2: Verse Feature Extraction** (Uses discourse structure)
```python
def pass2_feature_extraction(verse_ref):
    """Extract features using discourse context"""
    # Load discourse structure from Pass 1
    chapter = get_chapter(verse_ref)
    discourse = load_discourse_structure(chapter)

    verse_data = load_verse(verse_ref)

    # Now predict with full context
    features = predict_features(
        verse_data,
        participant_registry=discourse.participants,
        coreference_chains=discourse.coreferences,
        topic_context=discourse.topics
    )

    return features
```

#### Pros

✅ **Best accuracy** - Combines LLM discourse understanding + systematic extraction
✅ **Separation of concerns** - Discourse analysis separate from feature extraction
✅ **Reusable structure** - Pass 1 output used by all features
✅ **Cacheable** - Discourse structure computed once, reused many times
✅ **Human reviewable** - Can manually verify Pass 1 output
✅ **Incremental improvement** - Refine discourse analysis without re-running extraction

#### Cons

⚠️ **Most complex** - Two separate processing pipelines
⚠️ **Highest cost** - LLM analysis of full chapters + verse-level processing
⚠️ **Dependencies** - Pass 2 blocked on Pass 1 completion
⚠️ **Error propagation** - Pass 1 errors affect all Pass 2 predictions
⚠️ **Storage overhead** - Must store intermediate discourse structures

#### Implementation Plan

**Phase 1: Design** (1 week)
1. Define discourse structure schema
2. Design prompt for Pass 1 discourse analysis
3. Create validation tests

**Phase 2: Pass 1 Implementation** (2 weeks)
1. Build chapter-level discourse analyzer
2. Test on 5 chapters (diverse genres)
3. Validate output quality

**Phase 3: Pass 2 Integration** (2 weeks)
1. Modify feature extractors to consume discourse structure
2. Test accuracy improvement vs verse-only
3. Build caching layer

**Phase 4: Scale** (3 weeks)
1. Process discourse structure for all books
2. Human review of discourse structures
3. Refine based on errors

**Estimated Timeline**: 8 weeks to production-ready
