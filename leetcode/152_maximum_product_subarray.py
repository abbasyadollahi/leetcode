# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        mx = float('-inf')
        sub = []
        switch = False
        product = left = right = 1

        for num in nums:
            if num == 0:
                mx = max(mx, self.compute_max(product, left, right, sub), 0)
                sub = []
                switch = False
                product = left = right = 1
            else:
                sub.append(num)
                product *= num
                if switch is False and num < 0:
                    left = product
                    right = num
                    switch = True
                elif num > 0:
                    right *= num
                else:
                    right = num

        return max(mx, self.compute_max(product, left, right, sub))

    def compute_max(self, product: int, left: int, right: int, sub: list[int]) -> int:
        if len(sub) == 0:
            return float('-inf')
        if len(sub) == 1:
            return max(sub)
        if product > 0:
            return product
        else:
            return max(product // left, product // right)
