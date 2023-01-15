import gc
import sys
import types
from threading import Thread
from warnings import warn

from database import Database
from dll_node import DLLNode


class LRUCache:
    """
    The `LRUCache` class represents a cache storage machine (for example a redis machine) which
    returns the currently stored value for a given resource. In the situation where the resource
    isn't present, the cache machine will get it from the database and store it in cache. If there
    is no more storage space, it will free memory by deleting the least recently used resource.
    To make the read/writes as close to real time, the cache prioritizes returning the resource
    first while creating threads to deal with the rest of the business logic.
    """

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
