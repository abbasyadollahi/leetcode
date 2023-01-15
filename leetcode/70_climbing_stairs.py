# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        base = list(range(n + 1))
        for i in range(3, n + 1):
            base[i] = sum(base[i-2:i])

        return base[n]

    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        total = 0
        two_back = 1
        one_back = 2
        for _ in range(3, n):
            total = two_back + one_back
            two_back = one_back
            one_back = total

        return two_back + one_back
