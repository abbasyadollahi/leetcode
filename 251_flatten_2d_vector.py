# https://leetcode.com/problems/flatten-2d-vector/

class Solution:
    def __init__(self, vector):
        """
        :type vector: List[List[int]]
        """

        self.values = self.__flattenLists(vector)

    def __flattenLists(self, lists):
        """
        :type lists: List[List[int]]
        :rtype: List[int]
        """

        values = []
        for row in lists:
            values += row

        return values


    def next(self):
        return self.values.pop(0) if self.hasNext() else None

    def hasNext(self):
        return bool(self.values)

sol = Solution([[1, 2, 3], [4, 5, 6, 7], [8, 9]])
sol = Solution([[1,2], [3], [4,5,6]])
sol = Solution([])
