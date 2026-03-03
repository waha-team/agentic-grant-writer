# Stage 02: Deep Research

> **Your job:** For each foundation, build a comprehensive dossier (prioritize the shortlist, but do them all). This is the intelligence-gathering stage. Each foundation gets its own subfolder with numbered research documents.

---

## Before You Start

1. Read ALL files in `CONTEXT/`
2. Read the project's `00-PROJECT_BRIEF.md` and `01-PROSPECTS.md`

## What to Do

For each project subfolder in this directory:

### Step 1: Select Top Foundations
From 01-PROSPECTS.md, select the top 8-12 foundations to research deeply. Prioritize by:
1. Strongest mission alignment (in their own words)
2. 990 shows grants to similar organizations
3. Open application process
4. Grant size in our target range

**IMPORTANT: Check "Previously Researched Foundations" section in PROSPECTS.md first.** 
- If a foundation has existing research (dossier in another project folder), do NOT create a new dossier
- Instead, create a brief "adaptation note" explaining how the existing research applies to this project
- Only create new dossiers for foundations marked as "New" in PROSPECTS.md

### Step 2: Create Foundation Subfolders
For each selected foundation, create a subfolder inside the project folder using the **priority naming convention** defined below. Apply this convention from the start — it carries through all pipeline stages.

**Foundation Folder Naming Convention:**

| Prefix | Meaning | When to Use |
|--------|---------|-------------|
| `01-`, `02-`, etc. | Ready to proceed | Open process, no blockers. Number by priority. |
| `H-` | Human action needed | **BLOCKED**: Requires Josh/team decision BEFORE any progress can be made (e.g., intro meeting required before applying, must verify theological alignment, deadline passed) |
| `CL-` | Cycle closed | **BLOCKED**: Waiting for next application cycle to open |
| `IO-` | Invite only | **BLOCKED**: No public application process; cannot apply without invitation |
| `NA-` | Not applicable | **BLOCKED**: Can't apply (wrong org type, geography, etc.) |
| `S-` | Suspended | **BLOCKED**: Foundation paused applications |

**Key principle:** Only use a status prefix if there is a GENUINE BLOCKER that prevents forward progress. Having a warm path (R-) or needing to contact someone (H-) is NOT a blocker if the foundation has an open application process you could use directly.

**Examples:**
- `01-gospel-volunteers/` - Open process, no blockers → just number it
- `H-tyndale-house/` - Intro meeting REQUIRED before applying → genuine blocker
- `IO-maclellan-foundation/` - No public application → genuine blocker
- `S-stewardship-foundation/` - Applications suspended → genuine blocker

At Stage 02, number the open-process foundations with NO blockers in priority order (`01-`, `02-`, etc.). Only add status prefixes to foundations with genuine blockers. Foundations keep their labels through stages 02 → 03 → 04 → 05.

**IMPORTANT: For folders with status prefixes (H-, IO-, CL-, NA-, S-), the FIRST LINES of `00-BRIEFING.md` must explain the blocker.** This explanation should appear before the standard briefing template content.

---

## Citation Standard (applies to ALL documents in this stage)

Every external fact must be traceable. Use inline citations in this format, immediately after the claim:

```
([Source Name](URL))
```

**Examples:**
- `"Plowing new ground for a greater harvest." ([E91 Website](https://e91foundation.org/about))`
- `Total assets: $57.9M ([ProPublica 990, 2023](https://projects.propublica.org/nonprofits/organizations/12345678))`
- `Blair Austin, Co-President ([ProPublica 990, 2023](https://projects.propublica.org/nonprofits/...))`
- `Gave $25,000 to Biblica for the Reach4Life Project ([ProPublica 990, 2023](https://projects.propublica.org/...))`

**What must be cited:**
- Any quote from a foundation's website, FAQ, or grant guidelines
- Every grant amount in the 990 analysis
- All board member names and titles
- Founding dates, asset sizes, total grantmaking figures
- Any fact sourced from ProPublica, Candid, Cause IQ, GrantStation, LinkedIn, or news articles

**What does not need a citation:**
- Waha's own organizational information (sourced from CONTEXT/ files — those are already authoritative)
- Your own analysis, conclusions, or strategic recommendations (make clear these are your interpretation, not sourced facts)
- Information the reader can verify immediately from a URL already present in the document

**Common source name conventions:**
- `([ProPublica 990, YYYY](URL))` — for IRS 990 data via ProPublica
- `([Foundation Website](URL))` — for mission statements, FAQs, grant guidelines
- `([Foundation FAQ](URL))` — specifically for FAQ pages
- `([Cause IQ](URL))` — for Cause IQ database entries
- `([LinkedIn](URL))` — for board member profiles
- `([GrantStation](URL))` — for GrantStation database

If a URL is unavailable for a specific claim (e.g., data from a paywalled source or a page that no longer exists), write `([Source: Name — URL unavailable])` so the reader knows you have a source but it isn't linkable.

---

Inside each, create the following numbered documents:

---

#### `00-BRIEFING.md` — Foundation Overview

This is the foundation intelligence brief. Someone should be able to read just this file and understand everything about this funder.

**For status-prefixed folders (H-, NA-, IO-, CL-, R-, S-), start with the status explanation:**

```
# Briefing: [Foundation Name]

> **Status: [TAG] — [One-line reason for this status]**
> [2-3 sentences explaining WHY this foundation has this status tag]

*Research date: [DATE]*

## Identity
- **Full legal name:** [from 990]
- **EIN:** [from 990]
- **Website:** [URL]
- **Location:** [city, state]
- **Year established:** [from 990 or website]
- **Type:** [Private foundation / Community foundation / Corporate foundation / Family foundation]

## Mission & Priorities (IN THEIR OWN WORDS)
[Copy their exact mission statement from their website, with citation: "Quote." ([Foundation Website](URL))]

[Copy their stated funding priorities/program areas, verbatim, with citation]

## What They Actually Fund (from 990 analysis)
[Summarize what their 990 grantee lists reveal about their REAL priorities vs. stated priorities. Cite the specific 990 year for each grant mentioned: $X to Organization Y ([ProPublica 990, YYYY](URL))]

## History & Context
[Brief history of the foundation. Who founded it? Why? Any notable shifts in priorities? Cite sources for historical facts. ([Foundation Website](URL)) or ([ProPublica 990, YYYY](URL))]

## Why Waha Is a Fit
[2-3 paragraphs connecting their specific priorities to this specific project. Use THEIR vocabulary to describe OUR work.]

## Why They Might Say No
[Honest assessment of potential objections or misalignment]
```

---

#### `01-990-ANALYSIS.md` — Financial & Giving Pattern Analysis

This is the strategic intelligence that prevents the "$10K ask to a $3K funder" mistake.

```
# 990 Analysis: [Foundation Name]

*990s reviewed: [YYYY, YYYY] — ([ProPublica](URL_to_foundation_page))*

## Giving Overview
- **Total grants per year:** $[X] (trending: up/down/stable)
- **Number of grants per year:** [N]
- **Median grant size:** $[X]
- **Average grant size:** $[X]
- **Grant range:** $[min] – $[max]
- **Most common grant size bracket:** $[X] – $[Y]

## First-Time vs. Repeat Grantee Analysis
- **Do they give to new organizations?** [Yes/No/Sometimes]
- **Typical first-time grant amount:** $[X] (if discernible)
- **Do first-time grantees grow over time?** [Pattern if visible]
- **Core/repeat grantees:** [List any organizations that appear year after year — these are their favorites. If we know any, note for warm introductions]

## Geographic Patterns
- **Where do their grantees operate?** [Domestic only? International? Specific regions?]

## Thematic Patterns
- **What types of work do they actually fund?** [List categories with approximate % of grants]
- **Any surprising grants?** [Grants outside their stated focus — could indicate flexibility]

## Similar Organizations Funded
[List any grantees that resemble Waha in mission, size, or work type. These are proof that we fit.]

## Recommended Ask Amount
- **First-time ask:** $[X] — based on [median first-time grant / median overall / specific reasoning]
- **Future relationship ask:** $[X] — based on growth pattern with repeat grantees
- **Rationale:** [1-2 sentences explaining why this number]

## Board of Directors / Officers (from 990)
[List all names and titles from the most recent 990. These feed into 02-KEY-PEOPLE.md]
```

---

#### `02-KEY-PEOPLE.md` — Decision Maker Profiles

This is a ~2-page research brief on the humans who decide.

```
# Key People: [Foundation Name]

*Research date: [DATE]*

---

## Board of Directors (from 990)

### [Name], [Title — e.g., Chair / Trustee / Director]
- **Background:** [Brief bio — professional background, other board memberships, areas of interest. Search LinkedIn, Google, other nonprofit 990s.]
- **LinkedIn:** [URL if found]
- **Relevant connections:** [Any overlap with Waha's network? Same church? Same missions org? Same industry?]
- **Notes for engagement:** [What might resonate with this person specifically?]

### [Name], [Title]
[Same format — repeat for each board member/officer]

---

## Staff / Program Officers (from website)

### [Name], [Title — e.g., Executive Director / Program Officer / Grants Manager]
- **Email:** [if publicly available]
- **LinkedIn:** [URL]
- **Background:** [Bio]
- **Notes:** [What do they seem to care about based on their public profile?]

---

## Warm Paths
- [ ] Check if any Waha team/board members know anyone listed above
- [ ] Check for shared networks: 24:14, Missional Tech, Bible translation community
- [ ] Check if any of Waha's partners (see PARTNERSHIPS.md) are grantees of this foundation → ask partner for introduction
- **Identified connections:** [List any found, or "None found — recommend cold outreach"]

## Recommended Salutation
[Based on who is most likely reviewing grants]
Example: "Dear [Name], [Name], and the [Foundation] team,"

## Recommended Contact Strategy
[DIRECT APPLICATION / WARM INTRODUCTION / COLD OUTREACH / ATTEND EVENT / LONG-TERM CULTIVATION]

**Recommended first action:** [Specific next step]
```

---

#### `03-VOCABULARY-AND-FRAMING.md` — Language Mapping

**This is the file that makes proposals feel tailored instead of generic.** It maps the foundation's language to ours so the proposal writer (Stage 04) can write in THEIR vocabulary. It may be the most important file in the project, so spend time making sure it's great.

```
# Vocabulary & Framing: [Foundation Name]

*This file maps their language to ours. When writing the proposal for this foundation, USE THEIR COLUMN, not ours.*

## Their Mission Keywords
[List the key terms from their mission statement and funding priorities]

## Language Mapping

| They Say                  | We Say                    | Use in Proposal                                                                |
|---------------------------|---------------------------|--------------------------------------------------------------------------------|
| [their term]              | [our equivalent]          | [their term]                                                                 |
| "Scripture engagement"    | "Discovery Bible Study"   | "Scripture engagement facilitated through Discovery Bible Studies"             |
| "underserved communities" | "unreached people groups" | "underserved communities who lack access to Scripture in their heart language" |
| "capacity building"       | "mobilization / training" | "building capacity among local believers to facilitate Scripture discovery"    |
| [etc.]                    | [etc.]                    | [etc.]                                                                         |

## Their Stated Values (verbatim from website/guidelines)
1. [Value 1 — exact quote]
2. [Value 2 — exact quote]
3. [Value 3]

## How We Map to Each Value
1. [Value 1] → [How Waha demonstrates this. Be specific.]
2. [Value 2] → [How Waha demonstrates this.]
3. [Value 3] → [How Waha demonstrates this.]

## Framing Recommendations
- **Lead with:** [What aspect of Waha to emphasize for this funder]
- **Avoid:** [What language or framing to avoid with this funder]
- **Tone:** [More formal? More personal? Story-driven? Data-driven?]
- **Funder type:** [Evangelical / Catholic / Broader Christian / Secular — see OUR_ORGANIZATION.md framing guide]

## Specific Grants They've Made That Relate to Us
[From 990 analysis — list grants they've given that are similar to what we'd propose]
- [Grantee Name] — $[X] for [purpose] (Year) — Similar because: [reason]
- [Grantee Name] — $[X] for [purpose] (Year) — Similar because: [reason]

## Draft "Why We Fit" Paragraph (in their language)
[Write a 3-4 sentence paragraph explaining why Waha fits this foundation's priorities, using exclusively THEIR vocabulary. This becomes the seed for the proposal's alignment section.]
```

---

### Step 3: Update Prospective Partners Registry
After completing all foundation dossiers, update `CONTEXT/PROSPECTIVE_PARTNERS.md`:
1. Update each researched foundation's entry with: status tag, research folder path, and key notes from the dossier
2. Add any new foundations that weren't in the registry
3. Ensure the status accurately reflects the folder naming (IO-, H-, S-, NA-, etc.)

### Step 4: Produce Shortlist Summary
After completing all foundation dossiers, create `SHORTLIST.md` in the project folder:

```
# Research Shortlist for [Project Name]

*Completed: [DATE]*
*Foundations researched: [N]*

## Ready to Draft (open process, no blockers)
| Foundation | Ask Amount | Deadline | Contact Strategy | Key Contact |
|-----------|-----------|----------|-----------------|-------------|
| [Name] | $[X] | [Date] | Direct Application | [Name, Title] |

## Relationship Needed (open process, but intro preferred/required)
| Foundation | Ask Amount | Deadline | Connection Path | Why Pursue |
|-----------|-----------|----------|-----------------|------------|
| [Name] | $[X] | [Date] | Pioneers intro | Strong alignment |

## Human Action Needed (open process, waiting on info/decision)
| Foundation | Ask Amount | Deadline | Action Needed |
|-----------|-----------|----------|---------------|
| [Name] | $[X] | [Date] | Josh to confirm X |

## Cycle Closed (waiting for next cycle)
| Foundation | Ask Amount | Next Cycle | Action |
|-----------|-----------|------------|--------|
| [Name] | $[X] | [Date] | Submit inquiry form to queue |

## Invite Only (no public application process)
| Foundation | Potential Ask | Connection Path | Why Pursue |
|-----------|-------------|-----------------|------------|
| [Name] | $[X] | Pioneers intro | Strong alignment, large grants |

## Not Applicable (can't apply)
| Foundation | Reason | Alternative |
|-----------|--------|-------------|
| [Name] | Funds local churches only | Partner with Pakistani church |
```

**IMPORTANT:** Foundations in "Ready to Draft", "Relationship Needed", and "Human Action Needed" all have OPEN processes and should ALL get proposals drafted. The difference is:
- **Ready to Draft:** Can submit immediately
- **Relationship Needed:** Draft proposal, but wait to submit until intro secured
- **Human Action Needed:** Draft proposal, but wait for specific info/decision before submitting

### Step 5: Move Forward
Move the project subfolder to `03-application-prep/`.

## Decision Points

Default to momentum. Flag in HUMAN_TODO.md:
- Perfect-fit foundation is invitation-only → "Josh: check network for connections to [foundation]"
- Fewer than 4 strong-fit foundations → "Only [X] strong fits. Options: broaden search, reframe project, or proceed"
- Deadline within 30 days → "URGENT: [Foundation] deadline [DATE]. Fast-track needed."
- Key person identified with possible warm path → "Josh: do you know [person] at [foundation]? They're connected to [network]."

### NOTE:

You have READ access to our CRM, which is kept up to date with Waha's relationships to other people and organizations.

Before you send something onto a Human, do due diligence, and check to see if there's anything about that organization in our CRM. Also, check the CRM for any other situation in which that will be helpful.

To access the CRM, use the Agentic Skill available to you in the `[grants root]/skills` directory, that will allow you READ access to our CRM, Attio. The env variable is avialble in `[grants root]/.env`. 


## Quality Standards

- Every foundation must have ALL numbered documents (00 through 03)
- 990 analysis must include actual grant amounts, not guesses
- Vocabulary mapping must use the foundation's exact words, not paraphrases
- Key people must have been actually researched (LinkedIn, Google), not fabricated
- Recommended ask amounts must be justified by 990 data
