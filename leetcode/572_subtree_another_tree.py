# https://leetcode.com/problems/subtree-of-another-tree/


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            else:
                return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

        roots = []

        nodes = [root]
        while nodes:
            node = nodes.pop()
            if node is None:
                continue
            if node.val == subRoot.val:
                roots.append(node)
            nodes.append(node.left)
            nodes.append(node.right)

        return any(is_same_tree(root, subRoot) for root in roots)
