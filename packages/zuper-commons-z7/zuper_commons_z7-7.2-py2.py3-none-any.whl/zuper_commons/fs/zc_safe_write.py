import gzip
import os
import random
from contextlib import contextmanager
from typing import Any, cast, ContextManager, IO, Iterator, overload, TYPE_CHECKING, Union

from .types import FilePath, Path

if TYPE_CHECKING:
    from typing import Literal
else:
    try:
        from typing import Literal
    except ImportError:
        from typing_extensions import Literal

__all__ = [
    "safe_read",
    "safe_write",
]


def is_gzip_filename(filename: Path) -> bool:
    return ".gz" in filename


#
# @overload
# def safe_write(filename: Path, mode: Literal["wb"], compresslevel: int) -> ContextManager[IO[bytes]]:
#     ...
#
#
# @overload
# def safe_write(filename: Path, mode: Literal["w"], compresslevel: int) -> ContextManager[IO[str]]:
#     ...


@contextmanager
def safe_write(filename: Path, mode: Literal["w", "wb"], compresslevel: int = 5) -> Iterator[IO[Any]]:
    """
    Makes atomic writes by writing to a temp filename.
    Also if the filename ends in ".gz", writes to a compressed stream.
    Yields a file descriptor.

    It is thread safe because it renames the file.
    If there is an error, the file will be removed if it exists.
    """
    dirname = os.path.dirname(filename)
    if dirname:
        if not os.path.exists(dirname):
            # noinspection PyBroadException
            try:
                os.makedirs(dirname, exist_ok=True)
            except:
                pass

                # Dont do this!
                # if os.path.exists(filename):
                # os.unlink(filename)
                #     assert not os.path.exists(filename)
                #
    n = random.randint(0, 10000)
    tmp_filename = "%s.tmp.%s.%s" % (filename, os.getpid(), n)
    try:
        if is_gzip_filename(filename):
            with gzip.open(filename=tmp_filename, mode=mode, compresslevel=compresslevel) as f:
                if mode == "w":
                    yield cast(IO[str], f)
                elif mode == "wb":
                    yield cast(IO[bytes], f)

        else:
            with open(tmp_filename, mode) as f2:
                if mode == "w":
                    yield cast(IO[str], f2)
                elif mode == "wb":
                    yield cast(IO[bytes], f2)
        # f.close()

        # if os.path.exists(filename):
        # msg = 'Race condition for writing to %r.' % filename
        #             raise Exception(msg)
        #
        # On Unix, if dst exists and is a file, it will be replaced silently
        #  if the user has permission.
        os.rename(tmp_filename, filename)
    except:
        if os.path.exists(tmp_filename):
            os.unlink(tmp_filename)
        if os.path.exists(filename):
            os.unlink(filename)
        raise


@overload
def safe_read(filename: FilePath, mode: Literal["rb"]) -> "ContextManager[IO[bytes]]":
    ...


@overload
def safe_read(filename: FilePath, mode: Literal["r"]) -> "ContextManager[IO[str]]":
    ...


if TYPE_CHECKING:

    def safe_read(
        filename: FilePath, mode: Literal["r", "rb"] = "rb"
    ) -> "ContextManager[Union[IO[str], IO[bytes]]]":
        return None  # type: ignore

else:

    @contextmanager
    def safe_read(
        filename: FilePath, mode: Literal["r", "rb"] = "rb"
    ) -> "Iterator[Union[IO[str], IO[bytes]]]":
        """
        If the filename ends in ".gz", reads from a compressed stream.
        Yields a file descriptor.
        """
        try:
            if is_gzip_filename(filename):
                with gzip.open(filename, mode) as f:
                    if mode == "r":
                        yield cast(IO[str], f)
                    elif mode == "rb":
                        yield cast(IO[bytes], f)

            else:
                with open(filename, mode) as f2:
                    if mode == "r":
                        yield cast(IO[str], f2)
                    elif mode == "rb":
                        yield cast(IO[bytes], f2)
        except:
            # TODO
            raise
