# https://leetcode.com/problems/maximum-alternating-subsequence-sum/


class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        dp_odd = [0] * len(nums)
        dp_even = [0] * len(nums)

        for i, num in enumerate(nums):
            dp_odd[i] = max(dp_odd[i - 1], dp_even[i - 1] - num)
            dp_even[i] = max(dp_even[i - 1], dp_odd[i - 1] + num)

        return max(dp_odd[-1], dp_even[-1])
