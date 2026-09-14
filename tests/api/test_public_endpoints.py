import httpx
import pytest

PUBLIC_COLLECTION = [
    ("/room", "rooms"),
    ("/message", "messages"),
]

@pytest.mark.parametrize(("url", "collection_key"), PUBLIC_COLLECTION, ids=["room", "message"])
def test_public_collection_returns_ok(
        http_client:httpx.Client, url: str, collection_key: str
):
    response = http_client.get(url)

    assert response.status_code == 200


@pytest.mark.parametrize(("url", "collection_key"), PUBLIC_COLLECTION, ids=["room", "message"])
def test_public_collection_returns_non_empty_list(
        http_client:httpx.Client, url: str, collection_key: str
):
    response = http_client.get(url)

    body = response.json()

    assert collection_key in body
    assert isinstance(body[collection_key], list)
    assert len(body[collection_key]) > 0

