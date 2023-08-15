import itertools
from dataclasses import dataclass
from typing import Callable, Dict, List, Optional, Sequence, Tuple, TYPE_CHECKING, TypeVar, Union

from .boxing import box, BoxStyle, NTuple, text_dimensions, ZO
from .coloring import get_length_on_screen
from .joinl import joinlines
from .text_sidebyside import pad, side_by_side

__all__ = [
    "HAlign",
    "Style",
    "VAlign",
    "do_padding",
    "format_rows_as_table",
    "format_table",
    "wrap_lines",
]

if TYPE_CHECKING:
    from typing import Literal

    HAlign = Literal["left", "center", "right", "inherit"]
    VAlign = Literal["top", "middle", "bottom", "inherit"]
else:
    try:
        # noinspection PyUnresolvedReferences,PyUnresolvedReferences
        from typing_extensions import Literal

        HAlign = Literal["left", "center", "right", "inherit"]
        VAlign = Literal["top", "middle", "bottom", "inherit"]
    except ImportError:
        HAlign = VAlign = str

INT_OR_INHERIT = Union[int, Literal["inherit"]]


@dataclass
class Style:
    halign: HAlign = "inherit"
    valign: VAlign = "inherit"
    padding_right: INT_OR_INHERIT = "inherit"
    padding_left: INT_OR_INHERIT = "inherit"


X = TypeVar("X")


# TR = TypeVar('TR', bound=Tuple[str, ...])


def format_rows_as_table(
    rows: Sequence[Sequence[object]], *, style: Union[Literal["none"], BoxStyle] = "pipes"
) -> str:
    cells = {}
    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            cells[(i, j)] = "" if cell is None else str(cell)
    return format_table(cells, style=style)


def color_alternate_lines(row: int, col: int, nrows: int, ncols: int, x: str) -> str:
    from ..ui import get_colorize_function

    color_header = get_colorize_function(None, None, attrs=["bold"])
    color_dark = get_colorize_function(None, None, attrs=["dark"])
    is_header = row == 0

    if is_header:
        return color_header(x)
    else:
        mi = row % 2
        mj = col % 2
        f: Dict[Tuple[int, int], Callable[[str], str]] = {
            (0, 0): str,
            (0, 1): str,
            (1, 0): color_dark,
            (1, 1): color_dark,
        }

        return f[(mi, mj)](x)


def color_none(row: int, col: int, nrows: int, ncols: int, x: str) -> str:
    return x


def format_table(
    cells: Dict[Tuple[int, int], str],
    *,
    draw_grid_v: bool = True,
    draw_grid_h: bool = True,
    style: Union[Literal["none"], BoxStyle] = "pipes",
    light_inside: bool = True,
    color: Optional[str] = None,
    attrs: Optional[List[str]] = None,
    col_style: Optional[Dict[int, Style]] = None,
    row_style: Optional[Dict[int, Style]] = None,
    cell_style: Optional[Dict[Tuple[int, int], Style]] = None,
    table_style: Optional[Style] = None,
    style_fun: Optional[Callable[[str], str]] = None,
    color_cell_function: Callable[[int, int, int, int, str], str] = color_none,
) -> str:
    """
    Styles: "none", "pipes", "lefts3", ...


    """
    default_table_stype = Style()
    default_row_style = Style()
    default_col_style = Style()
    default_cell_style = Style()
    # /media/idsc-nas01-volume1/docker
    #  {
    # -"data-root": "/media/idsc-nas01-volume1/docker"
    #     "runtimes": {
    #         "nvidia": {
    #             "path": "nvidia-container-runtime",
    #             "runtimeArgs": []
    #         }
    #     }
    # #  }
    table_style_: Style = table_style or default_table_stype
    col_styles = col_style or {}
    row_styles = row_style or {}
    cell_styles0 = cell_style or {}

    def get_row_style(row: int) -> Style:
        return row_styles.get(row, default_row_style)

    def get_col_style(col: int) -> Style:
        return col_styles.get(col, default_col_style)

    def get_cell_style(cell: Tuple[int, int]) -> Style:
        return cell_styles0.get(cell, default_cell_style)

    def resolve(a: List[X]) -> X:
        cur = a[0]
        for _ in a:
            if _ == "inherit":
                continue
            else:
                cur = _
        return cur

    def get_style(cell: Tuple[int, int]) -> Style:
        row, col = cell
        rows = get_row_style(row)
        cols = get_col_style(col)
        cels = get_cell_style(cell)
        halign_options: List[HAlign] = ["left", table_style_.halign, rows.halign, cols.halign, cels.halign]
        halign: HAlign = resolve(halign_options)
        valign_options: List[VAlign] = ["top", table_style_.valign, rows.valign, cols.valign, cels.valign]
        valign: VAlign = resolve(valign_options)
        padding_left_: INT_OR_INHERIT = resolve(
            [
                0,
                table_style_.padding_left,
                rows.padding_left,
                cols.padding_left,
                cels.padding_left,
            ]
        )
        padding_right_: INT_OR_INHERIT = resolve(
            [
                0,
                table_style_.padding_right,
                rows.padding_right,
                cols.padding_right,
                cels.padding_right,
            ]
        )
        return Style(
            halign=halign,
            valign=valign,
            padding_left=padding_left_,
            padding_right=padding_right_,
        )

    cells = dict(cells)
    # find all mentioned cells
    mentioned_js = set()
    mentioned_is = set()

    for i, j in cells:
        mentioned_is.add(i)
        mentioned_js.add(j)

    # add default = '' for missing cells
    nrows = max(mentioned_is) + 1 if mentioned_is else 1
    ncols = max(mentioned_js) + 1 if mentioned_js else 1
    coords = list(itertools.product(range(nrows), range(ncols)))
    for c in coords:
        if c not in cells:
            cells[c] = ""

    for (i, j), x in list(cells.items()):
        cells[(i, j)] = color_cell_function(i, j, nrows, ncols, x)

    # find max size for cells
    row_heights = [0] * nrows
    col_widths = [0] * ncols
    for (i, j), s in list(cells.items()):
        dims = text_dimensions(s)
        col_widths[j] = max(col_widths[j], dims.max_width)
        row_heights[i] = max(row_heights[i], dims.nlines)

    any_nonzero_col_width = any(_ > 0 for _ in col_widths)
    if any_nonzero_col_width:
        col_widths = [max(1, _) for _ in col_widths]

    # any_nonzero_row_height = any(_ > 0 for _ in row_heights)
    # if any_nonzero_row_height:
    row_heights = [max(1, _) for _ in row_heights]

    # print(f'row_heights={row_heights} col_widths={col_widths}')
    # pad all cells
    for (i, j), s in list(cells.items()):
        linelength = col_widths[j]
        nlines = row_heights[i]

        cell_style_ = get_style((i, j))

        if cell_style_.padding_left == "inherit":
            padding_left = 0
        else:
            padding_left = cell_style_.padding_left
        if cell_style_.padding_right == "inherit":
            padding_right = 0
        else:
            padding_right = cell_style_.padding_right
        padded = do_padding(
            s,
            linelength=linelength,
            nlines=nlines,
            halign=cell_style_.halign,
            valign=cell_style_.valign,
            padding_left=padding_left,
            padding_right=padding_right,
            style_fun=style_fun,
        )

        ibef: ZO = int_from_bool(i > 0)
        iaft: ZO = int_from_bool(i < nrows - 1)
        jbef: ZO = int_from_bool(j > 0)
        jaft: ZO = int_from_bool(j < ncols - 1)

        def m1(u: ZO, v: ZO) -> ZO:
            if u * v:
                return 1
            else:
                return 0

        neighs: NTuple = (
            (m1(ibef, jbef), ibef, m1(ibef, jaft)),
            (jbef, None, jaft),
            (m1(iaft, jbef), iaft, m1(iaft, jaft)),
        )

        draw_top: int = 1
        draw_left: int = 1
        draw_right: int = 1 if jaft == 0 else 0
        draw_bottom: int = 1 if iaft == 0 else 0

        if not draw_grid_v:
            draw_bottom = draw_top = 0
        if not draw_grid_h:
            draw_left = draw_right = 0
        d = draw_top, draw_right, draw_bottom, draw_left
        # print(f"d={d} neighs={neighs} style={style}")
        if style == "none":
            s = padded
        else:
            s = box(
                padded,
                neighs=neighs,
                style=style,
                draw_borders=d,
                light_inside=light_inside,
                color=color,
                attrs=attrs,
                style_fun=style_fun,
            )

        cells[(i, j)] = s  # .replace(' ', '%')

    parts = []
    for i in range(nrows):
        ss = []
        for j in range(ncols):
            ss.append(cells[(i, j)])

        s = side_by_side(ss, sep="")
        parts.append(s)

    sep = ""
    whole = sep.join(parts)  # OK like this!
    return whole


def wrap_lines(s: str, max_width: int) -> str:
    lines = s.splitlines()
    res = []

    while lines:
        l = lines.pop(0)
        n = get_length_on_screen(l)
        if n <= max_width:
            res.append(l)
        else:
            a = l[:max_width]
            b = "$" + l[max_width:]
            res.append(a)
            lines.insert(0, b)

    return joinlines(res)


def do_padding(
    s: str,
    linelength: int,
    nlines: int,
    halign: HAlign,
    valign: VAlign,
    padding_left: int,
    padding_right: int,
    style_fun: Optional[Callable[[str], str]] = None,
    pad_char: str = " ",
) -> str:
    padded_lines = pad(
        s,
        linelength=linelength,
        nlines=nlines,
        halign=halign,
        valign=valign,
        style_fun=style_fun,
    )
    pl = pad_char * padding_left
    pr = pad_char * padding_right
    if style_fun is not None:
        pl = style_fun(pl)
        pr = style_fun(pr)
    padded_lines = [pl + _ + pr for _ in padded_lines]

    sep = "\n"
    padded = sep.join(padded_lines)
    # padded = joinlines(padded_lines)

    return padded


def int_from_bool(x: bool) -> ZO:
    return 1 if x else 0
