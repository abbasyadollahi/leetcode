# https://leetcode.com/problems/merge-intervals/

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals = sorted(intervals, key=lambda i: i[0])
        start = [i[0] for i in intervals]
        end = [i[1] for i in intervals]

        e = 0
        merged = []
        interval = None
        for i, s in enumerate(start):
            if interval:
                if e < s:
                    interval[1] = e
                    merged.append(interval)
                    interval = [s, 0]
            else:
                interval = [s, 0]
            e = max(e, end[i])

        interval[1] = e
        merged.append(interval)
        return merged

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merge_idx_start = None
        merge_idx_end = None
        max_end = 0
        merges = []

        intervals = sorted(intervals, key=lambda i: i[0])
        for i, pair in enumerate(zip(intervals, intervals[1:])):
            intvl_now, intvl_next = pair
            end = max(intvl_now[1], max_end)
            if end >= intvl_next[0]:
                if merge_idx_start is None:
                    merge_idx_start = i
                merge_idx_end = i + 1
                max_end = max(end, intvl_next[1])
            else:
                if merge_idx_start is not None:
                    merges.append([merge_idx_start, merge_idx_end, max_end])
                    merge_idx_start = merge_idx_end = None
                    max_end = 0

        if merge_idx_start is not None:
            merges.append([merge_idx_start, merge_idx_end, max_end])

        for start, end, max_end in reversed(merges):
            intervals[start:end+1] = [[intervals[start][0], max_end]]

        return intervals
