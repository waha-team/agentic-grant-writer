---
name: grantstation-search
description: Search GrantStation's grant database for funding opportunities. Use when researching grants for projects - supports searching by geographic focus (countries), areas of interest (religious, education, health, etc.), and retrieving full details of specific grants. Requires cookies for authentication.
---

# GrantStation Search Skill

This skill enables searching GrantStation's grant database for funding opportunities.

## Quick Reference

```bash
cd grantstation-skill

# Search grants
node scripts/search.js search "Egypt,Morocco" international

# Get full details of a specific grant
node scripts/search.js details "https://grantstation.com/grantmakers/embassy-japan-egypt"

# See all filter options
node scripts/search.js options
```

## Commands

### 1. Search for Grants

```bash
node scripts/search.js search "COUNTRY1,COUNTRY2" <search_type>
```

**Parameters:**
- `COUNTRY1,COUNTRY2` - Comma-separated country names
- `search_type` - `international`, `us`, or `canadian` (default: `international`)

**Examples:**

```bash
# North Africa grants
node scripts/search.js search "Egypt,Algeria,Libya,Tunisia,Morocco" international

# Single country
node scripts/search.js search "Egypt" international

# US grants by state
node scripts/search.js search "California,Texas" us
```

### 2. Get Grant Details

```bash
node scripts/search.js details "GRANT_URL"
```

**Examples:**

```bash
# Full details of a specific grant
node scripts/search.js details "https://grantstation.com/grantmakers/embassy-japan-egypt"
```

The output includes:
- **Description** - What the funder does
- **Opportunity Information** - Deadlines, geographic scope
- **Areas of Interest** - What types of projects they fund
- **Types of Support** - Capital funds, project support, etc.
- **Eligibility** - Who can apply
- **Contact Information** - Email, phone, website

### 3. View All Search Options

```bash
node scripts/search.js options
```

Shows all available:
- Geographic filters (continents, countries, regions)
- Areas of interest (Arts, Education, Health, Religion, etc.)
- Types of support
- Application deadlines

## Search Types

| Type | URL | Description |
|------|-----|-------------|
| `international` | `/search/international-charitable` | International charitable funders |
| `us` | `/search/us-funders` | US charitable foundations |
| `canadian` | `/search/canadian-charitable` | Canadian charitable funders |

## Key Areas of Interest

### Religion & Faith-Based
- `Religion & Ethics: General`
- `Christian`
- `Islamic/Muslim`
- `Jewish`
- `Interfaith`

### Other Major Categories
- Arts, Culture & Humanities
- Education (K-12, Higher Education, Vocational)
- Health/Wellness (Healthcare Delivery, Mental Health, Disease Research)
- Community & Economic Development
- Environment & Animals
- Social Services (Youth, Seniors, Low-Income)

## Geographic Options

### North Africa
Egypt, Algeria, Libya, Tunisia, Morocco

### Middle East
Israel, Jordan, Lebanon, Palestinian Territories, Syria, Yemen, Iraq, Iran, Saudi Arabia, UAE

### Sub-Saharan Africa
Kenya, Nigeria, South Africa, Ghana, Ethiopia, Tanzania

### Europe
United Kingdom, Germany, France, Belgium, Netherlands

## Important Notes

1. **Authentication**: Cookies are pre-loaded from `cookies.txt`. If authentication fails, re-export cookies from your browser.

2. **Membership**: Full profile details require an active GrantStation membership. Basic search results are available to members.

3. **Cookie Expiration**: Cookies may expire. Re-export if you get redirected to login.

4. **URLs from Search**: Grant URLs from search results follow the pattern:
   - `https://grantstation.com/grantmakers/[funder-name]`

## Full Example Workflow

```bash
# 1. Find grants for Egypt in religious/mission work
node scripts/search.js search "Egypt" international

# 2. Get full details of a promising grant
node scripts/search.js details "https://grantstation.com/grantmakers/embassy-japan-egypt"
```

The details output includes all available information about the grant funder.
