# https://leetcode.com/problems/binary-search-tree-iterator/

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode) -> None:
        self.root = root
        self.parents = []

        if root:
            while root.left:
                self.parents.append(root)
                root = root.left
        self.node = root

    def next(self) -> int:
        nxt = self.node
        if self.node.right:
            self.node = self.node.right
            while self.node.left:
                self.parents.append(self.node)
                self.node = self.node.left
        else:
            self.node = self.parents.pop() if self.parents else None

        return nxt.val

    def hasNext(self) -> bool:
        return bool(self.node)
