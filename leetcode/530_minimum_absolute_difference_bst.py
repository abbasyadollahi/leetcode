# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder_traversal(node: Optional[TreeNode]) -> list[int]:
            if not node:
                return []

            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

        nums = inorder_traversal(root)
        return min(abs(right - left) for left, right in zip(nums, nums[1:]))
