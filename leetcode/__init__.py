from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class GraphNode:
    def __init__(self, val: int = 0, neighbors: list["GraphNode"] | None = None) -> None:
        self.val = val
        self.neighbors = neighbors or []


class RandomListNode:
    def __init__(
        self,
        val: int = 0,
        next: Optional["RandomListNode"] = None,
        random: Optional["RandomListNode"] = None,
    ) -> None:
        self.val = val
        self.next = next
        self.random = random
