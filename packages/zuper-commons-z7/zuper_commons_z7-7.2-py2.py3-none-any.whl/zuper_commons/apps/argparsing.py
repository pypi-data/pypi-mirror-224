import argparse
import sys
from typing import NoReturn, Optional

from zuper_commons.types import ZException

__all__ = [
    "ArgumentParsingException",
    "ArgumentParsingHelp",
    "ZArgumentParser",
]


class ArgumentParsingException(ZException):
    pass


class ArgumentParsingHelp(ZException):
    pass


class ZArgumentParser(argparse.ArgumentParser):
    def exit(self, status: int = 0, message: Optional[str] = None) -> NoReturn:
        if message:
            self._print_message(message, sys.stderr)
        if status == 0:
            raise ArgumentParsingHelp()
        else:
            raise ArgumentParsingException(message)

    def error(self, message: str) -> NoReturn:
        self.print_help(sys.stderr)
        raise ArgumentParsingException(message)
