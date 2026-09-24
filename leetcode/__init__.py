class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


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


class GraphNode:
    def __init__(self, val: int = 0, neighbors: list[GraphNode] | None = None) -> None:
        self.val = val
        self.neighbors = neighbors or []


class RandomListNode:
    def __init__(
        self,
        val: int = 0,
        next: RandomListNode | None = None,
        random: RandomListNode | None = None,
    ) -> None:
        self.val = val
        self.next = next
        self.random = random
