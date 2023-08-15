from .colors import color_float, color_magenta, color_yellow

__all__ = [
    "make_chars_visible",
]


def make_chars_visible(x: str, tabsize: int = 4, mark_end: bool = False, use_colors: bool = False) -> str:
    """Replaces whitespaces ' ' and '\t' with '␣' and '⇥'
    @rtype: object
    """
    sp = "␣"
    # if use_colors:
    #     sp = color_par(sp)
    x = x.replace(" ", sp)
    if tabsize == 4:
        tab = "├──┤"
    else:
        tab = "⇥"
    if use_colors:
        tab = color_float(tab)
    x = x.replace("\t", tab)
    #     nl = '␤\n'
    esc = "⏎"
    if use_colors:
        esc = color_yellow(esc)

    nl = esc + "\n"
    x = x.replace("\n", nl)

    if mark_end:
        if "\n" in x:
            eof = "$"
            if use_colors:
                eof = color_magenta(eof)
            x = x + eof
    return x
