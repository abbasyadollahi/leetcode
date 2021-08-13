# https://leetcode.com/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()
        self.recurse(candidates, target, [], combinations)
        return combinations


    def recurse(self, candidates: List[int], target: int, path: List[int], combinations: List[List[int]]) -> None:
        if target < 0:
            return
        if target == 0:
            combinations.append(path)
            return

        for i, candidate in enumerate(candidates):
            new_target = target - candidate
            self.recurse(candidates[i:], new_target, [*path, candidate], combinations)


sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))
print(sol.combinationSum([2, 3, 5], 7))
print(sol.combinationSum([2], 1))
print(sol.combinationSum([1], 1))
print(sol.combinationSum([1], 2))
