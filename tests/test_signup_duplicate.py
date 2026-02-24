from urllib.parse import quote


def test_signup_duplicate_returns_400(client):
    # Arrange
    activity = "Chess Club"
    encoded = quote(activity, safe="")
    # michael@mergington.edu is present in initial data
    email = "michael@mergington.edu"

    # Act
    response = client.post(f"/activities/{encoded}/signup", params={"email": email})

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json().get("detail", "")
