# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, s: str) -> int:
        col = 0
        ascii = 64
        l = len(s)
        for i, c in enumerate(s):
            col += (ord(c) - ascii) * 26 ** (l - i - 1)

        return col
