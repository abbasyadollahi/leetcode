from typing import List


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.left = None
        self.right = None


class Solution:
    def get_min_node(self, root: Node) -> Node:
        while root.left:
            root = root.left
        return root

    def insert_node(self, root: Node, value: int) -> Node:
        node = Node(value)
        if root is None:
            return node

        smaller = None
        bigger = None
        parent = None
        current = root
        while current:
            parent = current
            if current.value > value:
                bigger = current
                current = current.left
            else:
                smaller = current
                current = current.right

        if parent.value > value:
            parent.left = node
        else:
            parent.right = node

        if smaller:
            smaller.next = node
        if bigger:
            node.next = bigger

        return root

    def inorder_traversal(self, root: Node) -> List[int]:
        values = []
        if root:
            values = self.inorder_traversal(root.left)
            values.append(root.value)
            values = values + self.inorder_traversal(root.right)
        return values

    def next_traversal(self, root: Node) -> List[int]:
        values = []
        min_node = self.get_min_node(root)
        while min_node:
            values.append(min_node.value)
            min_node = min_node.next
        return values


sol = Solution()
root = Node(100)

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
