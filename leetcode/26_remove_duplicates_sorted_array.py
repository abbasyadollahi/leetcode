# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return None

        r = len(nums) - 1
        l = r - 1
        while r > 0:
            if nums[r] == nums[l]:
                nums.pop(r)
            r = l
            l -= 1

        return len(nums)
