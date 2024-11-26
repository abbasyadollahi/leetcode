# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = self.traverse(root)
        _, max_product = self.product(root, total)
        return max_product % (10**9 + 7)

    def traverse(self, root: Optional[TreeNode]) -> int:
        if root:
            return root.val + self.traverse(root.left) + self.traverse(root.right)
        else:
            return 0

    def product(self, root: Optional[TreeNode], total: int) -> tuple[int, int]:
        if root:
            total_left, max_left = self.product(root.left, total)
            total_right, max_right = self.product(root.right, total)
            total_root = total_left + total_right + root.val
            max_root = total_root * (total - total_root)
            return total_root, max(max_left, max_right, max_root)
        else:
            return 0, 0
