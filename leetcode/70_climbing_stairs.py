# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        options = 2
        base = [0] * (n + 1)

        for i in range(1, min(n, options) + 1):
            base[i] = sum(base[:i]) + 1

        for i in range(options + 1, n + 1):
            base[i] = sum(base[i-options:i])

        return base[n]
