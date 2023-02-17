from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class GraphNode:
    def __init__(self, val: int = 0, neighbors: list['GraphNode'] = None):
        self.val = val
        self.neighbors = neighbors or []


class RandomListNode:
    def __init__(self, val: int = 0, next: Optional['RandomListNode'] = None, random: Optional['RandomListNode'] = None):
        self.val = val
        self.next = next
        self.random = random
