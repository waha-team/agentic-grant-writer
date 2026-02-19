# Stage 04: Application Prep

> **Your job:** For each shortlisted foundation, gather the actual application requirements and produce a checklist of what needs to be prepared.

---

## Before You Start

1. Read `CONTEXT/OUR_ORGANIZATION.md`
2. Read `CONTEXT/IMPACT_DATA.md`
3. Read the `PROJECT_BRIEF.md`, `ALIGNMENT_ANALYSIS.md`, and `CONTACTS.md` inside each project subfolder

## What to Do

For each project subfolder found in this directory:

### Step 1: Gather Application Requirements
For each "Recommended" foundation (those with DIRECT APPLICATION or COLD OUTREACH strategy):

1. **Visit the foundation's grant application page**
2. **Document every requirement:**
   - Application format (online form, PDF, email, mailed packet)
   - Required sections (narrative, budget, timeline, etc.)
   - Word/page limits for each section
   - Required attachments (990, board list, financial statements, letters of support, etc.)
   - Deadline(s)
   - LOI requirements (if LOI comes before full application)
   - Any specific questions they ask
   - Reporting requirements after award

3. **If no application page exists** (some smaller foundations):
   - Note that a letter of inquiry is likely the best approach
   - Check if their 990 shows a consistent grant-making pattern
   - Recommend a standard LOI format

### Step 2: Gap Analysis
For each foundation, assess what Waha already has vs. what needs to be created:

**Likely already available:**
- Mission statement and organizational description (from CONTEXT/OUR_ORGANIZATION.md)
- Impact data and testimonials (from CONTEXT/IMPACT_DATA.md)
- Project description (from PROJECT_BRIEF.md)
- Basic budget (from PROJECT_BRIEF.md)

**Likely needs to be created or gathered:**
- Foundation-specific narrative (tailored to their priorities)
- Detailed budget in their required format
- Board list with affiliations
- Most recent 990 (Josh needs to provide)
- Audited financial statements (Josh needs to provide)
- Letters of support (if required — flag for human action)
- Specific metrics/evaluation plan aligned to their reporting requirements

### Step 3: Output
Create a file called `APPLICATION_PREP.md` inside the project's subfolder:

```
# Application Prep for [Project Name]

*Generated: [DATE]*

---

## [Foundation Name]

**Application type:** [online form / PDF / email / LOI first]
**Deadline:** [DATE or "rolling"]
**URL for application:** [direct link to application page]

### Requirements Checklist

- [ ] **Narrative / Project Description** — [word limit if specified]. Status: TO WRITE (Stage 05)
- [ ] **Budget** — [their format if specified]. Status: TO CREATE from PROJECT_BRIEF.md
- [ ] **Organizational Overview** — [word limit]. Status: ADAPT from OUR_ORGANIZATION.md
- [ ] **501(c)(3) Determination Letter** — Status: JOSH TO PROVIDE
- [ ] **Most Recent 990** — Status: JOSH TO PROVIDE
- [ ] **Board List** — Status: JOSH TO PROVIDE
- [ ] **Financial Statements** — Status: JOSH TO PROVIDE
- [ ] **Letters of Support** — Status: [NEEDED / NOT REQUIRED]
- [ ] [Any other foundation-specific requirements]

### Foundation-Specific Questions
[List any specific questions from the application, verbatim if possible]

1. [Question 1]
2. [Question 2]
3. [etc.]

### Recommended Framing
[From ALIGNMENT_ANALYSIS.md — how to position Waha for this funder]

### Grant Ask Amount
$[X] — [justification for this amount based on their typical range and our budget]

---

[Repeat for each foundation]
```

### Step 4: Identify Universal Documents Needed
Create or update a section at the top of APPLICATION_PREP.md listing documents that Josh/Alycia need to provide once (usable across all applications):

```
## Universal Documents Needed (Provide Once)

- [ ] 501(c)(3) determination letter (PDF)
- [ ] Most recent IRS Form 990
- [ ] Current board of directors list with affiliations
- [ ] Current year budget (organizational)
- [ ] Most recent audited financial statements (if available)
- [ ] Organizational chart
- [ ] Key staff bios
```

Add any missing universal documents to `HUMAN_TODO.md` with the note: "These documents are needed for multiple grant applications. Please gather and add to the project folder."

### Step 5: Move Forward
After creating APPLICATION_PREP.md, move the project subfolder to `05-proposal-drafts/`.

## Decision Points

**Default to momentum.** Keep moving unless:

- A foundation's application requires something Waha clearly doesn't have (e.g., audited financials, 3 years of 990s as the new entity) → Add to HUMAN_TODO.md: "[Foundation] requires [document]. If Waha doesn't have this yet, skip this foundation for now. Alternatively: [suggest workaround, e.g., 'submit Kingdom Strategies historical 990s with a cover note about the entity transition']."
- A deadline is less than 14 days away → Add to HUMAN_TODO.md: "URGENT DEADLINE: [Foundation] application due [DATE] for [project]. Fast-track needed."
- The application requires a letter of support from a specific type of partner → Add to HUMAN_TODO.md: "[Foundation] wants a letter of support from [type]. Josh: identify who could write this."

## Quality Standards

- Application requirements must come from the foundation's actual current website/guidelines, not cached or outdated information
- Every checklist item must have a clear status (TO WRITE, TO PROVIDE, AVAILABLE, NOT REQUIRED)
- The gap analysis must be honest — don't mark things as available if they need significant adaptation
