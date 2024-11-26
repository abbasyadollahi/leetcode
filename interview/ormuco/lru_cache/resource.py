import random


class Resource:
    """
    The `Resource` class represents a key value pair object which holds pseudo
    data (an integer between 0 and 1000000) for a resource.
    """

    def __init__(self, key: str) -> None:
        self.key = key
        self.value = random.randint(0, 1000000)
