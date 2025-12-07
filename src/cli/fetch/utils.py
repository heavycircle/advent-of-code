import datetime as dt
import os

from ..logger import get_logger

logger = get_logger()


def get_token() -> str:
    """Get the token from the environment"""
    token = os.getenv("AOC_SESSION", "")
    if not token:
        logger.error("Missing AOC_SESSION!")
        exit(1)

    return token


def validate_date(year: int, day: int) -> bool:
    """Validate we can get a file with this date"""

    # Basic sanity checking
    if year < 2015:
        return False
    if 2015 <= year <= 2024 and 1 <= day <= 25:
        return True

    # Current day - Ensure it's after midnight
    est = dt.timezone(dt.timedelta(hours=-5))
    delta = dt.datetime(year, 12, day, tzinfo=est) - dt.datetime.now(tz=est)
    return delta < dt.timedelta(seconds=0)
