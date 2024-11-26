# https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        nodes = defaultdict(list)

        def recurse(node: Optional[TreeNode], level: int) -> None:
            if node is None:
                return

            nodes[level].append(node.val)
            recurse(node.left, level + 1)
            recurse(node.right, level + 1)

        recurse(root, 0)

        return list(nodes.values())

    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []

        level = []
        nodes = [root]
        while nodes:
            level.append([node.val for node in nodes])
            nodes = [child for node in nodes for child in (node.left, node.right) if child is not None]

        return level
