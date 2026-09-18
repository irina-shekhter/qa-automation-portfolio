import itertools
from datetime import date, timedelta

import httpx
import pytest
from faker import Faker

_date_offset = itertools.count(start=100, step=3)

BASE_URL = "http://localhost:8080/api"


@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL


@pytest.fixture(scope="session")
def http_client(base_url: str) -> httpx.Client:
    print("\n>>> opening client")
    client = httpx.Client(base_url=base_url, timeout=10.0)

    yield client

    print("\n>>> closing client")
    client.close()


@pytest.fixture(scope="session")
def auth_token(http_client: httpx.Client) -> str:
    response = http_client.post(
        "/auth/login", json={"username": "admin", "password": "password"}
    )

    assert response.status_code == 200, f"Login failed: {response.text}"

    return response.json()["token"]


@pytest.fixture
def admin_client(base_url: str, auth_token: str) -> httpx.Client:
    client = httpx.Client(base_url=base_url, timeout=10.0)
    client.cookies.set("token", auth_token)

    yield client

    client.close()


fake = Faker()

ROOM_ID = 1


@pytest.fixture
def booking_payload() -> dict:
    offset = next(_date_offset)

    checkin = date.today() + timedelta(days=offset)
    checkout = checkin + timedelta(days=2)
    return {
        "roomid": ROOM_ID,
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "depositpaid": False,
        "email": fake.email(),
        "phone": fake.numerify("0##########"),
        "bookingdates": {
            "checkin": checkin.isoformat(),
            "checkout": checkout.isoformat(),
        },
    }


@pytest.fixture
def created_booking(admin_client: httpx.Client, booking_payload: dict) -> dict:
    create_response = admin_client.post("/booking", json=booking_payload)

    assert create_response.status_code == 200, (
        f"Setup failed: {create_response.status_code} {create_response.text}"
    )

    booking_id = _find_booking_id(admin_client, booking_payload)

    yield {"bookingid": booking_id, **booking_payload}

    admin_client.delete(f"/booking/{booking_id}")


def _find_booking_id(client: httpx.Client, payload: dict) -> int:
    response = client.get("/booking", params={"roomid": payload["roomid"]})

    for booking in response.json()["bookings"]:
        if (
            booking["firstname"] == payload["firstname"]
            and booking["lastname"] == payload["lastname"]
        ):
            return booking["bookingid"]

    raise AssertionError(
        f"Created booking not found for {payload['firstname']} {payload['lastname']}"
    )
