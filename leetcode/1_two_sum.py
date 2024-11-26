# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            if target - num in seen:
                break
            seen[num] = i

        return [seen[target - num], i]
