# https://leetcode.com/problems/middle-of-the-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        single = head
        double = head

        while double and double.next:
            single = single.next
            double = double.next.next

        return single
