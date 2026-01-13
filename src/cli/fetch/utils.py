import datetime as dt
import os
import sys

from cli.logger import get_logger


logger = get_logger()

START_YEAR = 2015
LAST_LONG_YEAR = 2024
LONG_DAYS = 25
FIRST_SHORT_YEAR = 2025
SHORT_DAYS = 12


def get_token() -> str:
    """Get the token from the environment"""
    token = os.getenv("AOC_SESSION", "")
    if not token:
        logger.error("Missing AOC_SESSION!")
        sys.exit(1)

    return token


def validate_date(year: int, day: int) -> bool:
    """Validate we can get a file with this date"""

    # Basic sanity checking
    if year < START_YEAR:
        return False
    if START_YEAR <= year <= LAST_LONG_YEAR and 1 <= day <= LONG_DAYS:
        return True

    # Current day - Ensure it's after midnight
    est = dt.timezone(dt.timedelta(hours=-5))
    delta = dt.datetime(year, 12, day, tzinfo=est) - dt.datetime.now(tz=est)
    return delta < dt.timedelta(seconds=0)
