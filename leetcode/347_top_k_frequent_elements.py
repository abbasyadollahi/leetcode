# https://leetcode.com/problems/top-k-frequent-elements/

import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [num for num, _ in Counter(nums).most_common(k)]

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequencies = [[] for _ in range(len(nums) + 1)]
        for num, frequency in Counter(nums).items():
            frequencies[frequency].append(num)

        top_k = []
        frequencies = iter(reversed(frequencies))
        while len(top_k) < k:
            top_k.extend(next(frequencies))

        return top_k

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        top_k = []
        for num, count in Counter(nums).items():
            if len(top_k) == k:
                min_count, min_num = heapq.heappop(top_k)
                heapq.heappush(top_k, (count, num) if count > min_count else (min_count, min_num))
            else:
                heapq.heappush(top_k, (count, num))

        return [num for _, num in top_k]
