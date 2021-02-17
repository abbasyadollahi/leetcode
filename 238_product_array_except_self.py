# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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
