# https://leetcode.com/problems/shuffle-the-array/

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [nums[i] for xy in zip(range(0, n), range(n, 2 * n)) for i in xy]
