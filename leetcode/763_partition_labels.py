# https://leetcode.com/problems/partition-labels/

from collections import defaultdict


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        partitions = []
        start_index = 0
        end_index = 0
        ranges_iterator = iter(self.get_ranges(s).values())
        while value := next(ranges_iterator, None):
            start, end = value
            if start <= end_index:
                end_index = max(end_index, end)
            else:
                partitions.append(1 + end_index - start_index)
                start_index = start
                end_index = end

        partitions.append(1 + end_index - start_index)
        return partitions

    def get_ranges(self, s: str) -> dict[str, tuple[int, int]]:
        ranges = defaultdict(list)
        for i, c in enumerate(s):
            ranges[c].append(i)

        ranges = {c: (indexes[0], indexes[-1]) for c, indexes in ranges.items()}

        return ranges
