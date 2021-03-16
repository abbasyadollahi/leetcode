# https://leetcode.com/problems/spiral-matrix/

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.nums = []
        self.min_row = 0
        self.min_col = 0
        self.max_row = len(matrix)
        self.max_col = len(matrix[0])
        self.matrix = matrix

        if self.max_row == 1 and self.max_col == 1:
            return matrix[0]

        increasing = True
        while self.min_row < self.max_row and self.min_col < self.max_col:
            self.traverse_row(increasing)
            self.traverse_col(increasing)
            increasing = not increasing

        return self.nums

    def traverse_row(self, increasing: bool) -> None:
        if increasing:
            self.nums += self.matrix[self.min_row][self.min_col:self.max_col]
            self.min_row += 1
        else:
            self.nums += reversed(self.matrix[self.max_row-1][self.min_col:self.max_col])
            self.max_row -= 1

    def traverse_col(self, increasing: bool) -> None:
        if increasing:
            self.nums += [row[self.max_col-1] for row in self.matrix[self.min_row:self.max_row]]
            self.max_col -= 1
        else:
            self.nums += reversed([row[self.min_col] for row in self.matrix[self.min_row:self.max_row]])
            self.min_col += 1
