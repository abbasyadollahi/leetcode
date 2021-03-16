# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

from typing import List


class Solution:
    def numPairsDivisibleBy60(self, songs: List[int]) -> int:
        count = 0
        counter = [0] * 60

        for song in songs:
            modded = song % 60
            count += counter[(60 - modded) % 60]
            counter[modded] += 1
        return count
