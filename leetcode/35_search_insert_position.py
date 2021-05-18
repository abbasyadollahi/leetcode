# https://leetcode.com/problems/search-insert-position/

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            num = nums[mid]
            if num > target:
                r = mid
            elif num < target:
                l = mid + 1
            else:
                return mid

        return l + (nums[l] < target)

    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return i + 1
