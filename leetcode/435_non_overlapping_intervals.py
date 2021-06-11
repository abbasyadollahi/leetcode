# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        last_end = None
        intervals = sorted(intervals, key=lambda i: (i[1], -i[0]))

        for intvl_now, intvl_next in zip(intervals, intervals[1:]):
            end = intvl_now[1] if last_end is None else last_end
            if last_end is not None:
                count += 1
            if end > intvl_next[0]:
                last_end = end
            else:
                last_end = None

        return count + (last_end is not None and end > intvl_next[0])
