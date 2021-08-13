# https://leetcode.com/problems/zigzag-iterator/

from typing import List, Tuple


class Solution:
    def __init__(self, *args: Tuple[List[int]]):
        self.values = self.flattenLists(args)

    def flattenLists(self, lists: Tuple[List[int]]) -> List[int]:
        values = []
        empty = False
        rows = len(lists)

        while not empty:
            empty = True
            for row in range(rows):
                if lists[row]:
                    empty = False
                    values.append(lists[row].pop(0))

        return values

    def next(self) -> int:
        return self.values.pop(0) if self.hasNext() else None

    def hasNext(self) -> bool:
        return bool(self.values)


sol = Solution([1, 2, 3], [4, 5, 6, 7], [8, 9])
sol = Solution([])
