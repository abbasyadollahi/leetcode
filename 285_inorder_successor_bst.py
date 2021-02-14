# https://leetcode.com/problems/inorder-successor-in-bst/

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessorBST(self, root, node, found=False):
        """
        :type root: Node
        :type node: Node
        :rtype: Node
        """

        if root is None:
            return None

        n = self.search(root, node)

        return n if isinstance(n, Node) else None

    def search(self, root, node, found=False):
        """
        :type root: Node
        :type node: Node
        :type found: bool
        :rtype: Node
        """

        if root.left:
            found = self.search(root.left, node, found)

        if found is True:
            return root
        elif isinstance(found, Node):
            return found
        found = root.val == node.val

        if root.right:
            found = self.search(root.right, node, found)

        return found

sol = Solution()

root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.left = Node(21)
root.right.right = Node(30)

print(sol.inorderSuccessorBST(root, Node(5)))
print(sol.inorderSuccessorBST(root, Node(8)).val)
print(sol.inorderSuccessorBST(root, Node(10)).val)
print(sol.inorderSuccessorBST(root, Node(14)).val)
print(sol.inorderSuccessorBST(root, Node(20)).val)
print(sol.inorderSuccessorBST(root, Node(21)).val)
print(sol.inorderSuccessorBST(root, Node(22)).val)
print(sol.inorderSuccessorBST(root, Node(30)))
