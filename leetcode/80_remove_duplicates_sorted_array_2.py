# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count = 1
        current = nums[0]

        for i, num in enumerate(nums[1:], 1):
            if num == current:
                if count < 2:
                    count += 1
                else:
                    nums[i] = None
            else:
                count = 1
                current = num

        i = j = 0
        while j < len(nums):
            if nums[i] is None:
                if nums[j] is None:
                    j += 1
                    continue
                nums[i] = nums[j]
                nums[j] = None
            else:
                i += 1
                j += 1

        return i
