import pytest
import os
from utils.api_client import APIClient
import logging

api = APIClient()

# @pytest.mark.parametrize("email, password, expected_status", [
#     (os.getenv("VALID_EMAIL"), os.getenv("VALID_PASSWORD"), 200),
#     (os.getenv("INVALID_EMAIL"), os.getenv("INVALID_PASSWORD"), 400), 
#     (os.getenv("EMPTY_EMAIL"), os.getenv("VALID_PASSWORD"), 400),  
#     (os.getenv("VALID_EMAIL"), os.getenv("EMPTY_PASSWORD"), 400) 
# ])
# def test_user_registration(email, password, expected_status):
#     """Test user registration API"""
#     response = api.post("/register", {"email": email, "password": password})
#     assert response.status_code == expected_status


def test_valid_user_registration():
    """Test registration with valid credentials"""
    response = api.post("/register", {"email": os.getenv("VALID_EMAIL"), "password": os.getenv("VALID_PASSWORD")})
    logging.info(f"Response Status Code: {response.status_code}")
    logging.info(f"Response JSON: {response.json()}")
    assert response.status_code == 200

def test_invalid_user_registration():
    """Test registration with invalid credentials"""
    response = api.post("/register", {"email": os.getenv("INVALID_EMAIL"), "password": os.getenv("INVALID_PASSWORD")})
    assert response.status_code == 400

def test_registration_with_empty_email():
    """Test registration with empty email"""
    response = api.post("/register", {"email": "", "password": os.getenv("VALID_PASSWORD")})
    assert response.status_code == 400

def test_registration_with_empty_password():
    """Test registration with empty password"""
    response = api.post("/register", {"email": os.getenv("VALID_EMAIL"), "password": ""})
    assert response.status_code == 400

