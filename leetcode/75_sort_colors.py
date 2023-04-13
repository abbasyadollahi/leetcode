# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        i_0 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i_0], nums[i] = nums[i], nums[i_0]
                i_0 += 1

        i_1 = i_0
        for i in range(i_0, len(nums)):
            if nums[i] == 1:
                nums[i_1], nums[i] = nums[i], nums[i_1]
                i_1 += 1

    def sortColors(self, nums: list[int]) -> None:
        i = 0
        i_0 = 0
        i_2 = len(nums) - 1
        while i <= i_2:
            if nums[i] == 0:
                nums[i_0], nums[i] = nums[i], nums[i_0]
                i_0 += 1
            elif nums[i] == 2:
                nums[i_2], nums[i] = nums[i], nums[i_2]
                i -= 1
                i_2 -= 1
            i += 1
