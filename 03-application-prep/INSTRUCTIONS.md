# Stage 03: Application Prep

> **Your job:** For each shortlisted foundation, gather actual application requirements and produce a checklist.

---

## Before You Start

1. Read `CONTEXT/OUR_ORGANIZATION.md` and `CONTEXT/FINANCIALS_SUMMARY.md`
2. Read the project's `PROJECT_BRIEF.md` and `SHORTLIST.md`
3. Read each foundation's dossier (00-BRIEFING through 03-VOCABULARY-AND-FRAMING)

## What to Do

For each project subfolder in this directory:

### Step 1: Gather Application Requirements
For each "Apply Now" foundation on the SHORTLIST:

1. Visit their grant application page
2. Document EVERY requirement:
   - Application format (online, PDF, email, mailed)
   - Required sections and word/page limits
   - Required attachments (990, board list, financials, letters of support)
   - Deadlines
   - LOI requirements (if LOI comes before full application)
   - Specific questions they ask (VERBATIM)
   - Reporting requirements after award

### Step 2: Create Application Requirements Document
Add `04-APPLICATION-REQUIREMENTS.md` to each foundation's subfolder:

```
# Application Requirements: [Foundation Name]

*Researched: [DATE]*

## Application Details
- **Type:** [online form / PDF / email / LOI first]
- **Deadline:** [DATE or "rolling"]
- **URL:** [direct link]
- **Submission method:** [online portal / email to X / mail to Y]

## Requirements Checklist

### Narrative Components
- [ ] Executive Summary — [word limit if specified] — Status: TO WRITE (Stage 04)
- [ ] Statement of Need — [word limit] — TO WRITE
- [ ] Project Description — [word limit] — TO WRITE
- [ ] Budget — [their format if specified] — TO CREATE
- [ ] Org Overview — [word limit] — ADAPT from OUR_ORGANIZATION.md
- [ ] Evaluation Plan — TO WRITE

### Required Attachments
- [ ] 501(c)(3) Determination Letter — JOSH TO PROVIDE
- [ ] Most Recent IRS Form 990 — JOSH TO PROVIDE
- [ ] Board of Directors List — JOSH TO PROVIDE
- [ ] Financial Statements — JOSH TO PROVIDE
- [ ] Letters of Support — [NEEDED / NOT REQUIRED]
- [ ] [Any other requirements]

### Foundation-Specific Questions (VERBATIM)
1. [Exact question from application]
2. [Exact question]
3. [etc.]

## Grant Ask Amount
$[X] — per 01-990-ANALYSIS.md recommendation

## Key Framing
[From 03-VOCABULARY-AND-FRAMING.md — brief reminder of how to position for this funder]
```

### Step 3: Universal Documents Checklist
Create or update `UNIVERSAL_DOCS_NEEDED.md` at the project folder level:

```
## Universal Documents (provide once, use across all applications)
- [ ] 501(c)(3) determination letter (PDF)
- [ ] Most recent IRS Form 990 (EIN: 35-2894107)
- [ ] Board of directors list with affiliations
- [ ] Current year organizational budget
- [ ] Most recent financial statements
- [ ] Key staff bios
- [ ] Organizational chart (if available)
```

Add any missing universal documents to `HUMAN_TODO.md`.

### Step 4: Move Forward
After creating 04-APPLICATION-REQUIREMENTS.md for all foundations, move project to `04-proposal-drafts/`.

## Decision Points

Flag in HUMAN_TODO.md:
- Foundation requires something Waha doesn't have → suggest workaround or skip
- Deadline < 14 days → "URGENT DEADLINE"
- Letters of support required → "Josh: identify who could write this for [foundation]"
