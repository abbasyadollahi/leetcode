# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        self.word = word
        self.length = len(word)

        for i in range(self.m):
            for j in range(self.n):
                if self.recurse(i, j, 0):
                    return True

    def recurse(self, i: int, j: int, index: int) -> bool:
        if self.board[i][j] is None:
            return False
        if self.board[i][j] != self.word[index]:
            return False

        if index == self.length - 1:
            return True

        next_index = index + 1
        tmp = self.board[i][j]
        self.board[i][j] = None
        # Up
        if i > 0 and self.recurse(i - 1, j, next_index):
            return True
        # Down
        if i < self.m - 1 and self.recurse(i + 1, j, next_index):
            return True
        # Left
        if j > 0 and self.recurse(i, j - 1, next_index):
            return True
        # Right
        if j < self.n - 1 and self.recurse(i, j + 1, next_index):
            return True

        # No successul word search so revert
        self.board[i][j] = tmp
        return False
