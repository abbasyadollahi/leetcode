# https://leetcode.com/problems/binary-tree-preorder-traversal/

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
