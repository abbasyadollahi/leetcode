# https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        prev = ''
        combinations = []
        length = len(nums) - 1

        for i, c in enumerate(nums):
            if c == prev: continue

            prev = c
            l = i + 1
            r = length

            while l < r:
                nl, nr = nums[l], nums[r]

                if l == i: l += 1
                elif r == i: r -= 1
                elif nl + nr < -c: l += 1
                elif nl + nr > -c: r -= 1
                else:
                    combinations.append(sorted([c, nl, nr]))
                    while nl == nums[l] and l < length: l += 1
                    while nr == nums[r] and r > i: r -= 1

        return combinations
