import inspect
import os
import sys
import traceback
from dataclasses import dataclass
from types import FrameType
from typing import Dict

# try:
#     from zuper_typing.common import DictIntStr
# except ImportError:
DictIntStr = dict

DEBUG_CANNOT_PRINT = False
__all__ = [
    "StackInfo",
    "get_stack_info",
]


def get_frame0(stacklevel: int) -> FrameType:
    frame = inspect.currentframe()
    assert frame is not None
    i = 0
    while True:
        if frame.f_back is None:
            from zuper_commons.types import ZException

            raise ZException()
        frame = frame.f_back
        i += 1
        if i == stacklevel:
            return frame


def get_frame(stacklevel: int) -> FrameType:
    # noinspection PyUnresolvedReferences,PyProtectedMember
    frame = sys._getframe(stacklevel)
    return frame
    # i = 0
    # while True:
    #     if frame.f_back is None:
    #         from zuper_commons.types import ZException
    #
    #         raise ZException()
    #     frame = frame.f_back
    #     i += 1
    #     if i == stacklevel:
    #         return frame


#
#
# def get_all_frames(stacklevel: int):
#     frame = inspect.currentframe()
#     i = 0
#     while True:
#         if frame.f_back is None:
#             break
#         frame = frame.f_back
#         i += 1
#         if i >= stacklevel:
#             yield frame
#
#
# def get_frame0(stacklevel: int):
#     stack = inspect.stack()
#     frame = stack[stacklevel]
#     return frame


@dataclass
class StackInfo:
    func_name: str
    filename: str
    lineno: int
    context: Dict[int, str]


#
# def get_full_stack_info(stacklevel: int) -> List[StackInfo]:
#     res = []
#     for f in get_all_frames(stacklevel + 2):
#         res.append(stack_info_from_frame(f))
#     return res
#


def stack_info_from_frame(frame: FrameType) -> StackInfo:
    context: Dict[int, str]
    # noinspection PyBroadException
    try:
        # context_size = 1
        lineno = frame.f_lineno
        pathname = inspect.getsourcefile(frame) or inspect.getfile(frame)
        # finfo = inspect.getframeinfo(frame, context=context_size)
        # finfo = traceback.extract_stack(f=frame.f_back, limit=1)[0]

        # pathname = finfo.filename
        # lineno = finfo.lineno
        funcname = str(frame.f_code.co_name)
        # funcname = str(finfo.function)
        locals_ = frame.f_locals
        context = DictIntStr()
        # for i, l in enumerate(finfo.code_context):
        #     context[lineno - context_size + 1] = l

        # if False:
        #     lines, start_lines = inspect.getsourcelines(frame.f_code)
        #     line_rel = lineno - start_lines
        #
        #     if line_rel >= len(lines) or line_rel < 0:
        #
        #         # print('nlines', len(lines), 'start', start_lines, 'lineno', lineno, 'lines', lines[0])
        #
        #         context = DictIntStr()
        #     else:
        #         context = DictIntStr()
        #         M = 3
        #         for i in range(line_rel - M, line_rel + M + 1):
        #             if 0 <= i < len(lines):
        #                 context[i + start_lines] = lines[i].rstrip()
        # else:
        #     context = DictIntStr()
    except:
        locals_ = {}
        if DEBUG_CANNOT_PRINT:
            funcname = f"!!!could not inspect()!!! {traceback.format_exc()}"
            pathname = "!!!"
        else:
            funcname = ""
            pathname = ""
        lineno = -1
        context = {}
        # print(list(locals))
    if "self" in locals_:
        # print(locals['self'])
        typename = locals_["self"].__class__.__name__
        funcname = typename + ":" + funcname

    return StackInfo(func_name=funcname, filename=pathname, lineno=lineno, context=context)


ENV_NO_STACK = "Z_LOG_NOSTACK"

IGNORE = ENV_NO_STACK in os.environ


def get_stack_info(stacklevel: int) -> StackInfo:
    if IGNORE:
        return StackInfo("n/a", "n/a", -1, {})
        # func_name: str
        # filename: str
        # lineno: int
        # context: Dict[int, str]

    frame = get_frame(stacklevel + 2)
    return stack_info_from_frame(frame)


#     # noinspection PyBroadException
#     try:
#         frame = get_frame(stacklevel + 2)
#         finfo = inspect.getframeinfo(frame, context=1)
#
#         pathname = finfo.filename
#         lineno = finfo.lineno
#         funcname = str(finfo.function)
#         locals_ = frame.f_locals
#
#         lines, start_lines = inspect.getsourcelines(frame.f_code)
#         line_rel = lineno - start_lines
#
#         if line_rel >= len(lines) or line_rel < 0:
#
#             # print('nlines', len(lines), 'start', start_lines, 'lineno', lineno, 'lines', lines[0])
#
#             context = DictIntStr()
#         else:
#             context = DictIntStr()
#             M = 3
#             for i in range(line_rel - M, line_rel + M + 1):
#                 if 0 <= i < len(lines):
#                     context[i + start_lines] = lines[i].rstrip()
#
#     except:
#         locals_ = {}
#         funcname = f"!!!could not inspect()!!! {traceback.format_exc()}"
#         pathname = "!!!"
#         lineno = -1
#         context = []
#         # print(list(locals))
#
#     if "self" in locals_:
#         # print(locals['self'])
#         typename = locals_["self"].__class__.__name__
#         funcname = typename + ":" + funcname
#
#
#     return StackInfo(
#         func_name=funcname, filename=pathname, lineno=lineno, context=context
#     )
#
