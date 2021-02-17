# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = self.combine(num)

        return num

    def combine(self, num: int) -> int:
        out = 0
        while num > 0:
            out += num % 10
            num //= 10

        return out
