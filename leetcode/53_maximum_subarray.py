# https://leetcode.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sub_array = nums[0:1]
        for i in range(1, len(nums)):
            sub_array.append(nums[i] + max(sub_array[i - 1], 0))

        return max(sub_array)

    def maxSubArray(self, nums: list[int]) -> int:
        current = 0
        maximum = float("-inf")

        for num in nums:
            current = max(current + num, num)
            maximum = max(maximum, current)

        return maximum
