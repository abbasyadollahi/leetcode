# https://leetcode.com/problems/excel-sheet-column-title/


class Solution:
    def convertToTitle(self, n: int) -> str:
        col = ""
        ascii = 65
        while n > 0:
            c = chr((n - 1) % 26 + ascii)
            col = c + col
            n = (n - 1) // 26

        return col
