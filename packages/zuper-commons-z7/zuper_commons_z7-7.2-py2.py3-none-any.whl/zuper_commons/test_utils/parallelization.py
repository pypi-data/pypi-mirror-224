import os
from typing import Tuple


def get_worker_index() -> Tuple[int, int]:
    """Returns i,n: machine index and number of tests"""
    i = int(os.environ.get("CIRCLE_NODE_INDEX", 0))
    n = int(os.environ.get("CIRCLE_NODE_TOTAL", 1))
    return i, n
