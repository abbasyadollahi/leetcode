# https://leetcode.com/problems/reorder-list/

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next

        stack = stack[len(stack) // 2 :]
        root = head
        while stack:
            node = stack.pop()
            head.next, node.next, head = node, head.next, head.next

        node.next = None
        return root


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first_half = head
        second_half_reversed = self.reverseList(self.splitList(head))
        self.mergeTwoLists(first_half, second_half_reversed)

    def splitList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        single = double = head
        while double and double.next:
            previous = single
            single = single.next
            double = double.next.next

        if double:
            single.next, split = None, single.next
        else:
            previous.next, split = None, single

        return split

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        while head is not None:
            head.next, head, previous = previous, head.next, head
        return previous

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode()
        while list1 and list2:
            head.next, list1 = list1, list1.next
            head = head.next
            head.next, list2 = list2, list2.next
            head = head.next

        leftover = list1 or list2
        while leftover:
            head.next, leftover = leftover, leftover.next
            head = head.next

        return dummy.next
