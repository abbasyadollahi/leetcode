# https://leetcode.com/problems/search-insert-position/


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            num = nums[m]
            if num > target:
                r = m
            elif num < target:
                l = m + 1
            else:
                return m

        return l + (nums[l] < target)

    def searchInsert(self, nums: list[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return i + 1
