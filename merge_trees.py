# https://leetcode.com/problems/merge-two-binary-trees/

class ListNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: ListNode
        :type t2: ListNode
        :rtype: ListNode
        """

        if t1 and t2:
            merged = ListNode(t1.val + t2.val)

            merged.left = self.mergeTrees(t1.left, t2.left)
            merged.right = self.mergeTrees(t1.right, t2.right)

            return merged
        else:
            return t1 or t2
