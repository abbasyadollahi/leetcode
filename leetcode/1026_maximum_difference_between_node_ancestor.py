# https://leetcode.com/problems/maximum-difference-between-root-and-ancestor/

from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return max(
            self.traverse(root.left, [root], [root]),
            self.traverse(root.right, [root], [root])
        )

    def traverse(self, root: Optional[TreeNode], min_ancestors: List[TreeNode], max_ancestors: List[TreeNode]) -> int:
        if root is None:
            return 0

        min_ancestor = min_ancestors[-1]
        max_ancestor = max_ancestors[-1]

        if root.val < min_ancestor.val:
            min_ancestors.append(root)
        if root.val > max_ancestor.val:
            max_ancestors.append(root)

        max_left = self.traverse(root.left, min_ancestors, max_ancestors)
        max_right = self.traverse(root.right, min_ancestors, max_ancestors)

        if root == min_ancestors[-1]:
            min_ancestors.pop()
        if root == max_ancestors[-1]:
            max_ancestors.pop()

        return max(
            abs(root.val - min_ancestor.val),
            abs(root.val - max_ancestor.val),
            max_left,
            max_right
        )
