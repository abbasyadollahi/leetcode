# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product = [1] * len(nums)

        p = 1
        for i in range(len(nums)):
            product[i] *= p
            p *= nums[i]

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            product[i] *= p
            p *= nums[i]

        return product

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        zeros = 0
        product = 1
        non_zero = False
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                non_zero = True
                product *= num

        product = product if non_zero else 0
        return [product if num == 0 and zeros == 1 else 0 if zeros else product // num for num in nums]
