# https://leetcode.com/problems/kth-largest-element-in-a-stream/


import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]) -> None:
        self.k = k
        self.scores = nums
        heapq.heapify(self.scores)

    def add(self, val: int) -> int:
        heapq.heappush(self.scores, val)
        while len(self.scores) > self.k:
            heapq.heappop(self.scores)
        return self.scores[0]
