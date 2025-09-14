# https://leetcode.com/problems/number-of-islands/


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        m = len(grid)
        n = len(grid[0])

        def clearIsland(i: int, j: int) -> None:
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] == "0":
                return

            grid[i][j] = "0"

            clearIsland(i - 1, j)
            clearIsland(i + 1, j)
            clearIsland(i, j - 1)
            clearIsland(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    clearIsland(i, j)
                    islands += 1

        return islands
