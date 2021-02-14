# https://leetcode.com/problems/add-digits/

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        while num > 9:
            num = self.combine(num)

        return num

    def combine(self, num):
        """
        :type num: int
        :rtype: int
        """

        out = 0
        while num > 0:
            out += num % 10
            num //= 10

        return out
