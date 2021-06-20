# https://leetcode.com/problems/word-search/

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        self.word = word
        self.length = len(word)

        for i in range(self.m):
            for j in range(self.n):
                if self.recurse(i, j, 0):
                    return True


    def recurse(self, i: int, j: int, idx: int) -> bool:
        if self.board[i][j] is None:
            return False
        if self.board[i][j] != self.word[idx]:
            return False

        if idx == self.length - 1:
            return True

        next_idx = idx + 1
        tmp = self.board[i][j]
        self.board[i][j] = None
        # Up
        if i > 0 and self.recurse(i - 1, j, next_idx):
            return True
        # Down
        if i < self.m - 1 and self.recurse(i + 1, j, next_idx):
            return True
        # Left
        if j > 0 and self.recurse(i, j - 1, next_idx):
            return True
        # Right
        if j < self.n - 1 and self.recurse(i, j + 1, next_idx):
            return True

        # No successul word search so revert
        self.board[i][j] = tmp
        return False
