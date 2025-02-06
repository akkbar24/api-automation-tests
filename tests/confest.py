# conftest.py

import logging

def pytest_configure(config):
    """Configure global logging."""
    logging.basicConfig(
        filename="reports/test_logs.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
