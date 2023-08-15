from typing import cast

from zuper_commons.text import format_error
from .misc_utils import dirname
from .types import DirPath, FilePath

__all__ = [
    "dir_from_package_name",
]

from functools import lru_cache


@lru_cache(maxsize=None)
def dir_from_package_name(d: str) -> DirPath:
    """This works for "package.sub" format. If it's only
    package, we look for __init__.py"""
    if "." in d:
        msg = "There are some bugs for subpackages. Don't use."
        raise NotImplementedError(msg)
    tokens = d.split(".")
    if len(tokens) == 1:
        package = d
        sub = "__init__"
    else:
        package = ".".join(tokens[:-1])
        sub = tokens[-1]
    try:
        from pkg_resources import resource_filename  # @UnresolvedImport

        res = cast(FilePath, resource_filename(package, sub + ".py"))

        if len(tokens) == 1:
            return dirname(res)
        else:
            return res
    except BaseException as e:  # pragma: no cover
        msg = format_error("Cannot resolve package name", d=d)
        raise ValueError(msg) from e
