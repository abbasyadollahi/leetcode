# https://leetcode.com/problems/k-closest-points-to-origin/

import heapq
import math


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def calculate_distance(point: tuple[int, int]) -> int:
            x, y = point
            return math.sqrt(x**2 + y**2)

        return sorted(points, key=calculate_distance)[:k]

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []
        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            if len(max_heap) == k:
                heapq.heappushpop(max_heap, (-distance, x, y))
            else:
                heapq.heappush(max_heap, (-distance, x, y))

        return [(x, y) for _, x, y in max_heap]
