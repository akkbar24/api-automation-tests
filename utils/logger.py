import logging

def setup_logger():
    """Configures logging for the test framework."""
    logging.basicConfig(
        filename="reports/test_logs.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)
