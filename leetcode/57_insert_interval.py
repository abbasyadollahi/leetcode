# https://leetcode.com/problems/insert-interval/

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        i = 0
        n = len(intervals)
        indexes = []
        start, end = newInterval
        while i < n and end >= intervals[i][0]:
            if start <= intervals[i][1]:
                indexes.append(i)
            i += 1

        if not indexes:
            if i == 0:
                return [newInterval] + intervals
            elif i == len(intervals):
                return intervals + [newInterval]
            else:
                intervals.insert(i, newInterval)
        else:
            first = indexes[0]
            last = indexes[-1]
            intervals[first:last+1] = [[min(start, intervals[first][0]), max(end, intervals[last][1])]]

        return intervals
