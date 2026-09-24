# https://leetcode.com/problems/invert-binary-tree/


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        nodes = [root]
        while nodes:
            node = nodes.pop()
            if node is None:
                continue
            node.left, node.right = node.right, node.left
            nodes.append(node.left)
            nodes.append(node.right)

        return root

    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
