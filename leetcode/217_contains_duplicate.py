# https://leetcode.com/problems/contains-duplicate/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
