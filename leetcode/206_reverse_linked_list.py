# https://leetcode.com/problems/reverse-linked-list/


from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head.next is not None:
            head.next, prev, head = prev, head, head.next

        return head

    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        prev = None
        while head is not None:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt

        return prev

    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        _, top = self.recursiveReverse(head)

        return top

    def recursiveReverse(self, head: ListNode) -> ListNode:
        if not head.next:
            return head, head

        nxt, top = self.recursiveReverse(head.next)
        nxt.next = head
        head.next = None

        return head, top
