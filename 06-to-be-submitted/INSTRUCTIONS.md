# Stage 06: To Be Submitted

> **Your job:** For each approved foundation, deeply enrich key decision-maker profiles, draft cold outreach messages, and sync everything to Attio CRM. This stage runs AFTER Vince approves foundations from the Stage 05 review summary.

---

## Before You Start

1. Read `TOOLS_AND_APIS.md` in this directory for API reference
2. Read the foundation's full dossier (all numbered files carried forward from Stage 05)
3. Read `CONTEXT/STYLE_GUIDE.md` for Waha's voice and tone
4. Read `CONTEXT/LETTERHEAD.md` for cover letter formatting on Waha letterhead
5. Read `CONTEXT/PARTNERSHIPS.md` for Waha's network (needed for finding connection points)
6. Read `CONTEXT/OUR_ORGANIZATION.md` for team bios (needed for matching outreach to team members)
7. Confirm you have access to: `$GROQ_API_KEY`, `$ATTIO_ACCESS_TOKEN` (from `.env`)

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

LinkedIn connection requests: **200 characters max** (hard limit for free LinkedIn accounts). Write one punchy sentence — who you are, the shared connection or hook, and a reason to connect. No ask, no pitch. Example: "Hi [Name], I'm Vince with Waha — we work alongside [shared org] in [area]. Would love to connect."
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
  - `status`: "Active" (delivery stage)

### 3b. Ensure Organization Exists

Search Attio `companies` for the foundation by name and/or domain.

- **If not found:** Create with all available data from the dossier: name, domain(s), description, primary location, LinkedIn URL, categories
- **If found:** Enrich any empty fields with new data from the dossier

Then add to the **Prospective Funding Organizations** list (`c60e5e8e-5e81-4cb2-ab7c-796039b53043`) if not already there. Set fields from the dossier research:

| Field | api_slug | Source |
|-------|----------|--------|
| Status | `status` | "Project(s) Identified" (use "Good Fit" if the foundation is being researched for general alignment but no specific funding proposal has been created yet) |
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
| Proposal URL | `url_of_proposal` | Link to the Google Drive folder containing the proposal documents (if available) |

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
| Draft Location | `draft_location` | Google Drive link to the individual outreach draft file (e.g., `vince--reid-karr--email.md`). Use `gws drive files list` to search for the file by name within the foundation's `00-COLD-OUTREACH-DRAFTS/` folder and get the `webViewLink`. |
| Topic of outreach | `topic_of_outreach` | 1-2 sentence summary of WHY we are reaching out to this person: the target project(s) and ask amount, the specific connection or hook that makes this foundation applicable (e.g., prior grantee overlap, board member's missions background, geographic alignment), and any key deadlines. This field is for at-a-glance context so the caller understands the pitch without opening the full draft. |

### 3g. Update Outreach Draft Files

Go back to each file in `00-COLD-OUTREACH-DRAFTS/` and fill in:
- The **Attio record link** for the person (in both the individual draft file and the OUTREACH-PLAN.md table)
- The Attio link format: `https://app.attio.com/waha-app/people/{record_id}`

---

## Step 4: Cover Letter on Letterhead

Every cover letter must be produced as a `.docx` file on Waha's official letterhead before submission. This step converts the existing `06-COVER-LETTER` markdown into a submission-ready Word document.

### When to Apply Letterhead

Check the foundation's `04-APPLICATION-REQUIREMENTS`:
- **Mail, online portal with attachments, or unspecified** → Full letterhead (this step)
- **Email submission** → Skip letterhead. The email letter stays as `.md` (pasted into email body). See the "Email Letter" column in `CONTEXT/LETTERHEAD.md` for formatting differences.

### How to Generate the Letterhead `.docx`

The letterhead uses floating positioned elements (logo, address text box) that must come from Alycia's template. **Do not generate from scratch** — use the template-based approach:

1. **Read the spec:** `CONTEXT/LETTERHEAD.md` for the full format reference.
2. **Read the cover letter:** Source content is `06-COVER-LETTER - [Foundation Name] - [Project Name].md` in the foundation folder.
3. **Read the application requirements:** `04-APPLICATION-REQUIREMENTS` for the recipient address, contact name, and submission method.

4. **Copy the template:** Start from `alycias-edits-temp/Cover Letter - KIF.docx` (the canonical letterhead source).

5. **Replace body content** via the `docx` skill's edit workflow (unpack → edit XML → repack):
   - **P1:** Replace `[Date]` with the actual date (e.g., "March 31, 2026")
   - **P2-P5:** Replace recipient address lines (name, org, street, city/state)
   - **P6:** Replace salutation text. Remove bold formatting if not wanted.
   - **P7-P13:** Replace body paragraphs. Create new `<w:p>` elements with Lora font, justified alignment (`w:jc val="both"`), `w:after="160"`, `w:line="264"`, `w:lineRule="auto"`. See `CONTEXT/letterhead-build-example.py` for the `make_body_para()` function.
   - **P14:** Replace closing phrase ("With gratitude," / "Respectfully," / "In Christ,")
   - **P15-P18:** Update sign-off block if the signer differs from Vince Kanagaraj
   - **Strip comments:** Remove all `<w:commentRangeStart>`, `<w:commentRangeEnd>`, and `<w:commentReference>` elements. Empty `word/comments.xml`.

6. **Output file:** Save as `06-COVER-LETTER - [Foundation Name] - [Project Name].docx` in the foundation folder (same name as the `.md`, with `.docx` extension — NOT `.md.docx`).

7. **One-page check:** The letter should fit on one page. If it overflows, tighten the prose first. If still overflows, reduce body `w:line` from 264 to 240 and `w:after` from 160 to 120. Note: LibreOffice renders wider than Word/Google Docs — verify in the target application.

### Sign-Off Calibration

The closing phrase depends on the foundation's character (from `03-VOCABULARY-AND-FRAMING`):
- **Explicitly Christian foundations** → "In Christ,"
- **Secular or mixed foundations** → "With gratitude," or "Respectfully,"

The signer is always Vince Kanagaraj, Partnerships Director, unless the outreach plan assigns a different team member.

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

After completing all four steps for a foundation:
- `02-KEY-PEOPLE-ENRICHED.md` exists with deep profiles, contact info, board overlaps, and content summaries
- `00-COLD-OUTREACH-DRAFTS/` exists (unless zero outreach targets) with OUTREACH-PLAN.md and individual draft files with Attio links
- Attio has: Project (found/confirmed), Organization (created/enriched + on Prospective Funding Orgs list), Funding Proposal (created + linked to Project and Organization), People (created/enriched + linked to Organization), outreach contacts on Cold Outreach list
- Summary note on the Funding Proposal in Attio
- `06-COVER-LETTER - [Foundation Name] - [Project Name].docx` exists on Waha letterhead (unless the submission method is email)

The foundation is now ready for human review and submission. Alycia monitors the Cold Outreach list daily, reviews outreach drafts, and assigns them to the recommended team members.

---

## CRITICAL: Contact Verification Before Outreach

**"Cited" does not mean "verified."** Before any outreach message is sent, the contact method must be confirmed as currently working:

1. **Email addresses:** Check the foundation's current website for the email. If the email only appears in a third-party aggregator (Grantsmanship Center, Cause IQ, etc.) but NOT on the foundation's own site, mark it `(aggregator-sourced — verify before sending)`.
2. **Phone numbers:** Same rule. Aggregators often package 990 data that may be years old — a trust company may have changed numbers, an administrator may have retired.
3. **LinkedIn profiles:** Confirm the profile is active (has recent activity or current role listed). Stale profiles suggest the person may have moved on.
4. **Physical addresses:** Cross-check against the foundation's most recent 990 filing on ProPublica.

**If a contact method cannot be independently verified from the foundation's own current web presence, flag it in the outreach draft:** `⚠️ UNVERIFIED: This [email/phone/address] is sourced from [aggregator name], not the foundation's own website. Confirm before sending.`

**Never fabricate contact information.** If you cannot find a working contact method, say so explicitly and suggest how the human team can find it. An honest "contact not found" is infinitely better than a fabricated or stale contact that wastes everyone's time.
