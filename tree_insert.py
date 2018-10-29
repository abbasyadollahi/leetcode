class TreeNode(object):
    def __init__(self, v):
        self.value = v
        self.next = None
        self.left = None
        self.right = None

class Solution():
    def get_min_node(self, root):
        """
        :param root" TreeNode
        """

        while root.left:
            root = root.left
        return root

    def insert_node(self, root, value):
        """
        :param root: TreeNode
        :param node: TreeNode
        """

        if root is None:
            return TreeNode(value)

        node = root
        prev = node
        while node:
            prev = node
            if node.value >= value:
               node = node.left
            elif node.value < value:
                node = node.right


        if prev.value < value:
            prev.right = TreeNode(value)
            prev.right.next = prev.next
            prev.next = prev.right
        else:
            prev.left = TreeNode(value)
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
        :param root" TreeNode
        """

        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.value)
            res = res + self.inorder_traversal(root.right)
        return res

    def next_traversal(self, root):
        """
        :param root" TreeNode
        """

        res = []
        min_node = self.get_min_node(root)
        while min_node.next:
            res.append(min_node.value)
            min_node = min_node.next
        res.append(min_node.value)
        return res

sol = Solution()

root = TreeNode(100)
print(sol.next_traversal(root))
root = sol.insert_node(root, 70)
print(sol.next_traversal(root))
root = sol.insert_node(root, 120)
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
root = sol.insert_node(root, 115)
print(sol.next_traversal(root))
root = sol.insert_node(root, 200)
print(sol.next_traversal(root))
