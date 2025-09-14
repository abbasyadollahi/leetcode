# https://leetcode.com/problems/last-stone-weight/

import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -(y - x))

        return -stones.pop() if stones else 0
