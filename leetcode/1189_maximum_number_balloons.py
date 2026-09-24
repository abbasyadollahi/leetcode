# https://leetcode.com/problems/maximum-number-of-balloons/

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        b_a_n = min(counts["b"], counts["a"], counts["n"])
        l_o = min(counts["l"], counts["o"]) // 2
        return min(b_a_n, l_o)
