"""
Size needs to be valid
Return the person that's been waiting the longest
Remove that person from the reservations

-----------------------------------------------------------

Given `large` take any valid size,
otherwise, only take exact matches for size

If a person has been waiting for over 1800 seconds,
they get priority and should addressed first

Queue above 1800 overrides any other rule (small or large)
"""

from typing import Optional


def get_next_in_line(reservations: list[dict], table_size: int, large: bool) -> Optional[str]:
    index = None
    max_queue_time = -1

    for i, reservation in enumerate(reservations):
        if reservation["size"] > table_size:
            continue

        override = large or reservation["queue_time"] > 1800
        if reservation["queue_time"] > max_queue_time and (override or reservation["size"] == table_size):
            index = i
            max_queue_time = reservation["queue_time"]
        elif (
            reservation["queue_time"] == max_queue_time
            and reservation["size"] > reservations[index]["size"]
            and override
        ):
            index = i

        if index is None:
            next_in_line = None
        else:
            next_in_line = reservations.pop(index)["name"]

        return next_in_line


reservations = [
    {"size": 5, "name": "Abbas", "queue_time": 600},
    {"size": 3, "name": "Laurent", "queue_time": 800},
    {"size": 6, "name": "Eric", "queue_time": 900},
    {"size": 9, "name": "Pierre", "queue_time": 300},
    {"size": 1, "name": "Jamal", "queue_time": 2200},
    {"size": 4, "name": "Tom", "queue_time": 2000},
]

table_size = 5

large = True
small = False

print(get_next_in_line(reservations, table_size, small))
print(get_next_in_line(reservations, table_size, small))
print(get_next_in_line(reservations, table_size, small))
print(get_next_in_line(reservations, table_size, small))
