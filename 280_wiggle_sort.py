# https://leetcode.com/problems/wiggle-sort/

class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        max_idx = len(nums) - 2
        for i, num in enumerate(nums):
            if i == max_idx:
                return nums
            if (i%2 == 0) == (num > nums[i+1]):
                nums[i] = nums[i+1]
                nums[i+1] = num

        return nums

sol = Solution()
print(sol.wiggleSort([3, 5, 2, 1, 6, 4]))
