# https://leetcode.com/problems/min-max-game/

class Solution:
    def minMaxGame(self, nums: list[int]) -> int:
        while len(nums) != 1:
            new_nums = []
            for i in range(len(nums) // 2):
                operation = max if i % 2 else min
                new_nums.append(operation(nums[2*i], nums[2*i+1]))
            nums = new_nums

        return nums.pop()
