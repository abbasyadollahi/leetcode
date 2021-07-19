# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import List


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.nodes = {}
        self.recurse(root, 0)

        return [self.nodes[i] for i in range(len(self.nodes))]

    def recurse(self, root: TreeNode, level: int) -> None:
        if root is None:
            return

        self.nodes[level] = self.nodes.get(level, [])
        self.nodes[level].append(root.val)
        self.recurse(root.left, level + 1)
        self.recurse(root.right, level + 1)

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        level = []
        nodes = [root]
        while nodes:
            level.append([node.val for node in nodes])
            nodes = [n for node in nodes for n in (node.left, node.right) if n is not None]

        return level
