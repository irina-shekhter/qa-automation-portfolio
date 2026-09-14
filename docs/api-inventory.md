# API Inventory

Restful Booker Platform endpoints discovered through browser DevTools
and direct service probing.

## Entry points

The platform can be accessed two ways, and they behave differently.

| Entry point | Base | Trailing slash |
|---|---|---|
| Reverse proxy (frontend) | `http://localhost:8080/api` | must be **omitted** — `/api/room/` returns 308 |
| Direct to service | `http://localhost:<port>` | **required** — `/room` returns 302 |

Tests target the proxy, since that is how a real client reaches
the platform.

## Services

| Service | Direct port | Proxy path |
|---|---|---|
| booking | 3000 | `/api/booking` |
| room | 3001 | `/api/room` |
| branding | 3002 | `/api/branding` |
| auth | 3004 | `/api/auth` |
| report | 3005 | `/api/report` |
| message | 3006 | `/api/message` |

## Authentication

`POST /api/auth/login`

Request:
```json
{"username": "admin", "password": "password"}
```

Response `200`:
```json
{"token": "e3AT2T5nzVBFlkG1"}
```

No `Set-Cookie` header is returned. The frontend stores the token
itself and sends it as a cookie on subsequent requests:


## Endpoints

| Method | Path | Auth | Notes |
|---|---|---|---|
| GET | `/api/room` | no | returns `{"rooms": [...]}` |
| GET | `/api/room/{id}` | no | 500 on unknown id — see RBP-001 |
| GET | `/api/message` | no | returns `{"messages": [...]}` |
| GET | `/api/branding` | no | single object |
| GET | `/api/booking` | yes | 403 without token |
| GET | `/api/booking?roomid={id}` | yes | filter by room |
| POST | `/api/auth/login` | no | returns token |
| GET | `/api/report` | ? | 400 without parameters — to investigate |