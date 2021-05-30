# https://leetcode.com/problems/merge-two-binary-trees/

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: Node, t2: Node) -> Node:
        if t1 and t2:
            merged = Node(t1.val + t2.val)

            merged.left = self.mergeTrees(t1.left, t2.left)
            merged.right = self.mergeTrees(t1.right, t2.right)

            return merged
        else:
            return t1 or t2
