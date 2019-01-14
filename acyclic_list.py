# https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head:
            return False

        last = head
        first = head.next
        while first is not last:
            if not first or not first.next:
                return False
            last = last.next
            first = first.next.next

        return True
