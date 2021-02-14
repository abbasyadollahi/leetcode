# https://leetcode.com/problems/zigzag-iterator/

class Solution:
    def __init__(self, *args):
        """
        :type *args: List[int]
        """

        self.values = self.__flattenLists(args)

    def __flattenLists(self, lists):
        """
        :type lists: Tuple[List[int]]
        :rtype: List[int]
        """

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


    def next(self):
        return self.values.pop(0) if self.hasNext() else None

    def hasNext(self):
        return bool(self.values)

sol = Solution([1, 2, 3], [4, 5, 6, 7], [8, 9])
sol = Solution([])
