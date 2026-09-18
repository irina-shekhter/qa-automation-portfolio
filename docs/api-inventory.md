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


## Booking validation rules

Discovered by probing `POST /api/booking`:

| Field | Rule | Response when violated |
|---|---|---|
| `phone` | 11–21 characters | `400` — correct |
| `bookingdates` | `checkout` must follow `checkin` | `500` — see RBP-003 |
| `bookingdates` | must not overlap an existing booking for the same room | `500` — see RBP-002 |

## Endpoints

| Method | Path | Auth | Notes |
|---|---|---|---|
| GET | `/api/room` | no | returns `{"rooms": [...]}` |
| GET | `/api/room/{id}` | no | 500 on unknown id — see RBP-001 |
| GET | `/api/message` | no | returns `{"messages": [...]}` |
| GET | `/api/branding` | no | single object |
| GET | `/api/booking` | yes | **requires** `roomid` query param — returns 400 without it |
| GET | `/api/booking?roomid={id}` | yes | returns `{"bookings": [...]}`; no `email`/`phone` in list items |
| POST | `/api/booking` | yes | returns `200 []` — no body, no `bookingid` |
| DELETE | `/api/booking/{id}` | yes | response code not yet verified |
| POST | `/api/auth/login` | no | returns token |
| GET | `/api/report` | ? | 400 without parameters — to investigate |