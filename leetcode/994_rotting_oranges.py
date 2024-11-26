# https://leetcode.com/problems/rotting-oranges/


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh_oranges = set((i, j) for i in range(m) for j in range(n) if grid[i][j] == 1)
        rotten_oranges = set((i, j) for i in range(m) for j in range(n) if grid[i][j] == 2)

        time = 0
        while rotten_oranges:
            rotten_orange_neighbors = set(
                (i + i_diff, j + j_diff)
                for i, j in rotten_oranges
                for i_diff, j_diff in ((0, 1), (1, 0), (0, -1), (-1, 0))
                if (i + i_diff) in range(m) and (j + j_diff) in range(n)
            )

            rotten_oranges = fresh_oranges & rotten_orange_neighbors
            fresh_oranges.difference_update(rotten_oranges)
            time += bool(rotten_oranges)

        if fresh_oranges:
            return -1
        else:
            return time
