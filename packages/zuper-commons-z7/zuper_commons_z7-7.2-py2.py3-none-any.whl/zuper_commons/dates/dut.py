from datetime import datetime

from dateutil.parser import parse
from dateutil.tz import tzutc

from zuper_commons.types import check_isinstance

__all__ = [
    "flexible_parse",
    "flexible_parse_assume_utc",
]


def flexible_parse(s: str) -> datetime:
    check_isinstance(s, str)
    return parse(s)


def flexible_parse_assume_utc(s: str) -> datetime:
    """This should be used on a date which does NOT have a timezone."""
    check_isinstance(s, str)
    d = flexible_parse(s)
    if d.tzinfo is None:
        d = d.replace(tzinfo=tzutc())
    return d
