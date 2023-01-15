# https://leetcode.com/problems/set-matrix-zeroes/

from typing import List, Tuple


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_rows = set()
        zero_cols = set()

        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col == 0:
                    self.recurse(i, j, matrix)

        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col is None:
                    matrix[i][j] = 0

    def recurse(self, i: int, j: int, matrix: List[List[int]]) -> None:
        matrix[i][j] = None
        for jj in range(len(matrix[0])):
            if matrix[i][jj] == 0:
                self.recurse(i, jj, matrix)
            matrix[i][jj] = None

        for ii in range(len(matrix)):
            if matrix[ii][j] == 0:
                self.recurse(ii, j, matrix)
            matrix[ii][j] = None
