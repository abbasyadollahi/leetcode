# https://leetcode.com/problems/as-far-from-land-as-possible/

from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    top = grid[i-1][j] if i > 0 else float('inf')
                    left = grid[i][j-1] if j > 0 else float('inf')
                    grid[i][j] += min(top, left) + 1

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if grid[i][j] != 1:
                    bottom = grid[i+1][j] if i < m - 1 else float('inf')
                    right = grid[i][j+1] if j < n - 1 else float('inf')
                    grid[i][j] = min(bottom + 1, right + 1, grid[i][j])

        return max((distance for row in grid for distance in row if 1 < distance < float('inf')), default=0) - 1
