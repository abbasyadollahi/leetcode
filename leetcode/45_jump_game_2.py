# https://leetcode.com/problems/jump-game-ii/

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> bool:
        i = 0
        length = len(nums) - 1

        count = min(1, length)
        while i + nums[i] < length:
            i = self.bestJump(nums, i)
            count += 1
        return count

    def bestJump(self, nums: List[int], index: int) -> int:
        jumps = range(index + 1, index + nums[index] + 1)
        best = 0
        jump = index
        for bonus, i in enumerate(jumps):
            if nums[i] + bonus >= best:
                jump = i
                best = nums[i] + bonus
        return jump
