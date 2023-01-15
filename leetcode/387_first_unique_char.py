# https://leetcode.com/problems/first-unique-character-in-a-string/

import string


class Solution:
    def firstUniqueChar(self, s: str) -> int:
        index = [s.index(c) for c in string.ascii_lowercase if s.count(c) == 1]
        return min(index) if index else -1
