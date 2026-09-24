# https://leetcode.com/problems/largest-unique-number/

from collections import Counter


class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        return max(
            [num for num, count in Counter(nums).items() if count == 1],
            default=-1,
        )
