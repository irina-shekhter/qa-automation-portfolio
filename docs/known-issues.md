# Known Issues

Defects found in the system under test (Restful Booker Platform)
during test development.

## RBP-001: Room service returns 500 for non-existent room id

**Service:** rbp-room
**Severity:** medium

**Steps to reproduce:**

GET http://localhost:3001/room/999

**Actual:** `500 Internal Server Error`
**Expected:** `404 Not Found`

**Impact:** Clients cannot distinguish a missing resource from a
server failure. Monitoring will raise false alerts on ordinary
lookups of deleted or mistyped room ids.

**Notes:** Same behaviour for `/room/0`. Non-numeric ids (`abc`)
and negative ids (`-1`) correctly return 404 because Spring fails
to match the route.


## RBP-002: Overlapping booking returns 500 instead of a conflict response

**Service:** rbp-booking
**Severity:** high

**Steps to reproduce:**

1. Authenticate as admin and obtain a token.
2. Create a booking for room 1 with any future date range:

```json
POST /api/booking
{
  "roomid": 1,
  "firstname": "Dupe",
  "lastname": "Test",
  "depositpaid": false,
  "email": "test@test.com",
  "phone": "+972545123456",
  "bookingdates": {"checkin": "2027-07-15", "checkout": "2027-07-17"}
}
```

3. Send the identical request a second time.

**Actual:** first request returns `200`, second returns
`500 Internal Server Error` with an empty body `[]`.

**Expected:** `409 Conflict` (or `400`) with a message identifying
the date conflict.

**Impact:** The client cannot distinguish "these dates are already
booked" from a server failure, so no meaningful message can be shown
to the guest. The empty response body provides no diagnostic
information. Date-collision handling is core booking functionality,
which makes an unhandled exception here higher risk than a similar
failure on a read endpoint.

**Notes:** Phone-number validation was initially suspected but ruled
out — the service correctly returns `400` for phone values outside
the accepted 11–21 character range. The failure is triggered solely
by the overlapping date range.


## RBP-003: Reversed date range returns 500 instead of a validation error

**Service:** rbp-booking
**Severity:** medium

**Steps to reproduce:**

Create a booking where `checkout` precedes `checkin`:

```json
POST /api/booking
{
  "roomid": 1,
  "firstname": "Reverse",
  "lastname": "Dates",
  "depositpaid": false,
  "email": "test@test.com",
  "phone": "+972545123456",
  "bookingdates": {"checkin": "2028-01-31", "checkout": "2028-01-21"}
}
```

**Actual:** `500 Internal Server Error`, empty body `[]`.
**Expected:** `400 Bad Request` identifying the invalid date range.

**Impact:** No validation of date ordering. The request reaches
business logic and throws, meaning the service accepts logically
impossible input as far as the API contract is concerned. Clients
receive no indication of what was wrong.

**Notes:** Date range was chosen far in the future to rule out a
collision with RBP-002.