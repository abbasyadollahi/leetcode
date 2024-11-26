# https://leetcode.com/problems/merge-intervals/


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
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

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        merge_index_start = None
        merge_index_end = None
        max_end = 0
        merges = []

        intervals = sorted(intervals, key=lambda i: i[0])
        for i, pair in enumerate(zip(intervals, intervals[1:])):
            interval_now, interval_next = pair
            end = max(interval_now[1], max_end)
            if end >= interval_next[0]:
                if merge_index_start is None:
                    merge_index_start = i
                merge_index_end = i + 1
                max_end = max(end, interval_next[1])
            else:
                if merge_index_start is not None:
                    merges.append([merge_index_start, merge_index_end, max_end])
                    merge_index_start = merge_index_end = None
                    max_end = 0

        if merge_index_start is not None:
            merges.append([merge_index_start, merge_index_end, max_end])

        for start, end, max_end in reversed(merges):
            intervals[start : end + 1] = [[intervals[start][0], max_end]]

        return intervals

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged_intervals = []

        minimum = intervals[0][0]
        maximum = intervals[0][1]
        for start, end in intervals:
            if maximum >= start:
                maximum = max(maximum, end)
            else:
                merged_intervals.append([minimum, maximum])
                minimum = start
                maximum = end

        merged_intervals.append([minimum, maximum])
        return merged_intervals
