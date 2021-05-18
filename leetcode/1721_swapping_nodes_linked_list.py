# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

from collections import deque


class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None


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
        l.value, r.value = r.value, l.value
        return head
