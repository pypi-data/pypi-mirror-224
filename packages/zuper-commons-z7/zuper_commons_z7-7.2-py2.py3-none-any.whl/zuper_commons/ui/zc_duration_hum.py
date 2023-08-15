import math

from decimal import Decimal
from typing import Union

__all__ = [
    "duration_compact",
    "size_compact",
]


def duration_compact(seconds0: Union[float, Decimal]) -> str:
    if seconds0 < 0:
        return "-" + duration_compact(-seconds0)
    seconds = float(seconds0)
    # if isinstance(seconds0, Decimal):
    #     seconds = float(seconds0)
    # else:
    #     seconds = seconds0
    us = int(math.ceil(seconds * 1000 * 1000))
    total_milliseconds, microseconds = divmod(us, 1000)
    total_seconds, milliseconds = divmod(total_milliseconds, 1000)
    total_minutes, seconds = divmod(total_seconds, 60)
    total_hours, minutes = divmod(total_minutes, 60)
    total_days, hours = divmod(total_hours, 24)
    years, days = divmod(total_days, 365)
    #
    # minutes = int(minutes)
    # hours = int(hours)
    # days = int(days)
    # years = int(years)

    duration = []
    if years > 0:
        duration.append("%dy" % years)
    else:
        if days > 0:
            duration.append(f"{days}d")
        if (days < 3) and (years == 0):
            if hours > 0:
                duration.append(f"{hours}h")
            if (hours < 3) and (days == 0):
                if minutes > 0:
                    duration.append(f"{minutes}m")
                if (minutes < 3) and (hours == 0):
                    if seconds > 0:
                        duration.append(f"{seconds}s")
                    if (seconds < 3) and (minutes == 0):
                        if milliseconds > 0:
                            duration.append(f"{milliseconds}ms")
                        if milliseconds < 3 and seconds == 0:
                            if microseconds > 0:
                                duration.append(f"{microseconds}us")

    if not duration:
        return "0"
    return " ".join(duration)


def size_compact(nbytes: int) -> str:
    KB = 1024
    MB = KB * 1024
    GB = MB * 1024
    TB = GB * 1024
    if nbytes > TB:
        return f"{nbytes / TB:.1f} TB"
    if nbytes > GB:
        return f"{nbytes / GB:.1f} GB"
    if nbytes > MB:
        return f"{nbytes / MB:.1f} MB"
    if nbytes > KB:
        return f"{nbytes / KB:.1f} KB"
    return f"{nbytes} B"
