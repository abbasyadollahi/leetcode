# https://leetcode.com/problems/diameter-of-binary-tree/


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        def traverse(node: TreeNode | None) -> tuple[int, int]:
            if node is None:
                return 0, 0

            left = traverse(node.left)
            right = traverse(node.right)

            return (
                max(left[0], right[0], left[1] + right[1] + 1),
                max(left[1], right[1]) + 1,
            )

        return traverse(root)[0] - 1
