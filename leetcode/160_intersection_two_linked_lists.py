# https://leetcode.com/problems/intersection-of-two-linked-lists/

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a
