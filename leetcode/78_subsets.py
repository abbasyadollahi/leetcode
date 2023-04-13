# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        return set([tuple(nums), *[subset for i in range(len(nums)) for subset in self.subsets(nums[:i] + nums[i+1:])]])
