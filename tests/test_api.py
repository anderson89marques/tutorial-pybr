from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from orders.api import app


@pytest.fixture
def client():
    return TestClient(app)


def test_healthcheck(client):
    response = client.get("/healthcheck")
    assert response.status_code == HTTPStatus.OK

def test_healthcheck_response_content_type_is_json(client):
    response = client.get("/healthcheck")
    assert response.headers['Content-type'] == "application/json"

def test_healthcheck_response_status_ok(client):
    response = client.get("/healthcheck")
    assert response.json() == {"status": "ok"}
