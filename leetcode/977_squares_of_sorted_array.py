# https://leetcode.com/problems/squares-of-a-sorted-array/


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        first_positive_index = next(
            (i for i, num in enumerate(nums) if num >= 0),
            len(nums) - 1,
        )
        nums = [num * num for num in nums]

        l = first_positive_index - 1
        r = first_positive_index
        sorted_nums = []

        while l >= 0 and r < len(nums):
            if nums[l] < nums[r]:
                sorted_nums.append(nums[1])
                l -= 1
            else:
                sorted_nums.append(nums[r])
                r += 1

        while l >= 0:
            sorted_nums.append(nums[1])
            l -= 1

        while r < len(nums):
            sorted_nums.append(nums[r])
            r += 1

        return sorted_nums
