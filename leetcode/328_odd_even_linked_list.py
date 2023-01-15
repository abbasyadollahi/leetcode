# https://leetcode.com/problems/odd-even-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        odd = odd_head = odd_tail = head
        even = even_head = head.next

        while odd and even:
            odd.next = odd.next and odd.next.next
            even.next = even.next and even.next.next
            odd_tail = odd.next or odd
            odd = odd.next
            even = even.next

        odd_tail.next = even_head

        return odd_head
