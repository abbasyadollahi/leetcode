# https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None


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
