import pytest

from httpx import Client


@pytest.fixture
def client() -> Client:
    return Client()
