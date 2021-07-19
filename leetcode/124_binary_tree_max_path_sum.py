# https://leetcode.com/problems/binary-tree-maximum-path-sum/

from typing import Tuple


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return max(self.recurse(root))

    def recurse(self, root: TreeNode) -> Tuple[int, int]:
        if root is None:
            return float('-inf'), float('-inf')

        left_included_sum, left_excluded_sum = self.recurse(root.left)
        right_included_sum, right_excluded_sum = self.recurse(root.right)

        return (
            root.val + max(left_included_sum, right_included_sum, 0),
            max(root.val, left_excluded_sum, right_excluded_sum, root.val + max(left_included_sum, 0) + max(right_included_sum, 0))
        )
