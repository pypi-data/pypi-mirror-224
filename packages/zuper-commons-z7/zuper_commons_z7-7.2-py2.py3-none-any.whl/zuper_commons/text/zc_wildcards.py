import re
from typing import cast, Iterator, List, Pattern, Sequence, TypeVar, Union

__all__ = [
    "expand_string",
    "expand_wildcard",
    "get_wildcard_matches",
    "wildcard_matches",
    "wildcard_to_regexp",
]

X = TypeVar("X")


def flatten(seq: Iterator[Sequence[X]]) -> List[X]:
    res: List[X] = []
    for l in seq:
        res.extend(l)
    return res


TS = TypeVar("TS", bound=str)


def expand_string(x: Union[str, Sequence[str]], options: Sequence[TS]) -> List[TS]:
    if isinstance(x, list):
        return flatten(expand_string(y, options) for y in x)
    elif isinstance(x, str):
        x0 = x.strip()
        if "," in x0:
            splat = [_ for _ in x0.split(",") if _]  # remove empty
            return flatten(expand_string(y, options) for y in splat)
        elif "*" in x0:
            return list(expand_wildcard(x0, options))
        else:
            return [cast(TS, x)]
    else:
        raise AssertionError(x)


def wildcard_to_regexp(arg0: str) -> Pattern[str]:
    """Returns a regular expression from a shell wildcard expression."""
    arg = arg0.replace(".", "\\.")
    arg = arg.replace("*", ".*")
    a = re.compile("\A" + arg + "\Z")
    # print(f'arg0 {arg0!r} arg {arg!r} a {a!r}')
    return a


def has_wildcard(s: str) -> bool:
    return s.find("*") > -1


def expand_wildcard(wildcard: str, universe: Sequence[TS]) -> List[TS]:
    """
    Expands a wildcard expression against the given list.
    Raises ValueError if none found.

    :param wildcard: string with '*'
    :param universe: a list of strings
    """
    from zuper_commons.types import ZValueError

    if not has_wildcard(wildcard):
        msg = "No wildcards in %r." % wildcard
        raise ZValueError(msg)

    matches = list(get_wildcard_matches(wildcard, universe))

    if not matches:
        msg = "Could not find matches for pattern."
        raise ZValueError(msg, pattern=wildcard, universe=universe)

    return matches


def get_wildcard_matches(wildcard: str, universe: Sequence[TS]) -> Iterator[TS]:
    """
    Expands a wildcard expression against the given list.
    Yields a sequence of strings.

    :param wildcard: string with '*'
    :param universe: a list of strings
    """
    regexp = wildcard_to_regexp(wildcard)
    for x in universe:
        if regexp.match(x):
            yield x


def wildcard_matches(wildcard: str, x: str) -> bool:
    regexp = wildcard_to_regexp(wildcard)
    return regexp.match(x) is not None
