# https://leetcode.com/problems/merge-two-sorted-lists/


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = current = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        leftover = list1 or list2
        while leftover:
            current.next = leftover
            leftover = leftover.next
            current = current.next

        return dummy.next
