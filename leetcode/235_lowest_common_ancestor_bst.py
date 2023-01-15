# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def traverse(node: TreeNode) -> bool:
            if node is None:
                return False

            left = traverse(node.left)
            right = traverse(node.right)

            if (left and right) or ((left or right) and node in [p, q]):
                self.lca = node

            return left or right or node in [p, q]

        self.lca = None
        traverse(root)
        return self.lca

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def traverse(node: TreeNode) -> TreeNode:
            if node is None:
                return None
            if node in [p, q]:
                return node

            children = (traverse(node.left), traverse(node.right))
            if p in children and q in children:
                return node

            return next(filter(None, children), None)

        return traverse(root)
