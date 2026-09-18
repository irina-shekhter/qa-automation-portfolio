import httpx


def test_create_booking_appears_in_list(
    admin_client: httpx.Client, created_booking: dict
):
    response = admin_client.get(
        "/booking", params={"roomid": created_booking["roomid"]}
    )

    assert response.status_code == 200

    booking_ids = [b["bookingid"] for b in response.json()["bookings"]]

    assert created_booking["bookingid"] in booking_ids
