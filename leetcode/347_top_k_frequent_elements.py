# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in Counter(nums).most_common(k)]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = [[] for _ in range(len(nums) + 1)]
        for num, frequency in  Counter(nums).items():
            frequencies[frequency].append(num)

        top_k = []
        frequencies = iter(reversed(frequencies))
        while len(top_k) < k:
            top_k.extend(next(frequencies))

        return top_k
