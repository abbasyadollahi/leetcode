# https://leetcode.com/problems/sum-root-to-leaf-numbers/

from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(node: Optional[TreeNode], total: int) -> int:
            total *= 10
            total += node.val

            if node.left and node.right:
                return traverse(node.left, total) + traverse(node.right, total)
            elif node.left or node.right:
                return traverse(node.left or node.right, total)
            else:
                return total

        return traverse(root, 0)
