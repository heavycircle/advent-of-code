from .fetch_real import fetch_real
from .fetch_test import fetch_test


def fetch(year: int, day: int) -> bool:
    return fetch_real(year, day) and fetch_test(year, day)


__all__ = ["fetch"]
