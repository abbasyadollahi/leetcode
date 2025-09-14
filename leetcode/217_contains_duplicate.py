# https://leetcode.com/problems/contains-duplicate/


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
