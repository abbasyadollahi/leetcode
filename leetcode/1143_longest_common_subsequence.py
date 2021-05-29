# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i, t1 in enumerate(text1, 1):
            for j, t2 in enumerate(text2, 1):
                if t1 == t2:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n1][n2]
