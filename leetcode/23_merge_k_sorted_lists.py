# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        nums = []
        for l in lists:
            while l:
                nums.append(l.val)
                l = l.next

        head = current = ListNode(0)
        for n in sorted(nums):
            current.next = ListNode(n)
            current = current.next

        return head.next
