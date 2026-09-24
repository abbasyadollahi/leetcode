# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        current_node = head
        next_node = head.next
        while current_node is not None:
            while next_node is not None and next_node.val == current_node.val:
                next_node = next_node.next
            current_node.next = current_node = next_node
            if current_node is not None:
                next_node = current_node.next
        return head
