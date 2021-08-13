# https://leetcode.com/problems/number-of-islands/

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        row_len = len(grid)
        col_len = len(grid[0])

        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == '1':
                    self.clearIsland(row, col, grid)
                    islands += 1

        return islands

    def clearIsland(self, row: int, col: int, grid: List[List[str]]) -> None:
        row_len = len(grid)
        col_len = len(grid[0])

        grid[row][col] = '0'

        r = row - 1
        if r >= 0 and grid[r][col] == '1':
            self.clearIsland(r, col, grid)

        r = row + 1
        if r < row_len and grid[r][col] == '1':
            self.clearIsland(r, col, grid)

        c = col - 1
        if c >= 0 and grid[row][c] == '1':
            self.clearIsland(row, c, grid)

        c = col + 1
        if c < col_len and grid[row][c] == '1':
            self.clearIsland(row, c, grid)


sol = Solution()

islands = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]
print(sol.numIslands(islands))

islands = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
print(sol.numIslands(islands))
