def test_root_redirect(client):
    # Arrange: client fixture
    # Act: request root without following redirects
    response = client.get("/", follow_redirects=False)

    # Assert: redirect to static index
    assert response.status_code in (301, 302, 307, 308)
    assert "/static/index.html" in response.headers.get("location", "")
