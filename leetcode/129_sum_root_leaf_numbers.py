# https://leetcode.com/problems/sum-root-to-leaf-numbers/


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def traverse(node: TreeNode | None, total: int) -> int:
            total *= 10
            total += node.val

            if node.left and node.right:
                return traverse(node.left, total) + traverse(node.right, total)
            elif node.left or node.right:
                return traverse(node.left or node.right, total)
            else:
                return total

        return traverse(root, 0)
