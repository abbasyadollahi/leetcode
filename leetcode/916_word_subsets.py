# https://leetcode.com/problems/word-subsets/

from collections import Counter
from functools import reduce
from operator import ior


class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        max_counter = reduce(ior, map(Counter, words2))
        return [word1 for word1 in words1 if Counter(word1) >= max_counter]
