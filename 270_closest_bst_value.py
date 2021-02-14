# https://leetcode.com/problems/closest-binary-search-tree-value/

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def closestValueBST(self, root, value, lo=float('-inf'), hi=float('inf')):
        """
        :type root: Node
        :type value: float
        :rtype: float
        """

        if not root:
            return None

        if root.val == value:
            return value
        elif root.val < value:
            lo = root.val
            if root.right:
                return self.closestValueBST(root.right, value, lo, hi)
        else:
            hi = root.val
            if root.left:
                return self.closestValueBST(root.left, value, lo, hi)

        return min([lo, hi], key=lambda x: abs(x - value))

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

print(sol.closestValueBST(root, 9))
print(sol.closestValueBST(root, 10))
print(sol.closestValueBST(root, 10.5))
print(sol.closestValueBST(root, 23))

root = Node(9)
root.left = Node(4)
root.left.left = Node(3)
root.left.right = Node(6)
root.left.right.left = Node(5)
root.left.right.right = Node(7)
root.right = Node(17)
root.right.right = Node(22)
root.right.right.left = Node(20)

print(sol.closestValueBST(root, 4))
print(sol.closestValueBST(root, 18))
print(sol.closestValueBST(root, 12))
