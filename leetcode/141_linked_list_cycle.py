# https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
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

    def hasCycle(self, head: ListNode) -> bool:
        last = first = head

        while first is not None and first.next is not None:
            first = first.next.next
            last = last.next
            if first is last:
                return True

        return False
