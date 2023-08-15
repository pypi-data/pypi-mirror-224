from contextlib import contextmanager
from typing import Iterator, Optional, Type

from zuper_commons.types import ZAssertionError

__all__ = [
    "assert_raises",
    "convert_exception",
]


@contextmanager
def assert_raises(
    ExceptionType: Type[Exception], pass_through: Optional[Type[Exception]] = None, **kwargs: object
) -> Iterator[None]:
    if pass_through is None:
        pass_through = ExceptionType

    # noinspection PyBroadException
    try:
        yield
    except ExceptionType:
        pass
    except pass_through:
        raise
    except BaseException as e:
        raise
        # msg = f"Expected exception {ExceptionType.__name__} but obtained {type(e).__name__}."
        # raise ZAssertionError(msg, **kwargs) from e
    else:
        msg = f"Expected exception {ExceptionType.__name__} but none was thrown."
        raise ZAssertionError(msg, **kwargs)


@contextmanager
def convert_exception(ExceptionType: Type[Exception], e: Exception) -> Iterator[None]:
    """Useful to convert NotImplementedError in SkipTest"""
    try:
        yield
    except ExceptionType as e_:
        raise e from e_
