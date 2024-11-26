# https://leetcode.com/problems/find-duplicate-subtrees/

from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> list[TreeNode]:
        subtrees = defaultdict(list)

        def traverse(node: Optional[TreeNode]) -> str:
            if not node:
                return "."

            subtree = f"[{traverse(node.left)}<{node.val}>{traverse(node.right)}]"
            subtrees[subtree].append(node)

            return subtree

        traverse(root)

        return [nodes[0] for _, nodes in subtrees.items() if len(nodes) > 1]
