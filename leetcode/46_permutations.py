# https://leetcode.com/problems/permutations/


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
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

    def permute(self, nums: list[int]) -> list[list[int]]:
        def generate_permutations(permutation: list[int], choices: list[int]) -> list[list[int]]:
            permutations = []
            for i, choice in enumerate(choices):
                permutations.extend(generate_permutations([*permutation, choice], [*choices[:i], *choices[i + 1 :]]))
            if not choices:
                permutations.append(permutation)
            return permutations

        return generate_permutations([], nums)
