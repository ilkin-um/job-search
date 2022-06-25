import json


def test_create_user(client):
    data = {
        "username": "test",
        "email": "test",
        "password": "test",
    }
    response = client.post("/users/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "test"
    assert response.json()["is_active"] == True
