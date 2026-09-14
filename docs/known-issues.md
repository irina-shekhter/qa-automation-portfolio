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