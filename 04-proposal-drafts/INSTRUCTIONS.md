# Stage 04: Proposal Drafts

> **Your job:** Write complete, tailored proposals for each foundation. Every proposal must use THEIR vocabulary, address THEIR people by name, be sized to THEIR giving patterns, and lead with THE PROBLEM.

---

## Before You Start

1. Read `CONTEXT/STYLE_GUIDE.md` — **READ THIS CAREFULLY, especially the "Sales Letter" section**
2. Read `CONTEXT/FUNDER_ALIGNMENT_GUIDE.md` — especially the "How to Describe Waha to a Funder" quick-reference table for funder-type-specific framing
3. Read `CONTEXT/OUR_ORGANIZATION.md`, `CONTEXT/IMPACT_DATA.md`, `CONTEXT/PARTNERSHIPS.md`
4. For EACH foundation, read its entire dossier (documents 00 through 04)
5. **Check `CONTEXT/PROSPECTIVE_PARTNERS.md`** for any status updates on foundations

## Critical Rules

**RULE 1: USE THEIR LANGUAGE.** Read `03-VOCABULARY-AND-FRAMING - [Foundation Name] - [Project Name].md` for each foundation. Use their vocabulary column, not ours. If they say "Scripture engagement," you say "Scripture engagement." If they say "capacity building," you say "capacity building." Never force our jargon onto their priorities.

**RULE 1a: DEFINE ALL ACRONYMS.** Never use an acronym on first reference without spelling it out. Grant reviewers may not know what DBS, DMC, or DMM mean. First use: "Discovery Bible Study (DBS)"; subsequent uses: "DBS". See `CONTEXT/STYLE_GUIDE.md` for the acronym reference table.

**RULE 2: LEAD WITH THE PROBLEM.** Especially for foundations that don't know us. The first thing they read should make them care about the problem. Waha is the answer, not the opening.

**RULE 3: PERSONALIZE EVERYTHING.** Use names from `02-KEY-PEOPLE - [Foundation Name] - [Project Name].md` in salutations. Reference specific grants they've made (from `01-990-ANALYSIS - [Foundation Name] - [Project Name].md`). Mention shared networks or partners.

**RULE 4: SIZE THE ASK TO THEIR PATTERNS.** Use the recommended ask from `01-990-ANALYSIS - [Foundation Name] - [Project Name].md`, not our total project budget. If the project costs $25K and their median first-time grant is $3K, ask for $3K toward a specific component.

## What to Do

For each project subfolder in this directory:

### Step 1: Prioritize
Start with: nearest deadlines → highest alignment → simplest applications.

### Step 2: Write Each Proposal
Add these files to each foundation's subfolder:

#### `05-PROPOSAL-DRAFT - [Foundation Name] - [Project Name].md`

Structure per foundation's requirements (from `04-APPLICATION-REQUIREMENTS - [Foundation Name] - [Project Name].md`). If they don't specify, use this structure:

**1. Executive Summary** (1 paragraph)
The problem. Who we are (1 sentence). What we're asking for. Why it matters. Written in THEIR vocabulary.

**2. Statement of Need / The Problem** (1-2 paragraphs)
THIS IS THE MOST IMPORTANT SECTION. Remember: this is a sales letter. Make them feel the urgency.
- Open with a vivid story or striking data point
- Name the problem in THEIR language (from 03-VOCABULARY-AND-FRAMING.md)
- Use specific numbers: 7,000 unreached people groups, [X] million speakers of [language], etc.
- Show what happens if nothing changes
- Connect to THEIR stated priorities: "As [Foundation Name] recognizes in your commitment to [their stated priority]..."

**3. Our Solution** (2-3 paragraphs)
- What Waha does — described using THEIR vocabulary
- Why it works — evidence from IMPACT_DATA.md
- What specifically this grant funds — concrete activities from PROJECT_BRIEF.md
- Name-drop 2-3 relevant partners from PARTNERSHIPS.md

**4. Evidence of Impact** (1-2 paragraphs)
- Specific results: "30 groups multiplied to 90 in 50 days"
- Reference similar organizations they've funded (from 990 analysis): "Like [grantee they've funded], Waha..."
- At least one testimonial from IMPACT_DATA.md / `IMPACT_DATA/*`  (send out a sub-agent to research, if needed)

**5. Budget** (table + narrative)

- Sized to the specific ask amount (from 01-990-ANALYSIS.md recommendation)
- If asking for partial project funding, clearly show which component this covers
- Brief justification for each line item

**6. Organizational Capacity** (1-2 paragraphs)
- Why Waha is the right team
- Reference partnerships and ecosystem
- Mention Meta Language Technology Partner status if relevant

**7. Evaluation & Reporting** (1 paragraph)
- What we'll measure (tied to THEIR stated outcomes)
- How we'll report back

**8. Sustainability** (1 paragraph)
- How work continues after grant. For localization: permanent resource at zero marginal cost.

#### `06-COVER-LETTER - [Foundation Name] - [Project Name].md`

Personalized cover letter:

- **Addressed to specific people** from 02-KEY-PEOPLE.md
- Use format: "Dear [Name], [Name], and the [Foundation] grant review team,"
- NEVER "Dear Grant Administrator" if you have names
- 3-4 paragraphs max
- Reference any warm connection or shared network
- Reference a specific grant they've made that relates
- Clear ask with specific dollar amount
- Express genuine alignment with THEIR mission (in THEIR words)

#### `07-LOI-DRAFT - [Foundation Name] - [Project Name].md` (if foundation requires Letter of Inquiry first)

**IMPORTANT: Always produce BOTH the LOI and the full proposal in the same pass.** Don't stop at the LOI. The LOI gets sent first; the full proposal is pre-written and ready to submit immediately when the invitation comes back. This eliminates delays.

LOI format (1-2 pages max):
- Opening: the problem (1 paragraph, compelling)
- Who we are (2-3 sentences)
- Project summary (1 paragraph)
- Budget range (1 sentence — sized to their 990 patterns)
- Close: request for invitation to submit full proposal
- Use their vocabulary throughout

#### `APPLICATION-ANSWERS - [Foundation Name] - [Project Name].md` (if foundation has specific questions)

Answer each question from `04-APPLICATION-REQUIREMENTS - [Foundation Name] - [Project Name].md` directly. Use their vocabulary.

### Step 3: Self-Check Before Moving On

For each proposal, verify:
- [ ] Uses the foundation's own vocabulary (check against `03-VOCABULARY-AND-FRAMING - [Foundation Name] - [Project Name].md`)
- [ ] All acronyms defined on first use (DBS, DMC, DMM, etc.)
- [ ] Leads with the problem, not with who we are
- [ ] Addresses specific people by name in cover letter
- [ ] Ask amount matches `01-990-ANALYSIS - [Foundation Name] - [Project Name].md` recommendation
- [ ] References at least one specific grant they've made to a similar org
- [ ] Includes at least one story AND one data point
- [ ] Budget math adds up
- [ ] No security-sensitive details exposed
- [ ] Within word/page limits
- [ ] Name-drops 2-3 relevant partners
- [ ] **Valid markdown** — key-value blocks use lists/tables, blank lines around headers/lists/tables (see `CONTEXT/STYLE_GUIDE.md`)

### Step 4: Reorganize and Create Status Documents

After drafting all proposals, reorganize the foundation folders using this naming convention:

**Folder Naming Convention:**

| Prefix | Meaning | When to Use |
|--------|---------|-------------|
| `01-`, `02-`, etc. | Drafted and ready | Proposal written, ready for review/submission immediately |
| `R-` | Relationship needed | Open process, but warm intro strongly preferred/required before submission |
| `H-` | Human action needed | Open process, but waiting on specific info/decision from Josh |
| `CL-` | Cycle closed | Waiting for next application cycle |
| `IO-` | Invite only | No public application process; needs connection to get invited |
| `NA-` | Not applicable | Can't apply (wrong org type, geography, etc.) |
| `S-` | Suspended | Foundation paused applications |

**IMPORTANT: For folders with status prefixes (H-, NA-, IO-, CL-, R-, S-), the FIRST LINES of `00-BRIEFING - [Foundation Name] - [Project Name].md` must explain WHY the foundation has that status.** This explanation should appear before the standard briefing content, so anyone opening the file immediately understands the blocker.

**Process:**

1. **For drafted foundations:** Rename to `01-[Foundation]`, `02-[Foundation]`, etc. based on priority (deadline urgency → alignment → ask size)

2. **For relationship-needed foundations (`R-`):** Create `00-STATUS-RELATIONSHIP-NEEDED.md`:
   ```
   # Status: Relationship Needed Before Submission

   ## Why This Foundation
   [Brief summary of alignment and why worth pursuing]

   ## Application Status
   - **Process:** [Open LOI / Open application]
   - **Deadline:** [Date or "Rolling"]
   - **Blocker:** [Why relationship needed before submitting]

   ## Connection Paths (check CRM first)
   - [ ] [Partner name] — [relationship to foundation]
   - [ ] [Network/person] — [potential connection]

   ## Recommended Approach
   1. [Specific step to pursue connection]
   2. [Next step after connection made]
   3. Submit LOI/proposal

    ## Proposal Status
    Drafted and ready. (See `05-PROPOSAL-DRAFT - [Foundation Name] - [Project Name].md` and `06-COVER-LETTER - [Foundation Name] - [Project Name].md`)

   ## Deadline Pressure
   [Urgency level]
   ```

   **Always write the proposal for R- foundations.** The relationship blocker is about *when* to submit, not *whether* to prepare. A proposal ready to send the moment the door opens is far more valuable than a placeholder. Write it now; send it when the introduction is secured.

3. **For foundations needing human action (`H-`):** Create `00-STATUS-ACTION-NEEDED.md`:
   ```
   # Status: Human Action Needed

   ## Why This Foundation
   [Brief summary of why this is a good fit]

   ## What's Blocking Submission
   [Specific action needed from Josh/Alycia]

   ## What Happens Next
   [What will be done once blocker is resolved]

   ## Deadline Pressure
   [Urgency level and deadline if applicable]
   ```

   **Always write the proposal for H- foundations.** The human action is a prerequisite to *submitting*, not to *preparing*. The proposal should be complete and waiting.

4. **For cycle-closed foundations (`CL-`):** Create `00-STATUS-CYCLE-CLOSED.md`:
   ```
   # Status: Cycle Closed
   
   ## Next Cycle
   [When applications reopen]
   
   ## Action to Take Now
   [e.g., "Submit inquiry form to be in queue"]
   
   ## Calendar Reminder
   [When to follow up]
   ```

5. **For invite-only foundations (`IO-`):** Create `00-STATUS-INVITE-ONLY.md`:
   ```
   # Status: Invite Only
   
   ## Why Pursue This Foundation
   [Alignment, grant size, strategic value]
   
   ## Connection Paths (check CRM first)
   - [ ] [Partner name] — [relationship to foundation]
   - [ ] [Network name] — [why this might connect]
   
   ## Recommended Approach
   [Specific steps to pursue connection]
   ```

6. **For not-applicable foundations (`NA-`):** Create `00-STATUS-NOT-APPLICABLE.md`:
   ```
   # Status: Not Applicable
   
   ## Why We Can't Apply
   [Specific reason: wrong org type, geography, etc.]
   
   ## Alternative Approach
   [If any exists, e.g., "Partner with local church as grantee"]
   
   ## Keep or Archive?
   [Keep for reference / Archive and remove from pipeline]
   ```

### Step 5: Update Prospective Partners Registry
Update `CONTEXT/PROSPECTIVE_PARTNERS.md`:
1. Update each foundation's status based on folder naming convention (01-, R-, H-, IO-, etc.)
2. Add notes on proposal status (drafted, ready to submit, blocked, etc.)
3. Add any new foundations that were researched but not in the original prospect list

### Step 6: Move Forward

After reorganizing and creating status documents, move project to `05-review/` for Alycia to review.

## Decision Points

Flag in HUMAN_TODO.md but keep moving:
- Can't answer a specific question from context → Put "[JOSH: PLEASE ANSWER — (question)]" inline
- Foundation requires very different framing (e.g., secular) → Note prominently at top of proposal
- Budget doesn't fit their range even with adjustment → Note mismatch, suggest solution


### NOTE:

You have READ access to our CRM, which is kept up to date with Waha's relationships to other people and organizations.

Before you send something onto a Human, do due diligence, and check to see if there's anything about that organization in our CRM. Also, check the CRM for any other situation in which that will be helpful.

To access the CRM, use the Agentic Skill available to you in the `[grants root]/skills` directory, that will allow you READ access to our CRM, Attio. The env variable is avialble in `[grants root]/.env`. 


