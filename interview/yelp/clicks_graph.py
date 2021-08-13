import random
from typing import Dict, List, Tuple


ORIGINAL_CLICKS = [
    ('A', 'B'),
    ('B', 'C'),
    ('B', 'BC'),
    ('C', 'D'),
    ('D', 'E'),
    ('E', 'F'),     # Destination 2
    ('BC', 'BD'),   # Destination 1
    # ('F', 'B'),     # Creates error
    # ('BD', 'B'),    # Creates error
]
CLICKS = ORIGINAL_CLICKS[:]
random.shuffle(CLICKS)

# Given the shuffled click data and an origin page, find the final destination page
# Ex: input 'A' -> output: 'B'

"""
All visits are unique
No visit is missing

A -> B -> C --> D -> E -> F (F)
     B -> BC -> BD          (BD)
"""


def get_click_destination(clicks: List[Tuple[str, str]], origin: str) -> List[str]:
    clicks_dict = {}
    for o, d in clicks:
        clicks_dict[o] = clicks_dict.get(o, []) + [d]

    raise_cycle(clicks_dict, origin, set(origin))

    destinations = recurse(clicks_dict, origin)
    return destinations


def raise_cycle(clicks_dict: Dict[str, List[str]], origin: str, seen: set) -> None:
    destinations = clicks_dict[origin]
    if len(destinations) > 1:
        for d in destinations:
            raise_cycle(clicks_dict, d, set(origin))
    else:
        d = destinations[0]
        if d in seen:
            raise ValueError(f'The origin and destination pair ({origin}, {d}) creates a cycle')
        elif d in clicks_dict:
            seen.add(d)
            raise_cycle(clicks_dict, d, seen)


def recurse(clicks_dict: Dict[str, List[str]], origin: str) -> List[str]:
    if origin not in clicks_dict:
        return [origin]
    return [d for destination in clicks_dict[origin] for d in recurse(clicks_dict, destination)]


print(get_click_destination(CLICKS, 'A'))
