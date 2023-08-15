import fnmatch
import os
import time
from collections import defaultdict
from typing import Any, Callable, cast, Dict, Iterator, List, Optional, Sequence, Tuple, Union

from zuper_commons.types import check_isinstance
from . import logger
from .misc_utils import join, realpath
from .types import DirPath, FilePath, Path, RelDirPath, RelFilePath

__all__ = [
    "locate_dirs_only",
    "locate_files",
    "locate_files_only",
    "walk_typed",
]


def locate_files_only(
    directory: DirPath,
    pattern: Union[str, Sequence[str]],
    followlinks: bool = True,
    normalize: bool = True,
    ignore_patterns: Optional[Sequence[str]] = None,
) -> Sequence[FilePath]:
    return cast(
        Sequence[FilePath],
        locate_files(
            directory,
            pattern,
            followlinks=followlinks,
            include_directories=False,
            include_files=True,
            normalize=normalize,
            ignore_patterns=ignore_patterns,
        ),
    )


def locate_dirs_only(
    directory: DirPath,
    pattern: Union[str, Sequence[str]],
    followlinks: bool = True,
    normalize: bool = True,
    ignore_patterns: Optional[Sequence[str]] = None,
) -> Sequence[DirPath]:
    return cast(
        Sequence[DirPath],
        locate_files(
            directory,
            pattern,
            followlinks=followlinks,
            include_directories=True,
            include_files=False,
            normalize=normalize,
            ignore_patterns=ignore_patterns,
        ),
    )


def locate_files(
    directory: DirPath,
    pattern: Union[str, Sequence[str]],
    followlinks: bool = True,
    include_directories: bool = False,
    include_files: bool = True,
    normalize: bool = True,
    ignore_patterns: Optional[Sequence[str]] = None,
) -> Sequence[Path]:
    """
    pattern is either a string or a sequence of strings

    NOTE: if you do not pass ignore_patterns, it will use  MCDPConstants.locate_files_ignore_patterns

    ignore_patterns = ['*.bak']

    normalize = uses realpath
    """
    if not os.path.exists(directory):
        msg = f"Root directory does not exist: {directory}"
        logger.warning(msg)
        return []
        # raise ValueError(msg)

    t0 = time.time()

    ignore_patterns_: List[str]
    if ignore_patterns is None:
        ignore_patterns_ = []
    else:
        ignore_patterns_ = list(ignore_patterns)

    patterns: Sequence[str]
    if isinstance(pattern, str):
        patterns = [pattern]
    else:
        patterns = list(pattern)
        for p in patterns:
            check_isinstance(p, str)
    # directories visited
    # visited = set()
    # visited_basename = set()
    # print('locate_files %r %r' % (directory, pattern))
    filenames: List[Path] = []

    def matches_pattern(x: str) -> bool:
        return any(fnmatch.fnmatch(x, _) or (x == _) for _ in patterns)

    def should_ignore_resource(x: str) -> bool:
        return any(fnmatch.fnmatch(x, _) or (x == _) for _ in ignore_patterns_)

    def accept_dirname_to_go_inside(_root_: DirPath, d_: DirPath) -> bool:
        if should_ignore_resource(d_):
            return False
        # XXX
        # dd = os.path.realpath(os.path.join(root_, d_))
        # if dd in visited:
        #     return False
        # visited.add(dd)
        return True

    def accept_dirname_as_match(_: DirPath) -> bool:
        return include_directories and not should_ignore_resource(_) and matches_pattern(_)

    def accept_filename_as_match(_: FilePath) -> bool:
        return include_files and not should_ignore_resource(_) and matches_pattern(_)

    ntraversed = 0
    for root0, dirnames0, files in os.walk(directory, followlinks=followlinks):
        root = cast(DirPath, root0)
        ntraversed += 1
        dirnames = [
            cast(DirPath, _) for _ in dirnames0 if accept_dirname_to_go_inside(root, cast(DirPath, _))
        ]
        for f in cast(List[RelFilePath], files):
            # logger.info('look ' + root + '/' + f)
            if accept_filename_as_match(cast(FilePath, f)):
                filenames.append(join(root, f))
        for d in cast(List[RelDirPath], dirnames):
            if accept_dirname_as_match(cast(DirPath, d)):
                filenames.append(join(root, d))

    if normalize:
        real2norm: Dict[Path, List[Path]] = defaultdict(list)
        for norm in filenames:
            real = realpath(norm)
            real2norm[real].append(norm)
            # print('%s -> %s' % (real, norm))

        for k, v in real2norm.items():
            if len(v) > 1:
                msg = f"In directory:\n\t{directory}\n"
                msg += f"I found {len(v)} paths that refer to the same file:\n"
                for n_ in v:
                    msg += f"\t{n_}\n"
                msg += f"refer to the same file:\n\t{k}\n"
                msg += "I will silently eliminate redundancies."
                # logger.warning(msg) # XXX

        filenames = list(real2norm.keys())

    seconds = time.time() - t0

    if seconds > 5:
        n = len(filenames)
        nuniques = len(set(filenames))
        msg = (
            f"{seconds:.1f} s for locate_files({directory},{pattern}): {ntraversed} traversed, "
            f"found {n} filenames ({nuniques} uniques)"
        )

        logger.debug(msg)
    return filenames


T = Tuple[DirPath, List[RelDirPath], List[RelFilePath]]


def walk_typed(
    dirname: DirPath,
    topdown: bool = True,
    onerror: Optional[Callable[[OSError], Any]] = None,
    followlinks: bool = False,
) -> Iterator[T]:
    for root, dirs, files in os.walk(dirname, topdown=topdown, onerror=onerror, followlinks=followlinks):
        x = (root, dirs, files)
        yield cast(T, x)
