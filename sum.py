# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        l = 0
        r = len(nums) - 1
        nums.sort()

        while l < r:
            total = nums[l] + nums[r]

            if total == target:
                return [l, r]
            elif total > target:
                r -= 1
            else:
                l += 1

        return None

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 23))
print(sol.twoSum([2, 7, 11, 15], 22))
