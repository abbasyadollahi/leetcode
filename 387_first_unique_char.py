# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqueChar(self, s):
        """
        :type s: String
        :rtype: int
        """

        chars = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(c) for c in chars if s.count(c) == 1]
        return min(index) if index else -1
