# https://www.geeksforgeeks.org/maximum-sum-tree-adjacent-levels-not-allowed/

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def maxSumWithNoAdjacent(self, root: Node, total: int) -> int:
        if not root:
            return 0, total

        left, total = self.maxSumWithNoAdjacent(root.left, total)
        right, total = self.maxSumWithNoAdjacent(root.right, total)

        if left + right < root.value:
            total += root.value - left - right
            return root.value, total

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
