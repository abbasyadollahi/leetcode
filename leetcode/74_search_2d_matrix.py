# https://leetcode.com/problems/search-a-2d-matrix/


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0]) - 1
        cols = len(matrix[0])

        while l <= r:
            mid = (l + r) // 2
            num = matrix[mid // cols][mid % cols]
            if num < target:
                l = mid + 1
            elif num > target:
                r = mid - 1
            else:
                return True

        return False
