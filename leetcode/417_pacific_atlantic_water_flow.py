# https://leetcode.com/problems/pacific-atlantic-water-flow/

from typing import Callable


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        self.coords = []
        self.m = len(heights)
        self.n = len(heights[0])
        self.heights = heights
        self.visited = set()
        self.directions = [
            [1, 0],  # down
            [-1, 0],  # up
            [0, 1],  # right
            [0, -1],  # left
        ]

        for i, row in enumerate(heights):
            for j, height in enumerate(row):
                pacific = self.traverse(i, j, height, self.is_pacific)
                self.visited.clear()
                if pacific:
                    atlantic = self.traverse(i, j, height, self.is_atlantic)
                    self.visited.clear()
                    if atlantic:
                        self.coords.append((i, j))
        return self.coords

    def traverse(self, i: int, j: int, height: int, is_done: Callable[[int, int], bool]) -> bool:
        if i < 0 or j < 0 or i >= self.m or j >= self.n or (i, j) in self.visited or self.heights[i][j] > height:
            return False
        elif is_done(i, j):
            return True
        else:
            self.visited.add((i, j))
            for ii, jj in self.directions:
                if self.traverse(i + ii, j + jj, min(height, self.heights[i][j]), is_done):
                    return True
        return False

    def is_pacific(self, i: int, j: int) -> bool:
        return i == 0 or j == 0

    def is_atlantic(self, i: int, j: int) -> bool:
        return i == self.m - 1 or j == self.n - 1
