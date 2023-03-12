from functools import lru_cache
from collections.abc import Callable


def cache(func: Callable) -> Callable:
    cache = {}

    def a(*args, **kwargs):
        if not cache.get(args):
            g = func(*args, **kwargs)
            cache[args] = g
            return g
        else:
            return cache[args]

    return a


def cache_lru(func: Callable) -> Callable:
    return lru_cache(func)
