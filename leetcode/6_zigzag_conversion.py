# https://leetcode.com/problems/zigzag-conversion/

from itertools import zip_longest


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        i = 0
        step = 1
        rows = [''] * numRows
        for c in s:
            rows[i] += c
            if (step < 0 and i == 0) or (step > 0 and i == numRows - 1):
                step = -step
            i += step

        return ''.join(rows)

    def convert(self, s: str, numRows: int) -> str:
        rows = [None] * numRows
        step = 2 * (numRows - 1)

        for i in range(numRows):
            first_slice = slice(i, None, step)
            if 0 < i < numRows - 1:
                second_slice = slice(i + step - (2 * i), None, step)
                rows[i] = ''.join(map(''.join, zip_longest(s[first_slice], s[second_slice], fillvalue='')))
            else:
                rows[i] = s[first_slice]

        return ''.join(rows)
