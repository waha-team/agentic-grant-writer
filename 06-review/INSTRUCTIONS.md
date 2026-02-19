# Stage 06: Review

> **Your job:** Critically review each proposal draft against the foundation's criteria and Waha's standards. Produce a review summary that tells the human reviewers exactly what needs attention before submission.

---

## Before You Start

1. Read `CONTEXT/STYLE_GUIDE.md`
2. Read `CONTEXT/OUR_ORGANIZATION.md`
3. Read `CONTEXT/IMPACT_DATA.md`
4. Read everything in the project subfolder — the original brief, alignment analysis, application prep, and all drafts

## What to Do

For each project subfolder found in this directory:

### Step 1: Review Each Foundation's Proposal
For every foundation subfolder (e.g., `kern-family-foundation/`), evaluate:

#### Completeness Check
- [ ] Does the proposal address every section/question required by the foundation?
- [ ] Is the budget complete and does the math add up?
- [ ] Are all required attachments noted in APPLICATION_PREP.md accounted for?
- [ ] Is a cover letter or LOI included if needed?

#### Alignment Check
- [ ] Does the framing match this specific funder's priorities?
- [ ] Is the language appropriate for the funder type (evangelical, Catholic/Orthodox, broader Christian, secular)?
- [ ] Does the proposal make a clear case for why THIS foundation should fund THIS project?
- [ ] Is the ask amount appropriate for the foundation's typical grant size?

#### Quality Check
- [ ] Does it follow the STYLE_GUIDE.md?
- [ ] Is there at least one specific story/testimonial?
- [ ] Is there at least one compelling data point?
- [ ] Is it compelling? Would YOU fund this if you were the program officer?
- [ ] Is it concise? Could any sections be tightened?
- [ ] Is the tone confident without being arrogant?

#### Accuracy Check
- [ ] Are all statistics consistent with IMPACT_DATA.md?
- [ ] Is the budget consistent with PROJECT_BRIEF.md?
- [ ] Are there any claims that might not be verifiable?
- [ ] Is the organizational description accurate and current?

#### Security Check
- [ ] Are there any named individuals in restricted-access nations?
- [ ] Are there any specific locations mentioned that shouldn't be?
- [ ] Would this proposal put anyone at risk if it were shared publicly?

#### Sensitivity Check
- [ ] Does the proposal respect the foundation's theological/denominational perspective?
- [ ] Is there anything that might be culturally insensitive?
- [ ] Could any language be misinterpreted as manipulative or exploitative?

### Step 2: Produce Review Summary
Create a file called `REVIEW.md` inside the project's subfolder:

```
# Review Summary for [Project Name]

*Review completed: [DATE]*
*Proposals reviewed: [NUMBER]*

---

## Overall Assessment

[2-3 sentences: Is this project ready for submission? What's the general quality level? Any systemic issues across all proposals?]

## [Foundation Name]

**Status:** READY FOR SUBMISSION / NEEDS MINOR EDITS / NEEDS MAJOR REVISION / NOT RECOMMENDED

### Strengths
- [What's strong about this proposal]

### Issues Found
- **[CRITICAL/MINOR]:** [Description of issue and specific location in draft]
- **[CRITICAL/MINOR]:** [Description of issue]

### Specific Edits Needed
1. [Specific edit with location: "In PROPOSAL_DRAFT.md, paragraph 3, change X to Y"]
2. [Specific edit]

### Human Review Needed
- [Any decisions that require human judgment: "Confirm the budget breakdown is accurate", "Verify this testimonial has permission for use", etc.]

---

[Repeat for each foundation]

## Cross-Proposal Issues
[Any issues that affect multiple proposals — e.g., "All proposals reference 100K+ users but IMPACT_DATA.md hasn't been updated since Q3"]

## Recommended Submission Order
1. [Foundation] — Deadline [DATE], Status: Ready
2. [Foundation] — Deadline [DATE], Status: Needs minor edits
3. [etc.]
```

### Step 3: Add Any Blocking Issues to HUMAN_TODO.md
If any proposal has CRITICAL issues that prevent submission, add to HUMAN_TODO.md with:
- Which project and foundation
- What the issue is
- What the human needs to do to resolve it
- How urgent it is (include deadline if relevant)

### Step 4: Mark Project as Complete
If all proposals are READY FOR SUBMISSION or NEEDS MINOR EDITS:

Create a file called `READY_FOR_SUBMISSION.md` in the project subfolder:

```
# [Project Name] — Ready for Submission

The following proposals have been drafted and reviewed. Human review and submission needed.

## Submission Queue

| Foundation | Ask Amount | Deadline | Status | Submitter |
|-----------|-----------|----------|--------|-----------|
| [Name] | $[X] | [Date] | Ready | [Assign to Alycia/Valeria] |
| [Name] | $[X] | [Date] | Minor edits needed | [Assign] |

## Before Submitting

1. Read REVIEW.md for any specific edits needed
2. Verify all [JOSH: PLEASE ANSWER] placeholders have been filled in
3. Gather universal documents (see APPLICATION_PREP.md)
4. Have Josh or Alycia do a final read of each proposal
5. Submit via the method specified in APPLICATION_PREP.md
6. Log submission in PAST_GRANTS.md (move to "Applied" section)

## After Submitting

1. Note submission date
2. Set calendar reminder for expected response timeline
3. Note any follow-up actions (thank you email, check-in call, etc.)
```

## Quality Standards

- Reviews must be specific and actionable, not vague ("needs improvement" is not helpful; "paragraph 3 claims 120K users but IMPACT_DATA.md says 100K+" is helpful)
- Critical issues must be flagged in HUMAN_TODO.md, not just in REVIEW.md
- The submission queue must be prioritized by deadline
- Security issues are always CRITICAL, never MINOR

# FINAL WORK:


When you give completed these instructions, please ensure that you use PANDOC to make a docx copy version of every .md document, to make it easier to read the output of your work on Google Drive.
