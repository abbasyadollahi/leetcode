# https://leetcode.com/problems/count-complete-tree-nodes/


from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        height = self.height(root)
        rheight = self.height(root.right)
        if height == rheight + 1:
            return 2 ** (height - 1) + self.countNodes(root.right)
        else:
            return 2 ** (height - 2) + self.countNodes(root.left)

    def height(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + self.height(root.left)
