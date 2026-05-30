def test_get_activities_returns_expected_shape(client):
    # Arrange

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(data, dict)
    assert "Chess Club" in data

    chess = data["Chess Club"]
    assert {"description", "schedule", "max_participants", "participants"}.issubset(chess.keys())
    assert isinstance(chess["participants"], list)
