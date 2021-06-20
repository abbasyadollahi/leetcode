# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        if len(s) == 1:
            return s
        if len(s) == 2:
            return s if s[0] == s[1] else s[1]

        best = s[:2] if s[0] == s[1] else s[0]
        for i in range(len(s) - 1):
            b = self.extend(s, i)
            if len(b) >= len(best):
                best = b

        return best if len(best) > 1 else s[-1]

    def extend(self, s: str, i: int) -> str:
        l = i - 1
        r = i + 1
        best = s[i]
        pair = s[i] == s[i+1]

        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                best = s[l] + best + s[r]
                l -= 1
                r += 1
            elif pair and best[0] == s[r]:
                pair = False
                best = best + s[r]
                r += 1
            else:
                return best

        return best + s[r] if pair and r < len(s) and best[0] == s[r] else best

    def longestPalindrome(self, s: str) -> str:
        self.n = len(s)

        longest = ''
        for i in range(self.n):
            longest = max(
                longest,
                self.expand(s, i, i),
                self.expand(s, i, i + 1),
                key=len
            )

        return longest

    def expand(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < self.n and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

sol = Solution()
print(sol.longestPalindrome('babad'))
print(sol.longestPalindrome('a'))
print(sol.longestPalindrome('abc'))
print(sol.longestPalindrome('abba'))
print(sol.longestPalindrome('abbas'))
print(sol.longestPalindrome('babababab'))
print(sol.longestPalindrome('ssssssssssssssss'))
print(sol.longestPalindrome('aaaaaa'))
