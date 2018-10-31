class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.left = None
        self.right = None

class Solution():
    def get_min_node(self, root):
        """
        :type root: ListNode
        """

        while root.left:
            root = root.left
        return root

    def insert_node(self, root, value):
        """
        :type root: ListNode
        :type node: ListNode
        """

        if root is None:
            return ListNode(value)

        node = root
        prev = node
        while node:
            prev = node
            if node.val >= value:
               node = node.left
            elif node.val < value:
                node = node.right


        if prev.val < value:
            prev.right = ListNode(value)
            prev.right.next = prev.next
            prev.next = prev.right
        else:
            prev.left = ListNode(value)
            min_node = self.get_min_node(root)
            if min_node is prev.left:
                min_node.next = prev
            else:
                while min_node.next is not prev:
                    min_node = min_node.next
                min_node.next = prev.left
                prev.left.next = prev

        return root

    def inorder_traversal(self, root):
        """
        :type root: ListNode
        """

        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.val)
            res = res + self.inorder_traversal(root.right)
        return res

    def next_traversal(self, root):
        """
        :type root: ListNode
        """

        res = []
        min_node = self.get_min_node(root)
        while min_node.next:
            res.append(min_node.val)
            min_node = min_node.next
        res.append(min_node.val)
        return res

sol = Solution()
root = ListNode(100)

root = sol.insert_node(root, 70)
print(sol.next_traversal(root))
root = sol.insert_node(root, 50)
print(sol.next_traversal(root))
root = sol.insert_node(root, 40)
print(sol.next_traversal(root))
root = sol.insert_node(root, 35)
print(sol.next_traversal(root))
root = sol.insert_node(root, 110)
print(sol.next_traversal(root))
root = sol.insert_node(root, 150)
print(sol.next_traversal(root))
root = sol.insert_node(root, 105)
print(sol.next_traversal(root))
root = sol.insert_node(root, 120)
print(sol.next_traversal(root))
root = sol.insert_node(root, 115)
print(sol.next_traversal(root))
root = sol.insert_node(root, 200)
print(sol.next_traversal(root))
