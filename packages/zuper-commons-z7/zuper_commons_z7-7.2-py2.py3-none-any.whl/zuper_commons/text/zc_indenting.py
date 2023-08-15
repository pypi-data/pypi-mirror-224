from typing import Callable, List, Optional

from .coloring import get_length_on_screen
from .joinl import joinlines
from ..types import ZValueError

__all__ = [
    "indent",
    "make_par_tree",
]


def indent(
    s: str,
    prefix: str,
    first: Optional[str] = None,
    last: Optional[str] = None,
    one: Optional[str] = None,
) -> str:
    if not isinstance(s, str):
        s = "{}".format(s)

    assert isinstance(prefix, str), type(prefix)
    lines = s.splitlines()
    if not lines:
        return ""

    if first is None:
        first = prefix
    if one is None:
        if first is not None:
            one = first
        else:
            one = prefix
    if last is None:
        couples = [("│", "└"), ("┋", "H")]
        for a, b in couples:
            if a in prefix:
                last = prefix.replace(a, b)
                break
        else:
            last = prefix

    assert isinstance(last, str)
    # print(f'{prefix!r:10} -> {get_length_on_screen(prefix)}')
    # print(f'{first!r:10} -> {get_length_on_screen(first)}')
    m = max(get_length_on_screen(prefix), get_length_on_screen(first))

    prefix = " " * (m - get_length_on_screen(prefix)) + prefix
    first = " " * (m - get_length_on_screen(first)) + first
    last = " " * (m - get_length_on_screen(last)) + last
    one = " " * (m - get_length_on_screen(one)) + one
    assert "\n" not in (prefix + first + last + one), (prefix, first, last, one, s)
    # different first prefix
    res = [f"{prefix}{line.rstrip()}" for line in lines]

    if len(lines) == 1:
        res[0] = f"{one}{lines[0].rstrip()}"
    # elif len(lines) == 2:
    #     res[0] = f"{one}{lines[0].rstrip()}"
    #     res[1] = f"{one}{lines[0].rstrip()}"
    elif len(lines) >= 2:
        res[0] = f"{first}{lines[0].rstrip()}"
        res[-1] = f"{last}{lines[-1].rstrip()}"

    return joinlines(res)


def make_par_tree(
    paragraphs: List[str],
    color_struct: Optional[Callable[[str], str]],
) -> str:
    if color_struct is None:
        C = lambda x: x
    else:
        C = color_struct
    s = ""
    for i, par in enumerate(paragraphs):
        if not isinstance(par, str):
            raise ZValueError(f"Expected a string, got {type(par)}", paragraphs=paragraphs)
        par = par.rstrip()
        is_last = i == len(paragraphs) - 1
        if not is_last:
            s += indent(par, C("│ "), first=C("├ "), last=C("│ "), one=C("├ "))
        else:
            s += indent(par, "  ", first=C("└ "))
    #
    # s = s.replace('\n', '!$$$$')
    # s = s.replace('$$$$', '\n')
    return s
