# https://leetcode.com/problems/counting-elements/

from collections import Counter


class Solution:
    def countElements(self, arr: list[int]) -> int:
        counts = Counter(arr)
        total = 0
        for num in sorted(counts.keys()):
            total += counts[num] * bool(num + 1 in counts)
        return total
