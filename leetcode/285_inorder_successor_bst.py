# https://leetcode.com/problems/inorder-successor-in-bst/


from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderSuccessorBST(self, root: TreeNode, node: TreeNode) -> TreeNode:
        if root is None:
            return None

        n = self.search(root, node)

        return n if isinstance(n, TreeNode) else None

    def search(self, root: TreeNode, node: TreeNode, found: bool = False) -> TreeNode:
        if root.left:
            found = self.search(root.left, node, found)

        if found is True:
            return root
        elif isinstance(found, TreeNode):
            return found
        found = root.val == node.val

        if root.right:
            found = self.search(root.right, node, found)

        return found

    def inorderSuccessorBST(self, root: TreeNode, node: TreeNode) -> TreeNode:
        stack = []
        if root is None:
            return None

        while root is not None and root.val != node.val:
            stack.append(root)
            if root.val > node.val:
                root = root.left
            else:
                root = root.right

        if root is None:
            return None

        stack.append(root)
        if root.right:
            top_sub_tree = root.right
            while root.right:
                root = root.right
                if root.left:
                    while root.left:
                        root = root.left
                    return root
            return top_sub_tree
        else:
            while len(stack):
                parent = stack.pop()
                if parent.val > node.val:
                    return parent

        return None


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

print(sol.inorderSuccessorBST(root, TreeNode(5)))
print(sol.inorderSuccessorBST(root, TreeNode(8)).val)
print(sol.inorderSuccessorBST(root, TreeNode(10)).val)
print(sol.inorderSuccessorBST(root, TreeNode(14)).val)
print(sol.inorderSuccessorBST(root, TreeNode(20)).val)
print(sol.inorderSuccessorBST(root, TreeNode(21)).val)
print(sol.inorderSuccessorBST(root, TreeNode(22)).val)
print(sol.inorderSuccessorBST(root, TreeNode(30)))
