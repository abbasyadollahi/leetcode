# https://leetcode.com/problems/closest-binary-search-tree-val/

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValueBST(self, root: Node, val: float, lo: float = float('-inf'), hi: float = float('inf')) -> float:
        if not root:
            return None

        if root.val == val:
            return val
        elif root.val < val:
            lo = root.val
            if root.right:
                return self.closestValueBST(root.right, val, lo, hi)
        else:
            hi = root.val
            if root.left:
                return self.closestValueBST(root.left, val, lo, hi)

        return min([lo, hi], key=lambda x: abs(x - val))

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
