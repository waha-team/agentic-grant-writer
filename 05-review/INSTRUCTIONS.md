# Stage 05: Review

> **Your job:** Critically review each proposal. Produce a review summary telling human reviewers exactly what needs attention.

---

## Before You Start

1. Read everything: CONTEXT files, project brief, and each foundation's full dossier (00-07)
2. **Check `CONTEXT/PROSPECTIVE_PARTNERS.md`** for any status updates on foundations

## What to Do

For each foundation's proposal set, evaluate against these checks:

### The "Sales Letter" Check
- [ ] Does it lead with the problem, not with who we are?
- [ ] Would a first-time reader care about this problem after the first paragraph?
- [ ] Is there a clear "so what?" — why should THIS foundation invest in THIS?
- [ ] Is the core compelling idea clear and memorable?

### Vocabulary & Personalization Check
- [ ] Does the proposal use the foundation's own language? (Check against `03-VOCABULARY-AND-FRAMING - [Foundation Name] - [Project Name].md`)
- [ ] Are there any places where we used our jargon instead of theirs?
- [ ] Is the cover letter addressed to specific people? (Check against `02-KEY-PEOPLE - [Foundation Name] - [Project Name].md`)
- [ ] Does it reference specific grants they've made? (From `01-990-ANALYSIS - [Foundation Name] - [Project Name].md`)
- [ ] Are relevant partners mentioned? (From PARTNERSHIPS.md)

### 990-Informed Strategy Check
- [ ] Is the ask amount consistent with `01-990-ANALYSIS - [Foundation Name] - [Project Name].md` recommendation?
- [ ] Is the ask sized for a first-time grantee (not our full project budget)?
- [ ] If requesting partial funding, is it clear which component the grant covers?

### Completeness Check
- [ ] Every required section/question addressed? (Per `04-APPLICATION-REQUIREMENTS - [Foundation Name] - [Project Name].md`)
- [ ] Budget complete and math correct?
- [ ] All required attachments noted?

### Quality Check
- [ ] At least one story/testimonial?
- [ ] At least one compelling data point?
- [ ] All acronyms defined on first use? (DBS, DMC, DMM, etc.)
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

### Markdown Formatting Check
- [ ] Key-value blocks (contact info, org details) use lists, tables, or blank-line separation?
- [ ] Blank lines before and after all headers?
- [ ] Blank lines before and after all lists and tables?
- [ ] Document renders correctly when pasted into Google Docs?

## Output

Add `07-REVIEW-NOTES - [Foundation Name] - [Project Name].md` to each foundation's subfolder:

```
# Review Notes: [Foundation Name]

*Reviewed: [DATE]*

## Status: [READY / MINOR EDITS / MAJOR REVISION / NOT RECOMMENDED]

## Strengths
- [What's strong]

## Issues Found
- **[CRITICAL/MINOR]:** [Issue and location in draft]

## Specific Edits
1. [Specific edit: "In `05-PROPOSAL-DRAFT - [Foundation Name] - [Project Name].md`, paragraph 3, change X to Y"]

## Vocabulary Audit
- [Any places where our language was used instead of theirs]
- [Undefined acronyms that need spelling out]

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
1. Read `07-REVIEW-NOTES - [Foundation Name] - [Project Name].md` for each foundation
2. Fill in any [ALYCIA: PLEASE ANSWER] placeholders
3. Gather universal documents
4. Final human read of each proposal
5. Submit via method in `04-APPLICATION-REQUIREMENTS - [Foundation Name] - [Project Name].md`
```

Add any CRITICAL issues to HUMAN_TODO.md.

### Final Step: Update Prospective Partners Registry
Update `CONTEXT/PROSPECTIVE_PARTNERS.md`:
1. Update each foundation's status to reflect review findings
2. Note any issues that need to be resolved before submission

Move project to `06-submitted/` ONLY after human reviews are complete and submissions begin.
