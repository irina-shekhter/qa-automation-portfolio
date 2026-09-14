import httpx
import pytest


@pytest.mark.parametrize(
    "room_id",
    ["abc", "-1"],
    ids=["non-numeric", "negative"],
)
def test_invalid_room_id_returns_not_found(http_client: httpx.Client, room_id: str):
    response = http_client.get(f"/room/{room_id}")

    assert response.status_code == 404


@pytest.mark.xfail(
    reason="RBP-001: returns 500 Internal Server Error instead of 404",
    strict=True,
)
@pytest.mark.parametrize("room_id", [999,0], ids=["unknown-id", "zero-id"])
def test_unknown_room_returns_not_found(http_client: httpx.Client, room_id: int):
    response = http_client.get(f"/room/{room_id}")

    assert response.status_code == 404