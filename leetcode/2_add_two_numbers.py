# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        multiplier = 1
        sum_int = 0
        while l1 and l2:
            sum_int += (l1.val + l2.val) * multiplier
            multiplier *= 10
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum_int += l1.val * multiplier
            multiplier *= 10
            l1 = l1.next

        while l2:
            sum_int += l2.val * multiplier
            multiplier *= 10
            l2 = l2.next

        sum_str = str(sum_int)[::-1]
        sum_l = ListNode(sum_str[0])
        sum_l_node = sum_l
        for i in sum_str[1:]:
            sum_l_node.next = ListNode(int(i))
            sum_l_node = sum_l_node.next

        return sum_l
