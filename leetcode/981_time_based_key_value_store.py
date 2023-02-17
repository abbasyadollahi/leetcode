# https://leetcode.com/problems/time-based-key-value-store/

import bisect
from collections import defaultdict
from typing import Optional


class TimeMap:
    def __init__(self):
        self.store = defaultdict(lambda: {'timestamps': list(), 'keys': dict()})

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key]['keys'][timestamp] = value
        self.store[key]['timestamps'].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store and timestamp in self.store[key]['keys']:
            return self.store[key]['keys'].get(timestamp)
        elif key in self.store:
            return self.store[key]['keys'].get(self._find_closest_timestamp(timestamp, self.store[key]['timestamps']), "")
        else:
            return ""

    def _find_closest_timestamp(self, timestamp: int, timestamps: list[int]) -> Optional[int]:
        index = bisect.bisect_right(timestamps, timestamp) - 1
        if timestamps[index] <= timestamp:
            return timestamps[index]
        else:
            return None
