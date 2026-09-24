# https://leetcode.com/problems/contiguous-array/

from collections import defaultdict


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        count = 0
        indexes = defaultdict(list)
        indexes[0].append(-1)
        for i, num in enumerate(nums):
            if num:
                count += 1
            else:
                count -= 1
            indexes[count].append(i)

        return max(index[-1] - index[0] for index in indexes.values())
