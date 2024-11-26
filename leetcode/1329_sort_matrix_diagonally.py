# https://leetcode.com/problems/sort-the-matrix-diagonally/


class Solution:
    def diagonalSort(self, matrix: list[list[int]]) -> list[list[int]]:
        if not matrix:
            return matrix

        num_row = len(matrix)
        num_col = len(matrix[0])

        self.sort(matrix, num_row, num_col, 0, 0)

        for i in range(1, num_row):
            self.sort(matrix, num_row, num_col, i, 0)

        for j in range(1, num_col):
            self.sort(matrix, num_row, num_col, 0, j)

        return matrix

    def sort(self, matrix: list[list[int]], num_row: int, num_col: int, i: int, j: int) -> None:
        nums = []

        ii, jj = i, j
        while ii < num_row and jj < num_col:
            nums.append(matrix[ii][jj])
            ii += 1
            jj += 1

        ii, jj = i, j
        for num in sorted(nums):
            matrix[ii][jj] = num
            ii += 1
            jj += 1
