import logging
from pathlib import Path


# Create the logs folder if it doesn't exist
Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    filename="logs/application.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def log_recommendation(
    request: str,
    preferences: dict,
    retrieved_context: str,
):
    """Logs each recommendation request."""

    logging.info("User Request: %s", request)
    logging.info("Preferences: %s", preferences)
    logging.info("Retrieved Context: %s", retrieved_context)