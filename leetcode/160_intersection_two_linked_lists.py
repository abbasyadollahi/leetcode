# https://leetcode.com/problems/intersection-of-two-linked-lists/

class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class Solution:
    def getIntersectionNode(self, head_a: ListNode, head_b: ListNode) -> ListNode:
        if not head_a or not head_b:
            return None

        a, b = head_a, head_b
        while a is not b:
            a = a.next if a else head_b
            b = b.next if b else head_a

        return a
