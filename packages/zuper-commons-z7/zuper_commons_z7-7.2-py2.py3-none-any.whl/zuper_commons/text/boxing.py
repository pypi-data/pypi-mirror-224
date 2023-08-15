from dataclasses import dataclass
from typing import Callable, Dict, List, Optional, Tuple, TYPE_CHECKING

from . import joinpars
from .coloring import remove_escapes
from .text_sidebyside import pad

if TYPE_CHECKING:
    from typing import Literal
else:
    try:
        from typing import Literal
    except ImportError:
        from typing_extensions import Literal

__all__ = [
    "BoxStyle",
    "NTuple",
    "ZO",
    "box",
    "text_dimensions",
]


@dataclass
class TextDimensions:
    nlines: int
    max_width: int


def text_dimensions(s: str) -> TextDimensions:
    if not s.isprintable():
        s = remove_escapes(s)
    lines = s.splitlines()
    if lines:
        max_width = max(len(_) for _ in lines)
    else:
        max_width = 0
    return TextDimensions(nlines=len(lines), max_width=max_width)


#
# U+250x   ─   ━   │   ┃   ┄   ┅   ┆   ┇   ┈   ┉   ┊   ┋   ┌   ┍   ┎   ┏
# U+251x   ┐   ┑   ┒   ┓   └   ┕   ┖   ┗   ┘   ┙   ┚   ┛   ├   ┝   ┞   ┟
# U+252x   ┠   ┡   ┢   ┣   ┤   ┥   ┦   ┧   ┨   ┩   ┪   ┫   ┬   ┭   ┮   ┯
# U+253x   ┰   ┱   ┲   ┳   ┴   ┵   ┶   ┷   ┸   ┹   ┺   ┻   ┼   ┽   ┾   ┿
# U+254x   ╀   ╁   ╂   ╃   ╄   ╅   ╆   ╇   ╈   ╉   ╊   ╋   ╌   ╍   ╎   ╏
# U+255x   ═   ║   ╒   ╓   ╔   ╕   ╖   ╗   ╘   ╙   ╚   ╛   ╜   ╝   ╞   ╟
# U+256x   ╠   ╡   ╢   ╣   ╤   ╥   ╦   ╧   ╨   ╩   ╪   ╫   ╬   ╭   ╮   ╯
# U+257x   ╰   ╱   ╲   ╳   ╴   ╵   ╶   ╷   ╸   ╹   ╺   ╻   ╼   ╽   ╾   ╿

BoxStyle = Literal["pipes", "heavy", "light", "circo", "spaces", "none", "lefts", "lefts2", "lefts3", "debug"]

boxes: Dict[BoxStyle, List[str]] = {
    "pipes": "╔ ═ ╗ ║ ╝ ═ ╚ ║ ╬ ╠ ╣ ╦  ╩ ═ ║ ┼ ╟ ╢ ╤ ╧ ─ │".split(),
    "heavy": "┏ ━ ┓ ┃ ┛ ━ ┗ ┃ ╋ ┣ ┫ ┳  ┻ ━ ┃ ┼ ┠ ┨ ┯ ┷ ─ │".split(),
    "light": "┌ ─ ┐ │ ┘ ─ └ │ ┼ ├ ┤ ┬  ┴ ─ │ ┼ ├ ┤ ┬ ┴ ─ │".split(),
    "circo": "╭ ─ ╮ │ ╯ ─ ╰ │ ┼ ├ ┤ ┬  ┴ ─ │ ┼ ├ ┤ ┬ ┴ ─ │".split(),
    "debug": "A B C D E F G H I L M N  O P Q R S T U V W Z".split(),
    # "lefts": "A B C D E F G H I L M N  O P Q R S T U V W Z".split(),
}
boxes["lefts"] = [" " * 1 if _ == "Z" else "" for _ in boxes["debug"]]
boxes["lefts2"] = [" " * 2 if _ == "Z" else "" for _ in boxes["debug"]]
boxes["lefts3"] = [" " * 3 if _ == "Z" else "" for _ in boxes["debug"]]
boxes["spaces"] = [" "] * len(boxes["pipes"])

CORNERS = ["corner"]
ZO = Literal[0, 1]
NTuple = Tuple[Tuple[ZO, ZO, ZO], Tuple[ZO, None, ZO], Tuple[ZO, ZO, ZO]]
NEIGH: NTuple = ((0, 0, 0), (0, None, 0), (0, 0, 0))


def box(
    s: str,
    style: BoxStyle = "pipes",
    neighs: NTuple = NEIGH,
    draw_borders: Tuple[int, int, int, int] = (1, 1, 1, 1),
    light_inside: bool = True,
    color: Optional[str] = None,
    attrs: Optional[List[str]] = None,
    style_fun: Optional[Callable[[str], str]] = None,
) -> str:
    from zuper_commons.ui import get_colorize_function

    dims = text_dimensions(s)
    padded = pad(s, dims.nlines, dims.max_width, style_fun=style_fun)

    (tl_n, tc_n, tr_n), (ml_n, _, mr_n), (bl_n, bc_n, br_n) = neighs

    assert tl_n is not None
    assert tc_n is not None
    assert tr_n is not None
    assert ml_n is not None
    assert mr_n is not None
    assert bl_n is not None
    assert bc_n is not None
    assert br_n is not None

    S = boxes[style]
    assert len(S) == 22, len(S)
    (
        tl,
        tc,
        tr,
        mr,
        br,
        bc,
        bl,
        ml,
        Pc,
        Pr,
        Pl,
        Pd,
        Pu,
        H,
        V,
        Pc_light,
        Pr_light,
        Pl_light,
        Pd_light,
        Pu_light,
        H_light,
        V_light,
    ) = S

    if light_inside:
        Pc = Pc_light
        Pu = Pu_light
        Pd = Pd_light
        Pr = Pr_light
        Pl = Pl_light
        H = H_light
        V = V_light

    TT = Tuple[Literal[0, 1], Literal[0, 1], Literal[0, 1]]
    tl_use_dict: Dict[TT, str] = {
        (0, 0, 0): tl,
        (0, 0, 1): Pd,
        (0, 1, 0): Pr,
        (0, 1, 1): Pc,  # XXX
        (1, 0, 0): Pc,  # XXX
        (1, 0, 1): Pc,  # XXX
        (1, 1, 0): Pc,
        (1, 1, 1): Pc,
    }
    tl_use = tl_use_dict[(tl_n, tc_n, ml_n)]

    tr_use_dict: Dict[TT, str] = {
        (0, 0, 0): tr,
        (0, 0, 1): Pd,
        (0, 1, 0): Pc,
        (0, 1, 1): Pc,
        (1, 0, 0): Pl,
        (1, 0, 1): Pc,
        (1, 1, 0): Pc,
        (1, 1, 1): Pc,
    }
    tr_use = tr_use_dict[(tc_n, tr_n, mr_n)]

    br_use_dict: Dict[TT, str] = {
        (0, 0, 0): br,
        (0, 0, 1): Pc,
        (0, 1, 0): Pl,
        (0, 1, 1): Pc,
        (1, 0, 0): Pu,
        (1, 0, 1): Pc,
        (1, 1, 0): Pc,
        (1, 1, 1): Pc,
    }
    br_use = br_use_dict[(mr_n, bc_n, br_n)]

    bl_use_dict: Dict[TT, str] = {
        (0, 0, 0): bl,
        (0, 0, 1): Pr,
        (0, 1, 0): Pc,
        (0, 1, 1): Pc,
        (1, 0, 0): Pu,
        (1, 0, 1): Pc,
        (1, 1, 0): Pc,
        (1, 1, 1): Pc,
    }
    bl_use = bl_use_dict[(ml_n, bl_n, bc_n)]

    mr_use = {0: mr, 1: V}[mr_n]
    ml_use = {0: ml, 1: V}[ml_n]
    tc_use = {0: tc, 1: H}[tc_n]
    bc_use = {0: bc, 1: H}[bc_n]

    draw_top, draw_right, draw_bottom, draw_left = draw_borders

    if not draw_right:
        tr_use = ""
        mr_use = ""
        br_use = ""

    if not draw_left:
        tl_use = ""
        ml_use = ""
        bl_use = ""

    top = tl_use + tc_use * dims.max_width + tr_use
    bot = bl_use + bc_use * dims.max_width + br_use

    def f(_: str) -> str:
        if not _:
            return ""
        if style_fun:
            _ = style_fun(_)
        if color is not None or attrs:
            fc = get_colorize_function(color, attrs=attrs)
            _ = fc(_)
        return _

    top_col = f(top)
    bot_col = f(bot)
    mr_use_col = f(mr_use)
    ml_use_col = f(ml_use)

    new_lines = []
    if draw_top and top_col:
        new_lines.append(top_col)

    for l in padded:
        new_lines.append(ml_use_col + l + mr_use_col)

    if draw_bottom and bot_col:
        new_lines.append(bot_col)
    # sep = "\n"
    # final = sep.join(new_lines)  # ok
    final = joinpars(new_lines)  # ok

    # print(f'{final!r}')
    return final


# begin = termcolor.colored('║', 'yellow', attrs=['dark'])
# ending = termcolor.colored('║', 'yellow', attrs=['dark'])  # ↵┋
