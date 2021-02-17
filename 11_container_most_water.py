# https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_area = 0

        while start < end:
            h = min(height[start], height[end])
            w = end - start

            if h * w > max_area:
                max_area = h * w

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area

sol = Solution()
print (sol.maxArea([1,8,6,2,5,4,8,3,7]))
print (sol.maxArea([1,2,2,2,2,2,2,2,2,2,2,2,1]))
print (sol.maxArea([6,10,3,3,4,5,4,1]))
print (sol.maxArea([1,3,1,6,4,10,3,5,6,9]))
