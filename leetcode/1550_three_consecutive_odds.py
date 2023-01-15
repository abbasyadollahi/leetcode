# https://leetcode.com/problems/three-consecutive-odds/

from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds_count = 0
        window_start = 0
        window_end = 2
        length = len(arr)

        if length < 3:
            return False

        for i in range(window_start, window_end + 1):
            arr[i] = arr[i] % 2
            odds_count += arr[i]

        while window_end < length - 1:
            if odds_count == 3:
                return True

            odds_count -= arr[window_start]
            window_start += 1
            window_end += 1
            arr[window_end] = arr[window_end] % 2
            odds_count += arr[window_end]

        return odds_count == 3
