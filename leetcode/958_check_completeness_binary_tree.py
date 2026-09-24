# https://leetcode.com/problems/check-completeness-of-a-binary-tree/


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        end = False
        queue = [root]
        while queue:
            next_queue = []
            for node in queue:
                if not node:
                    end = True
                elif end:
                    return False
                else:
                    next_queue.append(node.left)
                    next_queue.append(node.right)
            queue = next_queue
        return True
