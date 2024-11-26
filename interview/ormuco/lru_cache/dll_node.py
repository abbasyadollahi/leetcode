class DLLNode:
    """
    The `DDLNode` class represents the doubly linked list node that the caches use to keep track of
    the resource usage. The linked list is used as a queue, where the head is the least recently used
    and the tail is the most recently used. Each node stores the data associated to its resource.
    """

    def __init__(self, key: str, value: int) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
