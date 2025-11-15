# Historical Error Tracking Framework

**Created:** 2025-11-12
**Purpose:** Track when/why/how errors emerge and spread to predict future patterns

---

## Why Track History?

Understanding error lifecycle helps:
1. **Predict future errors** - patterns repeat
2. **Target correction efforts** - address at source
3. **Measure effectiveness** - track decline after correction
4. **Prevent propagation** - catch errors early

---

## Historical Data Points

### Timeline Tracking

```yaml
error_history:
  first_appearance:
    date: "{earliest documented instance}"
    source: "{where first found}"
    context: "{how it appeared}"

  popularization:
    date: "{when it became widespread}"
    trigger: "{what caused spread}"
    key_sources: ["{influential sources that spread it}"]

  peak_prevalence:
    period: "{when most common}"
    indicators: "{publications, sermons, etc.}"
    geographic_spread: "{regional or global}"

  current_status:
    date: "2025-11-12"
    trend: "{increasing|stable|declining}"
    recent_sources: ["{where still appearing}"]

  correction_efforts:
    first_refutation: "{date and source}"
    major_corrections: ["{list significant pushback}"]
    effectiveness: "{high|medium|low}"
```

---

## Categorization by Origin

### Type 1: Sermon Illustration Gone Viral
**Characteristics:**
- Started as memorable teaching tool
- Spread orally (sermon → sermon)
- Eventually published in books/devotionals
- Hard to trace original source

**Example: G1411 dunamis → dynamite**
- **Origin:** Unknown preacher ~1950s-1960s
- **Spread:** Sermon illustrations, devotional materials
- **Mechanism:** Memorability (alliteration, vivid imagery)
- **Peak:** 1980s-2000s widespread adoption
- **Current:** Still common despite corrections

**Pattern:** Oral → Published → Systematic

---

### Type 2: Apologetics Argument
**Characteristics:**
- Originated in evangelism/apologetics context
- Designed to prove doctrinal point
- Spread through mission organizations
- Resistant to correction (tied to doctrine)

**Example: H430 Elohim → Trinity proof**
- **Origin:** Early Christian apologetics (post-NT)
- **Spread:** Apologetics materials, evangelism to Jews/Muslims
- **Mechanism:** Simple "grammatical proof" of doctrine
- **Peak:** Ongoing (still used in apologetics)
- **Current:** Widespread in evangelistic contexts

**Pattern:** Doctrine Defense → Mission → Entrenchment

---

### Type 3: Etymology Enthusiasm
**Characteristics:**
- Arose from fascination with word roots
- Greek/Hebrew seen as "unlocking hidden meaning"
- Spread through Bible study materials
- Based on partial linguistic knowledge

**Example: G1577 ekklesia → "called out ones"**
- **Origin:** Etymology analysis (ek + kaleo breakdown)
- **Spread:** Church identity teaching, systematic theology
- **Mechanism:** Feels scholarly, reinforces separation theology
- **Peak:** Widespread in evangelical/reformed circles
- **Current:** Common in church teaching

**Pattern:** Etymology Discovery → Teaching → Church Identity

---

### Type 4: Translation Note Fossilization
**Characteristics:**
- Started in old translation notes or study Bibles
- Perpetuated through copying
- Rarely questioned due to "authority" of source
- Difficult to update once in print

**Example:** Various study Bible notes
- **Origin:** Early study Bible editions
- **Spread:** Copied into subsequent editions/other Bibles
- **Mechanism:** Authority of printed resource
- **Current:** Slowly updating but entrenched

**Pattern:** Print → Authority → Perpetuation

---

## Tracking Propagation Mechanisms

### Mechanism 1: Oral Tradition (Sermon → Sermon)
**Speed:** Fast (years to decades)
**Reach:** Local → Regional → National
**Resistance to Correction:** High (no central authority)

**Indicators:**
- Multiple preachers teaching independently
- Geographic clustering (regional teaching patterns)
- Variations in phrasing (oral mutation)

---

### Mechanism 2: Published Materials
**Speed:** Moderate (decades to century)
**Reach:** Global
**Resistance to Correction:** Very High (print permanence)

**Indicators:**
- Books, study Bibles, commentaries
- Translation notes
- Curriculum materials

---

### Mechanism 3: Institutional Adoption
**Speed:** Slow (decades to century)
**Reach:** Deep (affects generations)
**Resistance to Correction:** Extremely High (institutional inertia)

**Indicators:**
- Seminary curricula
- Denominational materials
- Systematic theology texts

---

### Mechanism 4: Digital Viral Spread
**Speed:** Very Fast (months to years)
**Reach:** Global instant
**Resistance to Correction:** Variable (can correct quickly but also entrench)

**Indicators:**
- Blog posts with high shares
- Social media viral posts
- YouTube sermon clips
- Copy-paste across websites

---

## Historical Pattern Examples

### Pattern A: Dunamis → Dynamite

```yaml
timeline:
  1867: Dynamite invented by Alfred Nobel
  ~1950s-1960s: Error first appears in sermon illustrations (unknown origin)
  1970s-1980s: Spreads through evangelical preaching
  1990s-2000s: Appears in devotional books (Harvest Ministries, others)
  1984: D.A. Carson identifies as fallacy in "Exegetical Fallacies"
  2000s-2010s: Scholarly pushback increases (blogs, articles)
  2014: Multiple refutation articles published
  2020s: Still common despite corrections

propagation_analysis:
  mechanism: "Oral (sermon) → Published (devotional) → Digital (blogs)"
  speed: "70 years from origin to peak"
  resistance: "High - memorability trumps accuracy"

correction_effectiveness:
  scholarly_refutation: "Strong (Carson 1984+)"
  popular_impact: "Limited - still taught widely"
  institutional_change: "Minimal - not in curricula anyway"

trend_projection:
  2025-2030: "Gradual decline as corrections spread"
  2030-2040: "May persist in informal teaching"
  long_term: "Likely to continue in some circles indefinitely"
```

---

### Pattern B: Ekklesia → "Called Out Ones"

```yaml
timeline:
  Ancient: Ekklesia = assembly (standard meaning)
  Early Church: Christians adopted term for congregations
  Medieval-Reformation: Focus on NT Greek intensifies
  ~1800s-1900s: Etymology analysis becomes popular
  1900s: "Called out ones" teaching emerges
  Mid-1900s: Systematic church teaching adopts this
  2000s: Appears in church identity materials, sermon series
  2010s: Scholarly refutation increases (blogs, Stack Exchange)
  2021: Multiple refutation articles published
  2020s: Still widespread in evangelical/reformed churches

propagation_analysis:
  mechanism: "Etymology discovery → Church identity → Systematic teaching"
  speed: "100+ years from emergence to entrenchment"
  resistance: "Very High - tied to church self-understanding"

correction_effectiveness:
  scholarly_refutation: "Strong (BDAG, NIDNTTE, etc.)"
  popular_impact: "Limited - affects identity"
  institutional_change: "Slow - requires rethinking ecclesiology"

trend_projection:
  2025-2030: "Slow decline in academic contexts"
  2030-2040: "Persist in church teaching (identity invested)"
  long_term: "May take generations to fully correct"
```

---

## Trend Analysis Framework

### Increasing Trend (Growing Error)
**Indicators:**
- New publications citing it
- Social media shares increasing
- More churches teaching it
- Seminary adoption

**Response:**
- Immediate correction priority (P1)
- Proactive refutation campaign
- Seminary/denomination notification
- Quick reference cards distributed

---

### Stable Trend (Entrenched Error)
**Indicators:**
- Consistent mentions over time
- Neither growing nor declining
- Institutional entrenchment
- No major new sources but perpetuation

**Response:**
- Standard correction approach (P2-P3)
- Long-term education strategy
- Update study materials over time
- Next-generation focus

---

### Declining Trend (Correcting Error)
**Indicators:**
- Fewer new mentions
- Scholarly consensus established
- Major sources issuing corrections
- Next generation not learning it

**Response:**
- Continue corrections but lower priority (P3-P4)
- Document success for future reference
- Monitor for resurgence
- Maintain reference materials

---

## Integration with Schema

Add to `community-discussions.yaml`:

```yaml
error_history:
  first_documented:
    date: "{earliest known instance}"
    source: "{where found}"
    context: "{how it appeared}"

  popularization:
    period: "{when became widespread}"
    mechanism: "{oral|published|institutional|digital}"
    key_sources:
      - source: "{influential book/sermon/blog}"
        date: "YYYY"
        impact: "{how it contributed to spread}"

  peak_prevalence:
    period: "{when most common}"
    evidence: "{publications count, church adoption, etc.}"

  correction_timeline:
    first_refutation:
      date: "YYYY"
      source: "{Carson, blog, journal}"

    major_corrections:
      - date: "YYYY"
        source: "{source}"
        type: "{scholarly|popular|institutional}"
        impact: "{high|medium|low}"

  current_status:
    as_of: "2025-11-12"
    trend: "{increasing|stable|declining}"
    recent_activity:
      - date: "YYYY-MM"
        type: "{new publication|blog post|sermon|correction}"
        source: "{source}"

  projection:
    short_term: "{next 5 years}"
    medium_term: "{5-10 years}"
    long_term: "{10+ years}"
    confidence: "{high|medium|low}"
```

---

## Research Methods

### Finding First Appearance
1. **Google Books Ngram** - Track term frequency over time
2. **Archive searches** - Old sermon collections, periodicals
3. **Seminary archives** - Course materials, lecture notes
4. **Denominational archives** - Teaching materials history
5. **Expert interviews** - Ask senior pastors/scholars "When did you first hear this?"

### Tracking Propagation
1. **Publication search** - Books, articles mentioning error
2. **Sermon audio archives** - SermonAudio, church websites
3. **Blog/website search** - Wayback Machine for historical data
4. **Social media tracking** - Earliest mentions on platforms
5. **Curriculum analysis** - Bible college/seminary materials

### Measuring Correction Impact
1. **Before/after analysis** - Mentions pre/post correction
2. **Source updates** - Which publishers issued corrections
3. **Seminary adoption** - Course material changes
4. **Pastor surveys** - "Are you still teaching this?"
5. **Translation note updates** - Bible translation corrections

---

## Success Stories (Errors Successfully Corrected)

### Example: {Error that was corrected}
```yaml
error: "{what the error was}"
correction_campaign:
  start_date: "YYYY"
  key_actions:
    - "{major scholar published refutation}"
    - "{denomination issued correction}"
    - "{study Bible updated notes}"
  results:
    decline_rate: "{percentage decrease}"
    time_to_rare: "{years from peak to rare}"
    lessons_learned: "{what worked}"
```

*Note: To be filled in as Tool 4 produces measurable corrections*

---

## Predictive Value

Historical patterns help predict:

1. **Which new errors will spread** (characteristics of successful errors)
2. **How long correction takes** (based on mechanism and entrenchment)
3. **Which interventions work** (publication, institutional, viral correction)
4. **When to intervene** (early = easier correction)

See `ERROR-PREDICTION-SYSTEM.md` for full predictive framework.

---

**Status:** Framework complete, ready for data collection
**Next:** Apply to experiments, track correction effectiveness
