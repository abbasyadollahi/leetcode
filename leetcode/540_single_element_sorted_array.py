# https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            direction = (-1) ** (m % 2)
            if nums[m] == nums[m+direction]:
                l = m
                if m == (l + r) // 2:
                    l += 1
            elif nums[m] == nums[m-direction]:
                r = m
            else:
                return nums[m]

        return nums[l]
