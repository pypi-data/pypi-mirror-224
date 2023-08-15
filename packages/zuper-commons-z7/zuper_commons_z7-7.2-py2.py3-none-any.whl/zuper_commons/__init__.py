__version__ = "7.3"
__date__ = ""

__all__ = [
    "ZLogger",
]

from .logs import ZLogger

logger = ZLogger(name=__name__)

logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

logger.hello_module_finished(__name__)
