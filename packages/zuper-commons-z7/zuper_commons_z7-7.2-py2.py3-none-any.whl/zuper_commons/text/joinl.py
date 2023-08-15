from typing import Callable, Iterable

from zuper_commons.types import ZAssertionError, ZValueError

__all__ = [
    "apply_by_line",
    "check_lines_normalized",
    "check_wellbehaved_lines",
    "is_string_lines_normalized",
    "joinlines",
    "joinpars",
    "normalize_string_lines",
    "normalize_textlines",
]


def joinpars(pars: Iterable[str]) -> str:
    """
    Join paragraphs (chunks that may contain newlines).
    @param pars: E
    @return:
    """
    res = []
    for par in pars:
        assert isinstance(par, str), par
        if not par.endswith("\n"):
            par += "\n"
        res.append(par)
    return "".join(res)


def joinlines(lines0: Iterable[str]) -> str:
    """This assumes that no line contains a "\\n"."""
    lines = list(lines0)
    for l in lines:
        if "\n" in l:
            msg = f"Invalid input: contains newline {l!r}"
            raise ValueError(msg)
    return "".join(l + "\n" for l in lines)


def check_wellbehaved_lines(s: str) -> None:
    s2 = joinlines(s.splitlines())
    if s2 != s:
        msg = "The text is not well-behaved: joinlines(splitlines(s)) != s"
        raise ZValueError(msg, s=s, s2=s2)


def apply_by_line(f: Callable[[str], str], s: str) -> str:
    return joinlines(map(f, s.splitlines()))


def normalize_textlines(s: str) -> str:
    return joinlines(s.splitlines())


def is_string_lines_normalized(s: str) -> bool:
    if "\n" not in s:
        return True
    return s.endswith("\n")


def check_lines_normalized(s: str) -> None:
    if not is_string_lines_normalized(s):
        msg = "This string is not normalized. Because there is a \\n, it should end with a \\n."
        last = s[-100:]
        raise ZAssertionError(msg, string=repr(last))


def normalize_string_lines(string: str) -> str:
    """
    "a\nb\nc" -> "a\nb\nc\n"
    """
    if "\n" in string:
        if not string.endswith("\n"):
            string += "\n"

    return string
