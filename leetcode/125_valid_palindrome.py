# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue

            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].casefold() != s[r].casefold():
                return False

            l += 1
            r -= 1

        return True

    def isPalindrome(self, s: str) -> bool:
        s = list(filter(str.isalnum, s.casefold()))
        return s == s[::-1]
