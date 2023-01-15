# https://leetcode.com/problems/jump-game-ii/

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        def best_jump(index: int) -> int:
            best = 0
            jump = index
            jumps = range(index + 1, index + nums[index] + 1)
            for bonus, i in enumerate(jumps):
                if nums[i] + bonus >= best:
                    jump = i
                    best = nums[i] + bonus
            return jump

        i = 0
        length = len(nums) - 1
        count = min(1, length)
        while i + nums[i] < length:
            i = best_jump(i)
            count += 1
        return count

    def jump(self, nums: List[int]) -> int:
        count = 0
        l = r = best = 0
        length = len(nums) - 1
        while r < length:
            best = max(best, l + nums[l])
            if l == r:
                count += 1
                r = best
                best = 0
            l += 1
        return count

    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[0] = 0

        for i, num in enumerate(nums):
            for j in range(i + 1, min(i + num + 1, len(nums))):
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[-1]
