# https://leetcode.com/problems/01-matrix/

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = range(len(mat))
        cols = range(len(mat[0]))

        def traverse(i: int, j: int) -> int:
            visited = set()
            queue = deque([(i, j, int())])

            while queue:
                i, j, count = queue.popleft()
                if mat[i][j] == 0:
                    return count

                count += 1
                visited.add((i, j))

                queue.extend(
                    (ii, jj, count)
                    for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                    if (ii, jj) not in visited and ii in rows and jj in cols
                )

        return [[traverse(i, j) for j, num in enumerate(row)] for i, row in enumerate(mat)]

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    top = mat[i-1][j] if i > 0 else float('inf')
                    left = mat[i][j-1] if j > 0 else float('inf')
                    mat[i][j] = min(top, left) + 1

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if mat[i][j]:
                    bottom = mat[i+1][j] if i < m - 1 else float('inf')
                    right = mat[i][j+1] if j < n - 1 else float('inf')
                    mat[i][j] = min(bottom + 1, right + 1, mat[i][j])

        return mat
