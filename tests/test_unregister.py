from urllib.parse import quote


def test_unregister_from_activity(client):
    # Arrange
    activity = "Programming Class"
    encoded = quote(activity, safe="")
    email = "emma@mergington.edu"  # present in initial data

    # Act
    response = client.delete(f"/activities/{encoded}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    body = response.json()
    assert "Unregistered" in body.get("message", "")

    # Verify removal
    activities_resp = client.get("/activities")
    assert email not in activities_resp.json()[activity]["participants"]
