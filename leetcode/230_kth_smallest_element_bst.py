# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

import heapq
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.smallest = []
        self.traverse(root)
        return -self.smallest[0]

    def traverse(self, node: TreeNode) -> None:
        if node:
            if len(self.smallest) < self.k:
                heapq.heappush(self.smallest, -node.val)
            elif node.val < -self.smallest[0]:
                heapq.heapreplace(self.smallest, -node.val)
            self.traverse(node.left)
            self.traverse(node.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.smallest = []
        self.traverse(root)
        return self.smallest.pop()

    def traverse(self, node: TreeNode) -> None:
        if len(self.smallest) < self.k and node:
            self.traverse(node.left)
            if len(self.smallest) < self.k:
                self.smallest.append(node.val)
            self.traverse(node.right)
