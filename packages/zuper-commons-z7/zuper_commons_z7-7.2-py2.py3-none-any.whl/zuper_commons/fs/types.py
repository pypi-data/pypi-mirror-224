from typing import cast, NewType, TYPE_CHECKING

__all__ = [
    "AbsDirPath",
    "AbsFilePath",
    "AbsPath",
    "DirPath",
    "FileNameWithoutDir",
    "FilePath",
    "GID",
    "GroupName",
    "Path",
    "RelDirPath",
    "RelFilePath",
    "RelPath",
    "UID",
    "UserName",
    "check_AbsDirPath",
    "check_AbsFilePath",
    "check_AbsPath",
    "check_DirPath",
    "check_FilePath",
    "check_Path",
    "check_RelDirPath",
    "check_RelFilePath",
]

if TYPE_CHECKING:
    from typing import NewType, Union

    AbsDirPath = NewType("AbsDirPath", str)
    AbsFilePath = NewType("AbsFilePath", str)

    RelDirPath = NewType("RelDirPath", str)
    RelFilePath = NewType("RelFilePath", str)

    FilePath = Union[RelFilePath, AbsFilePath]
    DirPath = Union[RelDirPath, AbsDirPath]
    RelPath = Union[RelDirPath, RelFilePath]
    AbsPath = Union[AbsDirPath, AbsFilePath]
    Path = Union[RelDirPath, AbsDirPath, AbsFilePath, RelFilePath]

    FileNameWithoutDir = NewType("FileNameWithoutDir", RelFilePath)

    # DirEntryName = NewType("DirEntryName", RelPath)
else:
    AbsPath = str
    AbsFilePath = str
    AbsDirPath = str
    Path = str
    DirPath = str
    FilePath = str
    RelPath = str
    RelDirPath = str
    RelFilePath = str

    FileNameWithoutDir = str

UserName = NewType("UserName", str)
GroupName = NewType("GroupName", str)

UID = NewType("UID", int)
GID = NewType("GID", int)


def check_DirPath(x: str) -> DirPath:  # TODO: actually implement
    return cast(DirPath, x)


def check_FilePath(x: str) -> FilePath:  # TODO: actually implement
    return cast(FilePath, x)


def check_RelPath(x: str) -> RelPath:  # TODO: actually implement
    return cast(RelPath, x)


def check_AbsFilePath(x: str) -> AbsFilePath:  # TODO: actually implement
    return cast(AbsFilePath, x)


def check_AbsDirPath(x: str) -> AbsDirPath:  # TODO: actually implement
    return cast(AbsDirPath, x)


def check_AbsPath(x: str) -> AbsPath:  # TODO: actually implement
    return cast(AbsPath, x)


def check_RelDirPath(x: str) -> RelDirPath:  # TODO: actually implement
    return cast(RelDirPath, x)


def check_RelFilePath(x: str) -> RelFilePath:  # TODO: actually implement
    return cast(RelFilePath, x)


def check_Path(x: str) -> Path:  # TODO: actually implement
    return cast(Path, x)
