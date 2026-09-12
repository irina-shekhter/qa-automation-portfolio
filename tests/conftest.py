import httpx
import pytest


@pytest.fixture(scope="session")
def room_url() -> str:
    return "http://localhost:3001/room/"


@pytest.fixture(scope="session")
def http_client() -> httpx.Client:
    print("\n>>> opening client")
    client = httpx.Client(timeout=10.0)

    yield client

    print("\n>>> closing client")
    client.close()


@pytest.fixture
def rooms_response(http_client: httpx.Client, room_url: str) -> httpx.Response:
    return http_client.get(room_url)


@pytest.fixture(scope="session")
def message_url() -> str:
    return "http://localhost:3006/message/"
