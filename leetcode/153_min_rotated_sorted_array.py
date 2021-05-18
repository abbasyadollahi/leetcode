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

    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2

        while l < r:
            if nums[l] > nums[r] and nums[l] > nums[m]:
                r = m
                m = (l + r) // 2
            elif nums[l] > nums[r] and nums[l] < nums[m]:
                l = m
                m = (l + r) // 2
            elif nums[l] > nums[r] and nums[l] == nums[m]:
                return nums[l+1]
            else:
                return nums[l]

        return nums[l]
