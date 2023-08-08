"""
various helpers
"""

import datetime


def now():
    """ """

    return str(datetime.datetime.now())[:19]


def _from_date_to_generation(date):
    """ """
    li = [
        (1900, 1920),
        (1920, 1940),
        (1940, 1950),
        (1950, 1960),
        (1960, 1970),
        (1970, 1980),
        (1980, 1990),
        (1990, 2000),
        (2000, 2010),
        (2010, 2015),
        (2015, 2020),
        (2020, 2025),
    ]
    for x, y in li:
        if x <= date < y:
            return f"{x}-{y}"

    return ""
