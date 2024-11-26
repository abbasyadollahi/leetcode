# https://leetcode.com/problems/unique-paths/

import itertools


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0

        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

    def uniquePaths(self, m: int, n: int) -> int:
        return len(set(itertools.permutations([0] * (m - 1) + [1] * (n - 1))))

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]

        return dp[n - 1]
