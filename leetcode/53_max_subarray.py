# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None

        mx = nums[0]
        sub = nums[0:1]

        for i in range(1, len(nums)):
            sub.append(nums[i] + max(sub[i-1], 0))
            mx = max(mx, sub[i])

        return mx
