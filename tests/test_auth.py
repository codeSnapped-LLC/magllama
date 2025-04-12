import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_jwt_auth():
    response = client.post("/token", data={"username": "johndoe", "password": "secret"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_api_key_auth():
    response = client.get("/scans/trivy/", headers={"X-API-Key": "expected_api_key"})
    assert response.status_code == 200
