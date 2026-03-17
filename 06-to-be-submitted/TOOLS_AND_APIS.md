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

### Attio Record URLs

When linking back to Attio records in outreach drafts, use this format:
- People: `https://app.attio.com/waha-app/people/{record_id}`
- Companies: `https://app.attio.com/waha-app/companies/{record_id}`
- Funding Applications: `https://app.attio.com/waha-app/funding_applications/{record_id}`

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
