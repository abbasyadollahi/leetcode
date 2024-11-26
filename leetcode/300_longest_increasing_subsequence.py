# https://leetcode.com/problems/longest-increasing-subsequence/


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        lis = [0] * len(nums)

        for i, num in enumerate(nums):
            lis[i] = max((lis[j] if nums[j] < num else 0 for j in range(i)), default=0) + 1

        return max(lis)
