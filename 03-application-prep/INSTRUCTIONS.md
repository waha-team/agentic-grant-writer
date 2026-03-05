# Stage 03: Application Prep

> **Your job:** For each foundation, gather actual application requirements and produce a checklist.

---

## Before You Start

1. Read `CONTEXT/OUR_ORGANIZATION.md` and `CONTEXT/FINANCIALS_SUMMARY.md`
2. Read the project's `PROJECT_BRIEF.md` and `SHORTLIST.md`
3. Read each foundation's dossier (00-BRIEFING through 03-VOCABULARY-AND-FRAMING)
4. **Check `CONTEXT/PROSPECTIVE_PARTNERS.md`** for any updates on foundation status

## What to Do

For each project subfolder in this directory:

### Step 1: Gather Application Requirements
For **ALL foundations in "Ready to Draft", "Relationship Needed", AND "Human Action Needed" categories** on the SHORTLIST:

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

Add `04-APPLICATION-REQUIREMENTS - [Foundation Name] - [Project Name].md` to each foundation's subfolder:

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
- [ ] 501(c)(3) Determination Letter — **IN CONTEXT/501(c)(3) Letter.pdf**
- [ ] Most Recent IRS Form 990 — **NOT YET FILED** (new nonprofit; see UNIVERSAL_DOCS_NEEDED.md for handling)
- [ ] Board of Directors List — **IN CONTEXT/BOARD_OF_DIRECTORS.md**
- [ ] Financial Statements — **IN CONTEXT/FINANCIALS_SUMMARY.md**
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
Create or update `UNIVERSAL_DOCS_NEEDED.md` at the root folder level:

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

Also add any missing universal documents to `HUMAN_TODO.md`.

### Step 4: Update Prospective Partners Registry
Update `CONTEXT/PROSPECTIVE_PARTNERS.md`:
1. Update status for each foundation if new information was discovered
2. Add any new requirements or blockers discovered during application research

### Step 5: Move Forward

After creating `04-APPLICATION-REQUIREMENTS - [Foundation Name] - [Project Name].md` for all foundations, move the project to `04-proposal-drafts/`.

## Decision Points

Flag in HUMAN_TODO.md:
- Foundation requires something Waha doesn't have → suggest workaround or skip
- Deadline < 14 days → "URGENT DEADLINE"
- Letters of support required → "Josh: identify who could write this for [foundation]"

### NOTE:

You have READ access to our CRM, which is kept up to date with Waha's relationships to other people and organizations.

Before you send something onto a Human, do due diligence, and check to see if there's anything about that organization in our CRM. Also, check the CRM for any other situation in which that will be helpful.

To access the CRM, use the Agentic Skill available to you in the `[grants root]/skills` directory, that will allow you READ access to our CRM, Attio. The env variable is avialble in `[grants root]/.env`. 

