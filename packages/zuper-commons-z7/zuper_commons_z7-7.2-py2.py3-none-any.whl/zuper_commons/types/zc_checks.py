from typing import Any, NoReturn, Optional, overload, Tuple, Type, TypeVar, Union

from .exceptions import ZAssertionError, ZException, ZValueError

__all__ = [
    "check_isinstance",
    "check_not_None",
    "raise_desc",
    "raise_wrapped",
]

X = TypeVar("X")


# Y = TypeVar("Y")
#
# @overload
# def check_isinstance(ob: X, expected: Type[X], **kwargs: object) -> X:
#     ...
#
#
# @overload
# def check_isinstance(ob: Y, expected: type, **kwargs: object) -> NoReturn:
#     ...


def check_not_None(ob: Optional[X], **kwargs: Any) -> X:
    if ob is None:
        raise ZAssertionError("Expected not None", **kwargs)
    return ob


@overload
def check_isinstance(ob: object, expected: Type[X], **kwargs: object) -> X:
    pass


@overload
def check_isinstance(ob: object, expected: Tuple[Type[X], ...], **kwargs: object) -> X:
    pass


@overload
def check_isinstance(ob: object, expected: Union[type, Tuple[type, ...]], **kwargs: object) -> object:
    pass


def check_isinstance(ob: object, expected: type, **kwargs: object) -> object:
    if not isinstance(ob, expected):
        d = {"object": ob}
        d.update(kwargs)

        msg = f"Object not of expected type: expected {expected}, obtained {type(ob).__name__},"
        raise ZValueError(msg, **d)
    return ob
    # raise_type_mismatch(ob, expected, **kwargs)


#
# def raise_type_mismatch(ob: object, expected: type, **kwargs: object) -> NoReturn:
#     """ Raises an exception concerning ob having the wrong type. """
#     msg = "Object not of expected type:"
#     # e += "\n  expected: {}".format(expected)
#     # e += "\n  obtained: {}".format(type(ob))
#     # try:
#     #     msg = pretty_msg(e, **kwargs)
#     # except:
#     #     msg = e + "(! cannot write message)"
#     raise ZValueError(msg, expected=expected, obtained=type(ob), **kwargs)
#


def raise_desc(etype: Type[BaseException], msg: str, args_first: bool = False, **kwargs: object) -> NoReturn:
    """

    Example:
        raise_desc(ValueError, "I don't know", a=a, b=b)
    """

    from zuper_commons.text import pretty_msg

    assert isinstance(msg, str), type(msg)
    s1 = msg
    if kwargs:
        s2 = pretty_msg("", **kwargs)
    else:
        s2 = ""

    if args_first:
        s = s2 + "\n" + s1
    else:
        s = s1 + "\n" + s2

    raise etype(s)


def raise_wrapped(
    etype: Type[BaseException], e: BaseException, msg: str, compact: bool = False, **kwargs: object
) -> NoReturn:
    if issubclass(etype, ZException):
        # noinspection PyArgumentList
        raise etype(msg, **kwargs) from e

    from zuper_commons.text import indent, pretty_msg

    s = pretty_msg(msg, **kwargs)
    if compact:
        s += "\n" + indent(str(e), "| ")
    raise etype(s) from e

    # if not compact:
    #     raise etype(s) from e
    # else:
    #     e2 = etype(s)
    #     raise e2 from e
