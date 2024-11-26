# https://leetcode.com/problems/number-of-1-bits/

import math


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

    def hammingWeight(self, n: int) -> int:
        power = 2 ** math.floor(math.log2(max(n, 1)))
        bits = 0
        while n:
            if n >= power:
                n -= power
                bits += 1
            power //= 2

        return bits

    def hammingWeight(self, n: int) -> int:
        bits = 0
        while n:
            n &= n - 1
            bits += 1

        return bits
