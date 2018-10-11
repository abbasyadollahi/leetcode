# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val, nextn):
        self.val = val
        self.next = nextn

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # First way
        cur = head
        prev = head

        while (head.next != None):
            if cur.next == None or cur.next.next == cur:
                cur.next = prev
                cur = head
                prev = None
            else:
                prev = cur
                cur = cur.next


        # Second way
        current = head
        prev1 = head
        prev2 = None

        while (prev1 != None):
            new_prev = ListNode(prev1.val, prev1.next)
            current = current.next

            prev1.next = prev2

            prev2 = new_prev
            prev1 = current
