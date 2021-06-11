# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import List


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.order = iter(preorder)
        root = TreeNode(next(self.order))
        node_idx = inorder.index(root.val)
        self.recurse(root, inorder[:node_idx], inorder[node_idx+1:])

        return root

    def recurse(self, root: TreeNode, left: list, right: list):
        if left:
            node = TreeNode(next(self.order))
            node_idx = left.index(node.val)
            root.left = node
            self.recurse(node, left[:node_idx], left[node_idx+1:])

        if right:
            node = TreeNode(next(self.order))
            node_idx = right.index(node.val)
            root.right = node
            self.recurse(node, right[:node_idx], right[node_idx+1:])
