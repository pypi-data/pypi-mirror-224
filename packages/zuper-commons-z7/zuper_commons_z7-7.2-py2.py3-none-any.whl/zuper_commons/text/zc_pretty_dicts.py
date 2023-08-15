from typing import Mapping, Optional as O, TypeVar

from .coloring import get_length_on_screen
from .joinl import joinlines
from .zc_indenting import indent

__all__ = [
    "format_error",
    "pretty_dict",
    "pretty_msg",
]


def pretty_msg(head: str, **kwargs: object) -> str:
    return pretty_dict(head, kwargs)


format_error = pretty_msg


def pretty_dict(
    head: O[str],
    d: Mapping[str, object],
    omit_falsy: bool = False,
    sort_keys: bool = False,
    leftmargin: str = "│ ",  # | <-- note box-making
) -> str:
    head = head or ""
    head = head.rstrip()
    if not d:
        return head + ":  (empty dict)" if head else "(empty dict)"
    s = []
    n = max(get_length_on_screen(str(_)) for _ in d)

    ordered = sorted(d) if sort_keys else list(d)
    # ks = sorted(d)
    for k in ordered:
        v0 = d[k]

        if k == "__builtins__":
            # v = "(hiding __builtins__)"
            continue

        if omit_falsy and not hasattr(v0, "conclusive") and (not isinstance(v0, int)) and (not v0):
            continue
        prefix = (str(k) + ":").rjust(n + 1) + " "

        if isinstance(v0, TypeVar):
            # noinspection PyUnresolvedReferences
            v = f"TypeVar({v0.__name__}, bound={v0.__bound__})"
        elif isinstance(v0, dict):
            v = pretty_dict("", v0)
        else:
            v = str(v0)

        # note: if v is an empty string, this will give no lines
        lines = indent(v, "", first=prefix).splitlines()
        if not lines:
            # in that case we force a line to show up
            lines = [prefix]
        s.extend(lines)

    # return (head + ':\n' if head else '') + indent("\n".join(s), '| ')
    return (head + "\n" if head else "") + indent(joinlines(s), leftmargin)
