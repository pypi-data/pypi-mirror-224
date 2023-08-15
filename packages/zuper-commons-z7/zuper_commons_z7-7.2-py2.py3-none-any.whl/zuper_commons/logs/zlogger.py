import asyncio
import logging
import os
import sys
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import timezone
from typing import (
    Callable,
    ClassVar,
    Dict,
    Iterable,
    List,
    Mapping,
    NewType,
    Optional,
    Sequence,
    Set,
    Tuple,
    TYPE_CHECKING,
    Union,
)

if TYPE_CHECKING:
    from typing import Literal
else:
    try:
        from typing import Literal
    except ImportError:
        from typing_extensions import Literal

from .stack import get_stack_info, StackInfo

__all__ = [
    "LevelName",
    "LineFeeds",
    "LogEntry",
    "TAG_RAWLINE",
    "TAG_REDRAW",
    "ZLogger",
    "ZLoggerInterface",
    "get_as_strings",
    "get_min_level",
    "pretty_message",
]

LevelName = NewType("LevelName", str)

ENV_SHOW_MODULES_LOADING = "Z_SHOW_MODULES_LOADING"


@dataclass
class LogEntry:
    timestamp: float
    level: LevelName
    module: List[str]
    prefix: List[str]
    stack_info: StackInfo
    msg: Optional[str]
    kwargs: Dict[str, object]
    tags: List[str]
    labels: Dict[str, object]

    if TYPE_CHECKING:
        from zuper_commons.text import EventID

        event_id: Optional[EventID] = None
    else:
        event_id: Optional[int] = None


TAG_RAWLINE = "raw_line"
TAG_REDRAW = "redraw"
LineFeeds = Literal["\n", "\r", ""]  # empty, in the case of left-over


class ZLoggerInterface(ABC):
    ERROR = LevelName("ERROR")
    WARNING = LevelName("WARNING")
    INFO = LevelName("INFO")
    CRITICAL = LevelName("CRITICAL")
    DEBUG = LevelName("DEBUG")
    USER_ERROR = LevelName("USER_ERROR")
    USER_WARNING = LevelName("USER_WARNING")
    USER_INFO = LevelName("USER_INFO")
    #
    # NOTE_ERROR = LevelName("NOTE_ERROR")
    # NOTE_WARNING = LevelName("NOTE_WARNING")
    # NOTE_TODO = LevelName("NOTE_TODO")

    level_from_level_name: Dict[LevelName, int] = {
        DEBUG: 10,
        INFO: 20,
        WARNING: 30,
        ERROR: 40,
        CRITICAL: 50,
        USER_INFO: 90,
        USER_WARNING: 91,
        USER_ERROR: 92,
        # NOTE_ERROR: 120,
        # NOTE_WARNING: 110,
        # NOTE_TODO: 110,
    }

    @abstractmethod
    def setLevel(self, level0: Union[int, LevelName]) -> None:
        ...

    @abstractmethod
    def info(
        self,
        _msg: Optional[str] = None,
        *args: object,
        stacklevel: int = 0,
        tags: Iterable[str] = (),
        **kwargs: object,
    ) -> LogEntry:
        ...

    @abstractmethod
    def debug(
        self,
        _msg: Optional[str] = None,
        *args: object,
        stacklevel: int = 0,
        tags: Iterable[str] = (),
        **kwargs: object,
    ) -> LogEntry:
        ...

    @abstractmethod
    def warn(
        self,
        _msg: Optional[str] = None,
        *args: object,
        stacklevel: int = 0,
        tags: Iterable[str] = (),
        **kwargs: object,
    ) -> LogEntry:
        ...

    @abstractmethod
    def warning(
        self,
        _msg: Optional[str] = None,
        *args: object,
        stacklevel: int = 0,
        tags: Iterable[str] = (),
        **kwargs: object,
    ) -> LogEntry:
        ...

    @abstractmethod
    def error(
        self,
        _msg: Optional[str] = None,
        *args: object,
        stacklevel: int = 0,
        tags: Iterable[str] = (),
        **kwargs: object,
    ) -> LogEntry:
        ...

    @abstractmethod
    def user_error(
        self,
        _msg: Optional[str] = None,
        *args: object,
        stacklevel: int = 0,
        tags: Iterable[str] = (),
        **kwargs: object,
    ) -> LogEntry:
        ...

    @abstractmethod
    def user_info(
        self,
        _msg: Optional[str] = None,
        *args: object,
        stacklevel: int = 0,
        tags: Iterable[str] = (),
        **kwargs: object,
    ) -> LogEntry:
        ...

    @abstractmethod
    def raw_line(
        self,
        level: LevelName,
        channel: str,
        line: str,
        term: Optional[LineFeeds] = None,
        stacklevel: int = 0,
        timestamp: Optional[float] = None,
    ) -> LogEntry:
        ...

    @abstractmethod
    def get_child(
        self,
        names: Union[str, Sequence[str]],
        prefix: Sequence[str] = (),
        tags: Sequence[str] = (),
    ) -> "ZLoggerInterface":
        ...

    @abstractmethod
    def hello_module(self, name: str, version: str, filename: str, date: Optional[str] = None) -> None:
        ...

    @abstractmethod
    def hello_module_finished(self, name: str) -> None:
        ...

    @abstractmethod
    def log_entry(self, le: LogEntry) -> None:
        ...


def get_min_level(*, prefix: List[str], module: List[str]) -> int:
    prefix2 = tuple(prefix)
    module2 = tuple(module)

    def get_best_match(a: Dict[Tuple[str, ...], int], spec: Tuple[str, ...]) -> int:
        while spec:
            if spec in a:
                return a[spec]
            spec = spec[:-1]
        raise KeyError()

    try:
        m1 = get_best_match(ZLogger.name_to_level, module2)
    except KeyError:
        m1 = 0
    try:
        m2 = get_best_match(ZLogger.prefix_to_level, prefix2)
    except KeyError:
        m2 = 0
    return max(m1, m2)


def get_as_strings(msg: Optional[str], kwargs: Dict[str, object]) -> str:
    # kwargs3 = {}
    fmsg = msg
    #
    # for k, v in kwargs.items():
    #     pf = ZLogger.get_render_function(v)
    #     # noinspection PyBroadException
    #     try:
    #         v = pf(v)
    #     except:
    #         v = f"!!! Cannot write {k!r} ({type(v)}): {traceback.format_exc()}"
    #     if k == "msg":
    #         fmsg = v
    #     else:
    #         kwargs3[k] = v
    if fmsg is None:
        fmsg = ""
    pmsg = pretty_message(fmsg, (), kwargs)
    return pmsg


@dataclass
class InitModuleStack:
    name: str
    others: float
    loaded: List[str]


class StackManage:
    stack: List[InitModuleStack] = []

    modules: Dict[str, Tuple[float, str, str, Optional[str], Optional[str]]] = {}
    already_shown: Set[str] = set()

    @staticmethod
    def hello_module(name: str, version: str, filename: Optional[str], date: Optional[str] = None) -> None:
        stack = StackManage.stack
        StackManage.modules[name] = (time.time(), name, version, filename, date)
        loaded = list(sys.modules.keys())
        stack.append(InitModuleStack(name, 0, loaded))
        # names = [_.name for _ in stack]
        # sys.stderr.write(f'stack: {names}\n')

    @staticmethod
    def hello_module_finished(name: str) -> None:
        from zuper_commons.ui import duration_compact
        from zuper_commons.timing import now_utc

        stack = StackManage.stack
        if not stack:
            sys.stderr.write(f"ERROR: no stack when closing {name}\n")
            return

        if stack[-1].name != name:
            sys.stderr.write(f"ERROR: Forgot to close {stack[-1].name} now = {name}\n")
            return

        (t0, name, version, filename, date) = StackManage.modules[name]
        dt = time.time() - t0
        others = stack[-1].others
        previous_loaded = stack[-1].loaded
        loaded = list(sys.modules.keys())
        new_loaded = [m for m in loaded if m not in previous_loaded]
        new_loaded = [
            m
            for m in new_loaded
            if not any(m.startswith(_.name) for _ in stack)
            and not any(m.startswith(_) for _ in StackManage.modules)
        ]
        new_loaded = [m for m in new_loaded if m not in StackManage.already_shown]
        new_loaded = sorted(set([m.split(".")[0] for m in new_loaded]))
        net = dt - others
        # sys.stderr.write(f'{name:15}  others {others} net {int(net * 1000)} ms total {int(dt * 1000):5}
        # ms\n')
        # noinspection PyBroadException
        try:
            if date is not None:
                from zuper_commons.dates import flexible_parse

                p = flexible_parse(date)
                p = p.astimezone(tz=timezone.utc)

                s = duration_compact((now_utc() - p).total_seconds())
            else:
                s = "?"
        except:
            s = "?"

        if ENV_SHOW_MODULES_LOADING in os.environ:
            nload = len(new_loaded)
            msg = f"{name:25} {version:12} {s:12}  net {int(net * 1000):6} ms   tot {int(dt * 1000):5} "
            if nload:
                msg += f"   nload={nload}"

            sys.stderr.write(msg + "\n")

            if new_loaded:
                sys.stderr.write(f' loaded = {", ".join(new_loaded)} \n')

        StackManage.already_shown.update(new_loaded)
        # msg = f'{version:12} {s:5} {name:25} '

        stack.pop(-1)
        # sys.stderr.write(f'poppoed {p.name}\n')
        if stack:
            stack[-1].others += dt
        else:
            pass
            # sys.stderr.write(f'No stack after {name}\n')


class ZLogger(ZLoggerInterface):
    queue = asyncio.Queue()  # type: ignore
    queue_sentinel_eof = -1

    registered: "Dict[Tuple[str, ...], ZLogger]" = {}
    prefix_to_level: Dict[Tuple[str, ...], int] = {}
    name_to_level: Dict[Tuple[str, ...], int] = {}
    renderers: ClassVar[Dict[str, Callable[[object], str]]] = {"object": str}
    enable_simple = True

    # logger: Logger
    # debug_print = str

    name: Tuple[str, ...]
    prefix: Tuple[str, ...]
    tags: Tuple[str, ...]

    def __init__(
        self,
        name: Union[str, Tuple[str, ...]],
        prefix: Tuple[str, ...] = (),
        tags: Tuple[str, ...] = (),
    ):
        if isinstance(name, str):
            name = (name,)
        # name = name.replace("zuper_", "")
        assert isinstance(name, tuple), name
        for _ in name:
            assert isinstance(_, str), name
        assert isinstance(prefix, tuple), prefix
        for _ in prefix:
            assert isinstance(_, str), prefix
        assert isinstance(tags, tuple), tags

        for _ in tags:
            assert isinstance(_, str), tags
        self.name = name
        self.prefix = prefix
        self.level = logging.DEBUG
        self.tags = tags

        ZLogger.registered[name] = self
        # self.disable_version = "Z_LOGGER_NO_VERSIONS" in os.environ

    def hello_module(
        self, name: str, version: Optional[str], filename: Optional[str], date: Optional[str] = None
    ) -> None:
        StackManage.hello_module(name=name, version=version, filename=filename, date=date)
        # self.debug(
        #     module=name,
        #     filename=filename,
        #     version=version,
        #     date=date,
        #     tags=(TAG_VERSION,),
        # )

    def hello_module_finished(self, name: str) -> None:
        return StackManage.hello_module_finished(name)

    def info(
        self,
        _msg: Optional[str] = None,
        *args: object,
        stacklevel: int = 0,
        tags: Iterable[str] = (),
        **kwargs: object,
    ) -> LogEntry:
        return self._log(
            level=ZLogger.INFO,
            msg=_msg,
            args=args,
            stacklevel=stacklevel + 1,
            kwargs=kwargs,
            tags=tags,
        )

    def debug(
        self,
        _msg: Optional[str] = None,
        *args: object,
        stacklevel: int = 0,
        tags: Iterable[str] = (),
        **kwargs: object,
    ) -> LogEntry:
        return self._log(
            level=ZLogger.DEBUG,
            msg=_msg,
            args=args,
            stacklevel=stacklevel + 1,
            kwargs=kwargs,
            tags=tags,
        )

    def warn(
        self,
        _msg: Optional[str] = None,
        *args: object,
        stacklevel: int = 0,
        tags: Iterable[str] = (),
        **kwargs: object,
    ) -> LogEntry:
        return self._log(
            level=ZLogger.WARNING,
            msg=_msg,
            args=args,
            stacklevel=stacklevel + 1,
            kwargs=kwargs,
            tags=tags,
        )

    def warning(
        self,
        _msg: Optional[str] = None,
        *args: object,
        stacklevel: int = 0,
        tags: Iterable[str] = (),
        **kwargs: object,
    ) -> LogEntry:
        return self._log(
            level=ZLogger.WARNING,
            msg=_msg,
            args=args,
            stacklevel=stacklevel + 1,
            kwargs=kwargs,
            tags=tags,
        )

    def error(
        self,
        _msg: Optional[str] = None,
        *args: object,
        stacklevel: int = 0,
        tags: Iterable[str] = (),
        **kwargs: object,
    ) -> LogEntry:
        return self._log(
            level=ZLogger.ERROR,
            msg=_msg,
            args=args,
            stacklevel=stacklevel + 1,
            kwargs=kwargs,
            tags=tags,
        )

    def user_error(
        self,
        _msg: Optional[str] = None,
        *args: object,
        stacklevel: int = 0,
        tags: Iterable[str] = (),
        **kwargs: object,
    ) -> LogEntry:
        return self._log(
            level=ZLogger.USER_ERROR,
            msg=_msg,
            args=args,
            stacklevel=stacklevel + 1,
            kwargs=kwargs,
            tags=tags,
        )

    def user_info(
        self,
        _msg: Optional[str] = None,
        *args: object,
        stacklevel: int = 0,
        tags: Iterable[str] = (),
        **kwargs: object,
    ) -> LogEntry:
        return self._log(
            level=ZLogger.USER_INFO,
            msg=_msg,
            args=args,
            stacklevel=stacklevel + 1,
            kwargs=kwargs,
            tags=tags,
        )

    def raw_line(
        self,
        level: LevelName,
        channel: str,
        line: str,
        term: Optional[LineFeeds] = None,
        stacklevel: int = 0,
        timestamp: Optional[float] = None,
        labels: Optional[Dict[str, object]] = None,
    ) -> LogEntry:
        stack_info = get_stack_info(stacklevel + 1)
        if timestamp is None:
            timestamp = time.time()
        tags = list(self.tags)
        tags.append(TAG_RAWLINE)
        if line.endswith("\r"):
            tags.append(TAG_REDRAW)
        if labels is None:
            labels = {}
        le = LogEntry(
            timestamp=timestamp,
            msg=line,
            level=level,
            kwargs={},
            stack_info=stack_info,
            module=list(self.name),
            tags=tags,
            prefix=list(self.prefix) + [channel],
            labels=labels,
        )

        if ZLogger.enable_simple:
            min_level = get_min_level(prefix=le.prefix, module=le.module)
            c = ZLogger.level_from_level_name[le.level]
            if c >= min_level:
                # else:
                # fn = os.path.basename(le.filename)
                # if fn == '__init__.py':
                #     fn = os.path.basename(os.path.dirname(le.filename))
                # s = f'{le.level} {fn} {le.func_name}(): {le.msg}'
                prefix = "^ "
                s = get_as_strings(le.msg, le.kwargs)
                for line in s.splitlines():
                    sys.stderr.write(prefix + line + "\n")

        ZLogger.queue.put_nowait(le)
        return le

    @staticmethod
    def get_render_function(x: object) -> Callable[[object], str]:
        T = type(x)
        if isinstance(x, str):
            return str

        if isinstance(x, type):
            return ZLogger.renderers["object"]
        else:
            # noinspection PyArgumentList
            mro = T.mro()

            for K in mro:
                if K.__name__ in ZLogger.renderers:
                    return ZLogger.renderers[K.__name__]
            raise AssertionError(mro)

    def _log(
        self,
        level: LevelName,
        msg: Optional[str],
        args: Tuple[object, ...],
        stacklevel: int,
        tags: Iterable[str],
        kwargs: Dict[str, object],
        labels: Optional[Dict[str, object]] = None,
    ) -> LogEntry:
        if labels is None:
            labels = {}
        if not isinstance(msg, (str, type(None))):
            raise ValueError(f"not a string: {type(msg)}")
        stack_info = get_stack_info(stacklevel + 1)
        for i, a in enumerate(args):
            kwargs[str(i)] = a

        kwargs2 = {}
        for k, v in kwargs.items():
            if type(v).__name__ == "Tag":
                v2 = v
            else:
                # pf = self.get_render_function(v)
                # v2 = pf(v)
                v2 = v
            kwargs2[k] = v2
        # pmsg = pretty(msg, args, kwargs)
        le = LogEntry(
            timestamp=time.time(),
            # lineno=stack_info.lineno,
            msg=msg,
            level=level,
            kwargs=kwargs2,
            stack_info=stack_info,
            # filename=stack_info.pathname,
            # func_name=stack_info.func_name,
            module=list(self.name),
            tags=list(self.tags) + list(tags),
            prefix=list(self.prefix),
            labels=labels,
        )
        self.log_entry(le)
        return le

    def log_entry(self, le: LogEntry) -> None:
        if ZLogger.enable_simple:
            # if TAG_VERSION in le.tags:
            #     if not self.disable_version:
            #         try:
            #
            #             p = flexible_parse(le.kwargs["date"])
            #             p = p.astimezone(tz=timezone.utc)
            #
            #             from zuper_commons.ui import duration_compact
            #             from zuper_commons.timing import now_utc
            #
            #             s = duration_compact((now_utc() - p).total_seconds())
            #         except:
            #             s = "?"
            #
            #         msg = f'{le.kwargs["version"]:12} {s:5} {le.kwargs["module"]:25} '
            #         sys.stderr.write(msg + "\n")
            # else:
            min_level = get_min_level(prefix=le.prefix, module=le.module)
            c = ZLogger.level_from_level_name[le.level]
            if c >= min_level:
                fn = os.path.basename(le.stack_info.filename)
                if fn == "__init__.py":
                    fn = os.path.basename(os.path.dirname(le.stack_info.filename))

                kwargs3 = {}
                for k, v in le.kwargs.items():
                    pf = self.get_render_function(v)
                    kwargs3[k] = pf(v)
                pmsg = pretty_message(le.msg or "", (), kwargs3)
                # msg = le.msg.rstrip("\n")
                s = f"{le.level} {fn} {le.stack_info.func_name}(): {pmsg}"
                sys.stderr.write(s + "\n")
                sys.stderr.flush()

        ZLogger.queue.put_nowait(le)

    def get_child(
        self,
        names: Union[str, Sequence[str]],
        prefix: Sequence[str] = (),
        tags: Sequence[str] = (),
    ) -> "ZLogger":
        # logger_child = self.logger.getChild(child_name)
        if isinstance(names, str):
            names = names.split(".")
        if not isinstance(names, (list, tuple)):
            msg = f"Need a sequence of str, got {names!r}"
            raise ValueError(msg)
        if not isinstance(prefix, (list, tuple)):
            msg = f"Need a sequence of str, got {prefix!r}"
            raise ValueError(msg)
        if not isinstance(tags, (list, tuple, set)):
            msg = f"Need a sequence of str, got {tags!r}"
            raise ValueError(msg)
        child_name = self.name + tuple(names)
        child_prefix = self.prefix + tuple(prefix)
        child_tags = tuple(sorted(set(self.tags + tuple(tags))))
        return ZLogger(child_name, child_prefix, child_tags)

    def setLevel(self, level0: Union[int, LevelName]) -> None:
        if isinstance(level0, str):
            # noinspection PyTypeChecker
            level = ZLogger.level_from_level_name[level0]
        else:
            level = level0
        self.level = level
        ZLogger.name_to_level[self.name] = level
        ZLogger.prefix_to_level[self.prefix] = level


#

#
# def get_print_function():
#     if ZLogger.debug_print is None:  # pragma: no cover
#         try:
#             # noinspection PyUnresolvedReferences
#             from zuper_typing import debug_print
#
#             ZLogger.debug_print = debug_print
#         except ImportError:
#             ZLogger.debug_print = str
#     return ZLogger.debug_print


def pretty_message(msg: str, args: Tuple[object, ...], kwargs: Mapping[str, object]) -> str:
    from ..text import pretty_dict

    res = {}

    def lab(x: str) -> str:
        return x
        # return termcolor.colored(x, attrs=["dark"])

    for i, a in enumerate(args):
        pf = ZLogger.get_render_function(a)
        use = str(i)
        res[lab(use)] = pf(a)

    for k, v in kwargs.items():
        pf = ZLogger.get_render_function(v)
        rendered = pf(v)
        if k == "msg":
            msg = rendered
        else:
            res[lab(k)] = rendered

    if res:
        s = pretty_dict(msg, res, leftmargin=" ", omit_falsy=False)
    else:
        s = msg
    return s
    #
    # if not self.logger.is_enabled_for(level):
    #     return
