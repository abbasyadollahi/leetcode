# https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = defaultdict(list)

        def recurse(node: Optional[TreeNode], level: int) -> None:
            if node is None:
                return

            nodes[level].append(node.val)
            recurse(node.left, level + 1)
            recurse(node.right, level + 1)

        recurse(root, 0)

        return list(nodes.values())

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        level = []
        nodes = [root]
        while nodes:
            level.append([node.val for node in nodes])
            nodes = [child for node in nodes for child in (node.left, node.right) if child is not None]

        return level
