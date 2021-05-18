# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]

        l = 0
        r = len(nums) - 1
        while l <= r and nums[(l+r)//2] != target:
            mid = (l + r) // 2
            num = nums[mid]
            if num > target:
                r = mid - 1
            elif num < target:
                l = mid + 1

        if l >= r:
            return [-1, -1]

        mid = (l + r) // 2

        ll = 0
        rr = mid
        while ll != rr:
            mm = (ll + rr) // 2
            num = nums[mm]
            if num == target:
                rr = mm - 1
            else:
                ll = mm
        first = ll if nums[ll] == target else ll + 1

        ll = mid
        rr = len(nums) - 1
        while ll != rr:
            mm = (ll + rr) // 2
            num = nums[mm]
            if num == target:
                ll = mm + 1
            else:
                rr = mm
        last = ll if nums[ll] == target else ll - 1

        return [first, last]
