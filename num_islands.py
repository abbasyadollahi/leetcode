# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        size = len(grid[0])

        for row, idx in enumerate(grid):
            row
