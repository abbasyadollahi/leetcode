# https://leetcode.com/problems/flip-string-to-monotone-increasing/


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = 0
        flips = 0

        for bit in s:
            if bit == "1":
                ones += 1
            else:
                flips = min(flips + 1, ones)

        return flips
