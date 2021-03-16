# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums) - 1
        m = (l + r) // 2

        while l < r:
            if nums[l] > nums[m] or (nums[l] <= nums[m] and nums[l] < nums[r]):
                r = m
            else:
                l = m + 1
            m = (l + r) // 2

        return nums[l]
