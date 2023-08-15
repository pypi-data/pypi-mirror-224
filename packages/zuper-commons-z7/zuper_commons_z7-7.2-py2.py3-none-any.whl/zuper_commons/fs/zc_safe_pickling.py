import pickle
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Literal
else:
    try:
        from typing import Literal
    except ImportError:
        from typing_extensions import Literal

from . import logger
from .types import FilePath
from .zc_safe_write import safe_read, safe_write

__all__ = [
    "safe_pickle_dump",
    "safe_pickle_load",
]


# debug_pickling = False


def safe_pickle_dump(
    value: object,
    filename: FilePath,
    protocol: int = pickle.HIGHEST_PROTOCOL,
    mode: Literal["wb"] = "wb",
    compresslevel: int = 5,
) -> None:
    # sys.setrecursionlimit(15000)
    with safe_write(filename, mode=mode, compresslevel=compresslevel) as f:
        try:
            pickle.dump(value, f, protocol)
        except KeyboardInterrupt:
            raise
        except BaseException:
            msg = f"Cannot pickle object of class {type(value)}."
            logger.error(msg)
            #
            # if debug_pickling:
            #     msg = find_pickling_error(value, protocol)
            #     logger.error(msg)
            raise


def safe_pickle_load(filename: FilePath) -> object:
    # TODO: add debug check
    with safe_read(filename, "rb") as f:
        return pickle.load(f)
        # TODO: add pickling debug
