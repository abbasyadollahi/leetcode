# https://leetcode.com/problems/subsets/


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        return set(
            [
                tuple(nums),
                *[subset for i in range(len(nums)) for subset in self.subsets(nums[:i] + nums[i + 1 :])],
            ]
        )

    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        return [
            [nums[i] for i, bit in enumerate(bitmask) if bit == "1"]
            for bitmask in [f"{mask:0{n}b}" for mask in range(2**n)]
        ]
