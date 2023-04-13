# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        levels: list[deque] = []
        def traverse(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return
            if depth == len(levels):
                levels.append(deque())

            if depth % 2:
                levels[depth].appendleft(node.val)
            else:
                levels[depth].append(node.val)

            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)

        traverse(root, 0)
        return levels
