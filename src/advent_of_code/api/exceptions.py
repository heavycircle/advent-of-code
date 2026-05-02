from __future__ import annotations


class AdventError(Exception):
    """Base class for all CLI Errors."""


class AdventInitError(AdventError):
    """Failure to initialize a new event."""


class AdventApiError(AdventError):
    """Failure to communicate with AdventOfCode remote services."""


class AdventSolveError(AdventError):
    """Failure to solve a challenge due to an impossible case."""
