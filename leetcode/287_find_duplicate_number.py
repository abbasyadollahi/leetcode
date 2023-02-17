# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        index = 0
        while nums[index]:
            old_index = index
            index, nums[old_index] = nums[index], 0
        return index
