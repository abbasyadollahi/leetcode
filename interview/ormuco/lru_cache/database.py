from typing import Never


class Singleton:
    def __init__(self, decorated: type) -> None:
        self._decorated = decorated

    def instance(self) -> "Singleton":
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self) -> Never:
        raise TypeError("Singletons must be accessed through the `instance()` method.")

    def __instancecheck__(self, inst: object) -> bool:
        return isinstance(inst, self._decorated)


@Singleton
class Database:
    """
    The `Database` class is a unique persistent database where the real values are stored.
    It is only accessed by the server for non cached requests or by the LRU caches when the
    resource isn't found in storage.
    """

    def __init__(self) -> None:
        self.db = {}

    def getItem(self, key: str) -> int | None:
        return self.db[key] if key in self.db else None

    def addItem(self, key: str, value: int) -> None:
        self.db[key] = value

    def removeItem(self, key: str) -> None:
        del self.db[key]
