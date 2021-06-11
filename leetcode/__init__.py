from typing import List


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class GraphNode:
    def __init__(self, val: int = 0, neighbors: List['GraphNode'] = None):
        self.val = val
        self.neighbors = neighbors or []


class RandomListNode:
    def __init__(self, val: int = 0, next: 'RandomListNode' = None, random: 'RandomListNode' = None):
        self.val = val
        self.next = next
        self.random = random
