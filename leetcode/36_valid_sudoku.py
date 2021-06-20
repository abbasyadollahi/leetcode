# https://leetcode.com/problems/valid-sudoku/

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i, row in enumerate(board):
            for j, field in enumerate(row):
                if (
                    field != '.' and (
                        not self.is_valid_row(field, row) or
                        not self.is_valid_column(board, field, j) or
                        not self.is_valid_grid(board, field, i, j)
                    )
                ):
                    return False

        return True

    def is_valid_row(self, field: str, row: List[str]) -> bool:
        return row.count(field) == 1

    def is_valid_column(self, board: List[List[str]], field: str, j: int) -> bool:
        return [row[j] for row in board].count(field) == 1

    def is_valid_grid(self, board: List[List[str]], field: str, i: int, j: int) -> bool:
        i_start = (i // 3) * 3
        i_end = i_start + 3
        j_start = (j // 3) * 3
        j_end = j_start + 3
        return [col for row in board[i_start:i_end] for col in row[j_start:j_end]].count(field) == 1

board1 = [
    ['5','3','.','.','7','.','.','.','.'],
    ['6','.','.','1','9','5','.','.','.'],
    ['.','9','8','.','.','.','.','6','.'],
    ['8','.','.','.','6','.','.','.','3'],
    ['4','.','.','8','.','3','.','.','1'],
    ['7','.','.','.','2','.','.','.','6'],
    ['.','6','.','.','.','.','2','8','.'],
    ['.','.','.','4','1','9','.','.','5'],
    ['.','.','.','.','8','.','.','7','9']
]

board2 = [
    ['8','3','.','.','7','.','.','.','.'],
    ['6','.','.','1','9','5','.','.','.'],
    ['.','9','8','.','.','.','.','6','.'],
    ['8','.','.','.','6','.','.','.','3'],
    ['4','.','.','8','.','3','.','.','1'],
    ['7','.','.','.','2','.','.','.','6'],
    ['.','6','.','.','.','.','2','8','.'],
    ['.','.','.','4','1','9','.','.','5'],
    ['.','.','.','.','8','.','.','7','9']
]

sol = Solution()
sol.isValidSudoku(board1)
sol.isValidSudoku(board2)
