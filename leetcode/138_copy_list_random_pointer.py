# https://leetcode.com/problems/copy-list-with-random-pointer/

class RandomListNode:
    def __init__(self, val: int = 0, next: 'RandomListNode' = None, random: 'RandomListNode' = None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: RandomListNode) -> RandomListNode:
        if not head:
            return None

        nodes = {}
        dummy = head
        while dummy:
            nodes[dummy.val] = RandomListNode(dummy.val)
            dummy = dummy.next

        copy = nodes[head.val]
        while head:
            n = nodes[head.val]
            n.next = nodes[head.next.val] if head.next else None
            n.random = nodes[head.random.val] if head.random else None
            head = head.next

        return copy
