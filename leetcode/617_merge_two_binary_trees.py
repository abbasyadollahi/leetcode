# https://leetcode.com/problems/merge-two-binary-trees/

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            merged = TreeNode(t1.val + t2.val)

            merged.left = self.mergeTrees(t1.left, t2.left)
            merged.right = self.mergeTrees(t1.right, t2.right)

            return merged
        else:
            return t1 or t2
