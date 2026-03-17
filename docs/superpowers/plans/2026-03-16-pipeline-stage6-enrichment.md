# Pipeline Stage 06 Enrichment & CRM Sync Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Insert a new Stage 06 ("To Be Submitted") into the grant pipeline with deep key-people enrichment, cold outreach drafts, and Attio CRM synchronization, plus enhance the Stage 05 review summary and rework Stage 07 (Submitted).

**Architecture:** This is a documentation/instructions change — no application code. We're creating and modifying INSTRUCTIONS.md files that guide AI agents through the grant pipeline. The pipeline is a kanban-style directory structure where folder location = project status. Each stage directory has an INSTRUCTIONS.md the agent reads to know what to do.

**Tech Stack:** Markdown INSTRUCTIONS files, Attio CRM (MCP tools), yt-dlp (CLI), Groq Whisper API (REST), ProPublica Nonprofit Explorer API (REST).

**Spec:** `docs/superpowers/specs/2026-03-16-pipeline-stage6-enrichment-design.md`

---

## File Map

| Action | File | Purpose |
|--------|------|---------|
| Rename dir | `06-submitted/` → `07-submitted/` | Stage renumbering |
| Create dir | `06-to-be-submitted/` | New stage directory |
| Modify | `05-review/INSTRUCTIONS.md` | Enhanced review summary table + updated stage reference |
| Create | `06-to-be-submitted/INSTRUCTIONS.md` | New stage: enrichment → outreach → CRM sync |
| Create | `06-to-be-submitted/TOOLS_AND_APIS.md` | Reference doc for yt-dlp, Groq, ProPublica, Attio |
| Modify | `07-submitted/INSTRUCTIONS.md` | Reworked as active verification stage |

---

## Chunk 1: Stage Renumbering & Review Summary Enhancement

### Task 1: Rename `06-submitted/` to `07-submitted/`

**Files:**
- Rename: `06-submitted/` → `07-submitted/`

- [ ] **Step 1: Rename the directory**

```bash
mv 06-submitted 07-submitted
```

- [ ] **Step 2: Verify contents moved intact**

```bash
ls 07-submitted/
```

Expected: `amharic-dbs-veit-foundation/` and `INSTRUCTIONS.md`

- [ ] **Step 3: Create the new `06-to-be-submitted/` directory**

```bash
mkdir 06-to-be-submitted
```

- [ ] **Step 4: Commit**

```bash
git add -A 06-submitted 07-submitted 06-to-be-submitted
git commit -m "Rename 06-submitted to 07-submitted, create empty 06-to-be-submitted

Stage renumbering: inserting new Stage 06 (To Be Submitted) between
review and submitted per pipeline enhancement spec."
```

---

### Task 2: Update `05-review/INSTRUCTIONS.md` — Review Summary Enhancement

**Files:**
- Modify: `05-review/INSTRUCTIONS.md:90-115`

This task makes two changes: (a) the review summary table gets new columns, and (b) the stage reference at the end changes from `06-submitted` to `06-to-be-submitted`.

- [ ] **Step 1: Replace the review summary template (lines 92-106)**

Replace the existing template block:

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

With the enhanced version:

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

- [ ] **Step 2: Update the final stage reference (line 115)**

Replace:
```
Move project to `06-submitted/` ONLY after human reviews are complete and submissions begin.
```

With:
```
Move approved foundations to `06-to-be-submitted/` after Vince reviews and approves. See `06-to-be-submitted/INSTRUCTIONS.md` for the enrichment and CRM sync workflow that happens before submission.

**Moving foundations to Stage 06:**
- Only foundations with numbered prefixes (`01-`, `02-`, etc.) are eligible
- Strip the numeric prefix when moving: `05-review/{project}/{03-foundation}/` → `06-to-be-submitted/{foundation}--{project}/`
- Foundations with status prefixes (`H-`, `R-`, `IO-`, `S-`, `NA-`) stay in Stage 05 until their blocker is resolved
```

- [ ] **Step 3: Read the modified file to verify it renders correctly**

Read `05-review/INSTRUCTIONS.md` and confirm the table format and stage reference look right.

- [ ] **Step 4: Commit**

```bash
git add 05-review/INSTRUCTIONS.md
git commit -m "Enhance review summary table with key contact, alignment, grant cycle columns

Adds 4 new columns to REVIEW_SUMMARY.md template: Key Contact (with
contact method), Website, Alignment (one-line fit summary), Grant Cycle
(with once-a-year warning). Updates stage reference from 06-submitted
to 06-to-be-submitted with entry criteria."
```

---

## Chunk 2: Stage 06 INSTRUCTIONS.md

### Task 3: Create `06-to-be-submitted/INSTRUCTIONS.md`

**Files:**
- Create: `06-to-be-submitted/INSTRUCTIONS.md`

This is the core deliverable — the instructions that guide the AI agent through deep enrichment, outreach draft generation, and CRM sync.

- [ ] **Step 1: Write the INSTRUCTIONS.md file**

Create `06-to-be-submitted/INSTRUCTIONS.md` with the following content:

```markdown
# Stage 06: To Be Submitted

> **Your job:** For each approved foundation, deeply enrich key decision-maker profiles, draft cold outreach messages, and sync everything to Attio CRM. This stage runs AFTER Vince approves foundations from the Stage 05 review summary.

---

## Before You Start

1. Read `TOOLS_AND_APIS.md` in this directory for API reference
2. Read the foundation's full dossier (all numbered files carried forward from Stage 05)
3. Read `CONTEXT/STYLE_GUIDE.md` for Waha's voice and tone
4. Read `CONTEXT/PARTNERSHIPS.md` for Waha's network (needed for finding connection points)
5. Read `CONTEXT/OUR_ORGANIZATION.md` for team bios (needed for matching outreach to team members)
6. Confirm you have access to: `$GROQ_API_KEY`, `$ATTIO_ACCESS_TOKEN` (from `.env`)

## Folder Naming

Each foundation folder in this stage is named `{foundation-name}--{project-name}/`. The project name (after `--`) is used to find the Project record in Attio during CRM sync.

---

## Step 1: Deep Enrichment

For each key person identified in the existing `02-KEY-PEOPLE` document, conduct a deep research pass. The original `02-KEY-PEOPLE` stays untouched for reference.

### Research Activities (per person)

1. **Web search:** Search for their name + foundation + role. Look for articles, blog posts, conference bios, speaking engagements, press mentions, and interviews.

2. **YouTube:** Search for talks or interviews they've given. Pull transcripts via `yt-dlp` and summarize key insights relevant to their grantmaking priorities and worldview. **Max 3 videos per person.**

3. **Podcasts:** Search for podcast appearances via web search. Download audio to `/tmp/grant-enrichment-{timestamp}/`, transcribe via Groq Whisper API, and summarize. **Max 2 podcasts per person.** Clean up temp files after transcription.

4. **Board overlap (990 cross-referencing):** Search their name across other foundations' 990 filings via the ProPublica Nonprofit Explorer API. Identify which other foundation boards they sit on — these are network connection points.

5. **Social profiles:** Search for LinkedIn profile URL, Twitter/X, and other social platforms. Try harder than the Stage 02 pass — search with full name + foundation name + location, try variations, check foundation websites for staff/board pages with profile links.

6. **Contact information:** Search for email addresses and phone numbers from public sources (foundation websites, conference speaker pages, organizational directories).

**Content cap:** Up to 5 multimedia sources per person total (no more than 3 videos, no more than 2 podcasts). Prioritize recent content.

**Error handling:** If a source is unavailable (video removed, API rate limit, 990 not filed, LinkedIn profile not found), skip it and note the gap in the output. Do not retry or block on failures — document what was attempted and move on. The goal is best-effort enrichment, not perfection.

### Output: `02-KEY-PEOPLE-ENRICHED.md`

Create `02-KEY-PEOPLE-ENRICHED - [Foundation Name] - [Project Name].md` in the foundation folder. For each person, include:

- **Full profile:** Role, background, tenure, public statements and positions
- **Contact info:** Email, phone, LinkedIn URL, Twitter/X, other social URLs (or note what was searched but not found)
- **Board overlap map:** Other foundations they serve on (from 990 cross-referencing), with links to ProPublica pages
- **Content summaries:** Key quotes, stated priorities, interests, and worldview from transcribed talks/posts
- **Network connections:** Shared boards with other foundations in our pipeline, mutual organizations, any connections to Waha's network (check PARTNERSHIPS.md)
- **All sources cited inline** using the project citation standard: `([Source](URL))`

---

## Step 2: Outreach Drafts

### Who Gets an Outreach Draft?

A person is a **quality cold outreach target** if they have:
- (a) A found contact method (email, LinkedIn, or phone), AND
- (b) A role suggesting influence over grantmaking (board member, program officer, executive director, trustee)

Administrative contacts (e.g., info@ email addresses) also get outreach drafts, but at **lower priority**.

People with no found contact method are documented in `02-KEY-PEOPLE-ENRICHED` but do **not** get outreach drafts.

If a foundation has **zero** quality outreach targets, skip the `00-COLD-OUTREACH-DRAFTS/` folder entirely and note the gap at the bottom of `02-KEY-PEOPLE-ENRICHED.md`.

### Create `00-COLD-OUTREACH-DRAFTS/` Folder

#### `OUTREACH-PLAN.md`

A summary document with:

```markdown
# Outreach Plan: [Foundation Name]

| Priority | Contact | Role | Channel | Team Member | Hook | Attio Link |
|----------|---------|------|---------|-------------|------|------------|
| 1 | [Name] | [Role] | LinkedIn | vince | [Why this person, what connection] | [Added in Step 3] |
| 2 | [Name] | [Role] | Email | josh | [Why this person, what connection] | [Added in Step 3] |
```

#### Individual Draft Files

Named: `{recommended-team-member}--{person-name}--{channel}.md`

Example: `vince--rebecca-smith--linkedin.md`

Each file contains:

```markdown
# Outreach: [Person Name] via [Channel]

## Context for [Team Member Name]
- **Who:** [Person name, role at foundation]
- **Why they matter:** [Their influence on grantmaking decisions]
- **Why you:** [Why this team member is the right person to reach out — network overlap, role alignment, shared interests]
- **Hook:** [What connection or angle to leverage]
- **Attio record:** [Link added in Step 3]

---

## Draft Message

[The actual message to send. Written in a warm, direct, ministry-peer-to-peer tone — not corporate. Reference CONTEXT/STYLE_GUIDE.md for voice.

LinkedIn messages: 2-4 sentences.
Emails: 1-2 short paragraphs.]
```

### Team Member Recommendation Logic

Recommend josh, vince, or jeff based on:
- **Network overlap:** Shared connections, mutual organizations, board membership in common
- **Role alignment:** Director-to-director, technical-to-technical
- **Shared interests or background:** Missions experience, geographic connections, thematic alignment

If no clear differentiator, default to vince (VP of Partnerships).

---

## Step 3: CRM Sync

Run these sub-steps **sequentially**. Each builds on the previous.

### 3a. Find/Confirm Project

Search Attio `projects` object for the project name (parsed from the `--{project-name}` portion of the folder name).

- **If found:** Use it as the anchor for all subsequent links. Note its record ID.
- **If not found:** STOP and confirm with the user before creating. A missing project almost always means a naming mismatch, not a missing record. If confirmed to create, use fields:
  - `project_name`: the project name
  - `type`: "Localization" / "Mobilization Initiative" / "New Product or Feature"
  - `status_funding`: "Pursuing Donors"

### 3b. Ensure Organization Exists

Search Attio `companies` for the foundation by name and/or domain.

- **If not found:** Create with all available data from the dossier: name, domain(s), description, primary location, LinkedIn URL, categories
- **If found:** Enrich any empty fields with new data from the dossier

Then add to the **Prospective Funding Organizations** list (`c60e5e8e-5e81-4cb2-ab7c-796039b53043`) if not already there. Set fields from the dossier research:

| Field | api_slug | Source |
|-------|----------|--------|
| Status | `status` | "Project(s) Identified" |
| Point(s) of contact | `point_s_of_contact` | Link to key contact person record (created in 3d) |
| Partnership alignment | `project_angle` | From `03-VOCABULARY-AND-FRAMING` alignment analysis |
| Alignment Score | `alignment_score` | From `00-BRIEFING` fit analysis (0-12) |
| Faith-Based Willingness | `faith_based_willingness` | From dossier research |
| Funder Type | `funder_type` | From `00-BRIEFING` (e.g., "Private Foundation", "Family Foundation") |
| Primary Contact | `primary_contact` | Name and title of key contact |
| Application Deadline | `application_deadline` | From `04-APPLICATION-REQUIREMENTS` |
| Red Flags | `red_flags` | From `07-REVIEW-NOTES` issues |
| Suggested First Ask | `suggested_first_ask` | From `01-990-ANALYSIS` recommended ask |

### 3c. Create Funding Proposal

Create a `funding_applications` record:

| Field | api_slug | Value |
|-------|----------|-------|
| Proposal Name | `project_name` | "[Foundation Name] — [Project Name]" |
| Status | `status` | "Drafting Initial Inquiry" (or appropriate stage based on what's been written) |
| Type | `type` | "Grant Application" / "Letter of Intent" / "Informal Proposal" (from `04-APPLICATION-REQUIREMENTS`) |
| Funding Requested | `funding_requested` | Ask amount in USD (from `01-990-ANALYSIS` recommended ask) |
| Project link | `projects_this_proposal_is_funding` | Record reference to the Project found in 3a |
| LOI Due Date | `loi_due` | From `04-APPLICATION-REQUIREMENTS` (if applicable) |
| Formal Proposal Due | `formal_proposal_due_date` | From `04-APPLICATION-REQUIREMENTS` (if applicable) |
| Receiving Organization | `receiving_proposal` | Record reference to the Organization from 3b. (Note: this slug is a legacy name — it means "the organization receiving this proposal") |

Then link the Project back to this Funding Proposal by updating the Project's `funding_application` field to include this record.

### 3d. Ensure People Exist

For each key person from `02-KEY-PEOPLE-ENRICHED.md`:

1. Search Attio `people` by name and/or email
2. **If not found:** Create with all enriched data:
   - `name` (first_name, last_name)
   - `email_addresses`
   - `phone_numbers`
   - `job_title`
   - `company`: record reference to the Organization from 3b
   - `linkedin`: LinkedIn URL
   - `description`: Brief summary of role and relevance
3. **If found:** Enrich any empty fields with new data
4. Link person to the Organization via the `company` field (if not already linked)

### 3e. Create Summary Note

Create a note on the Funding Proposal record summarizing:
- Key enrichment findings
- Outreach strategy (who is being contacted, via what channel)
- Links to the People and Organization records created above
- Any gaps or concerns from the enrichment pass

### 3f. Add Outreach Contacts to Cold Outreach List

For each person identified as a cold outreach target in Step 2, add to the **GRANTS: Cold Outreach** list (`8c459b90-5574-453f-bdf0-0067434e83c9`):

| Field | api_slug | Value |
|-------|----------|-------|
| Outreach type | `outreach_type` | "Linkedin" / "Email" / "Text" / "Referral Intro" (from the recommended channel in the outreach draft) |
| Primary Caller | `primary_caller` | Recommended team member: `josh@waha.app`, `vince@waha.app`, or `jeff@kingdomstrategies.co` |
| Outreach topic | `outreach_topic` | "Localization" / "Mobilization" / "Product" (based on the project type) |
| Priority | `priority` | "High" / "Medium" / "Low" (High = board member/director with strong connection point; Medium = program officer or staff; Low = administrative contact) |
| Status | `status` | "To contact" |
| Notes | `notes` | Brief context: why this person, what hook to use, which outreach draft file to reference |
| LOI Due Date | `date_of_publication` | LOI deadline from `04-APPLICATION-REQUIREMENTS` |
| Link to foundation site | `link_to_published_piece` | Foundation website URL |

### 3g. Update Outreach Draft Files

Go back to each file in `00-COLD-OUTREACH-DRAFTS/` and fill in:
- The **Attio record link** for the person (in both the individual draft file and the OUTREACH-PLAN.md table)
- The Attio link format: `https://app.attio.com/waha-app/people/{record_id}`

---

## Workspace Member Reference

| Name | Email | UUID |
|---|---|---|
| Josh Müller | `josh@waha.app` | `524d1952-a278-475f-ae73-e7d3613018c5` |
| Vince Kanagaraj | `vince@waha.app` | `b3063763-09a0-4054-8ddd-a461ccba814c` |
| Jeff Peterson | `jeff@kingdomstrategies.co` | `bf243fb3-d869-4c34-a60a-5673d5c421fc` |
| Alycia (Team) | `team@waha.app` | `27505c18-4a53-47ba-8955-897b9b0382d9` |

---

## Done Criteria

After completing all three steps for a foundation:
- `02-KEY-PEOPLE-ENRICHED.md` exists with deep profiles, contact info, board overlaps, and content summaries
- `00-COLD-OUTREACH-DRAFTS/` exists (unless zero outreach targets) with OUTREACH-PLAN.md and individual draft files with Attio links
- Attio has: Project (found/confirmed), Organization (created/enriched + on Prospective Funding Orgs list), Funding Proposal (created + linked to Project and Organization), People (created/enriched + linked to Organization), outreach contacts on Cold Outreach list
- Summary note on the Funding Proposal in Attio

The foundation is now ready for human review and submission. Alycia monitors the Cold Outreach list daily, reviews outreach drafts, and assigns them to the recommended team members.
```

- [ ] **Step 2: Read the file back to verify it renders correctly**

Read `06-to-be-submitted/INSTRUCTIONS.md` and verify all sections, tables, and templates are well-formed.

- [ ] **Step 3: Commit**

```bash
git add 06-to-be-submitted/INSTRUCTIONS.md
git commit -m "Add Stage 06 INSTRUCTIONS: deep enrichment, outreach drafts, CRM sync

Three sequential steps: (1) deep key-people enrichment with YouTube/podcast
transcription and 990 cross-referencing, (2) cold outreach draft generation
with team member recommendations, (3) Attio CRM sync creating/linking
Project, Organization, Funding Proposal, People, and outreach list entries."
```

---

## Chunk 3: Tools Reference & Stage 07 Rework

### Task 4: Create `06-to-be-submitted/TOOLS_AND_APIS.md`

**Files:**
- Create: `06-to-be-submitted/TOOLS_AND_APIS.md`

- [ ] **Step 1: Write the TOOLS_AND_APIS.md file**

```markdown
# Tools & APIs Reference

Reference for the AI agent running Stage 06. Not scripts — just enough context to know what's available and how to call it.

---

## yt-dlp — YouTube Transcript Extraction

**Purpose:** Pull transcripts from YouTube videos for key-person enrichment.

**Preferred approach — subtitles only (no video download):**
```bash
# Try auto-generated subtitles first (fastest, no download needed)
yt-dlp --write-auto-sub --sub-lang en --skip-download --sub-format vtt -o "/tmp/grant-enrichment-$(date +%s)/%(id)s" "VIDEO_URL"

# If no auto-subs available, try manual subtitles
yt-dlp --write-sub --sub-lang en --skip-download --sub-format vtt -o "/tmp/grant-enrichment-$(date +%s)/%(id)s" "VIDEO_URL"
```

**Fallback — download audio and transcribe via Groq:**
```bash
# Only if no subtitles available. Downloads audio only (smallest file).
yt-dlp -x --audio-format mp3 --audio-quality 5 -o "/tmp/grant-enrichment-$(date +%s)/%(id)s.%(ext)s" "VIDEO_URL"
```

Then transcribe the mp3 via Groq Whisper (see below).

**Always clean up after:**
```bash
rm -rf /tmp/grant-enrichment-*/
```

---

## Groq Whisper API — Audio Transcription

**Purpose:** Transcribe podcast audio to text.

**Auth:** `$GROQ_API_KEY` from `.env`

**Endpoint:** `https://api.groq.com/openai/v1/audio/transcriptions`

**Request:**
```bash
curl -s https://api.groq.com/openai/v1/audio/transcriptions \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -F "model=whisper-large-v3-turbo" \
  -F "file=@/tmp/grant-enrichment-TIMESTAMP/audio.mp3" \
  -F "response_format=text"
```

**Notes:**
- Max file size: 25MB. If a podcast is larger, consider downloading only a portion or using a lower quality setting.
- For longer files, the `whisper-large-v3-turbo` model is fastest.
- Response is plain text transcription.

---

## ProPublica Nonprofit Explorer API — 990 Cross-Referencing

**Purpose:** Find board overlaps by searching for people across foundation 990 filings.

**Base URL:** `https://projects.propublica.org/nonprofits/api/v2`

**Search for an organization:**
```
GET /search.json?q=FOUNDATION_NAME&state[id]=STATE_CODE
```

**Get 990 filing details:**
```
GET /organizations/EIN.json
```

**Get specific 990 filing (includes officers/board):**
```
GET /filings/FILING_ID.json
```

**Cross-referencing workflow:**
1. Search for the person's name across multiple foundation 990s
2. Look at the `officers` array in each filing for name matches
3. Note which foundations share board members — these are network connection points

**Note:** The API is free and rate-limited. If you hit rate limits, wait briefly and retry. For board member cross-referencing, start with the foundations already in our pipeline (check `CONTEXT/PROSPECTIVE_PARTNERS.md` for EINs).

---

## Attio CRM API

**Auth:** `$ATTIO_ACCESS_TOKEN` from `.env`

**Prefer MCP tools over raw API calls.** The Attio MCP tools handle auth and pagination automatically. Use them for all CRM operations:
- `search-records` — find existing records
- `create-record` — create new records
- `update-record` — enrich existing records
- `upsert-record` — create or update
- `add-record-to-list` — add to a list with entry values
- `create-note` — add notes to records
- `list-records-in-list` — check if a record is already on a list

### Key Object IDs

| Object | Slug | ID |
|---|---|---|
| People | `people` | `8a5fce6d-66fd-4e86-bb27-8e0bfdef13f4` |
| Companies | `companies` | `38ccc1e4-26e9-4254-ad17-e621b589384b` |
| Projects | `projects` | `5c46a344-c20c-4d7c-9358-ddd162014429` |
| Funding Applications | `funding_applications` | `0468e84d-9b69-42ca-a120-cf291d6389d2` |

### Key List IDs

| List | ID | Parent Object |
|---|---|---|
| GRANTS: Cold Outreach | `8c459b90-5574-453f-bdf0-0067434e83c9` | People |
| Prospective Funding Orgs | `c60e5e8e-5e81-4cb2-ab7c-796039b53043` | Companies |

### Workspace Members (for Primary Caller field)

| Name | Email | UUID |
|---|---|---|
| Josh Müller | `josh@waha.app` | `524d1952-a278-475f-ae73-e7d3613018c5` |
| Vince Kanagaraj | `vince@waha.app` | `b3063763-09a0-4054-8ddd-a461ccba814c` |
| Jeff Peterson | `jeff@kingdomstrategies.co` | `bf243fb3-d869-4c34-a60a-5673d5c421fc` |

### Cold Outreach List — Field Slugs

> **Note:** Some slugs are repurposed from the list's original template. The display names in Attio are correct; the API slugs have legacy names.

| Field | api_slug | Type | Options |
|---|---|---|---|
| Outreach type | `outreach_type` | select | Linkedin, Email, Text, Referral Intro |
| Primary Caller | `primary_caller` | actor-reference | workspace member email or UUID |
| Outreach topic | `outreach_topic` | select | Localization, Mobilization, Product |
| Priority | `priority` | select | High, Medium, Low |
| Status | `status` | status | To contact, Contacted, Not interested, Moving forward, Published, On hold, Canceled |
| Notes | `notes` | text | free text |
| LOI Due Date | `date_of_publication` | date | ISO 8601 (legacy slug — means LOI Due Date) |
| Link to foundation site | `link_to_published_piece` | text | URL (legacy slug — means foundation site link) |

### Prospective Funding Orgs List — Field Slugs

| Field | api_slug | Type |
|---|---|---|
| Status | `status` | status (Researching Opportunities / Good Fit / Brainstorming Projects / Project(s) Identified / Partnered) |
| Point(s) of contact | `point_s_of_contact` | record-reference (multi, links to people) |
| Partnership alignment | `project_angle` | text |
| Alignment Score | `alignment_score` | number (0-12) |
| Recommendation | `recommendation` | select |
| Faith-Based Willingness | `faith_based_willingness` | select |
| Funder Type | `funder_type` | select |
| Primary Contact | `primary_contact` | text |
| Application Deadline | `application_deadline` | date |
| Red Flags | `red_flags` | text |
| Outreach Email Draft | `outreach_email_draft` | text |
| Suggested First Ask | `suggested_first_ask` | number |

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
```

- [ ] **Step 2: Commit**

```bash
git add 06-to-be-submitted/TOOLS_AND_APIS.md
git commit -m "Add TOOLS_AND_APIS.md reference for Stage 06 agent

Covers yt-dlp transcript extraction, Groq Whisper transcription,
ProPublica 990 cross-referencing, and Attio CRM API with full
field slugs for Cold Outreach and Prospective Funding Orgs lists."
```

---

### Task 5: Rework `07-submitted/INSTRUCTIONS.md`

**Files:**
- Modify: `07-submitted/INSTRUCTIONS.md` (the file that was just renamed from `06-submitted/`)

- [ ] **Step 1: Rewrite the INSTRUCTIONS.md**

Replace the entire contents of `07-submitted/INSTRUCTIONS.md` with:

```markdown
# Stage 07: Submitted & Tracking

> **Your job:** Verify the Funding Proposal record in Attio is 100% complete, check for any communications about the submission, update the prospective partners registry, and maintain a local submission log.

---

## Before You Start

1. Read `06-to-be-submitted/TOOLS_AND_APIS.md` for Attio API reference
2. Identify the foundation's Funding Proposal record in Attio (created during Stage 06 CRM sync)
3. Confirm you have access to `$ATTIO_ACCESS_TOKEN` (from `.env`)

## Folder Naming

Same as Stage 06: `{foundation-name}--{project-name}/`

---

## Step 1: Final CRM Verification

Verify the Funding Proposal record in Attio is 100% complete:

- [ ] `project_name` — proposal name is clear and accurate
- [ ] `status` — set to "Submitted Initial Inquiry" or "Submitted Full Proposal" (with submission date)
- [ ] `type` — correct application type
- [ ] `funding_requested` — correct ask amount
- [ ] `projects_this_proposal_is_funding` — linked to the correct Project
- [ ] `receiving_proposal` — linked to the correct Organization
- [ ] `loi_due` / `formal_proposal_due_date` — deadlines populated
- [ ] People linked to the Organization (from Stage 06 Step 3d)
- [ ] Organization on the Prospective Funding Orgs list with all fields populated
- [ ] Summary note exists on the Funding Proposal

Fix any gaps or broken links found during verification.

---

## Step 2: Read Communications

Check for responses, confirmations, or follow-up requests **since the submission date** via:
- Gmail (MCP tool) — search for foundation name and contact emails
- Attio email/interaction records on the Organization and People records
- Notes logged on the Funding Proposal or Organization records

Log any findings as a new note on the Funding Proposal record in Attio.

---

## Step 3: Update Prospective Partners Registry

Update `CONTEXT/PROSPECTIVE_PARTNERS.md`:
- Set the foundation's status to reflect submission (e.g., "Submitted LOI 2026-03-16")
- Note any response or follow-up status

---

## Step 4: Local Submission Log

Create or update `SUBMISSION-LOG.md` in the foundation folder:

```
# Submission Log: [Foundation Name]

- **Date submitted:** [DATE]
- **Submitted by:** [Name]
- **Method:** [online portal / email / mail]
- **Confirmation received?** [Y/N]
- **Ask amount:** $[X]
- **Expected response date:** [DATE or "unknown"]
- **Follow-up scheduled:** [DATE — typically 2-4 weeks after expected response date]

## Follow-Up Actions
- [ ] Send thank-you email within 48 hours of submission
- [ ] Calendar reminder for follow-up check-in at [DATE]
- [ ] Calendar reminder for expected decision at [DATE]

## Outcome
- **Decision:** [AWARDED / DECLINED / PENDING / NO RESPONSE]
- **Amount awarded:** $[X] (if different from ask)
- **Date of decision:** [DATE]
- **Feedback received:** [Any feedback from the foundation]

## If Awarded
- [ ] Send thank-you letter within 1 week
- [ ] Note reporting requirements and deadlines
- [ ] Update CONTEXT/PROSPECTIVE_PARTNERS.md with award status
- [ ] Plan for renewal/growth: next ask of $[X] in [timeframe]

## If Declined
- [ ] Send gracious thank-you anyway
- [ ] Request feedback if appropriate
- [ ] Note lessons in "Rejection Analysis" below
- [ ] Update CONTEXT/PROSPECTIVE_PARTNERS.md with outcome
- [ ] Decide: reapply next cycle? Different project? Move on?

## Rejection Analysis (if declined)
- **Likely reason:** [Based on any feedback or our best guess]
- **What we'd change:** [For next application to this or similar funders]
- **Worth reapplying?** [Yes — next cycle / Yes — with different project / No — poor fit]
```

---

## Done Criteria

- Funding Proposal record in Attio is 100% complete with all links verified
- Any communications logged as notes
- `CONTEXT/PROSPECTIVE_PARTNERS.md` updated with submission status
- `SUBMISSION-LOG.md` created in the foundation folder

The Funding Proposal record being complete and accurate is the **primary deliverable**. The local submission log is secondary.

---

## Quarterly Review

Every quarter, review all foundations in `07-submitted/`:
1. Which applications are still pending? Follow up.
2. Which were awarded? Ensure reporting is on track.
3. Which were declined? Capture lessons.
4. Update `CONTEXT/PROSPECTIVE_PARTNERS.md` with final outcomes for each foundation.
```

- [ ] **Step 2: Read the file back to verify**

Read `07-submitted/INSTRUCTIONS.md` and confirm all sections render correctly.

- [ ] **Step 3: Commit**

```bash
git add 07-submitted/INSTRUCTIONS.md
git commit -m "Rework Stage 07 Submitted as active CRM verification stage

Adds: Funding Proposal completeness checklist, communications check
(Gmail + Attio), PROSPECTIVE_PARTNERS.md update step. Retains existing
submission log template and quarterly review process. Renamed from
Stage 06 to Stage 07."
```

---

## Chunk 4: Final Verification

### Task 6: End-to-End Verification

- [ ] **Step 1: Verify directory structure**

```bash
ls -la 05-review/INSTRUCTIONS.md
ls -la 06-to-be-submitted/INSTRUCTIONS.md
ls -la 06-to-be-submitted/TOOLS_AND_APIS.md
ls -la 07-submitted/INSTRUCTIONS.md
ls -la 07-submitted/amharic-dbs-veit-foundation/
```

All should exist. The amharic-dbs folder should be in `07-submitted/`.

- [ ] **Step 2: Verify no stale references remain**

```bash
grep -r "06-submitted" --include="*.md" 01-prospect-research/ 02-deep-research/ 03-application-prep/ 04-proposal-drafts/ 05-review/ 06-to-be-submitted/ 07-submitted/INSTRUCTIONS.md
```

Expected: no results (all references should now say `06-to-be-submitted` or `07-submitted`). The `07-submitted/amharic-dbs-veit-foundation/` internal docs are exempt — they are historical.

- [ ] **Step 3: Verify review summary table has new columns**

Read `05-review/INSTRUCTIONS.md` and confirm the REVIEW_SUMMARY.md template includes: Foundation, Ask, Deadline, Key Contact, Website, Alignment, Grant Cycle, Status, Submitter, Notes.

- [ ] **Step 4: Final commit (if any fixes needed)**

```bash
git add -A
git commit -m "Fix any remaining stale stage references"
```

Only commit if Step 2 found stale references that needed fixing.

- [ ] **Step 5: Summary**

Report to user:
- Files created: `06-to-be-submitted/INSTRUCTIONS.md`, `06-to-be-submitted/TOOLS_AND_APIS.md`
- Files modified: `05-review/INSTRUCTIONS.md`, `07-submitted/INSTRUCTIONS.md`
- Directories: `06-submitted/` → `07-submitted/`, `06-to-be-submitted/` created
- Total commits: 5-6
