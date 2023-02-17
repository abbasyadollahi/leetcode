# https://leetcode.com/problems/merge-k-sorted-lists/

class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
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

    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        k = len(lists)
        if k == 0:
            return None
        if k == 1:
            return lists[0]

        l1 = self.mergeKLists(lists[:k//2])
        l2 = self.mergeKLists(lists[k//2:])

        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode(None)
        head = l
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        leftover = l1 or l2
        while leftover:
            head.next = leftover
            leftover = leftover.next
            head = head.next

        return l.next
