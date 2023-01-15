# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

import math
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                break

        if not nums or (nums[(l + r) // 2] != target):
            return [-1, -1]

        # Left half
        ll = l
        rr = (l + r) // 2
        while ll <= rr:
            mm = (ll + rr) // 2
            if nums[mm] == target:
                rr = mm - 1
            elif nums[mm] < target:
                ll = mm + 1
        start = (ll + rr) // 2

        # Right half
        ll = (l + r) // 2
        rr = r
        while ll < rr:
            mm = math.ceil((ll + rr) / 2)
            if nums[mm] == target:
                ll = mm
            elif nums[mm] > target:
                rr = mm - 1
        end = (ll + rr) // 2

        return [start + 1, end]
