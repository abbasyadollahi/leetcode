# https://leetcode.com/problems/palindrome-linked-list/


from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        root = head

        nodes = 0
        while head:
            nodes += 1
            head = head.next

        prev = None
        head = root
        i = 0
        mid = nodes // 2
        odd = nodes % 2
        while i < mid:
            i += 1
            head.next, prev, head = prev, head, head.next

        if odd:
            head = head.next

        while prev and head:
            if prev.val != head.val:
                return False
            else:
                prev = prev.next
                head = head.next

        return True
