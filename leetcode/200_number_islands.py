# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        m = len(grid)
        n = len(grid[0])

        def clearIsland(i: int, j: int) -> None:
            grid[i][j] = '0'

            ii = i - 1
            if ii >= 0 and grid[ii][j] == '1':
                clearIsland(ii, j)

            ii = i + 1
            if ii < m and grid[ii][j] == '1':
                clearIsland(ii, j)

            jj = j - 1
            if jj >= 0 and grid[i][jj] == '1':
                clearIsland(i, jj)

            jj = j + 1
            if jj < n and grid[i][jj] == '1':
                clearIsland(i, jj)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    clearIsland(i, j)
                    islands += 1

        return islands
