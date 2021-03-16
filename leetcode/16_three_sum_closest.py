# https://leetcode.com/problems/3sum-closest/

import sys
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        prev = None
        closest = sys.maxsize
        length = len(nums) - 1

        for i, c in enumerate(nums):
            if c == prev:
                continue

            prev = c
            l = i + 1
            r = length

            while l < r:
                nl, nr = nums[l], nums[r]
                diff = nl + nr + c - target

                if diff < 0:
                    l += 1
                elif diff > 0:
                    r -= 1
                else:
                    return target

                closest = min(diff, closest, key=abs)

        return closest + target
