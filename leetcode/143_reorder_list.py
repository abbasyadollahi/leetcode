# https://leetcode.com/problems/reorder-list/

class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next

        stack = stack[len(stack)//2:]
        root = head
        while stack:
            node = stack.pop()
            head.next, node.next, head = node, head.next, head.next

        node.next = None
        return root
