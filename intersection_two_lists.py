# https://leetcode.com/problems/intersection-of-two-linked-lists/

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """

        if not headA or not headB:
            return None

        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a
