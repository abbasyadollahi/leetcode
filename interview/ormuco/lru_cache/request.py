from server import Server


class Request:
    """
    The `Request` class represents a resource request from some device for example.
    It includes the region of the user and can ask for a cached or non cached resource.
    Each request is directed to a main server which will handle the request.
    """

    def __init__(self, server: Server, region: str, resource: str, cached: bool = True) -> None:
        self.server = server
        self.region = region
        self.resource = resource
        self.cached = cached
