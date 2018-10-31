# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        mult = 1
        sum_int = 0
        while l1 and l2:
            sum_int += (l1.val + l2.val) * mult
            mult *= 10
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum_int += l1.val * mult
            mult *= 10
            l1 = l1.next

        while l2:
            sum_int += l2.val * mult
            mult *= 10
            l2 = l2.next

        sum_str = str(sum_int)[::-1]
        sum_l = ListNode(sum_str[0])
        sum_l_node = sum_l
        for i in sum_str[1:]:
            sum_l_node.next = ListNode(int(i))
            sum_l_node = sum_l_node.next

        return sum_l

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(2)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(9)

l3 = ListNode(0)

sol = Solution()

tc1 = sol.addTwoNumbers(l1, l2)
while tc1:
    print (tc1.val, end='')
    tc1 = tc1.next
print()

tc2 = sol.addTwoNumbers(l1, l3)
while tc2:
    print (tc2.val, end='')
    tc2 = tc2.next
print()
