# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x < 10:
            return True

        reverse = 0
        initial = x

        while x > 0:
            reverse = reverse*10 + x%10
            x = x//10

        return reverse == initial
