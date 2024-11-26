# https://leetcode.com/problems/shuffle-the-array/


class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        return [nums[i] for xy in zip(range(0, n), range(n, 2 * n)) for i in xy]
