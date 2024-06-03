# taskmanager
## objective
write a web application for managing tasks

### step 1
python backend
initially store data in memory
I expect the following APIs

GET /tasks
Get all tickets

GET/task/{ticket_id}
Get details of a single ticket

POST /task
payload
{"summary", "description", "reportor", "priority", "custom_fields": {...}}
response
201, {"id": {actual_ticket_id}}
Create a new ticket

PUT /task/{ticket_id}
payload
{"summary", "description", "reportor", "priority", "custom_fields": {...}}
response
202, {"message": "ticket updated"}
Update an existing ticket