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

    def insert_node(self, root: Node, value: Node) -> Node:
        if root is None:
            return Node(value)

        node = root
        prev = node
        while node:
            prev = node
            node = node.left if node.value >= value else node.right

        if prev.value < value:
            prev.right = Node(value)
            prev.right.next = prev.next
            prev.next = prev.right
        else:
            prev.left = Node(value)
            min_node = self.get_min_node(root)
            if min_node is prev.left:
                min_node.next = prev
            else:
                while min_node.next is not prev:
                    min_node = min_node.next
                min_node.next = prev.left
                prev.left.next = prev

        return root

    def inorder_traversal(self, root: Node) -> List[int]:
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.value)
            res = res + self.inorder_traversal(root.right)
        return res

    def next_traversal(self, root: Node) -> List[int]:
        res = []
        min_node = self.get_min_node(root)
        while min_node.next:
            res.append(min_node.value)
            min_node = min_node.next
        res.append(min_node.value)
        return res


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
