import httpx
import pytest


@pytest.fixture
def room_url():
    return "http://localhost:3001/room/"


@pytest.fixture
def rooms_response(room_url: str) -> httpx.Response:
    return httpx.get(room_url)