# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None

        start = head
        end = head
        for _ in range(n):
            if end.next:
                end = end.next
            else:
                return head.next

        while end.next:
            end = end.next
            start = start.next

        start.next = start.next.next

        return head


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(2)
l1.next.next.next.next = ListNode(22)
l1.next.next.next.next.next = ListNode(12)
l1.next.next.next.next.next.next = ListNode(5)
l1.next.next.next.next.next.next.next = ListNode(0)
l1.next.next.next.next.next.next.next.next = ListNode(31)

l2 = ListNode(1)
l2.next = ListNode(2)

l3 = None

sol = Solution()

tc1 = sol.removeNthFromEnd(l1, 4)
while tc1:
    print(tc1.val, end=", ")
    tc1 = tc1.next
print()

tc2 = sol.removeNthFromEnd(l2, 2)
while tc2:
    print(tc2.val, end=", ")
    tc2 = tc2.next
print()

tc3 = sol.removeNthFromEnd(l3, 2)
while tc3:
    print(tc3.val, end=", ")
    tc3 = tc3.next
print()
