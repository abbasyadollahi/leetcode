# https://leetcode.com/problems/reverse-bits/

import math


class Solution:
    def reverseBits(self, n: int) -> int:
        power = 2 ** math.floor(math.log2(max(n, 1)))
        bits = []
        while n or power:
            if n >= power:
                n -= power
                bits.append(1)
            else:
                bits.append(0)
            power //= 2

        bits = [0] * (32 - len(bits)) + bits
        return sum(bit * 2 ** i for i, bit in enumerate(bits))
