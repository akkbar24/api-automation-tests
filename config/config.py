import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    """Configuration settings for API testing"""

    BASE_URL = os.getenv("BASE_URL", "https://reqres.in/api")

    HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 10))
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))
    RETRY_DELAY = int(os.getenv("RETRY_DELAY", 2))
