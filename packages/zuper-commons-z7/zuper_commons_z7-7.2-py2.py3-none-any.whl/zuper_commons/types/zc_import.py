import sys
import traceback

from ..text import indent
from ..types import ZException

__all__ = [
    "ImportFailure",
    "import_name",
]


class ImportFailure(ZException):
    pass


def import_name(name: str) -> object:
    """
    Loads the python object with the given name.

    Note that "name" might be "module.module.name" as well.
    """
    if not isinstance(name, str):
        msg = "Need a string for name"
        raise ImportFailure(msg, name=name)
    #
    if name in sys.modules:
        return sys.modules[name]
    try:
        return __import__(name, fromlist=["dummy"])
    except ImportError:
        tb = traceback.format_exc()
        pass

    # split in (module, name) if we can
    if "." not in name:
        msg = "Cannot import name %r." % name
        msg += indent(tb, "> ")
        raise ImportFailure(msg)

    tokens = name.split(".")
    field = tokens[-1]
    module_name = ".".join(tokens[:-1])

    # other method, don't assume that in "M.x", "M" is a module.
    # It could be a class as well, and "x" be a staticmethod.
    try:
        module = import_name(module_name)
    except ImportError as e:
        msg = "Cannot load %r (tried also with %r):\n" % (name, module_name)
        msg += "\n" + indent("%s\n%s" % (e, traceback.format_exc()), "> ")
        raise ImportFailure(msg)

    if isinstance(module, type):
        if hasattr(module, field):
            return getattr(module, field)
        else:
            msg = f"No field {field!r}\n"
            msg += f" found in type {module!r}."
            raise ImportFailure(msg)

    if not field in module.__dict__:
        msg = f"No field {field!r}\n"
        msg += f" found in module {module!r}."
        raise ImportFailure(msg, known=sorted(module.__dict__))

    f = module.__dict__[field]

    # "staticmethod" are not functions but descriptors, we need
    # extra magic
    if isinstance(f, staticmethod):
        return f.__get__(module, None)
    else:
        return f
