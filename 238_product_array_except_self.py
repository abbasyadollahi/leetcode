# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        p = 1
        product = []
        for i in range(len(nums)):
            product.append(p)
            p *= nums[i]

        p = 1
        for i in range(len(nums)-1, -1, -1):
            product[i] *= p
            p *= nums[i]

        return product
