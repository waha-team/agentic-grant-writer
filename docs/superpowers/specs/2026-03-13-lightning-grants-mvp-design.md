# Lightning Grants MVP — Product Design Specification

**Date:** 2026-03-13
**Status:** Draft
**Domain:** lightninggrants.ai

## 1. Overview

Lightning Grants is a cloud-based, AI-powered grant research and writing platform for nonprofit organizations. It productizes an existing CLI-based agentic pipeline that automates foundation prospecting, 990 analysis, dossier building, vocabulary mapping, proposal drafting, and review.

**Target market:** Faith-based nonprofits with $500K–$5M annual revenue seeking to diversify funding through foundation grants.

**Pricing:** $2,000–$3,500/month per organization.

**Core value proposition:** Autonomous AI agents do 90%+ of the research and drafting work. The system defaults to action — when it identifies a need (board letter, LOI, cover letter), it researches the context and drafts the document itself rather than blocking on human input. Tokens are cheap; client time is expensive.

## 2. User Personas

### Development Director / Grant Writer
- Already writes grants, wants to 10x throughput
- Values: power, control, visibility into research quality, ability to refine proposals
- Interaction: Uses Project Prep Studio for brief development, reviews dossiers and proposals in detail, provides expert feedback

### Executive Director / Founder
- Wears many hats, no dedicated grant person
- Values: simplicity, minimal time investment, results
- Interaction: Quick brief creation via chat, reviews only final proposals, responds to tasks when prompted

## 3. System Architecture

Three processes, one language (TypeScript), one database.

### 3.1 Next.js App (Vercel)
- Project Prep Studio (chat UI)
- Grant Research Dashboard
- Task management UI
- Document upload portal
- Report viewer + DOCX export
- Thin API routes (job creation, task responses, file uploads)

### 3.2 Worker Process (Railway)
- Agent orchestrator (job polling, stage management)
- Prospect research agents
- Deep research agents (parallel per foundation)
- Proposal drafting agents
- ProPublica API integration (990 analysis)
- Web search integration
- OpenRouter API calls (global model config, default Claude)

### 3.3 Supabase (Managed)
- **Postgres:** All application data with Row-Level Security for multi-tenancy
- **Auth:** Email/password authentication, org membership
- **Storage:** Uploaded documents (501c3, 990s, annual reports), generated DOCX exports
- **Realtime:** Live subscriptions for dashboard updates as agents produce results

### 3.4 Communication Pattern
The database is the message bus. Next.js writes job rows; the worker polls for queued jobs, claims them, and writes results back. Supabase Realtime pushes updates to the browser. No Redis or message queue needed for MVP.

### 3.5 External Services
- **OpenRouter:** All AI reasoning, drafting, analysis. Model configurable globally by admin (not per-org). Default: Claude.
- **ProPublica Nonprofit Explorer API:** 990 data, grantee lists, board members, asset levels, giving patterns. Free.
- **Web Search:** Foundation discovery, website research, key people lookup.

## 4. Data Model

### 4.1 Core Tables

**`orgs`**
- id, name, ein, mission, settings (JSON), created_at

**`org_context`** — replaces the CONTEXT/ directory
- id, org_id, type (enum: profile, impact_stories, financials, partnerships, style_guide, search_criteria, statement_of_faith, board, governance), content (rich text/markdown), always_load (boolean), created_at, updated_at

Context loading tiers:
- **Always loaded** (always_load = true): org profile, style guide, search criteria, financials summary, statement of faith
- **Selectively loaded** (always_load = false): individual impact stories (matched by geography/theme), partnership details (matched by partner relevance), board/governance docs (when needed for applications), past grant history

**`projects`** — replaces project briefs + folder location as status
- id, org_id, name, description, brief_content (markdown), status (enum: prep, prospect_research, deep_research, application_prep, proposal_drafting, review, submitted), created_at, updated_at

**`prospects`** — replaces PROSPECTS.md + foundation subfolders
- id, project_id, foundation_name, ein, website, mission, tier (1/2/3), grant_range_min, grant_range_max, grant_median, suggested_ask, application_type (open/loi/invitation), grant_cycle, status (enum: identified, researching, complete, blocked, not_applicable, invite_only, cycle_closed, suspended), priority (integer), created_at, updated_at

**`dossiers`** — replaces the 00-07 numbered files per foundation
- id, prospect_id, type (enum: briefing, 990_analysis, key_people, vocabulary_framing, application_requirements, proposal_draft, cover_letter, review_notes), content (markdown with inline citations), created_at, updated_at

**`tasks`** — replaces HUMAN_TODO.md
- id, org_id, project_id (nullable), prospect_id (nullable), type (enum: blocking, non_blocking), title, description, status (enum: pending, in_progress, completed, dismissed), response (text, nullable), attachments (JSON array of storage paths), created_at, updated_at

When both project_id and prospect_id are null, the task is org-level (e.g., "Upload your 501(c)(3) letter"). This covers universal document needs.

**`documents`** — uploaded files
- id, org_id, name, file_path (Supabase Storage reference), doc_type (enum: 501c3, 990, annual_report, strategic_plan, board_resolution, other), extracted_content (text, nullable — AI-extracted on upload), created_at

**`agent_jobs`** — pipeline orchestration
- id, project_id, stage (enum: prospect_research, deep_research, application_prep, proposal_drafting, review), prospect_id (nullable, for per-foundation sub-jobs), status (enum: queued, running, completed, failed), error (text, nullable), started_at, completed_at

**`chat_messages`** — Project Prep Studio conversation history
- id, project_id, role (enum: user, assistant), content (text), created_at

**`users`** — extends Supabase Auth
- id (matches auth.users), org_id, name, email, role (enum: admin, member), created_at

### 4.2 Multi-Tenancy
Every table with user data includes an `org_id` column. Supabase Row-Level Security policies enforce that users can only access data belonging to their org. This is enforced at the database level, not the application level.

### 4.3 Cross-Project Intelligence
The prospect deduplication registry (replacing PROSPECTIVE_PARTNERS.md) is a query: all prospects across all projects for an org, grouped by EIN. Before adding a new prospect, the agent checks if this foundation has been researched in any project for this org.

## 5. User Experience

### 5.1 Project Prep Studio (Chat-Centric)

**Purpose:** Help the user develop and strengthen a project brief before it enters the research pipeline.

**Flow:**
1. User creates a new project — gives it a name, writes an initial description (or pastes from an existing doc)
2. AI reads the org's context and enters prep mode: "This looks like a Bible translation localization project. Let me help strengthen this brief..."
3. Back-and-forth dialogue — AI asks targeted questions: target population, budget range, partners involved, timeline, measurable outcomes. It pre-fills from org context where possible.
4. AI produces a structured brief — shown as a formatted preview in the chat. User can edit directly or keep chatting to refine.
5. User approves the brief → project status flips to `prospect_research` → worker picks it up automatically

**Design notes:**
- Chat history is preserved — user can return and refine the brief later
- The brief is a living document updated by the conversation
- AI should reference org context naturally ("I see you've partnered with YWAM before — should we mention that partnership in this brief?")

### 5.2 Grant Research Dashboard

**Purpose:** Show the user what the system is working on and surface items needing their attention.

**Components:**

**Project overview bar** — shows current stage, progress metrics (foundations found, dossiers complete, proposals drafted), time elapsed

**Tasks panel** — two sections:
- Blocking tasks (red) — rare. Only for things that truly cannot be worked around (e.g., missing 501(c)(3) letter). Each shows: what's needed, why it matters, action (upload/answer/provide contact)
- Non-blocking tasks (yellow) — common. AI has already drafted something or continued working, but human input would improve the result. Each shows: what's helpful, what the AI already did, action to enhance

**Foundation cards** — grid of prospects showing: name, tier badge, status indicator, alignment score, suggested ask amount. Click to expand into full dossier view.

**Reports list** — completed dossiers and proposals. Each shows:
- Web-rendered view (comfortable reading format, styled markdown)
- Export to DOCX button
- Status (draft / reviewed / approved)
- Last updated timestamp

**Realtime updates** — dashboard updates live via Supabase subscriptions. As agents complete work, new foundation cards appear, progress bars advance, and tasks surface without page refresh.

## 6. Agent Pipeline Architecture

### 6.1 Pipeline Stages

Each stage is a separate `agent_job`. If a stage fails, only that stage is retried. Stages run sequentially per project; within Stage 02, foundation research runs in parallel.

**Stage 01: Prospect Research**
- Input: approved project brief + org context (always-loaded)
- Agent searches the web for matching foundations
- Hits ProPublica API for 990 data on each candidate
- Cross-references existing prospects for this org (dedup by EIN)
- Writes prospect rows to DB as found (dashboard updates live)
- Creates non-blocking tasks if useful ("Upload your most recent annual report — this will strengthen faith-based applications")
- Output: 15–40 prospects with tier assignments and initial data
- On completion: creates Stage 02 jobs (one per selected prospect, parallel)

**Stage 02: Deep Research (parallel per foundation)**
- Input: prospect data + org context (always-loaded + selectively loaded based on foundation type)
- For each prospect, builds the 8-part dossier:
  - 00-BRIEFING: Foundation overview, history, mission, assets, timeline, contact info
  - 01-990-ANALYSIS: Grant ranges, first-time vs repeat patterns, board members, recommended ask
  - 02-KEY-PEOPLE: Decision makers, LinkedIn profiles, warm paths
  - 03-VOCABULARY-AND-FRAMING: Their language ↔ how to frame the client's work
  - 04-APPLICATION-REQUIREMENTS: Form fields, attachments, deadlines, format
  - 05-PROPOSAL-DRAFT: Initial tailored proposal
  - 06-COVER-LETTER: Personalized using key people and specific grants
  - 07-REVIEW-NOTES: Self-critique and compliance checklist
- Each dossier entry is written to DB as completed
- If the agent identifies a need (board endorsement letter, partner reference letter), it drafts it and creates a non-blocking task: "We drafted a board endorsement letter for [Foundation]. Please review and have your board chair sign."
- Blocking only when the system literally cannot proceed (e.g., foundation requires a specific document that doesn't exist and can't be drafted)

**Stage 03: Application Prep**
- Input: completed dossiers + org context
- Documents what each foundation needs (forms, attachments, deadlines, format)
- Builds compliance checklists
- Cross-references uploaded documents against requirements

**Stage 04: Proposal Drafting**
- Input: dossiers + application requirements + org context (with selectively loaded impact stories and partnerships)
- Applies golden rules from the existing system:
  1. Use THEIR language (from vocabulary mapping)
  2. Lead with THE PROBLEM
  3. Personalize with names and specific grants
  4. Size the ask to THEIR patterns
- Refines proposal drafts, cover letters, and LOIs
- Integrates any human task responses that have come in since Stage 02

**Stage 05: Review**
- Agent self-critiques each proposal against checklist:
  - Acronyms defined on first use?
  - Personalization placeholders filled?
  - Foundation's vocabulary used, not ours?
  - Problem leads, not buried?
  - Ask amount realistic for 990 patterns?
  - All claims cited?
  - Signatures/contact info correct?
- Marks proposals as "ready for review"
- User reviews in report viewer, approves or requests changes
- If changes requested → creates a revision job

### 6.2 Context Assembly

Before each AI call, the worker assembles context dynamically:

```
[Always-loaded org context]
  + [Project brief]
  + [Stage-specific instructions (prompt template from DB)]
  + [Relevant prospects and existing dossier content]
  + [Selectively loaded context based on foundation type and stage]
  + [Any human task responses relevant to this foundation]
```

This replaces the "read INIT.md + CONTEXT/ at session start" pattern from the CLI system. Selective loading keeps token usage efficient while maintaining quality.

### 6.3 Prompt Templates

Stage instructions (currently INSTRUCTIONS.md files) become prompt template records in the database. This allows:
- Versioning and A/B testing of prompts without code deploys
- Per-stage tuning of the AI model via OpenRouter
- Admin editing of prompt templates via a future admin UI

For MVP, these are seeded from the existing INSTRUCTIONS.md files during setup.

### 6.4 Agent Philosophy

**Draft everything, block almost nothing.** The agent's default behavior when it encounters a gap:
1. Research the context needed
2. Draft whatever document or response would fill the gap
3. Create a non-blocking task presenting the draft to the user
4. Continue working

Blocking tasks are reserved for hard dependencies where no draft is possible (missing legal documents, required signatures). The bar for blocking should be very high.

## 7. Technical Implementation

### 7.1 Stack
- **Runtime:** Node.js 20+ / TypeScript 5+
- **Frontend:** Next.js 15, React 19, Tailwind CSS 4
- **Database:** Supabase (Postgres 15+, Auth, Storage, Realtime)
- **AI:** OpenRouter API (default model: Claude, globally configurable)
- **Worker:** Standalone Node.js/TypeScript process
- **DOCX generation:** docx npm package or Pandoc
- **Local dev:** docker-compose (Supabase local + worker + Next.js dev server)

### 7.2 Project Structure
```
lightninggrants/
├── apps/
│   └── web/                    # Next.js application
│       ├── app/                # App Router pages
│       │   ├── (auth)/         # Login, signup
│       │   ├── (dashboard)/    # Authenticated app
│       │   │   ├── projects/   # Project list + detail
│       │   │   ├── prep/       # Project Prep Studio (chat)
│       │   │   ├── tasks/      # Task management
│       │   │   └── reports/    # Report viewer
│       │   └── api/            # API routes
│       ├── components/         # Shared UI components
│       └── lib/                # Client utilities, Supabase client
├── packages/
│   ├── db/                     # Supabase migrations, types, seed data
│   ├── agents/                 # Agent logic (shared between worker and API)
│   │   ├── orchestrator.ts     # Job claiming, stage routing
│   │   ├── stages/             # One module per pipeline stage
│   │   ├── tools/              # ProPublica, web search, DOCX generation
│   │   ├── context.ts          # Context assembly logic
│   │   └── prompts/            # Prompt templates (seeded to DB)
│   └── shared/                 # Shared types, constants, utilities
├── worker/                     # Worker process entry point
│   └── index.ts                # Job polling loop
├── docker-compose.yml          # Local dev: Supabase + worker
├── .env.example
└── package.json                # Workspace root (pnpm)
```

### 7.3 Deployment

**Local demo:**
```bash
pnpm install
docker-compose up -d    # Supabase local
pnpm db:migrate         # Run migrations
pnpm db:seed            # Seed prompt templates from existing INSTRUCTIONS.md
pnpm dev                # Next.js dev server + worker process
```

**Production:**
- **Next.js app:** `vercel deploy` (connect GitHub repo, auto-deploys on push)
- **Worker:** `railway up` (Dockerfile, auto-deploys on push)
- **Supabase:** Managed cloud instance (migrate via CLI)
- **Domain:** lightninggrants.ai → Vercel

**Environment variables:**
```
OPENROUTER_API_KEY=
OPENROUTER_MODEL=anthropic/claude-sonnet-4-20250514
SUPABASE_URL=
SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=
PROPUBLICA_BASE_URL=https://projects.propublica.org/nonprofits/api/v2
```

### 7.4 Security
- Supabase Row-Level Security on all tables (org isolation)
- Service role key used only by worker (never exposed to client)
- Anon key + JWT for client-side Supabase access
- File uploads validated by type and size
- OpenRouter API key stored as server-side env var only

## 8. MVP Scope

### In Scope
- Project Prep Studio (chat-based brief development)
- Research pipeline (stages 01–05, running via worker)
- Live dashboard with project status, foundation cards, progress indicators
- Task system (blocking + non-blocking, org/project/prospect level, with AI-drafted documents)
- Report viewer (web-rendered dossiers and proposals)
- DOCX export
- Document upload portal
- Multi-project support per org
- Supabase Auth (email/password)
- OpenRouter integration (global model config)
- Selective context loading
- ProPublica API integration
- Web search integration
- Docker-compose for local dev
- Deployment-ready for Vercel + Railway + Supabase

### Out of Scope (Future)
- Grant Warden human review workflow
- Tier-based project limits (Momentum vs Dominance)
- GrantStation / Attio CRM integrations
- Billing / Stripe integration
- Onboarding interview transcription processing
- Email notifications
- Team roles (admin vs viewer permissions)
- Analytics / reporting on win rates
- Custom branding per org

## 9. Production Roadmap — Post-MVP

### 9.1 Billing & Subscriptions (Stripe)
**What's needed:**
- Stripe account + product/price configuration (two tiers: Momentum $2K/mo, Dominance $3.5K/mo)
- Stripe Checkout for initial signup
- Stripe Customer Portal for self-service billing management
- Webhook handler for subscription events (created, updated, cancelled, payment failed)
- `subscriptions` table: org_id, stripe_customer_id, stripe_subscription_id, plan (momentum/dominance), status, current_period_end
- Middleware to check subscription status before allowing access
- Grace period handling for failed payments (e.g., 7-day grace before restricting access)

**Libraries:** `stripe` npm package, Stripe webhooks via Next.js API route

**Estimated effort:** 2–3 days

### 9.2 Team & Account Management
**What's needed:**
- Invite system: admin invites team members by email, creates pending user linked to org
- Role-based access: admin (full access, billing, settings) vs member (projects, tasks, reports)
- Org settings page: name, logo, billing info
- User profile: name, email, password change
- Future: SSO via Supabase Auth (Google, Microsoft)

**Estimated effort:** 2–3 days

### 9.3 Tier-Based Feature Gating
**What's needed:**
- Read subscription tier from `subscriptions` table
- Gate features: project limits, Grant Warden access, grant volume caps
- UI indicators for tier limits ("Upgrade to Dominance for unlimited projects")
- Upgrade flow → Stripe Checkout with prorated billing

**Estimated effort:** 1–2 days

### 9.4 Grant Warden Human Review Workflow
**What's needed:**
- Internal review queue (separate from client dashboard)
- Assignment system: proposals assigned to professional reviewer
- Inline annotation/commenting on proposals
- Review status: pending_review → in_review → reviewed → approved
- Client sees reviewed version with reviewer comments
- Notification to client when review is complete

**Estimated effort:** 3–5 days

### 9.5 Email Notifications
**What's needed:**
- Transactional email service (Resend or Postmark)
- Notification triggers: new blocking task, proposals ready for review, research complete
- Email templates (branded)
- User preferences: notification frequency (immediate, daily digest, off)

**Estimated effort:** 1–2 days

### 9.6 Onboarding Interview Processing
**What's needed:**
- Accept video/audio upload or meeting transcript (Zoom, Google Meet export)
- AI processes transcript → extracts org context, populates org_context records
- Identifies document gaps → creates initial org-level tasks
- Admin review of extracted context before making it live

**Estimated effort:** 2–3 days

### 9.7 Analytics & Reporting
**What's needed:**
- Dashboard: grants submitted, pending, won, lost, total funding secured
- Win rate tracking per foundation type, ask size, project type
- Pipeline velocity metrics (time per stage)
- ROI calculator: subscription cost vs funding secured

**Estimated effort:** 3–5 days

### 9.8 Additional Tool Integrations
- **GrantStation:** Requires Playwright-based scraping or partnership/API access. Adds breadth to prospect discovery.
- **Attio CRM:** Sync prospects and outcomes to CRM. Requires per-org API key or OAuth.
- **Candid/GuideStar:** Premium nonprofit data. Requires paid API access.
- **Grants.gov:** Federal grants database. Free API.

Each integration: 1–2 days

## 10. Open Questions

1. **Onboarding call tooling:** What platform will your team use for intake calls? This affects transcript format for future automated processing.
2. **DOCX template:** Should exported proposals follow a specific template/formatting, or is clean markdown-to-docx sufficient for MVP?
3. **Admin interface:** For MVP, will your team manage orgs/context via Supabase dashboard directly, or do you need an admin UI?
4. **Search provider:** Which web search API to use — Tavily, Serper, or SerpAPI? (All are cheap, ~$0.005/search)
5. **Demo data:** Should the MVP be seeded with Waha's existing context and research data for demo purposes?
