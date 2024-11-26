# https://leetcode.com/problems/binary-tree-right-side-view/

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        nodes = []

        def traverse(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return
            if len(nodes) < depth:
                nodes.append(node.val)

            traverse(node.right, depth + 1)
            traverse(node.left, depth + 1)

        traverse(root, 1)
        return nodes
