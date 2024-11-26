# https://leetcode.com/problems/reordered-power-of-2/

from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power = 1
        bound = 10**9
        digits = Counter(str(n))
        while power <= bound:
            if digits == Counter(str(power)):
                return True
            power *= 2
        return False
