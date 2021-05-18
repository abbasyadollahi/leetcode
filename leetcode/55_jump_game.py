# https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        length = len(nums) - 1

        while i + nums[i] < length:
            if nums[i] == 0:
                return False
            i = self.bestJump(nums, i)
        return True

    def bestJump(self, nums: List[int], index: int) -> int:
        jumps = range(index + 1, index + nums[index] + 1)
        best = 0
        jump = index
        for bonus, i in enumerate(jumps):
            if nums[i] + bonus >= best:
                jump = i
                best = nums[i] + bonus
        return jump