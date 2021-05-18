# https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        prev = None
        while head != None:
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
