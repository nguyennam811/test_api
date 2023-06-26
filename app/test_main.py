from fastapi.testclient import TestClient
from fastapi import status
from .main import app

client = TestClient(app)

def test_get_user():
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()