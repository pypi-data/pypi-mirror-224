from contextlib import contextmanager as orig_contextmanager
from typing import Callable, ContextManager, Iterator, TypeVar

X = TypeVar("X")
# F = TypeVar("F", bound=Callable[..., Iterator[X]])

__all__ = [
    "contextmanager",
]


def contextmanager(f: Callable[..., Iterator[X]]) -> Callable[..., ContextManager[X]]:
    return orig_contextmanager(f)
