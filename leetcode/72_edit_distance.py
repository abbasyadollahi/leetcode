# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.m = len(word1)
        self.n = len(word2)
        dp = [list(range(i, i + self.n + 1)) for i in range(self.m + 1)]

        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

        return dp[self.m][self.n]
