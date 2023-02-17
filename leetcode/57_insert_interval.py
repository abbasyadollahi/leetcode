# https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
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

    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        start_index = 0
        end_index = 0
        new_start, new_end = newInterval

        while start_index in range(len(intervals)) and new_start > intervals[start_index][1]:
            start_index += 1
        while end_index in range(len(intervals)) and new_end >= intervals[end_index][0]:
            end_index += 1

        if start_index in range(0, len(intervals)):
            min_start = min(new_start, intervals[start_index][0])
        else:
            min_start = new_start
        if end_index in range(1, len(intervals) + 1):
            max_end = max(new_end, intervals[end_index-1][1])
        else:
            max_end = new_end

        intervals[start_index:end_index] = [[min_start, max_end]]
        return intervals
