# https://leetcode.com/problems/merge-intervals/

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if not intervals:
            return []

        intervals = sorted(intervals, key=lambda x: x.start)
        start, end = [i.start for i in intervals], [i.end for i in intervals]

        e = 0
        merged = []
        interval = None
        for i, s in enumerate(start):
            if interval:
                if e < s:
                    interval.end = e
                    merged.append(interval)
                    interval = Interval(s)
            else:
                interval = Interval(s)
            e = max(e, end[i])

        interval.end = e
        merged.append(interval)
        return merged
