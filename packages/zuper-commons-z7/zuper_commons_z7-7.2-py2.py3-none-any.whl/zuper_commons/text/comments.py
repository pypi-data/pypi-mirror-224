__all__ = [
    "remove_hash_comments",
]

from .joinl import joinlines


def remove_hash_comments(s: str, remove_empty_lines: bool, comment_char: str = "#") -> str:
    def remove_comments(a: str) -> str:
        try:
            i = a.index(comment_char)
        except ValueError:
            return a
        else:
            return a[:i].rstrip()

    lines = s.splitlines()
    lines = list(map(remove_comments, lines))
    out = []
    for line in lines:
        if remove_empty_lines:
            line_stripped = line.strip(" ")
        else:
            line_stripped = line
        if line_stripped:
            out.append(line_stripped)
    return joinlines(out)
