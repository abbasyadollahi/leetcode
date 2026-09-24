# https://leetcode.com/problems/range-sum-of-bst/


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        if not root:
            return 0

        total = 0
        if root.val in range(low, high + 1):
            total += root.val
        if root.val > low:
            total += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            total += self.rangeSumBST(root.right, low, high)
        return total
