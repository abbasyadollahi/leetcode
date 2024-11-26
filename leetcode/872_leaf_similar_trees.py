# https://leetcode.com/problems/leaf-similar-trees/

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        return self.traverse(root1) == self.traverse(root2)

    def traverse(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return []

        if root.left or root.right:
            return self.traverse(root.left) + self.traverse(root.right)
        else:
            return [root.val]
