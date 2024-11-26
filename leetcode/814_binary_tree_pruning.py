# https://leetcode.com/problems/binary-tree-pruning/

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
            if root.val or root.left or root.right:
                return root
            else:
                return None
        else:
            return None
