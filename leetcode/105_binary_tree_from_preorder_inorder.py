# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        self.order = iter(preorder)
        root = TreeNode(next(self.order))
        node_index = inorder.index(root.val)
        self.recurse(root, inorder[:node_index], inorder[node_index+1:])

        return root

    def recurse(self, root: TreeNode, left: list, right: list):
        if left:
            node = TreeNode(next(self.order))
            node_index = left.index(node.val)
            root.left = node
            self.recurse(node, left[:node_index], left[node_index+1:])

        if right:
            node = TreeNode(next(self.order))
            node_index = right.index(node.val)
            root.right = node
            self.recurse(node, right[:node_index], right[node_index+1:])
