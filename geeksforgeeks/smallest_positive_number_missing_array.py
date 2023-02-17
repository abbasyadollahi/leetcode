# https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/

class Solution:
    def findMissing(self, nums: list[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if (nums[i] <= 0):
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        positive_nums = nums[j:]
        for num in nums[j:]:
            i = abs(num) - 1
            if (i < len(positive_nums) and num > 0 and positive_nums[i] > 0):
                positive_nums[i] = -positive_nums[i]

        return next((i for i, num in enumerate(positive_nums) if num > 0), len(positive_nums)) + 1

    def findMissing(self, nums: list[int]) -> int:
        nums = set(nums)
        largest = max(nums)
        for i in range(1, largest):
            if i not in nums:
                return i
        return max(largest, 0) + 1


sol = Solution()
assert sol.findMissing([2, 3, 7, 6, 8, -1, -10, 15]) == 1
assert sol.findMissing([2, 3, -7, 6, 8, 1, -10, 15]) == 4
assert sol.findMissing([1, 1, 0, -1, -2]) == 2
assert sol.findMissing([3, 1, 2]) == 4
