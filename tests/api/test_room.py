import httpx


def test_get_rooms_returns_ok(rooms_response: httpx.Response):
    assert rooms_response.status_code == 200


def test_get_rooms_returns_list_of_rooms(rooms_response: httpx.Response):
    body = rooms_response.json()

    assert "rooms" in body
    assert isinstance(body["rooms"], list)
    assert len(body["rooms"]) > 0


def test_rooms_has_expected_fields(rooms_response: httpx.Response):
    first_room = rooms_response.json()["rooms"][0]

    assert "roomid" in first_room
    assert "roomName" in first_room
    assert "type" in first_room
    assert "roomPrice" in first_room
