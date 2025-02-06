import pytest
import os
from utils.api_client import APIClient

api = APIClient()

# @pytest.mark.parametrize("email, password, expected_status", [
#     (os.getenv("VALID_EMAIL"), os.getenv("VALID_PASSWORD"), 200),
#     (os.getenv("INVALID_EMAIL"), os.getenv("INVALID_PASSWORD"), 400),
#     (os.getenv("EMPTY_EMAIL"), os.getenv("VALID_PASSWORD"), 400),
#     (os.getenv("VALID_EMAIL"), os.getenv("EMPTY_PASSWORD"), 400)
# ])
# def test_user_login(email, password, expected_status):
#     """Test user login API"""
#     response = api.post("/login", {"email": email, "password": password})
#     assert response.status_code == expected_status


def test_valid_user_login():
    """Test login with valid credentials"""
    response = api.post("/login", {"email": os.getenv("VALID_EMAIL"), "password": os.getenv("VALID_PASSWORD")})
    assert response.status_code == 200

def test_invalid_user_login():
    """Test login with invalid credentials"""
    response = api.post("/login", {"email": os.getenv("INVALID_EMAIL"), "password": os.getenv("INVALID_PASSWORD")})
    assert response.status_code == 400

def test_login_with_empty_email():
    """Test login with empty email"""
    response = api.post("/login", {"email": "", "password": os.getenv("VALID_PASSWORD")})
    assert response.status_code == 400

def test_login_with_empty_password():
    """Test login with empty password"""
    response = api.post("/login", {"email": os.getenv("VALID_EMAIL"), "password": ""})
    assert response.status_code == 400


def test_login_with_invalid_email_format():
    """Test login with an invalid email format"""
    response = api.post("/login", {"email": os.getenv("INVALID_EMAIL_FORMAT"), "password": os.getenv("VALID_PASSWORD")})
    assert response.status_code == 400

