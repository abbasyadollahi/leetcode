# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = set()
        for i, n in enumerate(nums):
            if target - n in prev:
                return [nums.index(target-n), i]
            else:
                prev.add(n)

        return None

sol = Solution()
print(sol.twoSumSorted([2, 7, 11, 15], 23))
print(sol.twoSumSorted([2, 7, 11, 15], 22))
