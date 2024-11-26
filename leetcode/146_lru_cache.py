# https://leetcode.com/problems/lru-cache/


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            return self.cache.setdefault(key, self.cache.pop(key))
        return -1

    def put(self, key: int, value: int) -> None:
        self.cache.pop(key, None)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.pop(next(iter(self.cache.keys())))
