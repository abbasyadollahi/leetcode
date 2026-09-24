# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/


class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        return 1 - min([num for num in nums if num < 1], default=0)
