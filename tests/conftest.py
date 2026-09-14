import httpx
import pytest

BASE_URL = "http://localhost:8080/api"



@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL


@pytest.fixture(scope="session")
def http_client(base_url    ) -> httpx.Client:
    print("\n>>> opening client")
    client = httpx.Client(base_url=base_url, timeout=10.0)

    yield client

    print("\n>>> closing client")
    client.close()


@pytest.fixture(scope="session")
def auth_token(http_client:httpx.Client) -> str:
    response = http_client.post("/auth/login", json={"username": "admin", "password": "password"})

    assert response.status_code == 200, f"Login failde: {response.text}"

    return response.json()["token"]


@pytest.fixture
def admin_client(base_url: str, auth_token : str) -> httpx.Client:
    client = httpx.Client(base_url=base_url, timeout=10.0)
    client.cookies.set("token", auth_token)

    yield client

    client.close()
