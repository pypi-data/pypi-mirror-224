from typing import Callable, Dict, TypeVar

__all__ = [
    "dict_val_map",
]

K = TypeVar("K")
V = TypeVar("V")
W = TypeVar("W")


def dict_val_map(f: Callable[[V], W], d: Dict[K, V]) -> Dict[K, W]:
    res = {k: f(v) for k, v in d.items()}
    return res
