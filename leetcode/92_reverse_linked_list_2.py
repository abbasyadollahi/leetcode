# https://leetcode.com/problems/reverse-linked-list-ii/


from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        root = head

        i = 1
        first = None
        while i < left:
            first = head
            head = head.next
            i += 1

        last = head
        prev = None
        while i < right:
            head.next, prev, head = prev, head, head.next
            i += 1

        if first:
            first.next = head
        else:
            root = head

        last.next = head.next
        if prev:
            head.next = prev

        return root
