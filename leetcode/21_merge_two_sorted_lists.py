# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode(None)
        head = l
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        while l1:
            head.next = l1
            l1 = l1.next
            head = head.next

        while l2:
            head.next = l2
            l2 = l2.next
            head = head.next

        return l.next
