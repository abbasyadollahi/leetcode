# https://leetcode.com/problems/trapping-rain-water/

from typing import List


class Solution:
    def trapRain(self, elevation: List[int]) -> int:
        left = 0
        right = len(elevation) - 1

        rain = 0
        left_lvl = 0
        right_lvl = 0
        while left < right:
            if elevation[left] < elevation[right]:
                if elevation[left] >= left_lvl:
                    left_lvl = elevation[left]
                else:
                    rain += (left_lvl - elevation[left])
                left += 1
            else:
                if elevation[right] >= right_lvl:
                    right_lvl = elevation[right]
                else:
                    rain += (right_lvl - elevation[right])
                right -= 1
        return rain


sol = Solution()
print(sol.trapRain([0,1,0,2,1,0,1,3,2,1,2,1]))
