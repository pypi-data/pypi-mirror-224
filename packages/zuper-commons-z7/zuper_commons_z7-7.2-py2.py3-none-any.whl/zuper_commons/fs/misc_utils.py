import os
from typing import cast, overload

from .types import (
    AbsDirPath,
    AbsFilePath,
    AbsPath,
    DirPath,
    FileNameWithoutDir,
    FilePath,
    Path,
    RelDirPath,
    RelFilePath,
    RelPath,
)

__all__ = [
    "abspath",
    "basename",
    "dirname",
    "expanduser",
    "getcwd",
    "join",
    "joind",
    "joindn",
    "joinf",
    "joinfn",
    "normpath",
    "realpath",
    "relpath",
]


@overload
def join(a: RelDirPath, b: RelFilePath) -> RelFilePath:
    ...


@overload
def join(a: RelDirPath, b: RelDirPath) -> RelDirPath:
    ...


@overload
def join(a: AbsDirPath, b: RelFilePath) -> AbsFilePath:
    ...


@overload
def join(a: AbsDirPath, b: DirPath) -> AbsDirPath:
    ...


@overload
def join(a: DirPath, b: FilePath) -> FilePath:
    ...


@overload
def join(a: DirPath, b: DirPath) -> DirPath:
    ...


@overload
def join(a: DirPath, b: str) -> Path:
    ...


def join(a: str, b: str) -> str:
    return os.path.join(a, b)


@overload
def dirname(p: RelPath) -> RelDirPath:
    ...


@overload
def dirname(p: AbsPath) -> AbsDirPath:
    ...


def dirname(p: Path) -> DirPath:
    return normpath(cast(DirPath, os.path.dirname(p)))


@overload
def basename(p: FilePath) -> FileNameWithoutDir:
    ...


@overload
def basename(p: DirPath) -> RelDirPath:
    ...


def basename(p: Path) -> RelPath:
    return cast(RelPath, os.path.basename(p))


@overload
def realpath(path: DirPath) -> AbsDirPath:
    ...


@overload
def realpath(path: FilePath) -> AbsFilePath:
    ...


def realpath(path: Path) -> AbsPath:
    return cast(AbsPath, os.path.realpath(path))


@overload
def abspath(path: DirPath) -> AbsDirPath:
    ...


@overload
def abspath(path: FilePath) -> AbsFilePath:
    ...


def abspath(path: Path) -> AbsPath:
    return cast(AbsPath, os.path.abspath(path))


def getcwd() -> AbsDirPath:
    return cast(AbsDirPath, os.getcwd())


@overload
def normpath(path: RelFilePath) -> RelFilePath:
    ...


@overload
def normpath(path: RelDirPath) -> RelDirPath:
    ...


@overload
def normpath(path: FilePath) -> FilePath:
    ...


@overload
def normpath(path: DirPath) -> DirPath:
    ...


def normpath(path: Path) -> Path:
    return cast(Path, os.path.normpath(path))


@overload
def relpath(path: FilePath, start: Path) -> RelFilePath:
    ...


@overload
def relpath(path: DirPath, start: Path) -> RelDirPath:
    ...


def relpath(path: Path, start: Path) -> RelPath:
    return cast(RelPath, os.path.relpath(path, start))


@overload
def expanduser(path: RelDirPath) -> RelDirPath:
    ...


@overload
def expanduser(path: RelFilePath) -> RelFilePath:
    ...


@overload
def expanduser(path: AbsFilePath) -> AbsFilePath:
    ...


@overload
def expanduser(path: AbsDirPath) -> AbsDirPath:
    ...


def expanduser(path: Path) -> Path:
    return cast(Path, os.path.expanduser(path))


@overload
def joind(path: AbsDirPath, f: str) -> AbsDirPath:
    ...


@overload
def joind(path: RelDirPath, f: str) -> RelDirPath:
    ...


def joind(path: DirPath, f: str) -> DirPath:
    return cast(DirPath, os.path.join(path, f))


@overload
def joindn(path: AbsDirPath, *f: str) -> AbsDirPath:
    ...


@overload
def joindn(path: RelDirPath, *f: str) -> RelDirPath:
    ...


def joindn(path: DirPath, *f: str) -> DirPath:
    return cast(DirPath, os.path.join(path, *f))


@overload
def joinf(path: AbsDirPath, f: str) -> AbsFilePath:
    ...


@overload
def joinf(path: RelDirPath, f: str) -> RelFilePath:
    ...


def joinf(path: DirPath, f: str) -> FilePath:
    return cast(FilePath, os.path.join(path, f))


@overload
def joinfn(path: AbsDirPath, *f: str) -> AbsFilePath:
    ...


@overload
def joinfn(path: RelDirPath, *f: str) -> RelFilePath:
    ...


def joinfn(path: DirPath, *f: str) -> FilePath:
    return cast(FilePath, os.path.join(path, *f))
