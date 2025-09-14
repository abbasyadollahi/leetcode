# https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(node: Optional[TreeNode], depth: int) -> int:
            if node is None:
                return depth

            left_depth = traverse(node.left, depth + 1)
            right_depth = traverse(node.right, depth + 1)

            if -1 in [left_depth, right_depth] or abs(left_depth - right_depth) > 1:
                return -1

            return max(right_depth, left_depth)

        return traverse(root, 0) != -1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(node: Optional[TreeNode]) -> tuple[bool, int]:
            if node is None:
                return True, 0
            left_valid, left = traverse(node.left)
            right_valid, right = traverse(node.right)
            return left_valid and right_valid and abs(left - right) <= 1, 1 + max(left, right)

        return traverse(root)[0]
