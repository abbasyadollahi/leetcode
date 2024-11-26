# https://leetcode.com/problems/longest-arithmetic-subsequence/


class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        las = 0
        index_diffs = {i: {} for i in range(len(nums))}

        for i in range(len(nums)):
            for j in range(0, i):
                diff = nums[i] - nums[j]
                index_diffs[i][diff] = index_diffs[j].get(diff, 1) + 1
                las = max(las, index_diffs[i][diff])

        return las
