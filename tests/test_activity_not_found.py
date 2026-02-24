from urllib.parse import quote


def test_activity_not_found_returns_404_on_signup(client):
    # Arrange
    activity = "Nonexistent Activity"
    encoded = quote(activity, safe="")
    email = "someone@mergington.edu"

    # Act
    response = client.post(f"/activities/{encoded}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json().get("detail", "")
