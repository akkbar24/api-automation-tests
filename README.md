# api-automation-tests



# API Automation Test Framework

This repository contains an API automation test framework written in Python for testing various API endpoints.

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/akkbar24/api-automation-tests.git
cd api-automation-tests
```

### 2. Create and Activate Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:

    ```bash
    venv\Scripts\activate
    ```

- On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up Environment Variables

Create a `.env` file in the root directory of the project and define the following environment variables:

```bash
# API Base URL
BASE_URL=https://reqres.in/api

# Test User Credentials
VALID_EMAIL=eve.holt@reqres.in
VALID_PASSWORD=pistol
INVALID_EMAIL=invalid@example.com
INVALID_EMAIL_FORMAT=invalid-email
INVALID_PASSWORD=wrongpass
EMPTY_EMAIL=
EMPTY_PASSWORD=

# Timeout & Retry Settings
REQUEST_TIMEOUT=10
MAX_RETRIES=3
RETRY_DELAY=2
```

Make sure **not** to commit the `.env` file to version control. Add `.env` to your `.gitignore` file to ensure it isn't pushed to the repository.

### 5. Run Tests

```bash
pytest tests/ --maxfail=3 --disable-warnings --html=reports/test-report.html
```

### 6. View Test Results

The test results will be stored in the `reports/test-results.html` file. You can view them directly or use a tool to analyze the report.
