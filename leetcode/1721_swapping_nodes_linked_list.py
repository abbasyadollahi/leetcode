# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

from collections import deque


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        l = None
        r = None
        node = head

        i = 1
        temp = deque(maxlen=k)
        while node:
            if i == k:
                l = node
            temp.append(node)
            i += 1
            node = node.next

        r = temp.popleft()
        l.val, r.val = r.val, l.val
        return head
