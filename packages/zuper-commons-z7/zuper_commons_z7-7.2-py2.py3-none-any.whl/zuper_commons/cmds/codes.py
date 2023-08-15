from enum import IntEnum

__all__ = [
    "ExitCode",
    "get_explanation",
]


# ExitCode = NewType('ExitCode', int)


class ExitCode(IntEnum):
    OK = 0
    MISSING_COMMANDS = 100
    WRONG_COMMAND = 101
    OTHER_EXCEPTION = 99

    MISC_CANNOT_FIND = 102
    KEYBOARD_INTERRUPT = 103

    WRONG_CONDITIONS = 104

    WRONG_ARGUMENTS = 2


def get_explanation(c: ExitCode) -> str:
    d = {
        ExitCode.OK: "Success",
        ExitCode.MISSING_COMMANDS: "Missing command",
        ExitCode.WRONG_COMMAND: "Wrong command",
        ExitCode.OTHER_EXCEPTION: "Other exception",
    }
    return d.get(c, f"[unexplained code {c}]")
