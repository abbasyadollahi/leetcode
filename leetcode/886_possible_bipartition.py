# https://leetcode.com/problems/possible-bipartition/

from collections import defaultdict
from typing import Dict, List, Set


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        haters = defaultdict(set)
        for he, hates in dislikes:
            haters[he].add(hates)
            haters[hates].add(he)

        group1 = set()
        group2 = set()
        visited = [False] * (n + 1)
        def traverse(me: int, enemies: Set[int], my_group: Set[int], other_group: Set[int]) -> bool:
            if visited[me]:
                return me not in other_group

            visited[me] = True
            my_group.add(me)

            return all(
                traverse(enemy, haters[enemy], other_group, my_group)
                for enemy in enemies
            )

        return all(
            traverse(person, hates, group1, group2)
            for person, hates in haters.items()
            if not visited[person]
        )

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        haters = defaultdict(set)
        for he, hates in dislikes:
            haters[he].add(hates)
            haters[hates].add(he)

        union_find = UnionFind(list(range(1, n + 1)))
        for person, hates in haters.items():
            root = next(iter(hates))
            for hated in hates:
                union_find.union(root, hated)
            if union_find.connected(person, root):
                return False
        return True


class UnionFind:

    items: Dict[int, int]
    group_sizes: Dict[int, int]

    def __init__(self, items: List[int]) -> None:
        self.items = dict(zip(items, items))
        self.group_sizes = dict.fromkeys(items, 1)

    def find(self, x: int) -> int:
        """Find the root of the group `x` belongs to."""
        item = x
        while item != self.items[item]:
            item = self.items[item]

        while x != self.items[x]:
            x, self.items[x] = self.items[x], item

        return item

    def union(self, x: int, y: int) -> None:
        """Merge `x` and `y` groups."""
        x_root = self.find(x)
        y_root = self.find(y)

        x_size = self.group_sizes[x_root]
        y_size = self.group_sizes[y_root]

        if x_root == y_root:
            return

        if x_size > y_size:
            self.items[y_root] = x_root
            self.group_sizes[x_root] += y_size
            self.group_sizes[y_root] = 0
        else:
            self.items[x_root] = y_root
            self.group_sizes[y_root] += x_size
            self.group_sizes[x_root] = 0

    def connected(self, x: int, y: int) -> bool:
        """Check if `x` and `y` belong to the same group."""
        return self.find(x) == self.find(y)
