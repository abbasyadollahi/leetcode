# https://leetcode.com/problems/univalued-binary-tree/

from typing import Union


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Node) -> bool:
        return self.traverse(root, root.val)

    def traverse(self, root: Node, val: int) -> bool:
        return root is None or root.val == val and self.traverse(root.left, val) and self.traverse(root.right, val)
