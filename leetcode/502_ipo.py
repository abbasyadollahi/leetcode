# https://leetcode.com/problems/ipo/

import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        available = []
        projects = sorted(zip(capital, profits), reverse=True)

        for _ in range(k):
            while projects and projects[-1][0] <= w:
                _, profit = projects.pop()
                heapq.heappush(available, -profit)
            if available:
                w += -heapq.heappop(available)

        return w
