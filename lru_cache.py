import gc
import sys
import types
import random
from warnings import warn
from threading import Thread, Timer
from collections import defaultdict


##################################################
#                     Server                     #
##################################################

# The 'Server' class is the machine that requests go through before being redirected to the
# nearest LRU Cache Machine ('LRUCache') in the same region as the request. It handles the request
# distribution and, in case of non cached request, returns the resource from the database store.
# In the latter situation, the server will also created a thread to find which LRU cache the
# resource is located in and update that value to match the one stored in database.

class Server:
    def __init__(self):
        self.db = Database.instance()
        self.machines = defaultdict(lambda: [])
        self.resource_lru_cache_map = {}

    def addMachine(self, lru_cache: LRUCache):
        for region in lru_cache.regions:
            self.machines[region] += [lru_cache.rid]

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
                Thread(target=self.updateCache, args=(request, value)).start()
        if value is None:
            warn('Resource does not exist.')
        return value

    def updateLRUCache(self, request: Request, value: int):
        lru_cache = self.getNearestLRUCache(request)
        lru_cache.updateResource(request.resource, value)


##################################################
#         Distributed LRU Cache Machine          #
##################################################

# The 'LRUCache' class represents a cache storage machine (for example a redis machine) which
# returns the currently stored value for a given resource. In the situation where the resource
# isn't present, the cache machine will get it from the database and store it in cache. If there
# is no more storage space, it will free memory by deleting the least recently used resource.
# To make the read/writes as close to real time, the cache prioritizes returning the resource
# first while creating threads to deal with the rest of the business logic.

class LRUCache:
    NODE_SIZE = sys.getsizeof(DLLNode)

    def __init__(self, db: Database, rid: int, regions: str, max_size: int):
        self.db = db                            # Persistent database
        self.rid = rid                          # LRU Cache's region ID
        self.regions = regions                  # LRU Cache's service regions
        self.cache = {}                         # LRU Cache
        self.rhead = None                       # Head node of LRU queue
        self.rtail = None                       # Tail node of LRU queue
        self.max_size = max_size                # Max byte size of LRU Cache
        self.size = sys.getsizeof(self.cache)   # Current byte size of LRU Cache

    def __getattribute__(self, attr):
        method = object.__getattribute__(self, attr)
        if not method:
            raise Exception(f'Method {attr} not implemented.')
        if type(method) == types.MethodType:
            self.size = sys.getsizeof(self.cache)
            print(types.MethodType)
        return method

    def getResource(self, resource: str) -> int:
        if resource in self.cache:
            Thread(target=self.renewResource, args=(resource)).start()
            return self.cache[resource].value
        else:
            value = self.db.getItem(resource)
            Thread(target=self.addResource, args=(resource, value)).start()
            return value

    def addResource(self, resource: str, value: int):
        if value is None:
            warn('Resource does not exist.')
        else:
            node = DLLNode(resource, value)
            node.value = value
            node.prev = self.rtail
            self.cache[resource] = node
            if self.rhead is None and self.rtail is None:
                self.rhead = self.rtail = node
            else:
                if self.size + self.NODE_SIZE < self.max_size:
                    self.removeLRU()
                self.rtail.next = self.rtail = node

    def renewResource(self, resource: str):
        node = self.cache[resource]
        p, n = node.prev, node.next

        if n is not None:
            n.prev = p
            if p is not None:
                p.next = n
            else:
                self.rhead = n

            node.next = None
            node.prev = self.rtail
            self.rtail.next = self.rtail = node

    def updateResource(self, resource: str, value: int):
        if resource in self.cache:
            self.cache[resource].value = value
            self.renewResource(resource)
        else:
            self.addResource(resource, value)

    def removeLRU(self):
        if self.rhead is None:
            pass

        old_head = self.rhead
        self.rhead = self.rhead.next
        if old_head.next is not None:
            old_head.next.prev = old_head.next = None
        else:
            self.rtail = None
        del old_head
        del self.cache[old_head.key]
        gc.collect()

    def clear(self):
        self.cache = {}
        self.rhead = self.rtail = None
        gc.collect()


##################################################
#                Resource Request                #
##################################################

# The 'Request' class represents a resource request from some device for example. It includes
# the region of the user and can ask for a cached or non cached resource. Each request is
# directed to a main server which will handle the request.

class Request:
    def __init__(self, server: Server, region: str, resource: str, cached: bool = True):
        self.server = server
        self.region = region
        self.resource = resource
        self.cached = cached


##################################################
#                    Resource                    #
##################################################

# The 'Resource' class represents a key value pair object which holds pseudo data for a resource.

class Resource:
    def __init__(self, key: str):
        self.key = key
        self.value = random.randint(0, 1000000)


##################################################
#            Doubly Linked List Node             #
##################################################

# The 'DDLNode' class represents the doubly linked list node that the caches use to keep track of
# the resource usage. The linked list is used as a queue, where the head is the least recently used
# and the tail is the most recently used. Each node stores the data associated to its resource.

class DLLNode:
    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


##################################################
#              Persistent Database               #
##################################################

# The 'Database' class is a unique persistent database where the real values are stored. It is
# only accessed by the server for non cached requests or by the LRU caches when the resource
# isn't found in storage.

@Singleton
class Database:
    def __init__(self):
        self.db = {}

    def getItem(self, key: str) -> int:
        return self.db[key] if key in self.db else None

    def addItem(self, key: str, value: int):
        self.db[key] = value

    def removeItem(self, key: str):
        del self.db[key]


class Singleton:
    def __init__(self, decorated):
        self._decorated = decorated

    def instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `instance()` function.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)
