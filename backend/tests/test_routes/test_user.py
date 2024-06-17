from fastapi.testclient import TestClient

def test_create_user(client:TestClient):
    data = {"email": "ping@example.com", "password":"supresecret"}
    response = client.post("/users/",json=data)
    assert response.status_code == 201
    assert response.json()["email"] == "ping@example.com"

    




