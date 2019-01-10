# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSumSorted(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        l = 0
        r = len(nums) - 1

        while l < r:
            total = nums[l] + nums[r]

            if total == target:
                return [l, r]
            elif total > target:
                r -= 1
            else:
                l += 1

        return None

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        prev = set()
        for i, n in enumerate(nums):
            if target - n in prev:
                return [nums.index(target-n), i]
            else:
                prev.add(n)

        return None

sol = Solution()
print(sol.twoSumSorted([2, 7, 11, 15], 23))
print(sol.twoSumSorted([2, 7, 11, 15], 22))
