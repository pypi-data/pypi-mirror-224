import os
import sys
from contextlib import contextmanager
from functools import lru_cache
from typing import Any, Callable, cast, ClassVar, Dict, Iterator, MutableMapping, Optional

from typing_extensions import TypedDict

from zuper_commons.logs.stack import StackInfo

__all__ = [
    "AddContextOptions",
    "PASS_THROUGH",
    "PrintingError",
    "ZAssertionError",
    "ZCannotConnect",
    "ZEnvironmentException",
    "ZException",
    "ZExceptionDict",
    "ZFinalEnvironmentException",
    "ZKeyError",
    "ZNotImplementedError",
    "ZTempEnvironmentException",
    "ZTimeoutError",
    "ZTypeError",
    "ZValueError",
    "add_context",
    "add_info",
    "disable_colored",
]

PASS_THROUGH = (KeyboardInterrupt,)


class ZExceptionDict(TypedDict, total=False):
    pass


class ZException(Exception):
    msg: Optional[str]
    info: ZExceptionDict  # Dict[str, object]
    st: Optional[str]  # string representation

    entries_formatter: ClassVar[Callable[[object], str]] = repr

    # Allows a specific formatting for each KEY
    prop_formatting: ClassVar[Dict[str, Callable[[object], str]]] = {}

    def __init__(self, msg: Optional[str] = None, **info: object) -> None:
        self.st = None
        assert isinstance(msg, (str, type(None))), msg
        self.msg = msg
        self.info = cast(ZExceptionDict, info)

        # self.info['caller'] = get_stack_info(stacklevel+1)
        # self.info['stack'] = get_full_stack_info(stacklevel + 1)

    def pop_info_key(self, key: str) -> None:
        if key in self.info:
            self.info.pop(key)
            self.st = None

    def __str__(self) -> str:
        if self.st is None:
            try:
                self.st = self.get_str()
            except PASS_THROUGH:  # pragma: no cover
                raise
            #
            # except BaseException as e:
            #     self.st  = f"!!! could not print: {e}"
        assert self.st is not None
        return self.st

    def get_str(self) -> str:
        entries = {}
        for k, v in self.info.items():
            if k in ZException.prop_formatting:
                f = ZException.prop_formatting[k]
                try:
                    entries[k] = f(v)
                except Exception as e:
                    # noinspection PyBroadException
                    try:
                        entries[k] = f"!!! cannot print (prop {k} {f}): {e}"
                    except:
                        entries[k] = f"!!! cannot print (prop {k} {f}), and cannot print exception."
            else:
                # pf = ZLogger.get_render_function(v)
                try:
                    # noinspection PyCallByClass
                    entries[k] = ZException.entries_formatter(v)
                except Exception as e:
                    # noinspection PyBroadException
                    try:
                        entries[k] = f"!!! cannot print (ZException entries_formatter): {e}"
                    except:
                        entries[k] = (
                            f"!!! cannot print (ZException entries_formatter), and cannot print "
                            f"exception."
                        )

        if not self.msg:
            self.msg = ""
        assert self.msg is not None
        from zuper_commons.text import pretty_dict

        if len(entries) == 1:
            first = list(entries)[0]
            payload = entries[first]
            s = self.msg + f"\n{first}:\n{payload}"

        elif entries:
            s = pretty_dict(self.msg, entries)
        else:
            s = self.msg

        # s = sanitize_circle_ci(s)
        return s

    def __repr__(self) -> str:
        return self.__str__()


class ZEnvironmentException(ZException):
    pass


class ZTempEnvironmentException(ZEnvironmentException):
    pass


class ZCannotConnect(ZTempEnvironmentException):
    """Cannot connect to a resource"""


class ZFinalEnvironmentException(ZEnvironmentException):
    pass


def format_stack_info(si: StackInfo, C: int = 2) -> str:
    from zuper_commons.ui import color_ops
    from zuper_commons.text import joinlines

    ss = [f"In {si.func_name}, {si.filename}:{si.lineno}"]
    for lineno, line in si.context.items():
        if (si.lineno - C <= lineno <= si.lineno + C) and line.strip():
            if lineno == si.lineno:
                line = color_ops(line)
            prefix = f" {lineno:3d} | "
            ss.append(prefix + line)
    return joinlines(ss)


# def format_stack(a: List[StackInfo]) -> str:
#     return "\n".join(format_stack_info(_, C=1) for _ in reversed(a[:5]))


# ZException.prop_formatting["stack"] = format_stack


def disable_colored() -> bool:
    circle_job = os.environ.get("CIRCLE_JOB", None)
    return circle_job is not None


def sanitize_circle_ci(s: str) -> str:
    if disable_colored():
        from zuper_commons.text.coloring import remove_escapes

        s = remove_escapes(s)
        difficult = ["┋"]
        for c in difficult:
            s = s.replace(c, "")
        return s
    else:
        return s


class ZTypeError(ZException, TypeError):
    pass


class ZValueError(ZException, ValueError):
    pass


class ZKeyError(ZException, KeyError):
    pass


class ZAssertionError(ZException, AssertionError):
    pass


class ZNotImplementedError(ZException, NotImplementedError):
    pass


class ZIndexError(ZException, IndexError):
    pass


class ZAttributeError(ZException, AttributeError):
    pass


class ZTimeoutError(ZException, TimeoutError):
    pass


class PrintingError(Exception):
    pass


@contextmanager
def convert_simple_exceptions() -> Iterator[None]:
    try:
        yield
    except ZException:
        raise
    except AssertionError as e:
        # if e.args:
        #     raise ZAssertionError(value=e.args[0]) from e
        # else:
        raise ZAssertionError(str(e)) from e
    except ValueError as e:
        # if e.args:
        #     raise ZValueError(value=e.args[0]) from e
        # else:
        raise ZValueError(str(e)) from e
    except TypeError as e:
        # if e.args:
        #     raise ZTypeError(value=e.args[0]) from e
        # else:
        raise ZTypeError(str(e)) from e
    except KeyError as e:
        # if e.args:
        #     raise ZTypeError(value=e.args[0]) from e
        # else:
        raise ZKeyError(str(e)) from e
    except IndexError as e:
        # if e.args:
        #     raise ZTypeError(value=e.args[0]) from e
        # else:
        raise ZIndexError(str(e)) from e
    except AttributeError as e:
        # if e.args:
        #     raise ZTypeError(value=e.args[0]) from e
        # else:
        raise ZAttributeError(str(e)) from e
    except TimeoutError as e:
        raise ZTimeoutError(str(e)) from e


class AddContextOptions:
    use_line: ClassVar[bool] = False


# if __debug__:
#     AddContextOptions.use_line = True
#     # logger.info('debug is activated, using "AddContextOptions.use_line"')


@lru_cache(maxsize=1000)
def _relpath(x: str) -> str:
    return os.path.relpath(x)


@contextmanager
def add_context(stacklevel: int = 0, **kwargs0: object) -> Iterator[MutableMapping[str, object]]:
    d: dict[str, object] = dict(kwargs0)
    if AddContextOptions.use_line:
        # FIXME: too slow
        co = sys._getframe(2 + stacklevel).f_code  # type: ignore
        fn = _relpath(co.co_filename)

        up = "%s() %s:%d" % (co.co_name, fn, co.co_firstlineno)
        d2 = {"_where": up}
        d2.update(d)
        d = d2
    kwargs = {"context": d}
    try:
        with convert_simple_exceptions():
            yield d
    except PrintingError:
        raise
    except ZException as e:
        e_info = cast(Dict[str, Any], e.info)
        for k, v in kwargs.items():
            if k not in e.info:
                e_info[k] = v
                continue

            cur = e_info.get(k, ())
            # if cur != v:
            if isinstance(v, tuple):
                vv = v
            else:
                vv = (v,)
            if isinstance(cur, tuple):
                pass
            else:
                cur = (cur,)
            # try:
            # e_info[k] = vv + cur # most recent last
            e_info[k] = cur + vv  # most recent first
            # except TypeError as ee:
            #     e.info['EERRROR'] = f'k = {k} vv = {vv}  cur = {cur} {ee}'
        raise
    except Exception as e:
        from . import logger

        logger.error("Context for exception", exception_type=str(type(e)), context=kwargs)
        raise


@contextmanager
def add_info(**kwargs: object) -> Iterator[None]:
    try:
        yield
    except ZException as e:
        new_one = dict(kwargs)
        e_info = cast(Dict[str, Any], e.info)
        new_one.update(e_info)
        e.info = new_one  # type: ignore
        # for k, v in kwargs.items():
        #     e_info[k] = v
        raise
