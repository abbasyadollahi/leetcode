# https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/

from typing import List


class Solution:
    def findMissing(self, nums: List[int]) -> int:
        shift = self.segregate(nums)
        smallest = self.search(nums[shift:])
        return smallest

    def segregate(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if (nums[i] <= 0):
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return j

    def search(positive_nums: List[int]) -> int:
        length = len(positive_nums)
        for num in positive_nums:
            idx = abs(num) - 1
            if (idx < length and num > 0 and positive_nums[idx] > 0):
                positive_nums[idx] = -positive_nums[idx]

        return next((i for i, num in enumerate(positive_nums) if num > 0), length) + 1

    def findMissing(self, nums: List[int]) -> int:
        nums = set(nums)
        largest = max(nums)
        for i in range(1, largest):
            if i not in nums:
                return i
        return max(largest, 0) + 1
