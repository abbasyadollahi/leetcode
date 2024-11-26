# https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i, n1 in enumerate(nums, 1):
            for j, n2 in enumerate(nums, 1):
                if j > 2:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 2] + n2)
                else:
                    dp[i][j] = max(dp[i][j - 1], n2)

        return dp[n][n]
