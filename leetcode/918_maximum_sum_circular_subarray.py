# https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        current = 0
        minimum = float('inf')
        for num in nums:
            current = min(current + num, num)
            minimum = min(minimum, current)

        current = 0
        maximum = float('-inf')
        for num in nums:
            current = max(current + num, num)
            maximum = max(maximum, current)

        return max(sum(nums) - minimum or maximum, maximum)
