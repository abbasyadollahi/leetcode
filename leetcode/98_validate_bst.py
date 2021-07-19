# https://leetcode.com/problems/validate-binary-search-tree/

import sys


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
            return self.is_bounded(root, -sys.maxsize, sys.maxsize)

    def is_bounded(self, node: TreeNode, lower: int, upper: int) -> bool:
        if node is None:
            return True
        if node.val not in range(lower + 1, upper):
            return False

        return self.is_bounded(node.left, lower, node.val) and self.is_bounded(node.right, node.val, upper)
