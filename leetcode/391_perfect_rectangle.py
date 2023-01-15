# https://leetcode.com/problems/perfect-rectangle/

from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        top_right_x = float('-inf')
        top_right_y = float('-inf')
        bottom_left_x = float('inf')
        bottom_left_y = float('inf')

        area = 0
        corners = set()
        for b_l_x, b_l_y, t_r_x, t_r_y in rectangles:
            top_right_x = max(top_right_x, t_r_x)
            top_right_y = max(top_right_y, t_r_y)
            bottom_left_x = min(bottom_left_x, b_l_x)
            bottom_left_y = min(bottom_left_y, b_l_y)

            area += (t_r_x - b_l_x) * (t_r_y - b_l_y)

            for corner in [(b_l_x, b_l_y), (b_l_x, t_r_y), (t_r_x, b_l_y), (t_r_x, t_r_y)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)

        return (
            len(corners) == 4 and
            all(corner in corners for corner in [(bottom_left_x, bottom_left_y), (bottom_left_x, top_right_y), (top_right_x, bottom_left_y), (top_right_x, top_right_y)]) and
            area == (top_right_x - bottom_left_x) * (top_right_y - bottom_left_y)
        )
