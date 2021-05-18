# https://leetcode.com/problems/counting-bits/

from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        nums = [0] * (num + 1)
        bits = 1
        index = 1
        while index <= num:
            for _ in range(bits):
                if index <= num:
                    nums[index] = nums[index - bits] + 1
                    index += 1
            bits *= 2
        return nums
