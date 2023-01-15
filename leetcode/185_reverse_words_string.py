# https://leetcode.com/problems/reverse-words-in-a-string/

import re


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(re.split('\s+', s.strip())[::-1]) if s else ''
