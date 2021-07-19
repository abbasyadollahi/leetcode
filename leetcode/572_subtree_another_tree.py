# https://leetcode.com/problems/subtree-of-another-tree/

from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        queue = deque()
        queue.append(root)

        while len(queue):
            node = queue.popleft()
            if node.val == subRoot.val and self.verify_trees(node, subRoot):
                return True
            else:
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return False

    def verify_trees(self, root: TreeNode, sub_root: TreeNode) -> bool:
        if root is None and sub_root is None:
            return True
        elif root is None or sub_root is None:
            return False
        else:
            return (
                root.val == sub_root.val and
                self.verify_trees(root.left, sub_root.left) and
                self.verify_trees(root.right, sub_root.right)
            )
