# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def traverse(node: Optional[TreeNode]) -> tuple[int, int]:
            if node is None:
                return 0, 0

            left = traverse(node.left)
            right = traverse(node.right)

            return (
                max(left[0], right[0], left[1] + right[1] + 1),
                max(left[1], right[1]) + 1,
            )

        return traverse(root)[0] - 1
