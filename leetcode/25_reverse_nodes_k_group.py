# https://leetcode.com/problems/reverse-nodes-in-k-group/

class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head

        root = head
        for _ in range(k - 1):
            root = root.next

        prev = ListNode(None)
        while head:
            tail, next_tail = self.recurse(head.next, head, k - 1)
            if tail == head:
                head = None
            else:
                prev.next = next_tail
                prev = head
                head.next = tail
                head = tail

        return root

    def recurse(self, head: ListNode, prev: ListNode, depth: int) -> ListNode:
        if head and depth:
            tail, next_tail = self.recurse(head.next, head, depth - 1)
            if tail == head:
                return prev, None
            else:
                head.next = prev
                return tail, next_tail
        elif head and not depth:
            return head, prev
        elif not head and depth:
            return prev, None
        else:
            return None, prev
