# Lightning Grants MVP Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a demoable, deployment-ready MVP of Lightning Grants — a cloud-based grant research and writing platform.

**Architecture:** Next.js 15 full-stack app + TypeScript background worker + Supabase (Postgres/Auth/Storage/Realtime) + OpenRouter for AI. Monorepo with pnpm workspaces.

**Tech Stack:** TypeScript, Next.js 15, React 19, Tailwind CSS 4, Supabase, OpenRouter API, ProPublica API, `docx` npm package

**Spec:** `docs/superpowers/specs/2026-03-13-lightning-grants-mvp-design.md`

---

## Chunk 1: Project Scaffolding + Database

### Task 1: Initialize Monorepo

**Files:**
- Create: `lightninggrants/package.json`
- Create: `lightninggrants/pnpm-workspace.yaml`
- Create: `lightninggrants/tsconfig.base.json`
- Create: `lightninggrants/.gitignore`
- Create: `lightninggrants/.env.example`
- Create: `lightninggrants/.env` (from grants/.env OPENROUTER_API_KEY)

- [ ] **Step 1: Create project directory and root package.json**

```bash
mkdir -p /home/yeshu/projects/lightninggrants
cd /home/yeshu/projects/lightninggrants
```

```json
// package.json
{
  "name": "lightninggrants",
  "private": true,
  "scripts": {
    "dev": "concurrently \"pnpm --filter web dev\" \"pnpm --filter worker dev\"",
    "dev:web": "pnpm --filter web dev",
    "dev:worker": "pnpm --filter worker dev",
    "build": "pnpm --filter web build",
    "db:migrate": "pnpm --filter db migrate",
    "db:seed": "pnpm --filter db seed",
    "db:reset": "pnpm --filter db reset",
    "db:types": "pnpm --filter db generate-types",
    "typecheck": "tsc --build",
    "lint": "eslint ."
  },
  "devDependencies": {
    "concurrently": "^9.1.2",
    "typescript": "^5.7.3"
  }
}
```

```yaml
# pnpm-workspace.yaml
packages:
  - "apps/*"
  - "packages/*"
  - "worker"
```

- [ ] **Step 2: Create tsconfig.base.json**

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "outDir": "dist",
    "baseUrl": ".",
    "paths": {
      "@lightninggrants/db": ["packages/db/src"],
      "@lightninggrants/agents": ["packages/agents/src"],
      "@lightninggrants/shared": ["packages/shared/src"]
    }
  }
}
```

- [ ] **Step 3: Create .env.example and .env**

```bash
# .env.example
OPENROUTER_API_KEY=
OPENROUTER_MODEL=minimax/minimax-m2.5
NEXT_PUBLIC_SUPABASE_URL=http://127.0.0.1:54321
NEXT_PUBLIC_SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=
PROPUBLICA_BASE_URL=https://projects.propublica.org/nonprofits/api/v2
TAVILY_API_KEY=
```

Copy OPENROUTER_API_KEY from `/home/yeshu/projects/grants/.env`. Set OPENROUTER_MODEL to `minimax/minimax-m2.5`.

- [ ] **Step 4: Create .gitignore**

```
node_modules/
dist/
.next/
.env
.env.local
*.log
.supabase/
```

- [ ] **Step 5: Init git and commit**

```bash
cd /home/yeshu/projects/lightninggrants
git init
git add -A
git commit -m "chore: initialize monorepo with pnpm workspaces"
```

---

### Task 2: Create Shared Types Package

**Files:**
- Create: `lightninggrants/packages/shared/package.json`
- Create: `lightninggrants/packages/shared/tsconfig.json`
- Create: `lightninggrants/packages/shared/src/index.ts`
- Create: `lightninggrants/packages/shared/src/types.ts`
- Create: `lightninggrants/packages/shared/src/constants.ts`
- Create: `lightninggrants/packages/shared/src/enums.ts`

- [ ] **Step 1: Create package.json and tsconfig**

```json
// packages/shared/package.json
{
  "name": "@lightninggrants/shared",
  "version": "0.0.1",
  "private": true,
  "main": "src/index.ts",
  "types": "src/index.ts",
  "scripts": {
    "typecheck": "tsc --noEmit"
  },
  "devDependencies": {
    "typescript": "^5.7.3"
  }
}
```

- [ ] **Step 2: Define all enums from the spec**

```typescript
// packages/shared/src/enums.ts
export const OrgContextType = {
  PROFILE: 'profile',
  IMPACT_STORIES: 'impact_stories',
  FINANCIALS: 'financials',
  PARTNERSHIPS: 'partnerships',
  STYLE_GUIDE: 'style_guide',
  SEARCH_CRITERIA: 'search_criteria',
  STATEMENT_OF_FAITH: 'statement_of_faith',
  BOARD: 'board',
  GOVERNANCE: 'governance',
  PAST_GRANTS: 'past_grants',
  FUNDER_ALIGNMENT: 'funder_alignment',
  OTHER: 'other',
} as const;
export type OrgContextType = typeof OrgContextType[keyof typeof OrgContextType];

export const ProjectStatus = {
  PREP: 'prep',
  PROSPECT_RESEARCH: 'prospect_research',
  DEEP_RESEARCH: 'deep_research',
  APPLICATION_PREP: 'application_prep',
  PROPOSAL_DRAFTING: 'proposal_drafting',
  REVIEW: 'review',
  SUBMITTED: 'submitted',
} as const;
export type ProjectStatus = typeof ProjectStatus[keyof typeof ProjectStatus];

export const ProspectStatus = {
  IDENTIFIED: 'identified',
  RESEARCHING: 'researching',
  COMPLETE: 'complete',
  BLOCKED: 'blocked',
  NOT_APPLICABLE: 'not_applicable',
  INVITE_ONLY: 'invite_only',
  CYCLE_CLOSED: 'cycle_closed',
  SUSPENDED: 'suspended',
} as const;
export type ProspectStatus = typeof ProspectStatus[keyof typeof ProspectStatus];

export const DossierType = {
  BRIEFING: 'briefing',
  ANALYSIS_990: '990_analysis',
  KEY_PEOPLE: 'key_people',
  VOCABULARY_FRAMING: 'vocabulary_framing',
  APPLICATION_REQUIREMENTS: 'application_requirements',
  PROPOSAL_DRAFT: 'proposal_draft',
  COVER_LETTER: 'cover_letter',
  REVIEW_NOTES: 'review_notes',
} as const;
export type DossierType = typeof DossierType[keyof typeof DossierType];

export const DossierStatus = {
  DRAFT: 'draft',
  REVIEWED: 'reviewed',
  APPROVED: 'approved',
} as const;
export type DossierStatus = typeof DossierStatus[keyof typeof DossierStatus];

export const TaskType = {
  BLOCKING: 'blocking',
  NON_BLOCKING: 'non_blocking',
} as const;
export type TaskType = typeof TaskType[keyof typeof TaskType];

export const TaskStatus = {
  PENDING: 'pending',
  IN_PROGRESS: 'in_progress',
  COMPLETED: 'completed',
  DISMISSED: 'dismissed',
} as const;
export type TaskStatus = typeof TaskStatus[keyof typeof TaskStatus];

export const DocType = {
  C501C3: '501c3',
  F990: '990',
  ANNUAL_REPORT: 'annual_report',
  STRATEGIC_PLAN: 'strategic_plan',
  BOARD_RESOLUTION: 'board_resolution',
  OTHER: 'other',
} as const;
export type DocType = typeof DocType[keyof typeof DocType];

export const AgentJobStage = {
  PROSPECT_RESEARCH: 'prospect_research',
  DEEP_RESEARCH: 'deep_research',
  APPLICATION_PREP: 'application_prep',
  PROPOSAL_DRAFTING: 'proposal_drafting',
  REVIEW: 'review',
} as const;
export type AgentJobStage = typeof AgentJobStage[keyof typeof AgentJobStage];

export const AgentJobStatus = {
  QUEUED: 'queued',
  RUNNING: 'running',
  COMPLETED: 'completed',
  FAILED: 'failed',
} as const;
export type AgentJobStatus = typeof AgentJobStatus[keyof typeof AgentJobStatus];

export const ChatMessageType = {
  TEXT: 'text',
  BRIEF_PREVIEW: 'brief_preview',
} as const;
export type ChatMessageType = typeof ChatMessageType[keyof typeof ChatMessageType];

export const ApplicationType = {
  OPEN: 'open',
  LOI: 'loi',
  INVITATION: 'invitation',
} as const;
export type ApplicationType = typeof ApplicationType[keyof typeof ApplicationType];

export const UserRole = {
  ADMIN: 'admin',
  MEMBER: 'member',
} as const;
export type UserRole = typeof UserRole[keyof typeof UserRole];
```

- [ ] **Step 3: Define TypeScript interfaces for all tables**

```typescript
// packages/shared/src/types.ts
import type {
  OrgContextType, ProjectStatus, ProspectStatus,
  DossierType, DossierStatus, TaskType, TaskStatus,
  DocType, AgentJobStage, AgentJobStatus,
  ChatMessageType, ApplicationType, UserRole
} from './enums';

export interface Org {
  id: string;
  name: string;
  ein: string | null;
  mission: string | null;
  settings: Record<string, unknown>;
  created_at: string;
}

export interface OrgContext {
  id: string;
  org_id: string;
  type: OrgContextType;
  label: string | null;
  content: string;
  always_load: boolean;
  created_at: string;
  updated_at: string;
}

export interface Project {
  id: string;
  org_id: string;
  name: string;
  description: string | null;
  brief_content: string | null;
  status: ProjectStatus;
  created_at: string;
  updated_at: string;
}

export interface Prospect {
  id: string;
  project_id: string;
  foundation_name: string;
  ein: string | null;
  website: string | null;
  mission: string | null;
  tier: number | null;
  grant_range_min: number | null;
  grant_range_max: number | null;
  grant_median: number | null;
  suggested_ask: number | null;
  application_type: ApplicationType | null;
  grant_cycle: string | null;
  alignment_score: number | null;
  status: ProspectStatus;
  priority: number;
  created_at: string;
  updated_at: string;
}

export interface Dossier {
  id: string;
  prospect_id: string;
  type: DossierType;
  content: string;
  status: DossierStatus;
  created_at: string;
  updated_at: string;
}

export interface Task {
  id: string;
  org_id: string;
  project_id: string | null;
  prospect_id: string | null;
  type: TaskType;
  title: string;
  description: string;
  status: TaskStatus;
  response: string | null;
  attachments: string[];
  created_at: string;
  updated_at: string;
}

export interface Document {
  id: string;
  org_id: string;
  name: string;
  file_path: string;
  doc_type: DocType;
  extracted_content: string | null;
  created_at: string;
}

export interface AgentJob {
  id: string;
  project_id: string;
  stage: AgentJobStage;
  prospect_id: string | null;
  status: AgentJobStatus;
  error: string | null;
  retry_count: number;
  tokens_input: number | null;
  tokens_output: number | null;
  cost_usd: number | null;
  started_at: string | null;
  completed_at: string | null;
}

export interface ChatMessage {
  id: string;
  project_id: string;
  role: 'user' | 'assistant';
  content: string;
  message_type: ChatMessageType;
  created_at: string;
}

export interface PromptTemplate {
  id: string;
  stage: AgentJobStage;
  name: string;
  content: string;
  version: number;
  active: boolean;
  created_at: string;
  updated_at: string;
}

export interface User {
  id: string;
  org_id: string;
  name: string;
  email: string;
  role: UserRole;
  created_at: string;
}
```

- [ ] **Step 4: Create constants and index**

```typescript
// packages/shared/src/constants.ts
export const MAX_RETRIES = 3;
export const RETRY_DELAYS_MS = [30_000, 120_000, 600_000]; // 30s, 2m, 10m
export const MAX_CONCURRENT_DEEP_RESEARCH = 5;
export const WORKER_POLL_INTERVAL_MS = 5_000;
```

```typescript
// packages/shared/src/index.ts
export * from './types';
export * from './enums';
export * from './constants';
```

- [ ] **Step 5: Commit**

```bash
git add packages/shared/
git commit -m "feat: add shared types package with all enums, interfaces, and constants"
```

---

### Task 3: Create Database Package with Migrations

**Files:**
- Create: `lightninggrants/packages/db/package.json`
- Create: `lightninggrants/packages/db/tsconfig.json`
- Create: `lightninggrants/packages/db/src/index.ts`
- Create: `lightninggrants/packages/db/src/client.ts`
- Create: `lightninggrants/packages/db/supabase/migrations/00001_initial_schema.sql`
- Create: `lightninggrants/packages/db/supabase/seed.sql`
- Create: `lightninggrants/packages/db/supabase/config.toml`

- [ ] **Step 1: Create package.json**

```json
{
  "name": "@lightninggrants/db",
  "version": "0.0.1",
  "private": true,
  "main": "src/index.ts",
  "types": "src/index.ts",
  "scripts": {
    "migrate": "supabase db push",
    "seed": "supabase db reset --seed-only",
    "reset": "supabase db reset",
    "generate-types": "supabase gen types typescript --local > src/database.types.ts",
    "typecheck": "tsc --noEmit"
  },
  "dependencies": {
    "@supabase/supabase-js": "^2.49.4"
  },
  "devDependencies": {
    "typescript": "^5.7.3"
  }
}
```

- [ ] **Step 2: Write the full migration SQL**

Create `supabase/migrations/00001_initial_schema.sql` with all tables, enums, RLS policies, and indexes from the spec. Include:
- All custom enum types
- All 11 tables (orgs, org_context, projects, prospects, dossiers, tasks, documents, agent_jobs, chat_messages, prompt_templates, users)
- Foreign key constraints
- RLS policies (enable RLS, create policies for authenticated users to access their org's data)
- Indexes on frequently queried columns (org_id, project_id, prospect_id, status)
- Updated_at trigger function

See spec Section 4.1 for all column definitions.

- [ ] **Step 3: Write seed.sql with demo data**

Seed data should include:
- One demo org (Waha International, with EIN from existing CONTEXT/OUR_ORGANIZATION.md)
- One demo user
- Core org_context records (profile, style_guide, search_criteria, financials — ported from existing CONTEXT/ files)
- Prompt templates seeded from the existing INSTRUCTIONS.md files (stages 01-05)
- One sample project in `prep` status

- [ ] **Step 4: Create Supabase client wrapper**

```typescript
// packages/db/src/client.ts
import { createClient } from '@supabase/supabase-js';

export function createSupabaseClient(url: string, key: string) {
  return createClient(url, key);
}

export function createSupabaseAdmin(url: string, serviceRoleKey: string) {
  return createClient(url, serviceRoleKey, {
    auth: { autoRefreshToken: false, persistSession: false }
  });
}
```

```typescript
// packages/db/src/index.ts
export { createSupabaseClient, createSupabaseAdmin } from './client';
```

- [ ] **Step 5: Commit**

```bash
git add packages/db/
git commit -m "feat: add database package with migrations, seed data, and Supabase client"
```

---

### Task 4: Set Up Docker Compose for Local Supabase

**Files:**
- Create: `lightninggrants/docker-compose.yml`

- [ ] **Step 1: Create docker-compose.yml**

Use Supabase CLI's local dev setup rather than raw docker-compose. Initialize with `supabase init` in the db package, then configure.

```bash
cd /home/yeshu/projects/lightninggrants/packages/db
npx supabase init
```

- [ ] **Step 2: Start local Supabase and run migrations**

```bash
cd /home/yeshu/projects/lightninggrants/packages/db
npx supabase start
```

This outputs the local Supabase URL, anon key, and service role key. Update `.env` with these values.

- [ ] **Step 3: Run migrations and seed**

```bash
npx supabase db reset  # Runs migrations + seed
```

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "feat: add Supabase local dev setup with docker"
```

---

## Chunk 2: Next.js App Shell + Auth

### Task 5: Scaffold Next.js App

**Files:**
- Create: `lightninggrants/apps/web/` (Next.js 15 app)

- [ ] **Step 1: Create Next.js app**

```bash
cd /home/yeshu/projects/lightninggrants/apps
pnpm create next-app web --typescript --tailwind --eslint --app --src-dir=no --import-alias="@/*" --use-pnpm
```

- [ ] **Step 2: Update package.json to reference workspace packages**

Add dependencies:
```json
{
  "dependencies": {
    "@lightninggrants/shared": "workspace:*",
    "@lightninggrants/db": "workspace:*",
    "@supabase/ssr": "^0.5.2",
    "react-markdown": "^10.1.0",
    "lucide-react": "^0.469.0"
  }
}
```

- [ ] **Step 3: Set up Supabase client helpers for Next.js**

Create `apps/web/lib/supabase/server.ts` (server component client) and `apps/web/lib/supabase/client.ts` (browser client) following Supabase SSR patterns.

- [ ] **Step 4: Commit**

```bash
git add apps/web/
git commit -m "feat: scaffold Next.js 15 app with Tailwind and Supabase client"
```

---

### Task 6: Auth Pages + Middleware

**Files:**
- Create: `apps/web/app/(auth)/login/page.tsx`
- Create: `apps/web/app/(auth)/signup/page.tsx`
- Create: `apps/web/app/(auth)/layout.tsx`
- Create: `apps/web/middleware.ts`
- Create: `apps/web/app/(dashboard)/layout.tsx`

- [ ] **Step 1: Create auth layout (centered card)**

Simple centered layout for login/signup pages.

- [ ] **Step 2: Create login page**

Email + password form, calls Supabase `signInWithPassword`. Redirects to `/projects` on success.

- [ ] **Step 3: Create signup page**

Email + password + name + org name form. Creates auth user, then creates org + user records via API route.

- [ ] **Step 4: Create signup API route**

`apps/web/app/api/auth/signup/route.ts` — creates org and user records after Supabase auth signup.

- [ ] **Step 5: Create middleware for auth protection**

```typescript
// middleware.ts
// Protect all /dashboard routes — redirect to /login if not authenticated
// Allow /login, /signup, /api/auth/* without auth
```

- [ ] **Step 6: Create dashboard layout**

Sidebar with navigation: Projects, Tasks, Documents. Top bar with org name and logout.

- [ ] **Step 7: Commit**

```bash
git add apps/web/
git commit -m "feat: add auth pages, middleware, and dashboard layout"
```

---

## Chunk 3: Agent Infrastructure

### Task 7: Create Agents Package — OpenRouter Client

**Files:**
- Create: `lightninggrants/packages/agents/package.json`
- Create: `lightninggrants/packages/agents/tsconfig.json`
- Create: `lightninggrants/packages/agents/src/index.ts`
- Create: `lightninggrants/packages/agents/src/llm.ts`
- Create: `lightninggrants/packages/agents/src/llm.test.ts`

- [ ] **Step 1: Create package.json**

```json
{
  "name": "@lightninggrants/agents",
  "version": "0.0.1",
  "private": true,
  "main": "src/index.ts",
  "types": "src/index.ts",
  "scripts": {
    "test": "vitest run",
    "test:watch": "vitest",
    "typecheck": "tsc --noEmit"
  },
  "dependencies": {
    "@lightninggrants/shared": "workspace:*",
    "@lightninggrants/db": "workspace:*"
  },
  "devDependencies": {
    "vitest": "^3.1.1",
    "typescript": "^5.7.3"
  }
}
```

- [ ] **Step 2: Write OpenRouter client**

```typescript
// packages/agents/src/llm.ts
// Wraps OpenRouter's chat completions API (OpenAI-compatible)
// - chat(messages, options) -> { content, usage }
// - Tracks token usage for cost logging
// - Model from env OPENROUTER_MODEL
```

- [ ] **Step 3: Write test for LLM client**

Test that the client formats requests correctly, handles responses, and extracts token usage. Use mocked fetch.

- [ ] **Step 4: Commit**

```bash
git add packages/agents/
git commit -m "feat: add OpenRouter LLM client with token tracking"
```

---

### Task 8: Agent Tools — ProPublica + Search

**Files:**
- Create: `packages/agents/src/tools/propublica.ts`
- Create: `packages/agents/src/tools/propublica.test.ts`
- Create: `packages/agents/src/tools/search.ts`
- Create: `packages/agents/src/tools/search.test.ts`

- [ ] **Step 1: Write ProPublica API client**

```typescript
// packages/agents/src/tools/propublica.ts
// - searchOrganizations(query) -> results with EIN, name, assets
// - getOrganization(ein) -> full org details
// - getFilings(ein) -> 990 filings with grant data
```

Uses the free ProPublica Nonprofit Explorer API at `https://projects.propublica.org/nonprofits/api/v2`.

- [ ] **Step 2: Write tests for ProPublica client**

Mock fetch, test parsing of API responses.

- [ ] **Step 3: Write pluggable search interface + mock provider**

```typescript
// packages/agents/src/tools/search.ts
export interface SearchProvider {
  search(query: string, options?: { maxResults?: number }): Promise<SearchResult[]>;
}
export interface SearchResult {
  title: string;
  url: string;
  snippet: string;
}

// MockSearchProvider for demo — returns canned results
// TavilySearchProvider for production (when TAVILY_API_KEY is set)
```

- [ ] **Step 4: Write tests for search providers**

- [ ] **Step 5: Commit**

```bash
git add packages/agents/src/tools/
git commit -m "feat: add ProPublica API client and pluggable search provider"
```

---

### Task 9: Context Assembly

**Files:**
- Create: `packages/agents/src/context.ts`
- Create: `packages/agents/src/context.test.ts`

- [ ] **Step 1: Write context assembly logic**

```typescript
// packages/agents/src/context.ts
// assembleContext(supabase, orgId, projectId, stage, prospectId?) -> string
// 1. Load always_load=true org_context records
// 2. Load project brief
// 3. Load active prompt template for stage
// 4. If prospectId: load prospect data + existing dossier content
// 5. Selectively load additional context based on stage/foundation type
// 6. Load relevant completed task responses
// Returns assembled context string for LLM prompt
```

- [ ] **Step 2: Write tests**

Test that context assembly correctly filters always_load vs selective, includes project brief, includes stage prompt template.

- [ ] **Step 3: Commit**

```bash
git add packages/agents/src/context.ts packages/agents/src/context.test.ts
git commit -m "feat: add context assembly with selective loading"
```

---

## Chunk 4: Worker + Orchestrator

### Task 10: Create Worker Package

**Files:**
- Create: `lightninggrants/worker/package.json`
- Create: `lightninggrants/worker/tsconfig.json`
- Create: `lightninggrants/worker/src/index.ts`
- Create: `lightninggrants/worker/src/orchestrator.ts`
- Create: `lightninggrants/worker/src/orchestrator.test.ts`
- Create: `lightninggrants/worker/Dockerfile`

- [ ] **Step 1: Create worker package.json**

```json
{
  "name": "worker",
  "version": "0.0.1",
  "private": true,
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "start": "tsx src/index.ts",
    "test": "vitest run"
  },
  "dependencies": {
    "@lightninggrants/shared": "workspace:*",
    "@lightninggrants/db": "workspace:*",
    "@lightninggrants/agents": "workspace:*",
    "tsx": "^4.19.4"
  },
  "devDependencies": {
    "vitest": "^3.1.1",
    "typescript": "^5.7.3"
  }
}
```

- [ ] **Step 2: Write orchestrator**

```typescript
// worker/src/orchestrator.ts
// - claimJob(supabase) -> AgentJob | null (using FOR UPDATE SKIP LOCKED)
// - routeJob(job) -> calls appropriate stage handler
// - updateJobStatus(supabase, jobId, status, result?)
// - handleFailure(supabase, job, error) -> retry or mark failed
```

- [ ] **Step 3: Write worker main loop**

```typescript
// worker/src/index.ts
// Poll loop: every WORKER_POLL_INTERVAL_MS
// 1. Claim a job
// 2. Route to stage handler
// 3. On success: mark completed, advance project status
// 4. On failure: retry with backoff or mark failed
```

- [ ] **Step 4: Write Dockerfile**

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY . .
RUN corepack enable && pnpm install --frozen-lockfile
CMD ["pnpm", "run", "start", "--filter", "worker"]
```

- [ ] **Step 5: Write tests for orchestrator**

Test job claiming, routing, failure handling, retry logic.

- [ ] **Step 6: Commit**

```bash
git add worker/
git commit -m "feat: add worker with orchestrator, job polling, and retry logic"
```

---

### Task 11: Pipeline Stage Handlers

**Files:**
- Create: `packages/agents/src/stages/prospect-research.ts`
- Create: `packages/agents/src/stages/deep-research.ts`
- Create: `packages/agents/src/stages/application-prep.ts`
- Create: `packages/agents/src/stages/proposal-drafting.ts`
- Create: `packages/agents/src/stages/review.ts`
- Create: `packages/agents/src/stages/index.ts`

- [ ] **Step 1: Write Stage 01 — Prospect Research**

```typescript
// packages/agents/src/stages/prospect-research.ts
// Input: project brief + org context
// 1. Assemble context
// 2. Call LLM to generate search queries
// 3. Execute web searches
// 4. For each result, call ProPublica API for 990 data
// 5. Call LLM to score alignment and assign tiers
// 6. Write prospect rows to DB
// 7. Create non-blocking tasks if needed
// 8. On completion: create Stage 02 jobs for selected prospects
// 9. Update project status to deep_research
```

- [ ] **Step 2: Write Stage 02 — Deep Research**

```typescript
// packages/agents/src/stages/deep-research.ts
// Input: single prospect + org context
// Concurrency managed by orchestrator (max 5 via semaphore)
// 1. Assemble context for this specific prospect
// 2. For each dossier part (00-04):
//    a. Call LLM with part-specific prompt
//    b. Write dossier row to DB
// 3. Create non-blocking tasks (draft documents, request warm intros)
// 4. Update prospect status to complete
// 5. Check if all Stage 02 jobs for this project are complete
//    If so: create Stage 03 job, update project status
```

- [ ] **Step 3: Write Stage 03 — Application Prep**

```typescript
// packages/agents/src/stages/application-prep.ts
// 1. Load all prospects + their application_requirements dossiers
// 2. Load org's uploaded documents
// 3. For each prospect: cross-reference requirements vs documents
// 4. Update application_requirements dossier with compliance status
// 5. Create tasks for missing documents
// 6. Create Stage 04 jobs, update project status
```

- [ ] **Step 4: Write Stage 04 — Proposal Drafting**

```typescript
// packages/agents/src/stages/proposal-drafting.ts
// Input: prospect + all dossier parts 00-04
// 1. Assemble full context (always-load + selective + dossiers)
// 2. Call LLM to draft proposal (05-PROPOSAL-DRAFT)
// 3. Call LLM to draft cover letter (06-COVER-LETTER)
// 4. Call LLM for review notes (07-REVIEW-NOTES)
// 5. Write/update dossier rows
// 6. Check if all Stage 04 jobs complete → create Stage 05 job
```

- [ ] **Step 5: Write Stage 05 — Review**

```typescript
// packages/agents/src/stages/review.ts
// 1. Load all proposals for the project
// 2. For each: run self-critique checklist via LLM
// 3. Update review_notes dossier with critique results
// 4. Set dossier status to 'reviewed'
// 5. Update project status to 'review'
// (User reviews manually from here)
```

- [ ] **Step 6: Create stage index**

```typescript
// packages/agents/src/stages/index.ts
export { runProspectResearch } from './prospect-research';
export { runDeepResearch } from './deep-research';
export { runApplicationPrep } from './application-prep';
export { runProposalDrafting } from './proposal-drafting';
export { runReview } from './review';
```

- [ ] **Step 7: Commit**

```bash
git add packages/agents/src/stages/
git commit -m "feat: implement all 5 pipeline stage handlers"
```

---

## Chunk 5: Project Prep Studio (Chat UI)

### Task 12: Project CRUD + API Routes

**Files:**
- Create: `apps/web/app/api/projects/route.ts` (list + create)
- Create: `apps/web/app/api/projects/[id]/route.ts` (get + update)
- Create: `apps/web/app/api/projects/[id]/approve/route.ts` (approve brief → start pipeline)
- Create: `apps/web/app/api/projects/[id]/chat/route.ts` (send message + stream response)

- [ ] **Step 1: Create project list + create API**

GET returns all projects for user's org. POST creates a new project with status = prep.

- [ ] **Step 2: Create project detail + update API**

GET returns project by ID (with RLS check). PATCH updates brief_content.

- [ ] **Step 3: Create approve API**

POST sets project status to `prospect_research` and creates the first `agent_job` with stage = `prospect_research`.

- [ ] **Step 4: Create chat API with streaming**

POST accepts a message, loads project context, calls OpenRouter (streaming), saves both user and assistant messages to chat_messages. If the assistant generates a brief_preview, also updates projects.brief_content.

- [ ] **Step 5: Commit**

```bash
git add apps/web/app/api/projects/
git commit -m "feat: add project CRUD and chat API routes"
```

---

### Task 13: Project Prep Studio UI

**Files:**
- Create: `apps/web/app/(dashboard)/projects/page.tsx` (project list)
- Create: `apps/web/app/(dashboard)/projects/new/page.tsx` (create project)
- Create: `apps/web/app/(dashboard)/prep/[id]/page.tsx` (chat studio)
- Create: `apps/web/components/chat/chat-interface.tsx`
- Create: `apps/web/components/chat/message-bubble.tsx`
- Create: `apps/web/components/chat/brief-preview.tsx`
- Create: `apps/web/components/projects/project-card.tsx`

- [ ] **Step 1: Build project list page**

Grid of project cards showing name, status badge, date. "New Project" button.

- [ ] **Step 2: Build create project page**

Simple form: project name + initial description. Creates project via API, redirects to prep studio.

- [ ] **Step 3: Build chat interface component**

- Message list with auto-scroll
- Input bar at bottom with send button
- Streaming response display
- Handles both `text` and `brief_preview` message types

- [ ] **Step 4: Build brief preview component**

Rendered markdown preview of the brief. "Edit Brief" button opens an editor for `brief_content`. "Approve & Start Research" button calls the approve API.

- [ ] **Step 5: Build prep studio page**

Two-panel layout: chat on the left, brief preview on the right. Brief preview updates live as the AI refines it.

- [ ] **Step 6: Commit**

```bash
git add apps/web/app/(dashboard)/projects/ apps/web/app/(dashboard)/prep/ apps/web/components/
git commit -m "feat: add Project Prep Studio with chat interface and brief editor"
```

---

## Chunk 6: Dashboard + Reports

### Task 14: Grant Research Dashboard

**Files:**
- Create: `apps/web/app/(dashboard)/projects/[id]/page.tsx` (project dashboard)
- Create: `apps/web/components/dashboard/project-overview.tsx`
- Create: `apps/web/components/dashboard/foundation-card.tsx`
- Create: `apps/web/components/dashboard/progress-bar.tsx`
- Create: `apps/web/app/api/projects/[id]/prospects/route.ts`
- Create: `apps/web/app/api/projects/[id]/dossiers/route.ts`

- [ ] **Step 1: Create prospect + dossier API routes**

GET prospects for a project. GET dossiers for a prospect.

- [ ] **Step 2: Build project overview bar**

Shows: current stage name, progress metrics (X foundations found, Y dossiers complete, Z proposals drafted), time since project started.

- [ ] **Step 3: Build foundation cards grid**

Each card shows: foundation name, tier badge (1/2/3), status indicator (color-coded), alignment score bar, suggested ask amount. Clickable to expand.

- [ ] **Step 4: Build project dashboard page**

Combines overview bar + foundation cards grid + tasks panel (Task 16) + reports list (Task 15).

- [ ] **Step 5: Add Supabase Realtime subscription**

Subscribe to changes on `prospects`, `dossiers`, `tasks`, `agent_jobs` filtered by project_id. Update UI live when agents produce results.

- [ ] **Step 6: Commit**

```bash
git add apps/web/app/(dashboard)/projects/[id]/ apps/web/components/dashboard/ apps/web/app/api/projects/
git commit -m "feat: add Grant Research Dashboard with live updates"
```

---

### Task 15: Report Viewer + DOCX Export

**Files:**
- Create: `apps/web/app/(dashboard)/reports/[prospectId]/page.tsx`
- Create: `apps/web/components/reports/dossier-viewer.tsx`
- Create: `apps/web/components/reports/report-nav.tsx`
- Create: `apps/web/app/api/reports/[prospectId]/export/route.ts`
- Create: `packages/agents/src/tools/docx-export.ts`
- Create: `packages/agents/src/tools/docx-export.test.ts`

- [ ] **Step 1: Write DOCX export utility**

```typescript
// packages/agents/src/tools/docx-export.ts
// Takes dossier content (markdown) and converts to DOCX
// Uses 'docx' npm package
// Returns Buffer for download
```

- [ ] **Step 2: Write test for DOCX export**

- [ ] **Step 3: Create export API route**

GET `/api/reports/[prospectId]/export` — generates DOCX from all dossier parts for a prospect, returns as download.

- [ ] **Step 4: Build dossier viewer component**

Renders markdown content in a comfortable reading format. Tabs for each dossier part (Briefing, 990 Analysis, Key People, etc.). Status badge (draft/reviewed/approved). Approve and Request Changes buttons.

- [ ] **Step 5: Build report viewer page**

Dossier viewer + export button + navigation between prospects.

- [ ] **Step 6: Create request-changes API**

POST `/api/reports/[prospectId]/revise` — accepts feedback text, creates a new agent_job with stage=proposal_drafting for this prospect, stores feedback in a task.

- [ ] **Step 7: Commit**

```bash
git add apps/web/app/(dashboard)/reports/ apps/web/components/reports/ apps/web/app/api/reports/ packages/agents/src/tools/docx-export.*
git commit -m "feat: add report viewer with DOCX export and revision requests"
```

---

## Chunk 7: Tasks + Documents

### Task 16: Task System UI

**Files:**
- Create: `apps/web/app/(dashboard)/tasks/page.tsx`
- Create: `apps/web/components/tasks/task-card.tsx`
- Create: `apps/web/components/tasks/task-response-form.tsx`
- Create: `apps/web/app/api/tasks/route.ts`
- Create: `apps/web/app/api/tasks/[id]/route.ts`

- [ ] **Step 1: Create task API routes**

GET `/api/tasks` — list tasks for user's org (filterable by project, status, type).
PATCH `/api/tasks/[id]` — update task (add response, change status, add attachments).

- [ ] **Step 2: Build task card component**

Shows: title, description, type badge (blocking=red, non_blocking=yellow), linked project/prospect name. Action buttons: respond (text input), upload attachment, dismiss.

- [ ] **Step 3: Build task response form**

Text area for response + file upload for attachments. Submit updates the task via API.

- [ ] **Step 4: Build tasks page**

Two sections: Blocking (top, red border) and Non-blocking (below, yellow border). Shows count badges.

- [ ] **Step 5: Add tasks panel to project dashboard**

Embed a filtered view of tasks (for this project) in the project dashboard page.

- [ ] **Step 6: Commit**

```bash
git add apps/web/app/(dashboard)/tasks/ apps/web/components/tasks/ apps/web/app/api/tasks/
git commit -m "feat: add task management UI with response and attachment support"
```

---

### Task 17: Document Upload Portal

**Files:**
- Create: `apps/web/app/(dashboard)/documents/page.tsx`
- Create: `apps/web/components/documents/upload-form.tsx`
- Create: `apps/web/components/documents/document-list.tsx`
- Create: `apps/web/app/api/documents/route.ts`
- Create: `apps/web/app/api/documents/[id]/route.ts`

- [ ] **Step 1: Create document API routes**

GET `/api/documents` — list documents for user's org.
POST `/api/documents` — upload file to Supabase Storage, create document record, optionally trigger AI extraction of content.
DELETE `/api/documents/[id]` — remove document.

- [ ] **Step 2: Build upload form**

Drag-and-drop file upload with doc_type selector (501c3, 990, annual report, etc.). Progress indicator. Max file size validation.

- [ ] **Step 3: Build document list**

Table showing: name, type, upload date, extracted content preview. Download and delete actions.

- [ ] **Step 4: Build documents page**

Upload form + document list.

- [ ] **Step 5: Commit**

```bash
git add apps/web/app/(dashboard)/documents/ apps/web/components/documents/ apps/web/app/api/documents/
git commit -m "feat: add document upload portal with Supabase Storage"
```

---

## Chunk 8: Integration + Polish

### Task 18: Seed Prompt Templates from Existing Pipeline

**Files:**
- Create: `packages/db/src/seed-prompts.ts`

- [ ] **Step 1: Write script to read existing INSTRUCTIONS.md files and generate seed SQL**

Read from `/home/yeshu/projects/grants/01-prospect-research/INSTRUCTIONS.md` through `05-review/INSTRUCTIONS.md`. Transform each into a prompt_templates insert with appropriate stage enum value.

- [ ] **Step 2: Include CONTEXT files for demo org seed**

Read key files from `/home/yeshu/projects/grants/CONTEXT/` (OUR_ORGANIZATION.md, STYLE_GUIDE.md, SEARCH_CRITERIA.md, FINANCIALS_SUMMARY.md, IMPACT_DATA.md, FUNDER_ALIGNMENT_GUIDE.md) and generate org_context inserts.

- [ ] **Step 3: Update seed.sql with generated data**

- [ ] **Step 4: Commit**

```bash
git add packages/db/
git commit -m "feat: seed prompt templates and demo org context from existing pipeline"
```

---

### Task 19: End-to-End Integration Test

**Files:**
- Create: `lightninggrants/e2e/smoke-test.ts`

- [ ] **Step 1: Write smoke test script**

```typescript
// e2e/smoke-test.ts
// 1. Create org + user via API
// 2. Create project via API
// 3. Send chat messages to prep studio
// 4. Approve brief
// 5. Verify agent_job created with status=queued
// 6. Start worker, verify it claims the job
// 7. Verify prospects created in DB
// 8. Verify dossiers created
// 9. Export DOCX and verify it's valid
```

- [ ] **Step 2: Run smoke test**

```bash
pnpm exec tsx e2e/smoke-test.ts
```

- [ ] **Step 3: Fix any integration issues**

- [ ] **Step 4: Commit**

```bash
git add e2e/
git commit -m "test: add end-to-end smoke test for full pipeline"
```

---

### Task 20: Dev Experience + Final Polish

- [ ] **Step 1: Create root dev script that starts everything**

Update root package.json `dev` script to start Next.js + worker + verify Supabase is running.

- [ ] **Step 2: Create README.md with setup instructions**

Quick start: prerequisites, env setup, `pnpm install`, `supabase start`, `pnpm db:reset`, `pnpm dev`.

- [ ] **Step 3: Add Vercel configuration**

Create `apps/web/vercel.json` if needed. Ensure the app builds for Vercel deployment.

- [ ] **Step 4: Add Railway Dockerfile for worker**

Verify worker Dockerfile works.

- [ ] **Step 5: Final commit**

```bash
git add -A
git commit -m "chore: add dev scripts, README, and deployment configs"
```

---

## Task Dependency Graph

```
Task 1 (monorepo) → Task 2 (shared types) → Task 3 (database) → Task 4 (docker/supabase)
                                                    ↓
                    Task 5 (Next.js) ←──────────────┘
                         ↓
                    Task 6 (auth)
                         ↓
        ┌────────────────┼─────────────────┐
   Task 7 (LLM)    Task 12 (APIs)    Task 16 (tasks UI)
        ↓                ↓                 ↓
   Task 8 (tools)   Task 13 (prep UI) Task 17 (docs UI)
        ↓
   Task 9 (context)
        ↓
   Task 10 (worker)  Task 14 (dashboard)
        ↓                ↓
   Task 11 (stages)  Task 15 (reports)
        ↓                ↓
   Task 18 (seed)────────┘
        ↓
   Task 19 (e2e test)
        ↓
   Task 20 (polish)
```

**Parallelization opportunities:**
- Tasks 7-9 (agent infra) can run in parallel with Tasks 12-13 (project UI) and Tasks 16-17 (tasks/docs UI) — all depend only on Tasks 1-6
- Task 14 (dashboard) and Task 10 (worker) can start once their dependencies complete
- Task 18 (seed) depends on both the DB package and having the stage handlers done
- Task 19-20 are sequential at the end

## Notes for Josh

- **OPENROUTER_MODEL** set to `minimax/minimax-m2.5` per your request
- **Search provider** uses real Tavily API (key available in environment)
- **Demo seed data** uses Waha's actual CONTEXT files so the demo feels real
- **Tavily API key** available and configured for real web search
