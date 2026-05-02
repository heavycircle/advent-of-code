from __future__ import annotations

import datetime as dt
import os
from typing import Any

import requests

from advent_of_code.api import AdventApiError, ui


START_YEAR = 2015
LAST_LONG_YEAR = 2024
LONG_DAYS = 25
FIRST_SHORT_YEAR = 2025
SHORT_DAYS = 12


def get_token() -> str:
    """Get the token from the environment"""
    token = os.getenv("AOC_SESSION", "")
    if not token:
        raise AdventApiError("Missing AOC_SESSION!")
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


def safe_request(method: str, url: str, check: bool = True, **kwargs: Any) -> requests.Response:
    """Provide a safe(r) wrapper for requests.request.

    Args:
        method (str): HTTP method for request ('GET', 'POST', etc).
        url (str): Target URL.
        check (bool): Calls raise_for_status() and wraps HTTP errors.
        **kwargs: Arbitrary keyword arguments. Passed directly to requests.request.

    Returns:
        Response: The HTTP response object.

    Raises:
        AdventApiError: Network error occurs or a bad status code.

    """
    try:
        ui.out_debug(f"Sending {method.upper()} request to {url} . . .")
        response = requests.request(method, url, **kwargs)
        ui.out_debug(f"Response: {response.status_code}")
        if check:
            response.raise_for_status()
        return response

    except requests.exceptions.Timeout as e:
        ui.out_debug(f"Request timed out: {method.upper()} {url}")
        raise AdventApiError(f"Request timed out after {kwargs.get('timeout', '?')}s: {e}") from e

    except requests.exceptions.ConnectionError as e:
        ui.out_debug(f"Connection Failed: {method.upper()} {url}")
        raise AdventApiError(f"Failed to connect to {url}: {e}") from e

    except requests.exceptions.HTTPError as e:
        ui.out_debug(f"API Error: {method.upper()} {url}")
        raise AdventApiError(f"API returned error: {e}") from e

    except requests.exceptions.RequestException as e:
        ui.out_debug(f"Request Error: {method.upper()} {url}")
        raise AdventApiError(f"Unexpected request error: {e}") from e
