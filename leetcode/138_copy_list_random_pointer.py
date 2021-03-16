# https://leetcode.com/problems/copy-list-with-random-pointer/

class RandomListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.random = None


class Solution:
    def copyRandomList(self, head: RandomListNode) -> RandomListNode:
        if not head:
            return None

        nodes = {}
        dummy = head
        while dummy:
            nodes[dummy.value] = RandomListNode(dummy.value)
            dummy = dummy.next

        copy = nodes[head.value]
        while head:
            n = nodes[head.value]
            n.next = nodes[head.next.value] if head.next else None
            n.random = nodes[head.random.value] if head.random else None
            head = head.next

        return copy
