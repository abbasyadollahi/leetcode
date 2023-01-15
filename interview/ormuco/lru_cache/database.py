from typing import Callable


class Singleton:
    def __init__(self, decorated: Callable):
        self._decorated = decorated

    def instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through the `instance()` method.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


@Singleton
class Database:
    """
    The `Database` class is a unique persistent database where the real values are stored.
    It is only accessed by the server for non cached requests or by the LRU caches when the
    resource isn't found in storage.
    """

    def __init__(self):
        self.db = {}

    def getItem(self, key: str) -> int:
        return self.db[key] if key in self.db else None

    def addItem(self, key: str, value: int):
        self.db[key] = value

    def removeItem(self, key: str):
        del self.db[key]
