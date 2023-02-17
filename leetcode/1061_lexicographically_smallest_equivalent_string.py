# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

import string


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        union_find = UnionFind(list(string.ascii_lowercase))
        for letter1, letter2 in zip(s1, s2):
            union_find.union(letter1, letter2)

        return ''.join(map(union_find.find, baseStr))

class UnionFind:

    items: dict[str, int]
    group_sizes: dict[str, int]

    def __init__(self, items: list[str]) -> None:
        self.items = dict(zip(items, items))
        self.group_sizes = dict.fromkeys(items, 1)

    def find(self, x: str) -> str:
        """Find the root of the group `x` belongs to."""
        item = x
        smallest = x
        while item != self.items[item]:
            item = self.items[item]
            smallest = min(smallest, item)

        while x != self.items[x]:
            x, self.items[x] = self.items[x], smallest

        return smallest

    def union(self, x: str, y: str) -> None:
        """Merge `x` and `y` groups."""
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if x_root < y_root:
            self.items[y_root] = x_root
            self.group_sizes[x] += self.group_sizes[y]
            self.group_sizes[y] = 0
        else:
            self.items[x_root] = y_root
            self.group_sizes[y] += self.group_sizes[x]
            self.group_sizes[x] = 0
