import httpx


def test_login_returns_token(http_client: httpx.Client):
    response = http_client.post(
        "/auth/login",
        json={"username": "admin", "password": "password"},
    )

    assert response.status_code == 200

    body = response.json()

    assert "token" in body
    assert isinstance(body["token"], str)
    assert len(body["token"]) > 0


def test_booking_requires_authentication(http_client: httpx.Client):
    response = http_client.get("/booking", params={"roomid": 1})

    assert response.status_code in (401, 403)


def test_booking_accessible_with_valid_token(admin_client: httpx.Client):
    response = admin_client.get("/booking", params={"roomid": 1})

    assert response.status_code == 200
