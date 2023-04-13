# https://leetcode.com/problems/lfu-cache/

class CacheNode:
    def __init__(self, value: int, next: 'CacheNode' = None, previous: 'CacheNode' = None):
        self.count = 1
        self.value = value
        self.next = next
        self.previous = previous


class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.lru_node = None
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache[key].count += 1
            self._refresh_lfu(self.cache[key])
            self._refresh_lru()
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].count += 1
            self.cache[key].value = value
        else:
            self._drop_lru()
            self.cache[key] = CacheNode(value, next=self.lru_node)
            if self.lru_node:
                self.lru_node.previous = self.cache[key]
            else:
                self.lru_node = self.cache[key]

        self._refresh_lfu(self.cache[key])
        self._refresh_lru()

    def _refresh_lfu(self, node: CacheNode) -> None:
        swap_node = node
        while swap_node.next and swap_node.next.count <= node.count:
            swap_node = swap_node.next

        if node == swap_node:
            return
        elif node.next == swap_node:
            if node.previous:
                node.previous.next = swap_node

            swap_node.previous = node.previous

            node.previous = swap_node
            node.next = swap_node.next

            if swap_node.next:
                swap_node.next.previous = node
            swap_node.next = node
        else:
            # Temp nodes
            node_previous = node.previous
            node_next = node.next

            swap_node_next = swap_node.next

            # Move nodes
            if node_previous:
                node_previous.next = node_next
            if node_next:
                node_next.previous = node_previous

            node.next = swap_node_next
            node.previous = swap_node

            swap_node.next = node
            if swap_node_next:
                swap_node_next.previous = node

    def _refresh_lru(self) -> None:
        while self.lru_node and self.lru_node.previous:
            self.lru_node = self.lru_node.previous
        if self.lru_node and len(self.cache) > self.capacity:
            self.lru_node = self.lru_node.next
            if self.lru_node.previous:
                self.lru_node.previous.next = None
            self.lru_node.previous = None

    def _drop_lru(self) -> None:
        if self.lru_node and len(self.cache) == self.capacity:
            self.cache.pop(self.lru_node.value)
            self.lru_node = self.lru_node.next
            if self.lru_node and self.lru_node.previous:
                self.lru_node.previous.next = None


"""
node = [2]

 p       n
[ ] [1] [2]

[1] [2] [3] -

[2] [3] [ ]

 p       n
[ ] [1] [2]

[1] [2] [3] -

[2] [3] [ ]

"""

"""
node = [2]

 p       n
[ ] [1] [2]

[1] [2] [3] -

[2] [3] [4]

[3] [4] [ ]

 p       n
[ ] [1] [3]

[1] [3] [2]

[3] [2] [4] -

[2] [4] [ ]

"""


a = b = LFUCache()
