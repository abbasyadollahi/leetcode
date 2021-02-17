# https://leetcode.com/problems/flatten-2d-vector/

from typing import List


class Solution:
    def __init__(self, vector: List[List[int]]):
        self.values = self.flattenLists(vector)

    def flattenLists(self, lists: List[List[int]]) -> List[int]:
        values = []
        for row in lists:
            values += row

        return values

    def next(self) -> int:
        return self.values.pop(0) if self.hasNext() else None

    def hasNext(self) -> bool:
        return bool(self.values)

sol = Solution([[1, 2, 3], [4, 5, 6, 7], [8, 9]])
sol = Solution([[1,2], [3], [4,5,6]])
sol = Solution([])
