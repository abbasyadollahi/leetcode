# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return -1

        lo = 0
        hi = len(nums) - 1
        first = nums[0]

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid
            if nums[lo] == target:
                return lo
            elif first <= target < nums[mid] or target < nums[mid] < first or nums[mid] < first <= target:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1

sol = Solution()
print (sol.search([8,9,2,3,4], 9))
print (sol.search([4,5,6,7,0,1,2], 0))
print (sol.search([9,10,0,1,2,3,4,8], 7))
print (sol.search([9,10,0,1,2,3,4,8], 8))
print (sol.search([0,1,2,3,4,8,9,10,11,12], 0))
