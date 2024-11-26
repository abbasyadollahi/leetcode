"""
There is a price ingestion service which requires knowledge of financial instrument dependencies.
In order to be able to price a 'Parent' instrument, all 'Child' instruments must have been priced.
These 'Parent'-'Child' relationships are normalized and stored in a database in tabular format.

A query of the instrument-dependency table returns the following records:

+-------+-----------+----------+
|       | Parent ID | Child ID |
+-------+-----------+----------+
| 0     | A         | B        |
+-------+-----------+----------+
| 1     | B         | C        |
+-------+-----------+----------+
| 2     | C         | D        |
+-------+-----------+----------+
| 3     | B         | D        |
+-------+-----------+----------+
| 4     | E         | D        |
+-------+-----------+----------+
| 5     | F         | C        |
+-------+-----------+----------+
| 6     | F         | G        |
+-------+-----------+----------+
| 7     | E         | F        |
+-------+-----------+----------+

We do not allow users to query the table directly.
All the instrument-dependency data is exposed via service endpoints.

Task 0:
We wish to expose a new endpoint on the service.
User queries will supply an instrument ID and we must return a list of all dependent instrument IDs that are required for it to be priced.

Task 1:
Assume the instrument-dependency table now returns millions of rows and is queried by hundreds of clients.
How would you adjust your implementation to guarantee fast queries to all users?

Task 2:
We additionally wish to expose an endpoint which allows users to register a new Parent ID -> Child ID instrument mapping.
Implement the new endpoint with the same requirements of 'Task 1'.
"""

from collections import defaultdict
from functools import wraps
from pprint import pprint
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")
OriginalFunction = Callable[P, R]
DecoratedFunction = Callable[P, R]

DATA = [
    ("A", "B"),
    ("B", "C"),
    ("C", "D"),
    ("B", "D"),
    ("E", "D"),
    ("F", "C"),
    ("F", "G"),
    ("E", "F"),
]


def instrument_dependencies(data: list[tuple[str, str]]) -> dict[str, set[str]]:
    dependencies = defaultdict(set)
    for parent, child in data:
        dependencies[parent].add(child)

    return dependencies


dependencies = instrument_dependencies(DATA)
pprint(dependencies)


def fetch_dependents(p_id: str, dependencies: dict[str, set[str]]) -> set[str]:
    if not p_id or p_id not in dependencies:
        raise Exception(f"Invalid parent ID: {p_id}")

    dependents = set()

    queue = [*dependencies[p_id]]
    while queue:
        new_queue = []
        for node in queue:
            if node not in dependents:
                new_queue.extend(dependencies[node])
                dependents.add(node)

        queue = new_queue

    return dependents


dependents = fetch_dependents("A", dependencies)
print(dependents)

dependents = fetch_dependents("F", dependencies)
print(dependents)


def cacheable(fun: OriginalFunction) -> DecoratedFunction:
    cache = {}

    @wraps(fun)
    def decorated(*args: P.args, **kwargs: P.kwargs) -> R:
        p_id = args[0]
        if p_id not in cache:
            print(f"Cache miss: {p_id}")
            cache[p_id] = fun(cache, *args, **kwargs)

        return cache[p_id]

    return decorated


@cacheable
def cached_fetch_dependents(cache: dict[str, set[str]], p_id: str, dependencies: dict[str, set[str]]) -> set[str]:
    if not p_id or p_id not in dependencies:
        raise Exception(f"Invalid parent ID: {p_id}")

    dependents = set()

    def recurse(node: str) -> set[str]:
        if node in dependents:
            return cache[node]

        all_children = set()
        for child in dependencies[node]:
            children = recurse(child)
            all_children.update(children)
            cache[child] = children

            dependents.add(child)

        return all_children

    recurse(p_id)
    return dependents


dependents = cached_fetch_dependents("A", dependencies)
print(dependents)

dependents = cached_fetch_dependents("F", dependencies)
print(dependents)

dependents = cached_fetch_dependents("A", dependencies)
print(dependents)

dependents = cached_fetch_dependents("F", dependencies)
print(dependents)
