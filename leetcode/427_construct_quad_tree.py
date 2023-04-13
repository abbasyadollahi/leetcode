# https://leetcode.com/problems/construct-quad-tree/

from typing import Optional


class Node:
    def __init__(
        self,
        val: int,
        isLeaf: bool,
        topLeft: Optional['Node'] = None,
        topRight: Optional['Node'] = None,
        bottomLeft: Optional['Node'] = None,
        bottomRight: Optional['Node'] = None
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        n = len(grid)
        node = Node(grid[0][0], False)
        if sum(num for row in grid for num in row) in {0, n ** 2}:
            node.isLeaf = True
        else:
            mid = n // 2
            node.topLeft = self.construct([row[:mid] for row in grid[:mid]])
            node.topRight = self.construct([row[mid:] for row in grid[:mid]])
            node.bottomLeft = self.construct([row[:mid] for row in grid[mid:]])
            node.bottomRight = self.construct([row[mid:] for row in grid[mid:]])
        return node
