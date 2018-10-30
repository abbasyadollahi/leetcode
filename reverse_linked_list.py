class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reverseListV1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

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

    def reverseListV2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        current = head
        prev1 = head
        prev2 = None

        while (prev1 != None):
            new_prev = ListNode(prev1.val)
            new_prev.next = prev1.next
            current = current.next

            prev1.next = prev2
            prev2 = new_prev
            prev1 = current
