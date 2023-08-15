from datetime import datetime
from decimal import Decimal
from typing import NewType, Union

__all__ = [
    "AccountName",
    "CID",
    "CircleToken",
    "DateString",
    "DockerCompleteImageName",
    "DockerCompleteImageNameNormalized",
    "DockerImageDigest",
    "DockerOrganizationName",
    "DockerRegistryName",
    "DockerRepositoryName",
    "DockerSecret",
    "DockerTag",
    "DockerUsername",
    "EmailString",
    "EventID",
    "GitATagSHA",
    "GitBlobSHA",
    "GitBranchName",
    "GitBranchName",
    "GitCommitSHA",
    "GitCommitSHA",
    "GitOrgName",
    "GitRemoteName",
    "GitRepoName",
    "GitSHA",
    "GitShortCommitSHA",
    "GitShortSHA",
    "GitTagName",
    "GitTreeSHA",
    "GitTreeSHA",
    "GitURL",
    "GitUsername",
    "HTMLString",
    "IPAddressString",
    "IPCL",
    "IPCLPointer",
    "IPCLScalar",
    "JSONString",
    "LibraryName",
    "MD5Hash",
    "MacAddressString",
    "MarkdownStr",
    "ModuleSymbolName",
    "PipURLString",
    "PkgName",
    "PkgSpec",
    "PythonModuleName",
    "PythonQualName",
    "SHA1Hash",
    "SQLString",
    "ShelfName",
    "SpecName",
    "ThingName",
    "TopLevelPythonModuleName",
    "URLString",
    "VersionString",
    "XMLString",
]

EmailString = NewType("EmailString", str)
""" An email string """

MarkdownStr = NewType("MarkdownStr", str)
""" A Markdown string """

MD5Hash = NewType("MD5Hash", str)
""" A MD5 hash"""

SHA1Hash = NewType("SHA1Hash", str)
""" A SHA-1 hash"""

HTMLString = NewType("HTMLString", str)
""" A string containing HTML """

XMLString = NewType("XMLString", str)
""" A string containing XML """

JSONString = NewType("JSONString", str)
""" A string containing JSON """

URLString = NewType("URLString", str)
""" A string containing a URL """

SQLString = NewType("SQLString", str)
""" A string containing SQL """

PipURLString = NewType("PipURLString", URLString)
""" A string containing a PIP URL """

GitTagName = NewType("GitTagName", str)
GitBranchName = NewType("GitBranchName", str)
GitRemoteName = NewType("GitRemoteName", str)
GitOrgName = NewType("GitOrgName", str)
GitUsername = NewType("GitUsername", str)
AccountName = Union[GitOrgName, GitUsername]
GitRepoName = NewType("GitRepoName", str)

GitSHA = NewType("GitSHA", SHA1Hash)
GitShortSHA = NewType("GitShortSHA", str)
GitTreeSHA = NewType("GitTreeSHA", GitSHA)
GitBlobSHA = NewType("GitBlobSHA", GitSHA)
GitCommitSHA = NewType("GitCommitSHA", GitSHA)
GitShortCommitSHA = NewType("GitShortCommitSHA", GitShortSHA)
GitATagSHA = NewType("GitATagSHA", GitSHA)

EventID = NewType("EventID", int)
GitURL = NewType("GitURL", str)

VersionString = NewType("VersionString", str)
""" A version string ("1.2.3") """

PkgSpec = NewType("PkgSpec", str)
""" A Python package spec, like "pkg", "pkg==1.0", "pkg>=1,<2" """

PkgName = NewType("PkgName", PkgSpec)
""" A Python package name.   """

PythonModuleName = NewType("PythonModuleName", str)
""" A Python module name.  ("zuper_commons.text")  """

TopLevelPythonModuleName = NewType("TopLevelPythonModuleName", PythonModuleName)
""" A toplevel Python module name.  ("zuper_commons")  """

PythonQualName = NewType("PythonQualName", str)
""" A Python qualified name - might have (, -, etc. inside. """

CID = NewType("CID", str)

DateString = NewType("DateString", str)

CircleToken = NewType("CircleToken", str)

DockerRegistryName = NewType("DockerRegistryName", str)
DockerOrganizationName = NewType("DockerOrganizationName", str)
DockerRepositoryName = NewType("DockerRepositoryName", str)
DockerTag = NewType("DockerTag", str)
DockerImageDigest = NewType("DockerImageDigest", str)
DockerCompleteImageName = NewType("DockerCompleteImageName", str)
DockerCompleteImageNameNormalized = NewType("DockerCompleteImageNameNormalized", DockerCompleteImageName)
DockerUsername = NewType("DockerUsername", str)
DockerSecret = NewType("DockerSecret", str)

IPAddressString = NewType("IPAddressString", str)
MacAddressString = NewType("MacAddressString", str)

IPCL = NewType("IPCL", object)
IPCLPointer = NewType("IPCLPointer", IPCL)
# IPCL = NewType("IPCL", Union[bytes, str, float, Decimal, datetime, bool, dict, list, tuple])
IPCLScalar = Union[bytes, str, float, int, Decimal, datetime, bool]

SpecName = NewType("SpecName", str)
ThingName = NewType("ThingName", str)
LibraryName = NewType("LibraryName", str)
ShelfName = NewType("ShelfName", str)

ModuleSymbolName = NewType("ModuleSymbolName", str)  # module.module.symbol
