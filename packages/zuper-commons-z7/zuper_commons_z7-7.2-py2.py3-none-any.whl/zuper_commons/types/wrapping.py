from typing import Any, Callable, cast, TypeVar

__all__ = [
    "mywraps",
    "unwrap",
]

F = TypeVar("F", bound=Callable[..., Any])

G = TypeVar("G", bound=Callable[..., Any])


def unwrap(f: F) -> F:
    """Unwraps the original function through __wrapped__"""
    if hasattr(f, "__wrapped__"):
        return cast(F, unwrap(getattr(f, "__wrapped__")))
    else:
        return f


def mywraps(f: F) -> Callable[[G], G]:
    def _(f2: G) -> G:
        attrs = "__module__", "__name__", "__qualname__", "__doc__", "__annotations__"
        for attr in attrs:
            if hasattr(f, attr):
                setattr(f2, attr, getattr(f, attr))
        setattr(f2, "__wrapped__", f)
        return f2

    return _
