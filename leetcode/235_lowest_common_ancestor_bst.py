# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None
        self.p = p
        self.q = q
        self.traverse(root)
        return self.lca

    def traverse(self, node: TreeNode) -> bool:
        if self.lca is None and node:
            left = self.traverse(node.left)
            right = self.traverse(node.right)
            current = node in [self.p, self.q]
            if (left or current) and (right or current) and (left or right):
                self.lca = node
            return left or right or current
        return False
