# https://leetcode.com/problems/univalued-binary-tree/

from typing import Union


class Node:
    def __init__(self, value: int = 0):
        self.value  = value
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root: Node) -> bool:
        return self.traverse(root, root.value)

    def traverse(self, root: Node, value: int) -> bool:
        return root is None or root.value == value and self.traverse(root.left, value) and self.traverse(root.right, value)
