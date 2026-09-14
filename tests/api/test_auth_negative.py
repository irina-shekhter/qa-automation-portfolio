import httpx
import pytest

INVALID_CREDENTIALS = [
    ({"username": "admin", "password": "wrong"},"wrong-password"),
    ({"username": "nobody", "password": "password"}, "unknown-username"),
    ({"username": "admin", "password": ""}, "missing-password"),
    ({"username": "", "password": ""}, "empty-both"),
    ({}, "empty-body"),
]


@pytest.mark.parametrize(
    ("payload", "case"),
    INVALID_CREDENTIALS,
    ids=[case for _, case in INVALID_CREDENTIALS],
)
def test_login_with_invalid_credentials_returns_unauthorized(http_client:httpx.Client, payload: dict, case: str):
    response = http_client.post("/auth/login", json=payload)

    assert response.status_code == 401
    assert response.json() == {"error": "Invalid credentials"}
    assert "token" not in response.text