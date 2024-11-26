# https://leetcode.com/problems/palindromic-substrings/


class Solution:
    def countSubstrings(self, s: str) -> int:
        self.n = len(s)
        return sum(self.expand(s, i, i) + self.expand(s, i, i + 1) for i in range(self.n))

    def expand(self, s: str, l: int, r: int) -> int:
        count = 0
        while l >= 0 and r < self.n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
