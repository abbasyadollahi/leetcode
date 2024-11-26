# https://leetcode.com/problems/spiral-matrix-ii/


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        self.num = 1
        self.matrix = [[None] * n for _ in range(n)]
        self.min_row = 0
        self.min_col = 0
        self.max_row = n
        self.max_col = n

        if n == 1:
            return [[1]]

        increasing = True
        while self.min_row < self.max_row and self.min_col < self.max_col:
            self.traverse_row(increasing)
            self.traverse_col(increasing)
            increasing = not increasing

        return self.matrix

    def traverse_row(self, increasing: bool) -> None:
        new_num = self.num + self.max_col - self.min_col
        if increasing:
            self.matrix[self.min_row][self.min_col : self.max_col] = range(self.num, new_num)
            self.num = new_num
            self.min_row += 1
        else:
            self.matrix[self.max_row - 1][self.min_col : self.max_col] = reversed(range(self.num, new_num))
            self.num = new_num
            self.max_row -= 1

    def traverse_col(self, increasing: bool) -> None:
        new_num = self.num + self.max_row - self.min_row
        if increasing:
            for num, row in enumerate(self.matrix[self.min_row : self.max_row], self.num):
                row[self.max_col - 1] = num
            self.num = new_num
            self.max_col -= 1
        else:
            for num, row in enumerate(reversed(self.matrix[self.min_row : self.max_row]), self.num):
                row[self.min_col] = num
            self.num = new_num
            self.min_col += 1
