# https://leetcode.com/problems/closest-binary-search-tree-value/


from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValueBST(
        self,
        root: TreeNode,
        val: float,
        lo: float = float("-inf"),
        hi: float = float("inf"),
    ) -> float:
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

root = TreeNode(20)
root.left = TreeNode(8)
root.left.left = TreeNode(4)
root.left.right = TreeNode(12)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)
root.right = TreeNode(22)
root.right.left = TreeNode(21)
root.right.right = TreeNode(30)

print(sol.closestValueBST(root, 9))
print(sol.closestValueBST(root, 10))
print(sol.closestValueBST(root, 10.5))
print(sol.closestValueBST(root, 23))

root = TreeNode(9)
root.left = TreeNode(4)
root.left.left = TreeNode(3)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(5)
root.left.right.right = TreeNode(7)
root.right = TreeNode(17)
root.right.right = TreeNode(22)
root.right.right.left = TreeNode(20)

print(sol.closestValueBST(root, 4))
print(sol.closestValueBST(root, 18))
print(sol.closestValueBST(root, 12))
