# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

from typing import Union


class Node:
    def __init__(self, value: int = 0):
        self.value  = value
        self.left = None
        self.right = None


class Solution:
    def subtreeWithAllDeepest(self, root: Node) -> Node:
        node, _ = self.traverse(root, 0)
        return node

    def traverse(self, root: Node, level: int) -> Union[Node, int]:
        if root is None:
            return None, level

        l_node, l_level = self.traverse(root.left, level + 1)
        r_node, r_level = self.traverse(root.right, level + 1)

        if l_level == r_level:
            return root, l_level
        elif l_level > r_level:
            return l_node, l_level
        elif l_level < r_level:
            return r_node, r_level
