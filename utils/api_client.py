import requests
import time
import logging
from config.config import Config
from utils.logger import setup_logger

logger = setup_logger()

class APIClient:
    """Handles API requests, authentication, and retries."""

    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = Config.HEADERS
        self.token = None

    def post(self, endpoint, data):
        """Handles POST requests with retries."""
        url = f"{self.base_url}{endpoint}"
        for attempt in range(Config.MAX_RETRIES):
            response = requests.post(url, json=data, headers=self.headers, timeout=Config.REQUEST_TIMEOUT)
            if response.status_code == 200:
                if "token" in response.json():
                    self.token = response.json()["token"]
                return response
            logger.warning(f"POST {url} failed (Attempt {attempt + 1}): {response.text}")
            time.sleep(Config.RETRY_DELAY)
        return response

    def get(self, endpoint):
        """Handles GET requests with authentication token."""
        url = f"{self.base_url}{endpoint}"
        headers = self.headers.copy()
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        response = requests.get(url, headers=headers, timeout=Config.REQUEST_TIMEOUT)
        return response
