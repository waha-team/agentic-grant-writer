# Stage 01: Prospect Research

> **Your job:** Find 15–40 potential foundations for every project. Include initial 990 screening.

---

## Before You Start

1. Read `CONTEXT/OUR_ORGANIZATION.md`
2. Read `CONTEXT/SEARCH_CRITERIA.md` — especially the ask-sizing rules
3. Read `CONTEXT/FUNDER_ALIGNMENT_GUIDE.md` — understand Waha's mission and how to evaluate foundation alignment
4. Read `CONTEXT/PAST_GRANTS.md` — avoid duplicating known relationships
5. Read `CONTEXT/PARTNERSHIPS.md` — look for foundations that fund our partners
6. Read each project's `PROJECT_BRIEF.md`
7. **CRITICAL: Read `CONTEXT/PROSPECTIVE_PARTNERS.md`** — check if foundations have already been researched before adding them to your prospect list

## What to Do

For each project subfolder in this directory:

### Step 1: Understand the Project
Read PROJECT_BRIEF.md. Identify: funding type, geographic focus, budget range, relevant funder types.

### Step 2: Search for Prospects

**Primary searches (do all):**
- "[project geography] Christian foundation grants"
- "Bible translation grants foundation"
- "disciple making movement funding"
- "missions technology grants"
- "unreached people groups foundation funding"
- "[specific language/people group] ministry funding"
- "Christian ministry grants international"

**Partner-based searches (HIGH VALUE):**
- Search ProPublica 990 full-text for organizations that have granted to Waha's partners: "YWAM", "Pioneers", "Frontiers", "Biblica", "Youth With A Mission", "Faith Comes By Hearing", "Jesus Film Project", "Wycliffe" 
- If a foundation funds our partners, they may fund us

**Database searches:**
- ProPublica Nonprofit Explorer — search for foundations by keyword and review their 990-PF grantee lists
- Candid / Foundation Directory Online (if accessible)

 

### Step 3: Initial 990 Screening (DO THIS FOR EVERY PROSPECT)

For each foundation found, before adding to the list:

1. **Look up their 990-PF on ProPublica** (search by foundation name or EIN)
2. **Check their grantee list** — have they funded anything remotely similar?
3. **Note their typical grant range** — what's the median? min? max?
4. **Note grants to new vs. repeat grantees** — do first-time grants skew smaller?
5. **Check if they're active** — have they made grants in the last 2 years?
6. **Note board members/officers** — names from the 990 will be used in Stage 02

If you can't find a 990 (some are too small or too new), note "990 not found" and proceed.


### Step 4: Document Each Prospect

Create `PROSPECTS.md` in the project subfolder:

```
# Prospects for [Project Name]

*Generated: [DATE]*
*Prospects found: [NUMBER]*

---

## Tier 1: Strong Alignment

### [Foundation Name]
- **Website:** [URL]
- **EIN:** [if found]
- **Mission:** [1-2 sentences IN THEIR WORDS — copy their exact language]
- **990 Grant Data:** Median grant: $[X]. Range: $[min]–$[max]. Grants/year: [N]. Active: [Y/N]
- **First-time grantee pattern:** [if discernible — do new grantees get smaller amounts?]
- **Grant cycle:** [annual/rolling/invitation-only]
- **Application:** [open/LOI/invitation]
- **Key people from 990:** [Board members, officers — names and titles]
- **Why they fit:** [2-3 sentences connecting THEIR stated priorities to THIS project]
- **Suggested first ask:** $[X] — based on their 990 patterns
- **Red flags:** [any concerns]

## Tier 2: Moderate Alignment
[Same format]

## Tier 3: Worth Watching
[Same format]
```

### Step 5: Filter Already-Researched Foundations
Before finalizing the prospect list, cross-reference with `CONTEXT/PROSPECTIVE_PARTNERS.md`:

1. **Foundations already in PROSPECTIVE_PARTNERS.md** should be:
   - Listed in a separate section of PROSPECTS.md called "## Previously Researched Foundations"
   - NOT included in the Tier 1/2/3 sections
   - NOT passed to Stage 02 (their dossiers already exist)
   - Noted with reference to their existing research folder

2. **Example entry in PROSPECTS.md:**
   ```
   ## Previously Researched Foundations
   
   The following foundations from this prospect list have already been researched for other Waha projects. Their dossiers exist and should be referenced rather than re-researched.
   
   | Foundation | Status | Existing Research | Applies To |
   |------------|--------|-------------------|------------|
   | Crowell Trust | H | `02-deep-research/malagasy-dbs/H-crowell-trust/` | Spain's secular population = unreached |
   | Maclellan Foundation | IO | `02-deep-research/malagasy-dbs/IO-maclellan-foundation/` | Great Commission alignment |
   
   **Action:** When drafting proposals for this project, reference existing dossiers rather than creating new ones.
   ```

3. **Only NEW foundations** (not in PROSPECTIVE_PARTNERS.md) should proceed to Stage 02 for deep research.

### Step 6: Update Prospective Partners Registry
After creating PROSPECTS.md, update `CONTEXT/PROSPECTIVE_PARTNERS.md`:
1. Add each new foundation to the registry with: EIN, website, location, status, project name, mission summary, and key notes
2. For foundations already in the registry, update their status and add the new project
3. Do NOT duplicate entries — if a foundation is already listed, note that research exists and reference it

### Step 6: Move Forward
After creating PROSPECTS.md and updating PROSPECTIVE_PARTNERS.md, move the project subfolder to `02-deep-research/`.

## Decision Points

Default to momentum. Flag these in HUMAN_TODO.md:

- Fewer than 8 prospects → "Need to broaden search or adjust project scope"
- Project brief too vague → "Needs more detail. Specifically: [what's missing]"
- Project type rarely funded → "Consider reframing. Suggested angles: [X]"

## Quality Standards

- Minimum 15 prospects, aim for 25+
- Every prospect must have a working website URL
- Every prospect must have 990 data reviewed (or noted as unavailable)
- Foundation's mission must be captured in THEIR exact words
- Don't include foundations that explicitly exclude religious organizations
