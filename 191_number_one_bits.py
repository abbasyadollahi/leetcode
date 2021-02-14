# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        return bin(n).count('1')
