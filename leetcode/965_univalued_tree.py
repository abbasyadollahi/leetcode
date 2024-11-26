# https://leetcode.com/problems/univalued-binary-tree/


from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.traverse(root, root.val)

    def traverse(self, root: TreeNode, val: int) -> bool:
        return root is None or root.val == val and self.traverse(root.left, val) and self.traverse(root.right, val)
