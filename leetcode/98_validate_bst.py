# https://leetcode.com/problems/validate-binary-search-tree/

import sys
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def is_bounded(node: TreeNode, lower: int, upper: int) -> bool:
            if node is None:
                return True
            if node.val not in range(lower + 1, upper):
                return False

            return is_bounded(node.left, lower, node.val) and is_bounded(node.right, node.val, upper)

        return is_bounded(root, -sys.maxsize, sys.maxsize)
