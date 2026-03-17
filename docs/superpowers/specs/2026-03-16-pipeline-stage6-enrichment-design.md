# Pipeline Enhancement: Stage 06 To-Be-Submitted, Review Summary, and CRM Integration

**Date:** 2026-03-16
**Status:** Final
**Context:** Josh <> Vince 1:1 meeting (2026-03-16) — decision to add social outreach, deeper key-people research, and CRM sync to the grant pipeline before submission.

---

## Problem

The current pipeline moves proposals from review (Stage 05) directly to submitted (Stage 06) without:

1. Deep enrichment of key decision-makers — current key-people docs are ~100 words per person, not actionable for cold outreach
2. Draft outreach messages for the team to send alongside formal submissions
3. CRM synchronization — foundation data, funding proposals, and contacts aren't systematically created/linked in Attio
4. Enough information in the review summary for Vince to make quick approve/reject decisions

## Solution

Three changes:

1. **Enhance the Stage 05 review summary** with new columns Vince needs
2. **Insert a new Stage 06 ("To Be Submitted")** between review and submitted, with deep enrichment → outreach drafts → CRM sync
3. **Rework Stage 07 (renamed from 06) Submitted** as an active verification stage

---

## 1. Stage Renumbering

| Before | After |
|---|---|
| `06-submitted/` | `07-submitted/` |
| *(new)* | `06-to-be-submitted/` |

All INSTRUCTIONS.md files across stages 01-05 that reference "Stage 06" or `06-submitted` get updated to reflect the new numbering. The existing `06-submitted/amharic-dbs-veit-foundation/` moves to `07-submitted/`. Internal documents in that folder are left as-is — they are historical records of a completed submission and do not need stage number updates.

---

## 2. Review Summary Enhancement (Stage 05)

The `REVIEW_SUMMARY.md` template in `05-review/INSTRUCTIONS.md` gets extended with new columns. The existing prioritization logic stays intact.

### New Table Format

```markdown
## Submission Queue (prioritized by deadline)
| Foundation | Ask | Deadline | Key Contact | Website | Alignment | Grant Cycle | Status | Submitter | Notes |
|---|---|---|---|---|---|---|---|---|---|
```

The existing `Status` and `Submitter` columns are retained. **New columns** inserted before them:

- **Key Contact** — Primary contact person with role and best available contact method. Format: `Name (Role) · email@example.com` or `Name (Role) · [LinkedIn](url)` or `Name (Role) · 555-123-4567`. Priority: email > phone > LinkedIn > other social > "no contact found"
- **Website** — Foundation URL
- **Alignment** — One-line summary of *why the fit works* (not what the foundation is)
- **Grant Cycle** — Rolling vs. deadline, frequency. Include `⚠️ Once/year` warning prefix for foundations where rejection means waiting 12 months.

### Where This Changes

`05-review/INSTRUCTIONS.md` — the REVIEW_SUMMARY.md template section (currently at ~line 92). Updated so any future Stage 05 run produces the enriched table. Vince sees the new format the moment results land in `05-review/`.

---

## 3. New Stage: `06-to-be-submitted`

### Folder Structure

```
06-to-be-submitted/
├── INSTRUCTIONS.md
├── TOOLS_AND_APIS.md
└── {foundation-name}--{project-name}/
    ├── (all dossier files carried forward from 05-review)
    ├── 02-KEY-PEOPLE-ENRICHED.md
    └── 00-COLD-OUTREACH-DRAFTS/
        ├── OUTREACH-PLAN.md
        ├── vince--rebecca-smith--linkedin.md
        ├── jeff--craig-jones--email.md
        └── josh--tom-lin--linkedin.md
```

### Folder Naming

Individual foundation subfolders are cherry-picked from `05-review/{project-name}/{foundation-name}/` into `06-to-be-submitted/{foundation-name}--{project-name}/`. The project name is encoded after `--` in the folder name. This keeps the structure flat (easy to move in Google Drive) while preserving project context for CRM sync.

### Entry Criteria

A foundation moves from Stage 05 to Stage 06 only when **Vince approves it** from the review summary. This is an async decision — Vince reviews the `REVIEW_SUMMARY.md`, replies with which foundations to move forward, and Alycia (or Josh) cherry-picks those folders into `06-to-be-submitted/`.

**Only foundations with numbered prefixes** (`01-`, `02-`, etc. — meaning "ready to proceed, no blockers") are eligible for Stage 06. Foundations with status prefixes (`H-`, `R-`, `IO-`, `S-`, `NA-`) stay in Stage 05 until their blocker is resolved and the prefix is changed to a number.

**When moving to Stage 06:** strip the numeric prefix from the foundation folder name. `05-review/mongolian-dbs/03-jimmy-foundation/` becomes `06-to-be-submitted/jimmy-foundation--mongolian-dbs/`.

### Three Sequential Steps

#### Step 1: Deep Enrichment

For each key person identified in the existing `02-KEY-PEOPLE` document:

**Research activities:**
- Web search for name + foundation + role (articles, blog posts, conference bios, speaking engagements)
- YouTube search for talks/interviews — pull transcripts via `yt-dlp`, summarize key insights. **Max 3 videos per person.**
- Podcast search — find appearances via web search, download audio to `/tmp/grant-enrichment-{timestamp}/`, transcribe via Groq Whisper API (`$GROQ_API_KEY`), summarize. **Max 2 podcasts per person.**
- Cross-reference name across other foundations' 990s via ProPublica to find board overlaps and network connections
- Search for LinkedIn profile URL, Twitter/X, other social profiles
- Search for email addresses and phone numbers from public sources
- **Total content cap: up to 5 multimedia sources per person** (no more than 3 videos, no more than 2 podcasts; prioritize recent)

**Error handling:** If a source is unavailable (video removed, API rate limit, 990 not filed, LinkedIn profile not found), skip it and note the gap in the enriched output. Do not retry or block on failures — document what was attempted and move on. The goal is best-effort enrichment, not perfection.

**Temp file handling:** All downloaded audio/video goes to `/tmp/grant-enrichment-{timestamp}/`. Clean up after transcription.

**Output:** `02-KEY-PEOPLE-ENRICHED.md` — significantly expanded version of the original key-people doc. For each person:
- Full profile (role, background, tenure, public statements/positions)
- All found contact info (email, phone, LinkedIn URL, other social URLs)
- Board overlap map (other foundations they serve on, from 990 cross-referencing)
- Content summaries (key quotes, positions, interests from transcribed talks/posts)
- Network connections (shared boards, mutual organizations, connections to Waha's network)
- All sources cited inline

The original `02-KEY-PEOPLE` stays untouched for reference.

#### Step 2: Outreach Drafts

A person is a **quality cold outreach target** if they have: (a) a found contact method (email, LinkedIn, or phone), AND (b) a role that suggests influence over grantmaking decisions (board member, program officer, executive director, trustee). Administrative contacts (e.g., info@ addresses) get outreach drafts too, but at lower priority. People with no found contact method are documented in the enriched key-people file but do not get outreach drafts. If a foundation has zero quality outreach targets, skip the `00-COLD-OUTREACH-DRAFTS/` folder entirely and note the gap in `02-KEY-PEOPLE-ENRICHED.md`.

For each quality cold outreach target:

**`00-COLD-OUTREACH-DRAFTS/OUTREACH-PLAN.md`:**
- Summary table: who on the Waha team reaches out to whom, via what channel, with what message hook, and why this team member is the right match
- Prioritization of outreach order

**Individual draft files** named `{recommended-team-member}--{person-name}--{channel}.md`:
- **Intro section:** Who this person is, why they matter for this foundation/grant, why this specific team member should reach out, what connection or hook to leverage
- **Draft message:** The actual cold outreach message (LinkedIn message, email, etc.) written in a warm, direct, ministry-peer-to-peer tone — not corporate. Refer to `CONTEXT/STYLE_GUIDE.md` for Waha's voice. LinkedIn messages should be 2-4 sentences; emails can be 1-2 short paragraphs.
- **Attio link:** Link back to the person's Attio record (added after Step 3 creates the record)

The agent recommends the team member (josh/vince/jeff) based on:
- Network overlap (shared connections, mutual organizations)
- Role alignment (director-to-director, technical-to-technical)
- Shared interests or background

#### Step 3: CRM Sync

Sequential sub-steps:

**3a. Find/Confirm Project**
- Search Attio `projects` object for the project name (parsed from the `--{project-name}` in the folder name)
- If found: use it as the anchor for all subsequent links
- If not found: pause and confirm with the user before creating (the project should almost always already exist in Attio — a missing project likely means a naming mismatch, not a missing record). If confirmed to create: `project_name`, `type` (Localization/Mobilization/New Product), `status_funding` = "Pursuing Donors", `status` (delivery stage)

**3b. Ensure Organization Exists**
- Search Attio `companies` for the foundation by name and/or domain
- If not found: create with all available data (name, domain, description, location, LinkedIn, categories)
- If found: enrich any empty fields with new data
- Add to the "Prospective Funding Organizations" list (`c60e5e8e-5e81-4cb2-ab7c-796039b53043`) if not already there, with fields:
  - `status`: "Good Fit" or "Project(s) Identified"
  - Alignment Score, Recommendation, Faith-Based Willingness, Funder Type, Primary Contact, Application Deadline, etc. from the dossier research

**3c. Create Funding Proposal**
- Create a `funding_applications` record with:
  - `project_name`: proposal name (e.g., "Veit Foundation — Amharic DBS")
  - `status`: "Drafting Initial Inquiry" (or appropriate stage)
  - `type`: "Grant Application" / "Letter of Intent" / "Informal Proposal" (based on application type from `04-APPLICATION-REQUIREMENTS`)
  - `funding_requested`: ask amount (USD)
  - `projects_this_proposal_is_funding`: link to the Project record (record-reference)
  - `loi_due`: LOI deadline (if applicable)
  - `formal_proposal_due_date`: full proposal deadline (if applicable)
  - `receiving_proposal`: link to the Organization record (record-reference to `companies` — this field name is a legacy slug; it means "the organization receiving this proposal")
  - `url_of_proposal`: link to the Google Drive folder (if available)
- Link Project back to this Funding Proposal via `funding_application` field

**3d. Ensure People Exist**
- For each key person from `02-KEY-PEOPLE-ENRICHED.md`:
  - Search Attio `people` by name and/or email
  - If not found: create with all enriched data (name, email, phone, job title, LinkedIn, description)
  - If found: enrich any empty fields
  - Link person to the Organization via the `company` field

**3e. Create Summary Note**
- Create a note on the Funding Proposal summarizing the enrichment findings, key insights, and linking to the People and Organization records created above

**3f. Add Outreach Contacts to Cold Outreach List**
- For each person identified as a cold outreach target in Step 2:
- Add to the "GRANTS: Cold Outreach" list (`8c459b90-5574-453f-bdf0-0067434e83c9`) with:

| Field | api_slug | Value |
|---|---|---|
| Outreach type | `outreach_type` | "Linkedin" / "Email" / "Text" / "Referral Intro" (based on recommended channel) |
| Primary Caller | `primary_caller` | Recommended team member email: `josh@waha.app`, `vince@waha.app`, or `jeff@kingdomstrategies.co` |
| Outreach topic | `outreach_topic` | "Localization" / "Mobilization" / "Product" (based on project type) |
| Priority | `priority` | "High" / "Medium" / "Low" (based on alignment score and contact quality) |
| Status | `status` | "To contact" |
| Notes | `notes` | Brief context: why this person, what hook to use, reference to outreach draft file |
| LOI Due Date | `date_of_publication` | LOI deadline from application requirements |
| Link to foundation site | `link_to_published_piece` | Foundation website URL |

**3g. Update Outreach Draft Files**
- Go back to each file in `00-COLD-OUTREACH-DRAFTS/` and add the Attio record link for the person

### Workspace Member Reference

| Name | Email | UUID |
|---|---|---|
| Josh Müller | `josh@waha.app` | `524d1952-a278-475f-ae73-e7d3613018c5` |
| Vince Kanagaraj | `vince@waha.app` | `b3063763-09a0-4054-8ddd-a461ccba814c` |
| Jeff Peterson | `jeff@kingdomstrategies.co` | `bf243fb3-d869-4c34-a60a-5673d5c421fc` |
| Alycia (Team) | `team@waha.app` | `27505c18-4a53-47ba-8955-897b9b0382d9` |

---

## 4. Reworked Stage 07: Submitted

`07-submitted/INSTRUCTIONS.md` becomes an active verification stage:

**Step 1: Final CRM Verification**
- Verify the Funding Proposal record in Attio is 100% complete: all fields populated, all links correct (Project, Organization, People)
- Update Funding Proposal status to "Submitted Initial Inquiry" or "Submitted Full Proposal" with submission date

**Step 2: Read Communications**
- Check for responses, confirmations, or follow-up requests since the submission date via: Gmail (MCP tool), Attio email/interaction records, and any notes logged on the Funding Proposal or Organization records
- Log findings as notes on the Funding Proposal record in Attio

**Step 3: Update CONTEXT/PROSPECTIVE_PARTNERS.md**
- Update each foundation's status to reflect submission (e.g., "Submitted LOI 2026-03-16")

**Step 4: Local Submission Log**
- Create/update `SUBMISSION-LOG.md` in the foundation folder: submission date, method, confirmation received, reference numbers, follow-up dates

The Funding Proposal record being complete and accurate is the primary deliverable. The local file is secondary.

Folder naming continues the `{foundation-name}--{project-name}/` pattern from Stage 06.

---

## 5. TOOLS_AND_APIS.md Reference

A lightweight document in `06-to-be-submitted/` covering the tools available to the agent:

- **yt-dlp:** How to extract transcripts from YouTube videos. Temp directory pattern, cleanup.
- **Groq Whisper API:** Endpoint, auth via `$GROQ_API_KEY`, request/response format for audio transcription.
- **ProPublica Nonprofit Explorer API:** How to search for people across 990 filings to find board overlaps.
- **Attio API:** Auth via `$ATTIO_ACCESS_TOKEN`, key object IDs, list IDs, and field slugs needed for CRM sync.

Not scripts — reference material so the agent knows what's available and how to call it.

---

## 6. Attio Schema Reference

### Objects

| Object | Slug | ID |
|---|---|---|
| People | `people` | `8a5fce6d-66fd-4e86-bb27-8e0bfdef13f4` |
| Companies | `companies` | `38ccc1e4-26e9-4254-ad17-e621b589384b` |
| Projects | `projects` | `5c46a344-c20c-4d7c-9358-ddd162014429` |
| Funding Applications | `funding_applications` | `0468e84d-9b69-42ca-a120-cf291d6389d2` |

### Lists

| List | ID | Parent Object |
|---|---|---|
| GRANTS: Cold Outreach | `8c459b90-5574-453f-bdf0-0067434e83c9` | People |
| Prospective Funding Orgs | `c60e5e8e-5e81-4cb2-ab7c-796039b53043` | Companies |

### Prospective Funding Orgs List — Field Slugs & Enums

| Field | api_slug | Type | Writable | Notes |
|---|---|---|---|---|
| Status | `status` | status | Yes | Researching Opportunities, Good Fit, Brainstorming Projects, Project(s) Identified, Partnered |
| Point(s) of contact | `point_s_of_contact` | record-reference (multi) | Yes | Links to `people` |
| Where is there partnership alignment? | `project_angle` | text | Yes | |
| Alignment Score | `alignment_score` | number | Yes | 0-12 from alignment framework |
| Recommendation | `recommendation` | select | Yes | (options created on write) |
| Faith-Based Willingness | `faith_based_willingness` | select | Yes | Section B pass/fail gate |
| Funder Type | `funder_type` | select | Yes | Category per search criteria |
| Primary Contact | `primary_contact` | text | Yes | Name and title |
| Application Deadline | `application_deadline` | date | Yes | Next LOI/application deadline |
| Red Flags | `red_flags` | text | Yes | Disqualifying issues |
| Outreach Email Draft | `outreach_email_draft` | text | Yes | Cold outreach email |
| Suggested First Ask | `suggested_first_ask` | number | Yes | Based on 990 data |

### Cold Outreach List — Field Slugs & Enums

> **Note:** Some slugs are repurposed from the list's original template. `date_of_publication` = LOI Due Date, `link_to_published_piece` = Link to foundation site. The display names in Attio are correct; the API slugs just have legacy names.

| Field | api_slug | Type | Options |
|---|---|---|---|
| Outreach type | `outreach_type` | select | Linkedin, Email, Text, Referral Intro |
| Primary Caller | `primary_caller` | actor-reference | workspace member email or UUID |
| Outreach topic | `outreach_topic` | select | Localization, Mobilization, Product |
| Priority | `priority` | select | High, Medium, Low |
| Status | `status` | status | To contact, Contacted, Not interested, Moving forward, Published, On hold, Canceled |
| Notes | `notes` | text | free text |
| LOI Due Date | `date_of_publication` | date | ISO 8601 |
| Link to foundation site | `link_to_published_piece` | text | URL |

### Funding Applications — Status Pipeline

1. Drafting Initial Inquiry
2. Submitted Initial Inquiry
3. Drafting Full Proposal
4. Submitted Full Proposal
5. Funding Pledged
6. Funding Received
7. Funding Rejected

### Funding Applications — Type Options

- Grant Application
- Informal Proposal
- Letter of Intent
- FundraiseUp Campaign

---

## 7. Dependencies

- **Attio cold outreach list schema** — ✅ Finalized by Vince (2026-03-16)
- **Existing review summaries** — No backfill; new format applies to future runs only
- **Google Drive** — Alycia moves folders via file manager GUI; flat `{foundation}--{project}` naming supports this

## 8. Out of Scope

- Automated task assignment to team members (future consideration)
- Backfilling existing review summaries
- Script/tooling development (agent uses tools directly from instructions)
- Changes to stages 01-04
