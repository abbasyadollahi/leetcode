# https://leetcode.com/problems/domino-and-tromino-tiling/


class Solution:
    def numTilings(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0:4] = [0, 1, 2, 5]

        for i in range(4, n + 1):
            dp[i] = 2 * dp[i - 1] + dp[i - 3]

        return dp[n] % (10**9 + 7)
