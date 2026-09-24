# https://leetcode.com/problems/running-sum-of-1d-array/


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        current_sum = 0
        for i, num in enumerate(nums):
            nums[i] = current_sum = current_sum + num

        return nums
