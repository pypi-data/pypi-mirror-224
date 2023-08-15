import asyncio
import resource
from contextlib import asynccontextmanager
from typing import AsyncIterator, Optional

from zuper_commons.types import ZException

__all__ = [
    "limit_open_files",
]


class GlobalFSLimits:
    _open_files: Optional[asyncio.BoundedSemaphore] = None

    @staticmethod
    def _get_open_files() -> asyncio.BoundedSemaphore:
        soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
        if soft < 400:
            msg = f"Too few open descriptiors rlimit (soft: {soft}, hard: {hard}). "
            raise ZException(msg)

        if GlobalFSLimits._open_files is None:
            GlobalFSLimits._open_files = asyncio.BoundedSemaphore(200)

        return GlobalFSLimits._open_files


@asynccontextmanager
async def limit_open_files(n: int = 1, desc: str = "n/a") -> AsyncIterator[None]:
    # noinspection PyProtectedMember
    _ = n, desc
    # noinspection PyProtectedMember
    sem = GlobalFSLimits._get_open_files()
    # FIXME: here we should get n tokens from the semaphore, not just one
    async with sem:
        yield
