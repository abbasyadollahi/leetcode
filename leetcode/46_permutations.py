# https://leetcode.com/problems/permutations/

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 1:
            return [nums]

        if len(nums) == 2:
            return [nums, nums[::-1]]

        permutations = []
        for i in range(len(nums)):
            copy = nums.copy()
            num = copy.pop(i)
            perms = self.permute(copy)
            [p.insert(0, num) for p in perms]
            [permutations.append(p) for p in perms]

        return permutations

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.perms = []
        self.permutations([], nums)
        return self.perms

    def permutations(self, perm: List[int], choices: List[int]) -> None:
        for i, choice in enumerate(choices):
            self.permutations([*perm, choice], [*choices[:i], *choices[i+1:]])
        if not choices:
            self.perms.append(perm)
