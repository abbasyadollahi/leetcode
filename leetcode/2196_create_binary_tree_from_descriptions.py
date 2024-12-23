# https://leetcode.com/problems/create-binary-tree-from-descriptions/

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        parents = set()

        for parent, child, is_left in descriptions:
            children.add(child)
            parents.add(parent)

            child_node = nodes.get(child, TreeNode(child))
            parent_node = nodes.get(parent, TreeNode(parent))

            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

            nodes[child] = child_node
            nodes[parent] = parent_node

        return nodes[(parents - children).pop()]
