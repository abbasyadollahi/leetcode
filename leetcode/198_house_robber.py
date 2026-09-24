# https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i, _ in enumerate(nums, 1):
            for j, n2 in enumerate(nums, 1):
                if j > 2:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 2] + n2)
                else:
                    dp[i][j] = max(dp[i][j - 1], n2)

        return dp[n][n]

    def rob(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        robbed = [0] * (len(nums) + 1)
        robbed[1] = nums[0]
        robbed[2] = nums[1]
        for i in range(3, len(nums) + 1):
            robbed[i] = max(nums[i - 1] + robbed[i - 3], nums[i - 1] + robbed[i - 2], robbed[i - 1])
        return robbed[-1]
