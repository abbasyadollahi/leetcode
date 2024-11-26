# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
        r2i = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = r2i[s[-1]]
        next_r = r2i[s[0]]
        for i in range(len(s) - 1):
            r = next_r
            next_r = r2i[s[i + 1]]
            if r < next_r:
                total -= r
            else:
                total += r

        return total
