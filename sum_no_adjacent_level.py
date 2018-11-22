class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def maxSumWithNoAdjacent(self, root, total):
        """
        :type root: Node
        :type total: int
        :rtype: int
        :rtype: int
        """

        if not root:
            return 0, total

        left, total = self.maxSumWithNoAdjacent(root.left, total)
        right, total = self.maxSumWithNoAdjacent(root.right, total)

        if left + right < root.val:
            total += root.val - left - right
            return root.val, total

        return 0, total

sol = Solution()

root = Node(10)
root.left = Node(1)
root.left.left = Node(2)
root.left.left.left = Node(1)
root.left.right = Node(3)
root.left.right.left = Node(4)
root.left.right.right = Node(5)
print(sol.maxSumWithNoAdjacent(root, 0)[1])

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.left.left = Node(17)
root.left.left.left.left = Node(11)
root.left.left.right = Node(18)
root.left.left.right.left = Node(12)
root.left.left.right.right = Node(13)
root.right = Node(3)
root.right.left = Node(5)
root.right.left.left = Node(19)
root.right.right = Node(6)
root.right.right.left = Node(30)
print(sol.maxSumWithNoAdjacent(root, 0)[1])
