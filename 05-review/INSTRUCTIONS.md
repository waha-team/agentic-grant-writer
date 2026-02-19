# Stage 05: Review

> **Your job:** Critically review each proposal. Produce a review summary telling human reviewers exactly what needs attention.

---

## Before You Start

Read everything: CONTEXT files, project brief, and each foundation's full dossier (00-07).

## What to Do

For each foundation's proposal set, evaluate against these checks:

### The "Sales Letter" Check
- [ ] Does it lead with the problem, not with who we are?
- [ ] Would a first-time reader care about this problem after the first paragraph?
- [ ] Is there a clear "so what?" — why should THIS foundation invest in THIS?
- [ ] Is the core compelling idea clear and memorable?

### Vocabulary & Personalization Check
- [ ] Does the proposal use the foundation's own language? (Check against 03-VOCABULARY-AND-FRAMING.md)
- [ ] Are there any places where we used our jargon instead of theirs?
- [ ] Is the cover letter addressed to specific people? (Check against 02-KEY-PEOPLE.md)
- [ ] Does it reference specific grants they've made? (From 01-990-ANALYSIS.md)
- [ ] Are relevant partners mentioned? (From PARTNERSHIPS.md)

### 990-Informed Strategy Check
- [ ] Is the ask amount consistent with 01-990-ANALYSIS.md recommendation?
- [ ] Is the ask sized for a first-time grantee (not our full project budget)?
- [ ] If requesting partial funding, is it clear which component the grant covers?

### Completeness Check
- [ ] Every required section/question addressed? (Per 04-APPLICATION-REQUIREMENTS.md)
- [ ] Budget complete and math correct?
- [ ] All required attachments noted?

### Quality Check
- [ ] At least one story/testimonial?
- [ ] At least one compelling data point?
- [ ] Is it concise? Could sections be tightened?
- [ ] Confident without being arrogant?

### Accuracy Check
- [ ] Statistics consistent with IMPACT_DATA.md?
- [ ] Budget consistent with PROJECT_BRIEF.md?
- [ ] EIN correct (35-2894107)?
- [ ] Organizational description accurate?

### Security Check
- [ ] No named individuals in restricted-access nations?
- [ ] No specific locations that shouldn't be revealed?

## Output

Add `07-REVIEW-NOTES.md` to each foundation's subfolder:

```
# Review Notes: [Foundation Name]

*Reviewed: [DATE]*

## Status: [READY / MINOR EDITS / MAJOR REVISION / NOT RECOMMENDED]

## Strengths
- [What's strong]

## Issues Found
- **[CRITICAL/MINOR]:** [Issue and location in draft]

## Specific Edits
1. [Specific edit: "In 05-PROPOSAL-DRAFT.md, paragraph 3, change X to Y"]

## Vocabulary Audit
- [Any places where our language was used instead of theirs]

## Human Review Needed
- [Decisions requiring human judgment]
```

Then create `REVIEW_SUMMARY.md` in the project folder:

```
# Review Summary: [Project Name]

## Submission Queue (prioritized by deadline)
| Foundation | Ask | Deadline | Status | Submitter |
|-----------|-----|----------|--------|-----------|
| [Name] | $X | [Date] | Ready | [Assign] |

## Before Submitting
1. Read 07-REVIEW-NOTES.md for each foundation
2. Fill in any [JOSH: PLEASE ANSWER] placeholders
3. Gather universal documents
4. Final human read of each proposal
5. Submit via method in 04-APPLICATION-REQUIREMENTS.md
```

Add any CRITICAL issues to HUMAN_TODO.md.

Move project to `06-submitted/` once human reviews are complete and submissions begin.
