# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        node, _ = self.traverse(root, 0)
        return node

    def traverse(self, root: TreeNode | None, level: int) -> tuple[TreeNode | None, int]:
        if root is None:
            return None, level

        l_node, l_level = self.traverse(root.left, level + 1)
        r_node, r_level = self.traverse(root.right, level + 1)

        if l_level > r_level:
            return l_node, l_level
        if l_level < r_level:
            return r_node, r_level
        return root, l_level
