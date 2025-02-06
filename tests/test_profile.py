import pytest
import os
from unittest.mock import MagicMock
from utils.api_client import APIClient
import logging

api = APIClient()

@pytest.fixture
def mock_api(mocker):
    """Mock APIClient methods to prevent real API calls."""
    mocker.patch.object(api, "post")
    mocker.patch.object(api, "get")
    return api

@pytest.fixture
def valid_auth_token(mock_api):
    """Mock login API response to return a fake token."""
    mock_api.post.return_value = MagicMock(status_code=200, json=lambda: {"token": "mocked_token"})
    
    response = api.post("/login", {"email": "test@example.com", "password": "password"})
    assert response.status_code == 200
    return response.json().get("token")

def test_user_profile_valid_token(valid_auth_token, mock_api):
    """Test retrieving user profile with a valid authentication token (mocked)."""
    user_id = 2
    mock_api.get.return_value = MagicMock(
        status_code=200,
        json=lambda: {"data": {"id": user_id, "name": "Test User"}}
    )

    headers = {"Authorization": f"Bearer {valid_auth_token}"}
    response = api.get(f"/users/{user_id}", headers=headers)

    assert response.status_code == 200
    assert "data" in response.json()
    assert response.json()["data"]["id"] == user_id

def test_user_profile_invalid_token(mock_api):
    """Test retrieving user profile with an invalid authentication token (mocked)."""
    user_id = 2
    mock_api.get.return_value = MagicMock(status_code=401, json=lambda: {"error": "Unauthorized"})

    headers = {"Authorization": "Bearer INVALID_TOKEN"}
    response = api.get(f"/users/{user_id}", headers=headers)

    assert response.status_code == 401
    assert response.json()["error"] == "Unauthorized"

def test_user_profile_without_token(mock_api):
    """Test retrieving user profile without an authentication token (mocked)."""
    user_id = 2
    mock_api.get.return_value = MagicMock(status_code=401, json=lambda: {"error": "Missing token"})

    response = api.get(f"/users/{user_id}")  

    assert response.status_code == 401
    assert response.json()["error"] == "Missing token"

def test_user_profile_non_existing_user():
    """Test retrieving profile for a non-existing user (real API)."""
    user_id = 99999
    logging.info(f"Testing profile retrieval for non-existing user with ID {user_id}.")


    response = api.get(f"/users/{user_id}")
    
    logging.info(f"Response Status Code: {response.status_code}")
    logging.info(f"Response Body: {response.json()}")

    assert response.status_code == 404

    logging.info("Test completed for non-existing user retrieval.")
