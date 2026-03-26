# Stage 05: Review

> **Your job:** Critically review each proposal. Produce a review summary telling human reviewers exactly what needs attention.

---

## Before You Start

1. Read everything: CONTEXT files, project brief, and each foundation's full dossier (00-07)
2. **Check `CONTEXT/PROSPECTIVE_PARTNERS.md`** for any status updates on foundations
3. **Inventory existing organizational documents** before writing any "missing document" flags. In particular, confirm you have read: `CONTEXT/STATEMENT_OF_FAITH.md`, `CONTEXT/OUR_ORGANIZATION.md`, `CONTEXT/501C3_SUMMARY.md`, `CONTEXT/PARTNERSHIPS.md`. If a foundation requires a document that already exists in CONTEXT/, note "exists — needs [printing/signing/formatting]" rather than "not prepared."

## What to Do

For each foundation's proposal set, evaluate against these checks:

### The "Sales Letter" Check (Proposals)
- [ ] Does it lead with the problem, not with who we are?
- [ ] Would a first-time reader care about this problem after the first paragraph?
- [ ] Is there a clear "so what?" — why should THIS foundation invest in THIS?
- [ ] Is the core compelling idea clear and memorable?

### The "Invitation" Check (Cover Letters)

Cover letters are NOT proposal summaries or pitches. They are personal invitations to partnership in shared mission. Review against `CONTEXT/STYLE_GUIDE.md` Cover Letter Structure, Anti-Patterns, and Final Filter.

- [ ] Does the cover letter open with sender identification? ("My name is [Name], and I serve with Waha...")
- [ ] Is the salutation formally respectful? (Mr./Ms./Dr., not first names on first contact)
- [ ] Does it read as one continuous narrative, or as stacked independent blocks?
- [ ] Is there exactly one well-placed story that illustrates need or impact?
- [ ] Are stats used sparingly (once max per letter)?
- [ ] Is the ask stated at most once? (Or omitted for relationship-building letters with known eligibility blockers?)
- [ ] Is the tone an invitation to partnership, not a transactional pitch?
- [ ] Is partner/grant name-dropping contextual (creating familiarity) rather than boastful or data-wielding?
- [ ] Is faith language natural and humble, not preachy or performative?
- [ ] Is the URL (waha.app) only in the signature, not the body?
- [ ] Does it pass the Final Filter:
  - Feels like a conversation, not a grant summary?
  - Each paragraph leads naturally to the next?
  - Story is strategically placed?
  - Shared-funder connections are contextual and relational?
  - First-time reader would feel respected, invited, and clear on the ask?
- [ ] **Bottom line:** If it reads like a grant summary or trophy case → flag for rewrite. If it reads like a guided invitation into mission → it's ready.

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
- [ ] Statement of Faith / doctrinal statement content exists at `CONTEXT/STATEMENT_OF_FAITH.md` — do NOT flag as "not prepared." If a foundation requires a signed copy, note "needs printing and signing" (not "needs to be written").
- [ ] Lausanne Covenant alignment is documented in `CONTEXT/STATEMENT_OF_FAITH.md` and `CONTEXT/GOVERNANCE_POLICY_GUIDE.md` — check before flagging as unresolved.
- [ ] Before flagging ANY organizational document as missing, check the `CONTEXT/` directory first. Key files: `OUR_ORGANIZATION.md`, `501C3_SUMMARY.md`, `FINANCIALS_SUMMARY.md`, `STATEMENT_OF_FAITH.md`, `PARTNERSHIPS.md`, `IMPACT_DATA.md`, `STYLE_GUIDE.md`.

### Contact Information Verification Check
- [ ] Every person named in the cover letter and proposal can be traced to a cited source (990, website, LinkedIn). If not, flag as `[UNVERIFIED CONTACT]`.
- [ ] Every email address and phone number has a cited source. Third-party aggregators (Grantsmanship Center, Cause IQ, RocketReach) count as *cited* but NOT *verified* — mark these: "cited from [Source], not independently verified."
- [ ] **"Cited" ≠ "Verified."** Aggregator databases package 990 data that may be years old. A phone number that appears on The Grantsmanship Center may be a defunct trust company line. Before any submission, someone must confirm the contact method actually works (call, email, or check the foundation's current website).
- [ ] If contact info cannot be sourced, the proposal must use a generic addressee ("Dear Grant Review Committee") rather than an invented name.

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
| Foundation | Ask | Deadline | Key Contact | Website | Alignment | Grant Cycle | Status | Submitter | Notes |
|---|---|---|---|---|---|---|---|---|---|
| [Name] | $X | [Date] | [Name (Role) · contact] | [URL] | [One-line fit summary] | [Rolling/Annual/etc.] | [Ready] | [Assign] | [⚠️ Once/year if applicable] |

### Column Guide
- **Key Contact:** Primary contact with best available contact method (email > phone > LinkedIn > other). Format: `Name (Role) · email@example.com`
- **Website:** Foundation URL
- **Alignment:** One-line summary of WHY the fit works (not what the foundation is)
- **Grant Cycle:** Rolling vs. deadline, frequency. Prefix with `⚠️ Once/year` if rejection means waiting 12 months.

## Before Submitting
1. Read `07-REVIEW-NOTES - [Foundation Name] - [Project Name].md` for each foundation
2. Fill in any [ALYCIA: PLEASE ANSWER] placeholders
3. Gather universal documents
4. Final human read of each proposal
5. Submit via method in `04-APPLICATION-REQUIREMENTS - [Foundation Name] - [Project Name].md`
```

Add any CRITICAL issues to HUMAN_TODO.md.

### Generate Pipeline Triage Spreadsheet

After creating the markdown review summary, also generate `grant_pipeline_triage.xlsx` in the project's `05-review/{project}/` folder using `openpyxl`. This spreadsheet is the primary artifact Vince uses for triage decisions — it must be complete and well-formatted.

**Columns (in order):**

| # | Header | Width | Content |
|---|--------|-------|---------|
| 1 | Foundation | 28 | Foundation name |
| 2 | Your Decision | 16 | **Leave blank** — this is for Vince to fill in |
| 3 | Projects | 13 | Which project(s) this foundation could fund |
| 4 | Total Ask | 18 | Dollar amount or range (e.g., "$10,000" or "$5K–$10K") |
| 5 | Nearest Deadline | 13 | Date (e.g., "Apr 30, 2026") or "Rolling" |
| 6 | Status | 22 | Review status: Ready, Minor Edits, Major Revision, Not Recommended, Invite Only, N/A (cycle closed). Append "(blocked)" if a key blocker exists |
| 7 | Key Blocker | 38 | What's preventing submission, or "None — ready to go" |
| 8 | Contact Person | 24 | Name and role, e.g., "Joy Cline (ED)" |
| 9 | Contact Info | 40 | Best contact method(s): email · phone · website, separated by " · " |
| 10 | Warm/Cold | 12 | "WARM", "Cold", or "UNKNOWN" — based on CRM and prior contact data |

**Sort order:** Nearest deadline ascending (dated deadlines first, then "Rolling", then "No published deadline", then "Invite-only").

**Formatting spec:**

1. **Header row:** Bold white text (`FFFFFFFF`) on dark background (`FF1B1B1B`). Centered, wrap text, top-aligned. 10pt font.

2. **Data rows:** 10pt font, top-aligned, wrap text, thin top border on every row.

3. **Row color coding** — apply fill to entire row based on status:
   - `FFE8F5E9` (light green): Warm relationship exists (Warm/Cold = "WARM")
   - `FFE3F2FD` (light blue): Ready or near-ready with no hard blockers
   - No fill (transparent): Standard — minor edits, cold, no special status
   - `FFFFF3E0` (light orange): Blocked — has a key blocker that prevents submission
   - `FFFFEBEE` (light red): Not Recommended or Invite Only with no connection path

4. **Nearest Deadline column:** Bold red font (`FFE42535`) for all data rows.

5. **Auto-filter** enabled on the full data range.

**Python generation pattern:**

```python
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Foundation Triage"

# Define styles
header_font = Font(bold=True, size=10, color="FFFFFF")
header_fill = PatternFill(start_color="1B1B1B", end_color="1B1B1B", fill_type="solid")
header_align = Alignment(horizontal="center", vertical="top", wrap_text=True)
data_align = Alignment(vertical="top", wrap_text=True)
thin_border = Border(top=Side(style="thin"))
deadline_font = Font(bold=True, size=10, color="E42535")
data_font = Font(size=10)

# Row fills
GREEN = PatternFill(start_color="E8F5E9", end_color="E8F5E9", fill_type="solid")   # warm
BLUE = PatternFill(start_color="E3F2FD", end_color="E3F2FD", fill_type="solid")    # ready
ORANGE = PatternFill(start_color="FFF3E0", end_color="FFF3E0", fill_type="solid")  # blocked
RED = PatternFill(start_color="FFEBEE", end_color="FFEBEE", fill_type="solid")     # not recommended
NO_FILL = PatternFill(fill_type=None)                                               # standard

# Column widths
widths = [28, 16, 13, 18, 13, 22, 38, 24, 40, 12]

# ... populate headers, data rows, apply styles, enable auto_filter ...
# ws.auto_filter.ref = ws.dimensions
# wb.save("grant_pipeline_triage.xlsx")
```

**Row color logic:**
- If Warm/Cold == "WARM" → green
- If Status contains "Not Recommended" or (Status contains "Invite Only" and no warm connection) → red
- If Key Blocker indicates a hard blocker (not "None") and Status contains "blocked" → orange
- If Status contains "Ready" or is "Minor Edits" with no blocker → blue
- Otherwise → no fill

### Final Step: Update Prospective Partners Registry
Update `CONTEXT/PROSPECTIVE_PARTNERS.md`:
1. Update each foundation's status to reflect review findings
2. Note any issues that need to be resolved before submission

Move approved foundations to `06-to-be-submitted/` after Vince reviews and approves. See `06-to-be-submitted/INSTRUCTIONS.md` for the enrichment and CRM sync workflow that happens before submission.

**Moving foundations to Stage 06:**
- Only foundations with numbered prefixes (`01-`, `02-`, etc.) are eligible
- Strip the numeric prefix when moving: `05-review/{project}/{03-foundation}/` → `06-to-be-submitted/{foundation}--{project}/`
- Foundations with status prefixes (`H-`, `R-`, `IO-`, `S-`, `NA-`) stay in Stage 05 until their blocker is resolved
