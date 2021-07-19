import collections
import datetime
import functools
import math
from typing import List, Tuple


def main(s: str) -> bool:
    ...


print(main("(())()"))


# Step 1: Design a TTL cache
# cache = TTLCache(ttl=600)

# Follow up #1:
# How would you design your class to be easily testable?

# Follow up #2:
# Design the decorator
# @ttl_cache(ttl=600)
# def my_fun(val: str) -> None:
#     ...


class TTLCache:
    ttl: float

    def __init__(self, ttl: float, factor: float = 1) -> None:
        self.ttl = ttl



import time
from typing import *
class Clock:
    def __init__(self) -> None:
        self.timepoint = 0

    def sleep(self, amount: float) -> None:
        self.timepoint += amount

    def perf_counter(self) -> float:
        self.timepoint

class TTLCacheImpl:
    def __init__(self, *, _perf_counter: Callable[[], float] = time.perf_counter):
        self.perf_counter = _perf_counter

from threading import Lock

def ttl_cache(ttl: float):
    cache = TTLCache(ttl=ttl)
    def decorator(func):
        lock = Lock()
        @functools.wraps(func)
        def wrapper(arg):
            with lock:
                if arg in cache:
                    return cache.get(arg)
                else:
                    value = func(arg)
                    cache.add(arg, value)
                    return value
        return wrapper
    return decorator
