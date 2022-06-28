import json


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
