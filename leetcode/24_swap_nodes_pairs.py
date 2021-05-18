# https://leetcode.com/problems/swap-nodes-in-pairs/

class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head:
            root = self.swap(head)
            prev_head = head
            head = head.next
        else:
            return head

        while head:
            new_head = self.swap(head)
            prev_head.next = new_head
            prev_head = head
            head = head.next

        return root

    def swap(self, head: ListNode) -> ListNode:
        if head.next:
            new_head = head.next
            head.next = head.next.next
            new_head.next = head
            return new_head
        else:
            return head
