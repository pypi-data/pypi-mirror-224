from typing import Callable, cast, Optional, Sequence

import webcolors
from xtermcolor import XTermColorMap

from zuper_commons.types import ZAssertionError, ZValueError

__all__ = [
    "color_blue",
    "color_brown",
    "color_constant",
    "color_cyan",
    "color_dark_gray",
    "color_float",
    "color_gray",
    "color_green",
    "color_int",
    "color_magenta",
    "color_ops",
    "color_ops_light",
    "color_orange",
    "color_pink",
    "color_red",
    "color_synthetic_types",
    "color_typename",
    "color_typename2",
    "color_white_on_blue",
    "color_yellow",
    "colorize_rgb",
    "get_colorize_function",
]

use_cmap = XTermColorMap()


def colorize_rgb(x: str, rgb: Optional[str], bg_color: Optional[str] = None) -> str:
    if rgb is None and bg_color is None:
        return x

    rgb = interpret_color(rgb)
    bg_color = interpret_color(bg_color)

    if rgb is None:
        msg = "We do not support rgb=None"
        raise ZAssertionError(msg, rgb=rgb, bg_color=bg_color)

    fg_int = int(rgb[1:], 16) if rgb is not None else None
    bg_int = int(bg_color[1:], 16) if bg_color is not None else None

    if fg_int is None and bg_int is None:
        return x
    try:
        # r = colorize(x, rgb=fg_int, bg=bg_int)  # ask for stderr
        r = use_cmap.colorize(x, rgb=fg_int, bg=bg_int)

    except Exception as e:
        raise ZValueError(x=x, rgb=rgb, bg_color=bg_color) from e

    if r is None:
        raise NotImplementedError()
    return cast(str, r)


def interpret_color(x: Optional[str]) -> Optional[str]:
    if not x:
        return None
    if x.startswith("#"):
        return x
    return cast(str, webcolors.name_to_hex(x))


def get_colorize_function(
    rgb: Optional[str], bg_color: Optional[str] = None, attrs: Optional[Sequence[str]] = None
) -> Callable[[str], str]:
    T = "template"

    colorized = False
    if rgb is None and bg_color is None:
        Tc = T
    else:
        if rgb is None:
            rgb = "white"
        Tc = colorize_rgb(T, rgb, bg_color)
        colorized = True

    fmt_str = "\033[%dm"
    RESET = fmt_str % 0

    before, _, after = Tc.partition(T)

    if attrs:
        for a in attrs:
            before += fmt_str % ATTRIBUTES[a]
        if not colorized:
            after += RESET

    def f(s: str) -> str:
        assert isinstance(s, str), s
        if "\n" in s:
            lines = s.split("\n")  # OK

            lines2 = [before + _ + after if _ else "" for _ in lines]
            return "\n".join(lines2)
        else:
            return before + s + after

    return f


ATTRIBUTES = {"bold": 1, "dark": 2, "underline": 4, "blink": 5, "reverse": 7, "concealed": 8}

COLOR_ORANGE = "#ffb342"
COLOR_ORANGE_DARK = "#cfa342"

COLOR_WHITE = "#ffffff"
COLOR_RED = "#ff0000"
COLOR_BLUE = "#42a0ff"
# color_blue_light = "#62c0ff"
COLOR_BLUE_LIGHT = "#c2a0ff"
COLOR_GREEN = "#42ffa0"
COLOR_PINK = "#FF69B4"
COLOR_PINK2 = "#FF1493"
COLOR_MAGENTA_1 = "#a000a0"

COLOR_BROWN = "#b08100"
COLOR_YELLOW = "#FFFF00"
COLOR_DARK_GRAY = "#404040"
COLOR_GRAY = "#808080"

color_pink = get_colorize_function(COLOR_PINK2)
color_brown = get_colorize_function(COLOR_BROWN)
color_ops = get_colorize_function(COLOR_BLUE)
color_ops_light = get_colorize_function(COLOR_BLUE_LIGHT)
color_synthetic_types = get_colorize_function(COLOR_GREEN)
color_int = get_colorize_function(COLOR_PINK)
color_float = get_colorize_function(COLOR_PINK2)
color_typename = get_colorize_function(COLOR_ORANGE)
color_typename2 = get_colorize_function(COLOR_ORANGE_DARK)

color_constant = get_colorize_function(COLOR_PINK2)
color_magenta = get_colorize_function(COLOR_MAGENTA_1)
color_yellow = get_colorize_function(COLOR_YELLOW)
color_red = get_colorize_function(COLOR_RED)
color_green = get_colorize_function(COLOR_GREEN)
color_cyan = get_colorize_function("cyan")
color_blue = get_colorize_function(COLOR_BLUE)
color_dark_gray = get_colorize_function(COLOR_DARK_GRAY)
color_gray = get_colorize_function(COLOR_GRAY)
color_white_on_blue = get_colorize_function(COLOR_WHITE, COLOR_BLUE)

color_orange = get_colorize_function("orange")
