// https://leetcode.com/problems/add-two-numbers/

package leetcode;

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode root = new ListNode();

        int carry = 0;
        ListNode current = root;
        while (l1 != null && l2 != null) {
            ListNode node = new ListNode(l1.val + l2.val + carry);
            current.next = node;
            current = node;

            carry = node.val / 10;
            node.val %= 10;

            l1 = l1.next;
            l2 = l2.next;
        }

        ListNode leftover = l1 != null ? l1 : l2 != null ? l2 : null;
        while (leftover != null) {
            ListNode node = new ListNode(leftover.val + carry);
            current.next = node;
            current = node;

            carry = node.val / 10;
            node.val %= 10;

            leftover = leftover.next;
        }

        if (carry > 0) {
            ListNode node = new ListNode(carry);
            current.next = node;
            current = node;
        }

        return root.next;
    }
}
