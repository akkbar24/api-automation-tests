# API Test Suite Documentation

## Overview
This test suite automates the testing of various APIs related to user authentication and data retrieval. The suite covers the following use cases:

- **User Registration API**
- **User Login API**
- **Authenticated User Actions (Profile & Resources)**

The tests are designed to validate the correct behavior of the system for different input scenarios.

## Test Cases

### **1. User Registration**

#### **Test 1: Valid Registration**
- **Description**: Tests registration with valid email and password.
- **Request**:
  - **Method**: POST
  - **Endpoint**: `/register`
  - **Body**: 
    ```json
    {
      "email": "VALID_EMAIL",
      "password": "VALID_PASSWORD"
    }
    ```
- **Expected Response**:
  - **Status Code**: 200
  - **Response Body**: The user ID and Token should be returned in the response body.

#### **Test 2: Invalid Email**
- **Description**: Tests registration with an invalid email format.
- **Request**:
  - **Method**: POST
  - **Endpoint**: `/register`
  - **Body**: 
    ```json
    {
      "email": "invalidemail",
      "password": "VALID_PASSWORD"
    }
    ```
- **Expected Response**:
  - **Status Code**: 400

#### **Test 3: Empty Email**
- **Description**: Tests registration with an empty email.
- **Request**:
  - **Method**: POST
  - **Endpoint**: `/register`
  - **Body**: 
    ```json
    {
      "email": "",
      "password": "VALID_PASSWORD"
    }
    ```
- **Expected Response**:
  - **Status Code**: 400

#### **Test 4: Empty Password**
- **Description**: Tests registration with an empty password.
- **Request**:
  - **Method**: POST
  - **Endpoint**: `/register`
  - **Body**: 
    ```json
    {
      "email": "VALID_EMAIL",
      "password": ""
    }
    ```
- **Expected Response**:
  - **Status Code**: 400

---

### **2. User Login**

#### **Test 1: Valid Login**
- **Description**: Tests login with correct email and password.
- **Request**:
  - **Method**: POST
  - **Endpoint**: `/login`
  - **Body**: 
    ```json
    {
      "email": "VALID_EMAIL",
      "password": "VALID_PASSWORD"
    }
    ```
- **Expected Response**:
  - **Status Code**: 200
  - **Response Body**: The response should include a token.

#### **Test 2: Invalid Login**
- **Description**: Tests login with invalid credentials (incorrect email or password).
- **Request**:
  - **Method**: POST
  - **Endpoint**: `/login`
  - **Body**: 
    ```json
    {
      "email": "INVALID_EMAIL",
      "password": "INVALID_PASSWORD"
    }
    ```
- **Expected Response**:
  - **Status Code**: 400

#### **Test 3: Empty Credentials**
- **Description**: Tests login with empty email and password.
- **Request**:
  - **Method**: POST
  - **Endpoint**: `/login`
  - **Body**: 
    ```json
    {
      "email": "",
      "password": ""
    }
    ```
- **Expected Response**:
  - **Status Code**: 400

#### **Test 4: Empty Email**
- **Description**: Tests login with empty email.
- **Request**:
  - **Method**: POST
  - **Endpoint**: `/login`
  - **Body**: 
    ```json
    {
      "email": "",
      "password": "VALID_PASSWORD"
    }
    ```
- **Expected Response**:
  - **Status Code**: 400

#### **Test 5: Empty Password**
- **Description**: Tests login with empty password.
- **Request**:
  - **Method**: POST
  - **Endpoint**: `/login`
  - **Body**: 
    ```json
    {
      "email": "VALID_EMAIL",
      "password": ""
    }
    ```
- **Expected Response**:
  - **Status Code**: 400

#### **Test 6: Invalid Email Format**
- **Description**: Tests login with an invalid email format.
- **Request**:
  - **Method**: POST
  - **Endpoint**: `/login`
  - **Body**: 
    ```json
    {
      "email": "INVALID_EMAIL_FORMAT",
      "password": "VALID_PASSWORD"
    }
    ```
- **Expected Response**:
  - **Status Code**: 400

---

### **3. Authenticated User Actions (Profile & Resources)**

#### **Test 1: Get Profile (Authenticated)**
- **Description**: Tests accessing the user profile API with a valid authentication token.
- **Request**:
  - **Method**: GET
  - **Endpoint**: `/users/1`
  - **Authorization**: Bearer Token (obtained from login)
  - **Headers**:
    ```json
    {
      "Authorization": "Bearer VALID_TOKEN"
    }
    ```
- **Expected Response**:
  - **Status Code**: 200
  - **Response Body**: Should contain user profile data.

#### **Test 2: Get List of Resources (Authenticated)**
- **Description**: Tests accessing the list of resources API with a valid authentication token.
- **Request**:
  - **Method**: GET
  - **Endpoint**: `/unknown`
  - **Authorization**: Bearer Token (obtained from login)
  - **Headers**:
    ```json
    {
      "Authorization": "Bearer VALID_TOKEN"
    }
    ```
- **Expected Response**:
  - **Status Code**: 200
  - **Response Body**: Should contain a list of resources.

#### **Test 3: Invalid Token Access**
- **Description**: Tests access to the user profile API with an invalid or expired token.
- **Request**:
  - **Method**: GET
  - **Endpoint**: `/users/1`
  - **Authorization**: Bearer Token (invalid token)
  - **Headers**:
    ```json
    {
      "Authorization": "Bearer INVALID_TOKEN"
    }
    ```
- **Expected Response**:
  - **Status Code**: 401
  - **Response Body**: Should return an error indicating unauthorized access.

---

## **Test Execution & Reporting**

### **Running the Tests**
To run the tests, use the following command:

```bash
pytest --maxfail=3 --disable-warnings --alluredir=allure-results

pytest -s --log-cli-level=INFO .\tests\test_registration.py

## Test coverage 

pytest --cov=tests



pytest tests/ --html=reports/report.html --self-contained-html
