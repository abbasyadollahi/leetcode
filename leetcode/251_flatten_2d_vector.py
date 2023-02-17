# https://leetcode.com/problems/flatten-2d-vector/

class Solution:
    def __init__(self, vector: list[list[int]]):
        self.values = self.flattenLists(vector)

    def flattenLists(self, lists: list[list[int]]) -> list[int]:
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
