# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)

        for i in range(0, 1 + h_len - n_len):
            if haystack[i:i+n_len] == needle:
                return i

        return -1
