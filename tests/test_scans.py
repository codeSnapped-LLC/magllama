import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_get_scan_summary():
    response = client.get("/scans/trivy/summary")
    assert response.status_code == 200
    assert "total_scans" in response.json()

def test_get_scan_details():
    response = client.get("/scans/trivy/1/details")
    assert response.status_code in [200, 404]  # Depending on if the scan exists
