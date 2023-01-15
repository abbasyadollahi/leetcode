# https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root, 0) != -1

    def traverse(self, root: Optional[TreeNode], depth: int) -> int:
        if root is None:
            return depth

        left_depth = self.traverse(root.left, depth + 1)
        right_depth = self.traverse(root.right, depth + 1)

        if -1 in [left_depth, right_depth]:
            return -1
        if abs(left_depth - right_depth) > 1:
            return -1

        return max(right_depth, left_depth)
