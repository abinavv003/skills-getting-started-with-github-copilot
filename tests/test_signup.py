from urllib.parse import quote


def test_signup_for_activity(client):
    # Arrange
    activity = "Chess Club"
    encoded = quote(activity, safe="")
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{encoded}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    body = response.json()
    assert "Signed up" in body.get("message", "")

    # Verify participant was added
    activities_resp = client.get("/activities")
    assert email in activities_resp.json()[activity]["participants"]
