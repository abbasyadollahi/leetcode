// https://leetcode.com/problems/add-two-numbers/

class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    const root = new ListNode(0, null);

    let carry = 0;
    let current = root;
    while (l1 !== null && l2 !== null) {
        const node = new ListNode(l1.val + l2.val + carry);
        current.next = node;
        current = node;

        carry = Math.floor(node.val / 10);
        node.val %= 10

        l1 = l1.next;
        l2 = l2.next;
    }

    let leftover = l1 || l2;
    while (leftover !== null) {
        const node = new ListNode(leftover.val + carry);
        current.next = node;
        current = node;

        carry = Math.floor(node.val / 10);
        node.val %= 10

        leftover = leftover.next;
    }

    if (carry) {
        const node = new ListNode(carry);
        current.next = node;
        current = node;
    }

    return root.next;
};
