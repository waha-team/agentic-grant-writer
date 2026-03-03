# How to Create a PROJECT BRIEF from Attio

Our CRM, Attio, has a list of all the fundable projects which can be listed with this command:

```
curl -sS "https://api.attio.com/v2/objects/projects/records/query" -X POST -H "Authorization: Bearer ${ATTIO_ACCESS_TOKEN}" -H "Content-Type: application/json" -H "Accept: application/json" -d "{}"
```

or searched by project name with 

```
curl -sS "https://api.attio.com/v2/objects/projects/records/query" -X POST -H "Authorization: Bearer ${ATTIO_ACCESS_TOKEN}" -H "Content-Type: application/json" -H "Accept: application/json" -d '{"filter":{"project_name":{"contains":"[SEARCH TERM"}}}'
```

This filters on the project_name attribute using a contains match. You can also use {"text":{"equals":"..."}} for exact match or {"text":{"starts_with":"..."}} for prefix match.



If you are asked to create a project brief based on a project in Attio, do the following:

- [ ] search for and find the project using the search terms above (and, using the `skills/attio` skill to further research applicable entries). 
- [ ] If there are notes in the Attio project, make sure that they are read.

```
# To List Notes 
curl -sS "https://api.attio.com/v2/notes?parent_object=custom-projects&parent_record_id=490daa4e-33e5-4ec5-8986-5d61e82d2761&limit=100" -H "Authorization: Bearer ${ATTIO_ACCESS_TOKEN}"
# To List Comments 
curl -sS "https://api.attio.com/v2/threads?record_id=87ceaebc-8319-4156-be23-d7a1d84de000&object=custom-projects&limit=100" -H "Authorization: Bearer ${ATTIO_ACCESS_TOKEN}"
```

- [ ] Read all the md files in the CONTEXT directory
- [ ] Read the INSTRUCTIONS.md file in this directory

When you've completed that, draft a `00-PROJECT BRIEF.md` based on the Attio project, as described in the instructions, using all the information you have. 

When it's ready, inform the user, so they can review and move the project forward
