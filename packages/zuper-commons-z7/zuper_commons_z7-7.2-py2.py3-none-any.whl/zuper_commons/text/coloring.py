import re

# escape = re.compile('\x1b\[..?m')

escape = re.compile(r"\x1b\[[\d;]*?m")
escape1 = re.compile(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]")

__all__ = [
    "get_length_on_screen",
    "remove_escapes",
]


def remove_escapes(s: str) -> str:
    # check_isinstance(s, str)
    if s.isprintable():
        return s
    for es in [escape, escape1]:
        s = es.sub("", s)
    return s


def get_length_on_screen(s: str) -> int:
    """Returns the length of s without the escapes"""
    # check_isinstance(s, str)
    if s.isprintable():
        return len(s)
    return len(remove_escapes(s))
