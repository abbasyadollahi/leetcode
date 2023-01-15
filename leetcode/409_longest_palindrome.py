# https://leetcode.com/problems/longest-palindrome/

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest = 0
        odd_exists = False
        for count in Counter(s).values():
            leftover = count % 2
            longest += count - leftover
            odd_exists = odd_exists or bool(leftover)

        return longest + odd_exists

    def longestPalindrome(self, s: str) -> int:
        odd_count = sum(count % 2 for count in Counter(s).values())
        return len(s) - max(odd_count - 1, 0)
