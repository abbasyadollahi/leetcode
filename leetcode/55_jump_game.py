# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        i = 0
        length = len(nums) - 1

        while i + nums[i] < length:
            if nums[i] == 0:
                return False
            i = self.bestJump(nums, i)
        return True

    def bestJump(self, nums: list[int], index: int) -> int:
        jumps = range(index + 1, index + nums[index] + 1)
        best = 0
        jump = index
        for bonus, i in enumerate(jumps):
            if nums[i] + bonus >= best:
                jump = i
                best = nums[i] + bonus
        return jump

    def canJump(self, nums: list[int]) -> bool:
        jumps = nums[0]
        for i in range(1, len(nums)):
            if not jumps:
                return False
            jumps = max(nums[i], jumps - 1)
        return True
