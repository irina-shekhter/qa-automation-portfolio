import httpx


def test_first_message(http_client: httpx.Client):
    response = http_client.get("/message")
    assert response.status_code == 200


def test_get_messages_return_list_of_messages(http_client: httpx.Client):
    body = http_client.get("/message").json()

    assert "messages" in body
    assert isinstance(body["messages"], list)
    assert len(body["messages"]) > 0


def test_messages_has_expected_fields(http_client: httpx.Client):
    first_message = http_client.get("/message").json()["messages"][0]
    assert isinstance(first_message["id"], int)
    assert isinstance(first_message["name"], str)
    assert isinstance(first_message["subject"], str)
    assert isinstance(first_message["read"], bool)
