# Progressive Disclosure Exceptions

This document tracks files that exceed progressive disclosure limits with justification.

## Standard Limits

- **READMEs**: ≤200 lines
- **Topic files**: ≤400 lines
- **Technical references** (like STAGES.md): ≤500 lines

## Documented Exceptions

### learnings/README.md (568 lines)

**Limit**: 200 lines (README standard)
**Actual**: 568 lines
**Justification**: Comprehensive methodology guide consolidating 6 source files (57KB total). Content includes:
- 8 core prompt engineering patterns with templates
- 4-phase adversarial testing strategy with examples
- 6 common error patterns with detailed examples
- Complete best practices with DO/DON'T comparisons

**Why not split**:
- Loses coherence across methodology
- Creates navigation burden (6 separate files)
- Cross-references would be fragile
- Methodology needs to be read holistically

**Mitigation**:
- Clear table of contents
- Distinct sections with headers
- Quick reference guide at top
- Can be split in future if needed

### features/STAGES.md (550 lines)

**Limit**: 500 lines (technical reference exception)
**Actual**: 550 lines
**Justification**: Authoritative 6-stage feature development methodology. This is a **reference document**, not an overview README.

**Why not split**:
- Stages must be understood in sequence
- Templates are part of methodology (TBTA-REVIEW.md, TRANSLATOR-IMPACT.md)
- Splitting would break stage coherence

### structure/README.md (277 lines)

**Limit**: 200 lines
**Actual**: 277 lines
**Justification**: Documents complex hierarchical relationships between 59 features. Dense with structural information (feature trees, dependencies, validation patterns).

**Why not split**:
- Hierarchies need to be seen together
- Cross-references would be unclear if split
- Information density is high (not bloat)

## Citation Script Note

The `verify-citations.sh` script flags template placeholders like `{feature-name}` as unknown citations. These are **not** citations requiring ATTRIBUTION.md entries - they are template variables for feature developers to replace. This is expected behavior in STAGES.md, TEMPLATE.md, and learnings/README.md.

---

**Last Updated**: 2025-11-14
**Review Date**: After Phase 4 (feature migration) to assess if any docs grew too large
