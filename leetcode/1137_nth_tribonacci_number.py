# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        t_n_3 = 0
        t_n_2 = 1
        t_n_1 = 1
        t_n = t_n_1 + t_n_2 + t_n_3

        if n < 3:
            return [t_n_3, t_n_2, t_n_1][n]

        for n in range(3, n):
            t_n, t_n_1, t_n_2 = t_n + t_n_1 + t_n_2, t_n, t_n_1

        return t_n

    def tribonacci(self, n: int) -> int:
        t_n_2 = 0
        t_n_1 = 1
        t_n = t_n_1 + t_n_2

        for n in range(n):
            t_n, t_n_1, t_n_2 = t_n + t_n_1 + t_n_2, t_n, t_n_1

        return t_n_2
