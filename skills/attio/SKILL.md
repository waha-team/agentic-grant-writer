---
name: attio
description: Interact with Attio CRM (Waha workspace) to manage contacts, companies, deals, notes, tasks, lists, custom objects, and SDR workflows (prospecting, pipeline management, activity logging) via the Attio API; also usable for Josh’s future personal Attio CRM.
---

# Attio CRM

## Auth
- Requires env var: `ATTIO_ACCESS_TOKEN` (Bearer token)
- Base URL: `https://api.attio.com/v2`

## Default workflow (avoid duplicates)
1) Identify target: **object + record** (people/companies/deals/custom object) or **list entry**.
2) **Search first**:
   - Global: `POST /objects/records/search`
   - Or object-specific query: `POST /objects/{object}/records/query`
3) Then **create/update** the record.
4) Log activity (note/task) as needed.
5) Confirm back: what changed + record_id(s).

## Common endpoints (quick map)
- List objects (discover custom objects): `GET /objects`
- Global search: `POST /objects/records/search`
- Query records: `POST /objects/{object}/records/query`
- Create record: `POST /objects/{object}/records`
- Update record: `PATCH /objects/{object}/records/{record_id}`
- Notes: `POST /notes`
- Tasks: `POST /tasks`
- Lists: `GET /lists`, `POST /lists/{list_id}/entries/query`, `POST /lists/{list_id}/entries`, `PATCH /lists/{list_id}/entries/{entry_id}`

## Request templates

### Curl (single-line only — multi-line `\` continuations break in this environment)
```bash
curl -sS "https://api.attio.com/v2/objects" -H "Authorization: Bearer ${ATTIO_ACCESS_TOKEN}" -H "Content-Type: application/json"
```

### Python (preferred — handles JSON parsing and POST bodies cleanly)
```python
python3 -c "
import urllib.request, json, os
token = os.environ['ATTIO_ACCESS_TOKEN']
url = 'https://api.attio.com/v2/objects'
# For POST requests, add: data=json.dumps(payload).encode()
req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
resp = urllib.request.urlopen(req)
data = json.loads(resp.read())
print(json.dumps(data, indent=2))
"
```

## Reference
For concrete request bodies (people/companies/deals/search), read:
- `references/attio-api.md`

## Guardrails
- Never print or log tokens.
- Prefer search/query before create.
- If unsure about an attribute’s schema, list objects / fetch schemas (or ask Josh) before writing.
