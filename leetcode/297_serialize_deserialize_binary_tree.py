# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: TreeNode) -> str:
        nodes = []
        def traverse(node: TreeNode) -> None:
            if node is None:
                nodes.append('.')
            else:
                nodes.append(node.val)
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        return ','.join(map(str, nodes))

    def deserialize(self, data: str) -> TreeNode:
        nodes = iter(data.split(','))
        def traverse() -> TreeNode:
            val = next(nodes)
            if val == '.':
                return None
            else:
                node = TreeNode(int(val))
                node.left = traverse()
                node.right = traverse()
                return node

        root = traverse()
        return root
