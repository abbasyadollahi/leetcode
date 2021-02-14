# https://leetcode.com/problems/reverse-words-in-a-string/

import re

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        return ' '.join(re.split('\s+', s.strip())[::-1]) if s else ''
