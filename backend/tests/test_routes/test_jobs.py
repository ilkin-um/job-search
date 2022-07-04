import json
from fastapi import status


def test_create_job(client):
    data = {
        "title": "Software Developer",
        "company": "Doesitmatter",
        "company_url": "www.doesitmatter.com",
        "location": "Baku, Azerbaijan",
        "description": "python",
        "date_posted": "2022-06-28",
    }

    response = client.post("/jobs/create-job/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["company"] == "Doesitmatter"
    assert response.json()["description"] == "python"


def test_read_job(client):
    data = {
        "title": "Software Developer",
        "company": "Doesitmatter",
        "company_url": "www.doesitmatter.com",
        "location": "Baku, Azerbaijan",
        "description": "python",
        "date_posted": "2022-06-28",
    }

    response = client.post("/jobs/create-job/", json.dumps(data))

    response = client.get("/jobs/get/1/")
    assert response.status_code == 200
    assert response.json()["company"] == "Doesitmatter"
    assert response.json()["description"] == "python"


def test_read_all_jobs(client):
    data = {
        "title": "Software Developer",
        "company": "Doesitmatter",
        "company_url": "www.doesitmatter.com",
        "location": "Baku, Azerbaijan",
        "description": "python",
        "date_posted": "2022-06-28",
    }
    client.post("/jobs/create-job/", json.dumps(data))
    client.post("/jobs/create-job/", json.dumps(data))

    response = client.get("/jobs/all/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_update_a_job(client):
    data = {
        "title": "Software Developer",
        "company": "Doesitmatter",
        "company_url": "www.doesitmatter.com",
        "location": "Baku, Azerbaijan",
        "description": "python",
        "date_posted": "2022-06-28",
    }
    client.post("/jobs/create-job/", json.dumps(data))
    data["title"] = "test new title"
    response = client.put("/jobs/update/1", json.dumps(data))
    assert response.json()["msg"] == "Successfully updated data."


def test_delete_a_job(client):
    data = {
        "title": "Software Developer",
        "company": "Doesitmatter",
        "company_url": "www.doesitmatter.com",
        "location": "Baku, Azerbaijan",
        "description": "python",
        "date_posted": "2022-06-28",
    }
    client.post("/jobs/create-job/", json.dumps(data))
    msg = client.delete("/jobs/delete/1")
    response = client.get("/jobs/get/1/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
