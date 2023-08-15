import re

# By Seo Sanghyeon.  Some changes by Connelly Barnes.
from typing import Collection, List, Tuple, TypeVar, Union

# ---------------------------------------------------------
# natsort.py: Natural string sorting.
# ---------------------------------------------------------

__all__ = [
    "natsorted",
]


def try_int(s: str) -> Union[str, int]:
    "Convert to integer if possible."
    try:
        return int(s)
    except ValueError:
        return s


def natsort_key(s: str) -> Tuple[Union[str, int], ...]:
    "Used internally to get a tuple by which s is sorted."

    s = str(s)  # convert everything to string
    return tuple(map(try_int, re.findall(r"(\d+|\D+)", s)))


X = TypeVar("X", bound="str")


def natsorted(seq: Collection[X]) -> List[X]:
    "Returns a copy of seq, sorted by natural string sort."
    # convert set -> list
    return sorted(list(seq), key=natsort_key)
