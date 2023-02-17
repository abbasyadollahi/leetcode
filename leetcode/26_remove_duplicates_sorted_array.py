# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return None

        r = len(nums) - 1
        l = r - 1
        while r > 0:
            if nums[r] == nums[l]:
                nums.pop(r)
            r = l
            l -= 1

        return len(nums)
