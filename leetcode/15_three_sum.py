# https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        prev = None
        combinations = []
        length = len(nums) - 1

        for i, c in enumerate(nums):
            if c == prev:
                continue

            prev = c
            l = i + 1
            r = length

            while l < r:
                nl, nr = nums[l], nums[r]

                if nl + nr + c < 0:
                    l += 1
                elif nl + nr + c > 0:
                    r -= 1
                else:
                    combinations.append([c, nl, nr])
                    while nl == nums[l] and l < length:
                        l += 1
                    while nr == nums[r] and r > i:
                        r -= 1
        return combinations
