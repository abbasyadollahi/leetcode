# https://leetcode.com/problems/minimize-deviation-in-array/

import heapq


class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        max_heap = [-num * (1 + num % 2) for num in set(nums)]
        heapq.heapify(max_heap)

        minimum = -max(max_heap)
        min_deviation = float("inf")
        while True:
            maximum = -max_heap[0]
            min_deviation = min(min_deviation, maximum - minimum)

            if not maximum % 2:
                minimum = min(minimum, maximum // 2)
                heapq.heapreplace(max_heap, -maximum // 2)
            else:
                return min_deviation
