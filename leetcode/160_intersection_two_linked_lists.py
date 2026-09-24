# https://leetcode.com/problems/intersection-of-two-linked-lists/


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        if not headA or not headB:
            return None

        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a
