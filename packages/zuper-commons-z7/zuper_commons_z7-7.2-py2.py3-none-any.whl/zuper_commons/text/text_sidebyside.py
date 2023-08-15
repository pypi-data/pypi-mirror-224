from typing import Callable, List, Optional, Sequence

from .coloring import get_length_on_screen
from .joinl import joinlines

__all__ = [
    "pad",
    "side_by_side",
]

from ..types import ZValueError


def pad(
    text: str,
    nlines: int,
    linelength: int,
    halign: str = "left",
    valign: str = "top",
    style_fun: Optional[Callable[[str], str]] = None,
) -> List[str]:
    lines: List[str] = text.splitlines()
    if len(lines) < nlines:
        extra = nlines - len(lines)

        if valign == "top":
            extra_top = 0
            extra_bottom = extra
        elif valign == "bottom":
            extra_top = extra
            extra_bottom = 0
        elif valign == "middle":
            extra_bottom = int(extra / 2)
            extra_top = extra - extra_bottom
        else:
            raise ValueError(valign)
        assert extra == extra_top + extra_bottom

        lines_top = [""] * extra_top
        lines_bottom = [""] * extra_bottom
        lines = lines_top + lines + lines_bottom

    res: List[str] = []
    for l in lines:
        l0 = l
        extra = max(linelength - get_length_on_screen(l), 0)
        if halign == "left":
            extra_left = 0
            extra_right = extra
        elif halign == "right":
            extra_left = extra
            extra_right = 0
        elif halign == "center":
            extra_right = int(extra / 2)
            extra_left = extra - extra_right
        else:
            raise ValueError(halign)
        assert extra == extra_left + extra_right
        left = " " * extra_left
        right = " " * extra_right
        if style_fun:
            left = style_fun(left)

            right = style_fun(right)
        l = left + l + right

        if "\n" in l:
            raise ZValueError(l0=l0, l0r=repr(l0), l=l, lr=repr(l), style_fun=style_fun)
        res.append(l)

    # logger.debug(input=repr(text), output=res)
    return res


def side_by_side(
    args: Sequence[str], sep: str = " ", style_fun: Optional[Callable[[str], str]] = None
) -> str:
    from .boxing import text_dimensions

    args = list(args)
    lines: List[List[str]] = [_.splitlines() for _ in args]

    dims = [text_dimensions(_) for _ in args]

    nlines: int = max(_.nlines for _ in dims)

    linelengths: List[int] = [max((get_length_on_screen(line) for line in _), default=0) for _ in lines]
    padded = [pad(_, nlines, linelength, style_fun=style_fun) for _, linelength in zip(args, linelengths)]
    # logger.info(padded=padded)
    res = []
    for i in range(nlines):
        ls = [x[i] for x in padded]
        l = sep.join(ls)
        res.append(l)
    return joinlines(res)
