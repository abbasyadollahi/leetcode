from collections import defaultdict
from threading import Thread
from warnings import warn

from database import Database
from lru_cache import LRUCache
from request import Request


class Server:
    """
    The `Server` class is the machine that requests go through before being redirected to the
    nearest LRU Cache Machine (`LRUCache`) in the same region as the request. It handles the request
    distribution and, in case of non cached request, returns the resource from the database store.
    In the latter situation, the server will also created a thread to find which LRU cache the
    resource is located in and update that value to match the one stored in database.
    """

    def __init__(self) -> None:
        self.db = Database.instance()
        self.machines = defaultdict(list)
        self.resource_lru_cache_map = {}

    def addMachine(self, lru_cache: LRUCache) -> None:
        for region in lru_cache.regions:
            self.machines[region].append(lru_cache.rid)

    def getNearestLRUCache(self, request: Request) -> LRUCache:
        if request.resource in self.resource_lru_cache_map:
            return self.resource_lru_cache_map[request.resource]
        else:
            for lru_cache in self.machines[request.region]:
                if request.resource in lru_cache.cache:
                    break
            self.resource_lru_cache_map[request.resource] = lru_cache
            return lru_cache

    def handleRequest(self, request: Request) -> int:
        if request.cached:
            lru_cache = self.getNearestLRUCache(request)
            value = lru_cache.getResource(request.resource)
        else:
            value = self.db[request.resource]
            if value is not None:
                Thread(target=self.updateLRUCache, args=(request, value)).start()
        if value is None:
            warn("Resource does not exist.")
        return value

    def updateLRUCache(self, request: Request, value: int) -> None:
        lru_cache = self.getNearestLRUCache(request)
        lru_cache.updateResource(request.resource, value)
