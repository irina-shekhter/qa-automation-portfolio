import httpx


def test_get_rooms_returns_ok(http_client: httpx.Client):
    response = http_client.get("/room")
    assert response.status_code == 200


def test_get_rooms_returns_list_of_rooms(http_client: httpx.Client):
    body = http_client.get("/room").json()

    assert "rooms" in body
    assert isinstance(body["rooms"], list)
    assert len(body["rooms"]) > 0


def test_rooms_has_expected_fields(http_client: httpx.Client):
    first_room = http_client.get("/room").json()["rooms"][0]

    assert "roomid" in first_room
    assert "roomName" in first_room
    assert "type" in first_room
    assert "roomPrice" in first_room
