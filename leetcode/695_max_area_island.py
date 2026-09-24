# https://leetcode.com/problems/max-area-of-island/


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0
        m = len(grid)
        n = len(grid[0])

        def clearIsland(i: int, j: int) -> int:
            if not (i in range(m) and j in range(n)) or grid[i][j] == 0:
                return 0

            grid[i][j] = 0

            area = 0
            area += clearIsland(i - 1, j)
            area += clearIsland(i + 1, j)
            area += clearIsland(i, j - 1)
            area += clearIsland(i, j + 1)

            return 1 + area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, clearIsland(i, j))

        return max_area
